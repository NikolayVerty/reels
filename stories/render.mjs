#!/usr/bin/env node
// Рендер сторис для хайлайтов: stories/data.json -> output/highlights/<id>/*.png (1080x1920)
// Запуск из корня репозитория: node stories/render.mjs
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const data = JSON.parse(fs.readFileSync(path.join(here, 'data.json'), 'utf8'));
const outRoot = path.join(here, '..', 'output', 'highlights');

const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const br = (s) => esc(s).replace(/\n/g, '<br>');

// ---------- фон: схематичная карта города ----------
function rng(seed) { let s = seed; return () => (s = (s * 16807) % 2147483647) / 2147483647; }
function mapBg(seed) {
  const r = rng(seed * 97 + 13);
  let roads = '', blocks = '', pins = '';
  for (let i = 0; i < 9; i++) {
    const y = 120 + i * 210 + r() * 80;
    roads += `<path d="M-50 ${y} C 300 ${y + (r() - .5) * 220}, 700 ${y + (r() - .5) * 220}, 1130 ${y + (r() - .5) * 120}" />`;
  }
  for (let i = 0; i < 6; i++) {
    const x = 60 + i * 200 + r() * 60;
    roads += `<path d="M${x} -50 C ${x + (r() - .5) * 200} 600, ${x + (r() - .5) * 200} 1300, ${x + (r() - .5) * 120} 1970" />`;
  }
  for (let i = 0; i < 14; i++) {
    const x = r() * 1000, y = r() * 1850, w = 60 + r() * 140, h = 50 + r() * 120;
    blocks += `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="14" />`;
  }
  for (let i = 0; i < 7; i++) {
    const side = r() < .5, x = side ? 20 + r() * 35 : 1025 + r() * 35, y = 150 + r() * 1650, s = .6 + r() * .5;
    pins += `<g transform="translate(${x} ${y}) scale(${s})" opacity="${.2 + r() * .3}"><path d="M0 0 C -22 -30 -30 -42 -30 -58 A 30 30 0 1 1 30 -58 C 30 -42 22 -30 0 0Z" fill="#00A0E3"/><circle cx="0" cy="-58" r="11" fill="#0B1220"/></g>`;
  }
  return `<svg class="map" viewBox="0 0 1080 1920" preserveAspectRatio="xMidYMid slice">
    <g fill="rgba(255,255,255,.025)">${blocks}</g>
    <g fill="none" stroke="rgba(120,170,255,.08)" stroke-width="16" stroke-linecap="round">${roads}</g>
    <g fill="none" stroke="rgba(120,170,255,.06)" stroke-width="3">${roads}</g>
    ${pins}
  </svg>`;
}

// ---------- иконки ----------
const icons = {
  chart: '<path d="M8 40V24M20 40V14M32 40V20M44 40V8" stroke-width="6" stroke-linecap="round"/>',
  ruble: '<path d="M16 44V8h14a10 10 0 0 1 0 20H10M10 36h20" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>',
  route: '<circle cx="12" cy="40" r="5"/><circle cx="40" cy="12" r="5"/><path d="M12 35V26q0-8 8-8h12q8 0 8-6" stroke-width="5" fill="none" stroke-linecap="round"/>',
  star: '<path d="M26 4l6.5 14 15 1.6-11.3 10 3.3 15L26 37l-13.5 7.6 3.3-15L4.5 19.6l15-1.6z" stroke-width="3" stroke-linejoin="round"/>',
  user: '<circle cx="26" cy="17" r="10" stroke-width="5" fill="none"/><path d="M6 46c2-10 10-15 20-15s18 5 20 15" stroke-width="5" fill="none" stroke-linecap="round"/>',
  check: '<path d="M8 27l11 11 25-26" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
};
const icon = (k, size = 52) => `<svg width="${size}" height="${size}" viewBox="0 0 52 52" fill="currentColor" stroke="currentColor">${icons[k]}</svg>`;

// ---------- блоки ----------
function chart(c) {
  if (c.kind === 'bars') {
    const max = Math.max(...c.values);
    const bars = c.values.map((v, i) => `
      <div class="bar"><div class="val">${v}</div><div class="col ${i === c.values.indexOf(max) ? 'peak' : ''}" style="height:${Math.max(6, v / max * 100)}%"></div><div class="lbl">${esc(c.labels[i])}</div></div>`).join('');
    return `<div class="panel"><div class="ptitle">${esc(c.title)}</div><div class="bars">${bars}</div></div>`;
  }
  if (c.kind === 'rank') {
    const steps = c.steps.map(([t, v], i) => `<div class="rstep ${i === c.steps.length - 1 ? 'win' : ''}"><div class="rv">${esc(v)}</div><div class="rt">${esc(t)}</div></div>`).join('<div class="rarrow">→</div>');
    return `<div class="panel"><div class="ptitle">${esc(c.title)}</div><div class="rank">${steps}</div></div>`;
  }
  if (c.kind === 'price') {
    return `<div class="panel"><div class="ptitle">${esc(c.title)}</div>
      <div class="pbars"><div class="prow"><span>было</span><div class="pb old" style="width:100%">${c.from} ₽</div></div>
      <div class="prow"><span>стало</span><div class="pb new" style="width:${c.to / c.from * 100}%">${c.to} ₽</div></div></div></div>`;
  }
  if (c.kind === 'compare') {
    return `<div class="panel"><div class="ptitle">${esc(c.title)}</div><div class="cmp">
      <div class="cbox before"><b>${esc(c.before[0])}</b><span>${esc(c.before[1])}</span></div><div class="rarrow">→</div>
      <div class="cbox after"><b>${esc(c.after[0])}</b><span>${esc(c.after[1])}</span></div></div></div>`;
  }
  return '';
}

const stars = '<div class="stars">★★★★★</div>';

function frameHTML(f, hl) {
  switch (f.type) {
    case 'intro': return `
      <div class="kicker">${esc(f.kicker)}</div>
      <h1 class="huge">${br(f.title)}</h1>
      ${f.stats.length ? `<div class="grid">${f.stats.map(([n, l]) => `<div class="stat"><b>${esc(n)}</b><span>${esc(l)}</span></div>`).join('')}</div>` : ''}
      <div class="swipe">листай →</div>`;
    case 'case': return `
      <div class="chip">${esc(f.tag)}</div>
      <div class="big">${esc(f.big)}</div>
      <div class="bigl">${br(f.bigLabel)}</div>
      <div class="facts">${f.facts.map(([n, l]) => `<div class="fact"><b>${esc(n)}</b><span>${esc(l)}</span></div>`).join('')}</div>
      ${chart(f.chart)}`;
    case 'price': return `
      <div class="kicker">Тариф</div>
      <div class="pcard ${f.badge ? 'hot' : ''}">
        ${f.badge ? `<div class="badge">${esc(f.badge)}</div>` : ''}
        <div class="pname">${esc(f.name)}</div>
        <div class="pprice">${esc(f.price)}</div>
        <div class="pper">${esc(f.per)}</div>
        <ul>${f.items.map((i) => `<li>${icon('check', 34)}<span>${esc(i)}</span></li>`).join('')}</ul>
      </div>`;
    case 'step': return `
      <div class="stepn">${esc(f.n)}</div>
      <div class="kicker">Шаг ${esc(f.n)} из 05</div>
      <h1 class="huge">${br(f.title)}</h1>
      <p class="lead">${br(f.text)}</p>
      <div class="dots">${['01', '02', '03', '04', '05'].map((n) => `<i class="${n <= f.n ? 'on' : ''}"></i>`).join('')}</div>`;
    case 'quote': return `
      <div class="kicker">Отзыв клиента</div>
      <div class="qcard">
        ${stars}
        <div class="qhl">${esc(f.hl)}</div>
        <p class="qtext">«${esc(f.text)}»</p>
        <div class="who"><div class="ava">${esc(f.who[0])}</div><div><b>${esc(f.who)}</b><span>${esc(f.role)}</span></div></div>
      </div>`;
    case 'about': return `
      <div class="ava xl">НВ</div>
      <div class="kicker">Обо мне</div>
      <h1 class="huge">${esc(f.name)}</h1>
      <p class="lead">${esc(f.role)}</p>
      <div class="facts stack">${f.facts.map(([n, l]) => `<div class="fact"><b>${esc(n)}</b><span>${esc(l)}</span></div>`).join('')}</div>`;
    case 'team': return `
      <div class="kicker">Команда</div>
      <h1 class="huge">${br(f.title)}</h1>
      <div class="pills">${f.roles.map((r) => `<div class="pill">${esc(r)}</div>`).join('')}</div>`;
    case 'checklist': return `
      <div class="kicker">Бесплатно</div>
      <h1 class="huge">${br(f.title)}</h1>
      <div class="doc">${Array.from({ length: 6 }, (_, i) => `<div class="dline">${icon('check', 30)}<i style="width:${55 + (i * 37) % 40}%"></i></div>`).join('')}</div>
      <div class="facts">${f.stats.map(([n, l]) => `<div class="fact"><b>${esc(n)}</b><span>${esc(l)}</span></div>`).join('')}</div>`;
    case 'cta': return `
      <div class="kicker">${esc(f.kicker)}</div>
      <h1 class="huge">${br(f.title)}</h1>
      <div class="ctaline">${esc(f.line)}</div>
      <p class="lead">${esc(f.sub)}</p>`;
  }
  throw new Error('unknown frame type ' + f.type);
}

const CSS = `
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 1080px; height: 1920px; }
body { font-family: 'Inter', sans-serif; color: #fff; overflow: hidden;
  background: radial-gradient(1100px 900px at 85% 8%, rgba(0,160,227,.38), transparent 60%),
              radial-gradient(900px 800px at 0% 95%, rgba(99,102,241,.32), transparent 60%),
              linear-gradient(160deg, #0B1220 0%, #0E1A33 55%, #0B1220 100%); }
.map { position: absolute; inset: 0; width: 100%; height: 100%; }
.safe { position: absolute; left: 90px; right: 90px; top: 250px; bottom: 330px; display: flex; flex-direction: column; justify-content: center; gap: 34px; }
.top { position: absolute; top: 120px; left: 90px; right: 90px; display: flex; justify-content: space-between; align-items: center; font-size: 30px; color: rgba(255,255,255,.6); font-weight: 600; }
.brand { display: flex; align-items: center; gap: 14px; } .brand i { width: 46px; height: 46px; border-radius: 12px; background: #00A0E3; display: grid; place-items: center; font-style: normal; font-weight: 800; font-size: 17px; color: #fff; }
.prog { display: flex; gap: 8px; } .prog i { width: 34px; height: 6px; border-radius: 3px; background: rgba(255,255,255,.2); } .prog i.on { background: #fff; }
.kicker { font-size: 34px; font-weight: 700; color: #38BDF8; text-transform: uppercase; letter-spacing: 3px; }
.huge { font-family: 'Inter Display', 'Inter'; font-weight: 800; font-size: 104px; line-height: 1.02; letter-spacing: -2px; }
.lead { font-size: 44px; line-height: 1.35; color: rgba(255,255,255,.78); font-weight: 500; }
.swipe { font-size: 34px; color: rgba(255,255,255,.55); font-weight: 600; }
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 22px; }
.stat, .fact, .panel, .pcard, .qcard, .cbox, .pill, .doc {
  background: linear-gradient(160deg, rgba(255,255,255,.12), rgba(255,255,255,.04));
  border: 1.5px solid rgba(255,255,255,.14); border-radius: 36px;
  box-shadow: 0 30px 80px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.12); }
.stat { padding: 36px; } .stat b { display: block; font-size: 76px; font-weight: 800; letter-spacing: -1px; }
.stat span, .fact span { font-size: 30px; color: rgba(255,255,255,.65); font-weight: 500; }
.chip { align-self: flex-start; font-size: 32px; font-weight: 700; padding: 16px 30px; border-radius: 999px; background: rgba(0,160,227,.2); border: 1.5px solid rgba(56,189,248,.55); color: #7DD3FC; }
.big { font-family: 'Inter Display', 'Inter'; font-size: 230px; font-weight: 900; line-height: .9; letter-spacing: -6px;
  background: linear-gradient(180deg, #FFFFFF 20%, #7DD3FC); -webkit-background-clip: text; color: transparent; }
.bigl { font-size: 46px; font-weight: 600; line-height: 1.25; margin-top: -10px; }
.facts { display: flex; gap: 22px; } .facts.stack { flex-direction: column; }
.fact { flex: 1; padding: 30px 32px; } .fact b { display: block; font-size: 52px; font-weight: 800; letter-spacing: -1px; margin-bottom: 4px; }
.panel { padding: 36px 40px; } .ptitle { font-size: 30px; font-weight: 600; color: rgba(255,255,255,.65); margin-bottom: 26px; }
.bars { display: flex; align-items: flex-end; gap: 18px; height: 300px; }
.bar { flex: 1; height: 100%; display: flex; flex-direction: column; justify-content: flex-end; align-items: center; gap: 10px; }
.col { width: 100%; border-radius: 14px 14px 6px 6px; background: linear-gradient(180deg, rgba(125,211,252,.9), rgba(0,160,227,.35)); }
.col.peak { background: linear-gradient(180deg, #FDE68A, #F59E0B); box-shadow: 0 0 40px rgba(245,158,11,.5); }
.val { font-size: 30px; font-weight: 700; } .lbl { font-size: 26px; color: rgba(255,255,255,.6); }
.rank { display: flex; align-items: center; justify-content: space-between; }
.rstep { text-align: center; } .rv { font-size: 96px; font-weight: 900; color: rgba(255,255,255,.55); letter-spacing: -2px; }
.rstep.win .rv { color: #FDE68A; text-shadow: 0 0 40px rgba(245,158,11,.6); } .rt { font-size: 28px; color: rgba(255,255,255,.6); }
.rarrow { font-size: 60px; color: #38BDF8; font-weight: 700; }
.pbars { display: flex; flex-direction: column; gap: 22px; } .prow { display: flex; align-items: center; gap: 22px; } .prow span { width: 110px; font-size: 30px; color: rgba(255,255,255,.65); }
.pb { height: 92px; border-radius: 20px; display: flex; align-items: center; padding-left: 28px; font-size: 44px; font-weight: 800; }
.pb.old { background: rgba(255,255,255,.14); color: rgba(255,255,255,.7); text-decoration: line-through; } .pb.new { background: linear-gradient(90deg, #F59E0B, #FDE68A); color: #0B1220; min-width: 260px; }
.cmp { display: flex; align-items: center; gap: 20px; } .cbox { flex: 1; padding: 30px; border-radius: 28px; } .cbox b { display: block; font-size: 38px; } .cbox span { font-size: 28px; color: rgba(255,255,255,.65); }
.cbox.after { border-color: rgba(253,230,138,.6); background: linear-gradient(160deg, rgba(245,158,11,.25), rgba(245,158,11,.06)); }
.pcard { padding: 60px 56px; position: relative; } .pcard.hot { border: 3px solid #38BDF8; box-shadow: 0 0 0 10px rgba(56,189,248,.12), 0 30px 80px rgba(0,0,0,.4); }
.badge { position: absolute; top: -28px; right: 50px; background: #00A0E3; padding: 12px 28px; border-radius: 999px; font-size: 30px; font-weight: 700; }
.pname { font-size: 46px; font-weight: 700; color: #7DD3FC; } .pprice { font-size: 112px; font-weight: 900; letter-spacing: -3px; margin: 10px 0 0; } .pper { font-size: 34px; color: rgba(255,255,255,.65); margin-bottom: 40px; }
.pcard ul { list-style: none; display: flex; flex-direction: column; gap: 22px; } .pcard li { display: flex; align-items: center; gap: 20px; font-size: 38px; font-weight: 500; } .pcard li svg { color: #38BDF8; flex: none; }
.stepn { position: absolute; right: 40px; top: 330px; font-size: 520px; font-weight: 900; line-height: 1; color: rgba(255,255,255,.05); letter-spacing: -20px; }
.dots { display: flex; gap: 14px; } .dots i { width: 90px; height: 12px; border-radius: 6px; background: rgba(255,255,255,.18); } .dots i.on { background: linear-gradient(90deg, #00A0E3, #7DD3FC); }
.qcard { padding: 60px 56px; } .stars { color: #FBBF24; font-size: 56px; letter-spacing: 6px; }
.qhl { font-size: 60px; font-weight: 800; line-height: 1.1; margin: 24px 0; letter-spacing: -1px; } .qtext { font-size: 40px; line-height: 1.42; color: rgba(255,255,255,.85); }
.who { display: flex; align-items: center; gap: 24px; margin-top: 44px; } .who b { display: block; font-size: 36px; } .who span { font-size: 30px; color: rgba(255,255,255,.6); }
.ava { width: 96px; height: 96px; border-radius: 50%; display: grid; place-items: center; font-size: 42px; font-weight: 800; background: linear-gradient(135deg, #00A0E3, #6366F1); flex: none; }
.ava.xl { width: 260px; height: 260px; font-size: 100px; box-shadow: 0 0 0 12px rgba(56,189,248,.18), 0 30px 80px rgba(0,0,0,.4); }
.pills { display: flex; flex-wrap: wrap; gap: 18px; } .pill { padding: 26px 36px; border-radius: 999px; font-size: 38px; font-weight: 600; }
.doc { padding: 44px; display: flex; flex-direction: column; gap: 26px; } .dline { display: flex; align-items: center; gap: 22px; color: #22C55E; } .dline i { height: 22px; border-radius: 11px; background: rgba(255,255,255,.22); }
.ctaline { align-self: flex-start; font-size: 48px; font-weight: 800; padding: 30px 44px; border-radius: 28px; background: linear-gradient(90deg, #00A0E3, #38BDF8); box-shadow: 0 20px 60px rgba(0,160,227,.45); }
.foot { position: absolute; bottom: 190px; left: 90px; right: 90px; display: flex; justify-content: space-between; font-size: 30px; color: rgba(255,255,255,.5); font-weight: 600; }
/* обложка хайлайта */
.cover { position: absolute; inset: 0; display: grid; place-items: center; }
.cover .disc { width: 760px; height: 760px; border-radius: 50%; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 30px;
  background: radial-gradient(circle at 30% 25%, #38BDF8, #00A0E3 45%, #1E3A8A 100%); box-shadow: 0 0 0 18px rgba(255,255,255,.08), 0 40px 120px rgba(0,160,227,.5); color: #fff; }
.cover .disc svg { width: 260px; height: 260px; }
.cover .disc span { font-size: 64px; font-weight: 800; letter-spacing: -1px; }
`;

function page(inner, hl, idx, total, withMap = true) {
  const prog = total ? `<div class="prog">${Array.from({ length: total }, (_, i) => `<i class="${i <= idx ? 'on' : ''}"></i>`).join('')}</div>` : '';
  return `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>
    ${withMap ? mapBg(idx + hl.id.length * 7) : ''}
    ${inner}
  </body></html>`;
}

const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
const p = await ctx.newPage();
for (const hl of data.highlights) {
  const dir = path.join(outRoot, hl.id);
  fs.rmSync(dir, { recursive: true, force: true });
  fs.mkdirSync(dir, { recursive: true });
  await p.setContent(page(`<div class="cover"><div class="disc">${icon(hl.icon, 260)}</div></div>`, hl, 0, 0));
  await p.screenshot({ path: path.join(dir, '00-cover.png') });
  const n = hl.frames.length;
  for (let i = 0; i < n; i++) {
    const prog = `<div class="prog">${Array.from({ length: n }, (_, k) => `<i class="${k <= i ? 'on' : ''}"></i>`).join('')}</div>`;
    const inner = `<div class="top"><div class="brand"><i>360</i>${esc(data.handle)}</div>${prog}</div>
      <div class="safe">${frameHTML(hl.frames[i], hl)}</div>
      <div class="foot"><span>360-digital.ru</span><span>${esc(hl.cover)}</span></div>`;
    await p.setContent(page(inner, hl, i, n));
    await p.screenshot({ path: path.join(dir, String(i + 1).padStart(2, '0') + '.png') });
  }
  console.log(`${hl.id}: обложка + ${n} кадров`);
}
await browser.close();
console.log('Готово:', outRoot);
