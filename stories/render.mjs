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
const fontFace = [400, 500, 600, 700, 800].map((w) => ['cyrillic', 'latin'].map((sub) =>
  `@font-face{font-family:'Manrope';font-weight:${w};src:url('file://${path.join(here, 'fonts', `manrope-${sub}-${w}-normal.woff2`)}') format('woff2');}`).join('')).join('');

const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const br = (s) => esc(s).replace(/\n/g, '<br>');

// ---------- фон: схематичная карта города ----------
function rng(seed) { let s = seed; return () => (s = (s * 16807) % 2147483647) / 2147483647; }
function mapBg(seed) {
  const r = rng(seed * 97 + 13);
  let roads = '', pins = '';
  for (let i = 0; i < 7; i++) {
    const y = 160 + i * 260 + r() * 80;
    roads += `<path d="M-50 ${y} C 300 ${y + (r() - .5) * 200}, 700 ${y + (r() - .5) * 200}, 1130 ${y + (r() - .5) * 120}" />`;
  }
  for (let i = 0; i < 5; i++) {
    const x = 80 + i * 230 + r() * 60;
    roads += `<path d="M${x} -50 C ${x + (r() - .5) * 180} 600, ${x + (r() - .5) * 180} 1300, ${x + (r() - .5) * 100} 1970" />`;
  }
  for (let i = 0; i < 6; i++) {
    const side = r() < .5, x = side ? 20 + r() * 35 : 1025 + r() * 35, y = 150 + r() * 1650, sc = .6 + r() * .5;
    pins += `<g transform="translate(${x} ${y}) scale(${sc})" opacity="${.35 + r() * .35}"><path d="M0 0 C -22 -30 -30 -42 -30 -58 A 30 30 0 1 1 30 -58 C 30 -42 22 -30 0 0Z" fill="#FFC24B"/><circle cx="0" cy="-58" r="11" fill="#0F0F12"/></g>`;
  }
  return `<div class="grid-bg"></div>
  <div class="glow" style="width:900px;height:900px;right:-300px;top:-250px"></div>
  <div class="glow" style="width:700px;height:700px;left:-320px;bottom:-200px;opacity:.6"></div>
  <svg class="map" viewBox="0 0 1080 1920" preserveAspectRatio="xMidYMid slice">
    <g fill="none" stroke="rgba(255,255,255,.045)" stroke-width="18" stroke-linecap="round">${roads}</g>
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
      <div class="bar"><div class="val">${v}</div><div class="colbar ${i === c.values.indexOf(max) ? 'peak' : ''}" style="height:${Math.max(6, v / max * 100)}%"></div><div class="lbl">${esc(c.labels[i])}</div></div>`).join('');
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
${fontFace}
:root { --yellow:#FFC24B; --yellow-dark:#F5A623; --dark:#0F0F12; --graphite:#1A1A1F; --graphite-2:#25252C; --muted:#94949E; --green:#16A34A; }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 1080px; height: 1920px; }
body { font-family: 'Manrope', 'Inter', sans-serif; color: #fff; overflow: hidden; background: var(--dark); font-feature-settings: 'ss01' on; }
.grid-bg { position: absolute; inset: 0; opacity: .9;
  background-image: linear-gradient(rgba(255,255,255,.045) 2px, transparent 2px), linear-gradient(90deg, rgba(255,255,255,.045) 2px, transparent 2px);
  background-size: 108px 108px;
  -webkit-mask-image: radial-gradient(ellipse 85% 70% at 50% 40%, #000 30%, transparent 85%); }
.glow { position: absolute; border-radius: 50%; filter: blur(140px); background: rgba(255,194,75,.20); }
.map { position: absolute; inset: 0; width: 100%; height: 100%; }
.safe { position: absolute; left: 90px; right: 90px; top: 250px; bottom: 330px; display: flex; flex-direction: column; justify-content: center; gap: 34px; }
.top { position: absolute; top: 120px; left: 90px; right: 90px; display: flex; justify-content: space-between; align-items: center; font-size: 30px; color: rgba(255,255,255,.62); font-weight: 700; }
.brand { display: flex; align-items: center; gap: 14px; } .brand i { width: 50px; height: 50px; border-radius: 14px; background: var(--yellow); display: grid; place-items: center; font-style: normal; font-weight: 800; font-size: 19px; color: var(--dark); }
.prog { display: flex; gap: 8px; } .prog i { width: 34px; height: 6px; border-radius: 3px; background: rgba(255,255,255,.18); } .prog i.on { background: var(--yellow); }
.kicker { font-size: 32px; font-weight: 700; color: var(--yellow-dark); text-transform: uppercase; letter-spacing: 3px; }
.huge { font-weight: 800; font-size: 100px; line-height: 1.06; letter-spacing: -2px; }
.yt { background: linear-gradient(var(--yellow), var(--yellow)) no-repeat 0 100% / 100% 86%; color: var(--dark); padding: 0 10px; border-radius: 12px; -webkit-box-decoration-break: clone; }
.lead { font-size: 44px; line-height: 1.4; color: rgba(255,255,255,.66); font-weight: 500; }
.swipe { font-size: 34px; color: rgba(255,255,255,.5); font-weight: 700; }
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 22px; }
.stat, .fact, .qcard, .cbox, .pill, .doc { background: var(--graphite); border: 2px solid rgba(255,255,255,.08); border-radius: 36px; box-shadow: 0 30px 80px rgba(0,0,0,.45); }
.stat { padding: 36px; } .stat b { display: block; font-size: 74px; font-weight: 800; letter-spacing: -1.5px; color: var(--yellow); }
.stat span, .fact span { font-size: 30px; color: var(--muted); font-weight: 600; }
.chip { align-self: flex-start; font-size: 32px; font-weight: 700; padding: 14px 30px; border-radius: 999px; background: rgba(255,194,75,.16); border: 2px solid rgba(255,194,75,.32); color: var(--yellow); }
.big { font-size: 230px; font-weight: 800; line-height: .92; letter-spacing: -8px; color: var(--yellow); text-shadow: 0 0 120px rgba(255,194,75,.35); }
.bigl { font-size: 46px; font-weight: 700; line-height: 1.25; margin-top: -6px; }
.facts { display: flex; gap: 22px; } .facts.stack { flex-direction: column; }
.fact { flex: 1; padding: 30px 32px; } .fact b { display: block; font-size: 52px; font-weight: 800; letter-spacing: -1px; margin-bottom: 4px; }
/* белая панель с графиком — как .kase-panel на сайте */
.panel { background: #fff; color: var(--dark); border-radius: 36px; padding: 36px 40px; box-shadow: 0 30px 80px rgba(0,0,0,.5); }
.ptitle { font-size: 30px; font-weight: 700; color: #6B6B75; margin-bottom: 26px; }
.bars { display: flex; align-items: flex-end; gap: 18px; height: 290px; }
.bar { flex: 1; height: 100%; display: flex; flex-direction: column; justify-content: flex-end; align-items: center; gap: 10px; }
.colbar { width: 100%; border-radius: 12px 12px 4px 4px; background: var(--yellow); opacity: .55; }
.colbar.peak { opacity: 1; background: var(--yellow-dark); }
.val { font-size: 30px; font-weight: 800; } .lbl { font-size: 26px; color: #94949E; font-weight: 600; }
.rank { display: flex; align-items: center; justify-content: space-between; }
.rstep { text-align: center; } .rv { font-size: 96px; font-weight: 800; color: #C9C9CF; letter-spacing: -3px; }
.rstep.win .rv { color: var(--green); } .rt { font-size: 28px; color: #94949E; font-weight: 600; }
.rarrow { font-size: 60px; color: var(--yellow-dark); font-weight: 800; }
.pbars { display: flex; flex-direction: column; gap: 22px; } .prow { display: flex; align-items: center; gap: 22px; } .prow span { width: 110px; font-size: 30px; color: #6B6B75; font-weight: 600; }
.pb { height: 92px; border-radius: 20px; display: flex; align-items: center; padding-left: 28px; font-size: 44px; font-weight: 800; }
.pb.old { background: #EDEDF0; color: #94949E; text-decoration: line-through; } .pb.new { background: var(--yellow); color: var(--dark); min-width: 260px; }
.cmp { display: flex; align-items: center; gap: 20px; } .panel .cbox { flex: 1; padding: 30px; border-radius: 26px; background: #F4F4F6; border: none; box-shadow: none; color: var(--dark); }
.cbox b { display: block; font-size: 38px; font-weight: 800; } .cbox span { font-size: 28px; color: #6B6B75; font-weight: 600; }
.panel .cbox.after { background: #FFF6E0; } .cbox.after b { color: var(--green); }
.pcard { background: #fff; color: var(--dark); border-radius: 40px; padding: 64px 56px; position: relative; box-shadow: 0 30px 80px rgba(0,0,0,.5); }
.pcard.hot { outline: 6px solid var(--yellow); outline-offset: -6px; }
.badge { position: absolute; top: -30px; right: 50px; background: var(--yellow); color: var(--dark); padding: 12px 28px; border-radius: 999px; font-size: 30px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; }
.pname { font-size: 44px; font-weight: 800; color: var(--yellow-dark); } .pprice { font-size: 112px; font-weight: 800; letter-spacing: -4px; margin-top: 8px; } .pper { font-size: 34px; color: #6B6B75; font-weight: 600; margin-bottom: 40px; }
.pcard ul { list-style: none; display: flex; flex-direction: column; gap: 22px; } .pcard li { display: flex; align-items: center; gap: 20px; font-size: 38px; font-weight: 600; } .pcard li svg { color: var(--green); flex: none; }
.stepn { position: absolute; right: 30px; top: 330px; font-size: 520px; font-weight: 800; line-height: 1; color: rgba(255,194,75,.07); letter-spacing: -20px; }
.dots { display: flex; gap: 14px; } .dots i { width: 90px; height: 12px; border-radius: 6px; background: rgba(255,255,255,.14); } .dots i.on { background: var(--yellow); }
.qcard { padding: 60px 56px; } .stars { color: var(--yellow); font-size: 56px; letter-spacing: 6px; }
.qhl { font-size: 60px; font-weight: 800; line-height: 1.12; margin: 24px 0; letter-spacing: -1px; } .qtext { font-size: 40px; line-height: 1.45; color: rgba(255,255,255,.78); font-weight: 500; }
.who { display: flex; align-items: center; gap: 24px; margin-top: 44px; } .who b { display: block; font-size: 36px; } .who span { font-size: 30px; color: var(--muted); font-weight: 600; }
.ava { width: 96px; height: 96px; border-radius: 50%; display: grid; place-items: center; font-size: 42px; font-weight: 800; background: var(--yellow); color: var(--dark); flex: none; }
.ava.xl { width: 260px; height: 260px; font-size: 100px; box-shadow: 0 0 0 14px rgba(255,194,75,.16), 0 30px 80px rgba(0,0,0,.4); }
.pills { display: flex; flex-wrap: wrap; gap: 18px; } .pill { padding: 26px 36px; border-radius: 999px; font-size: 38px; font-weight: 700; }
.pill:nth-child(odd) { background: rgba(255,194,75,.16); border-color: rgba(255,194,75,.32); color: var(--yellow); }
.doc { padding: 44px; display: flex; flex-direction: column; gap: 26px; background: #fff; } .dline { display: flex; align-items: center; gap: 22px; color: var(--green); } .dline i { height: 22px; border-radius: 11px; background: #E8E8EC; }
.ctaline { align-self: flex-start; font-size: 48px; font-weight: 800; padding: 30px 46px; border-radius: 999px; background: var(--yellow); color: var(--dark); box-shadow: 0 20px 60px rgba(255,194,75,.35); }
.foot { position: absolute; bottom: 190px; left: 90px; right: 90px; display: flex; justify-content: space-between; font-size: 30px; color: rgba(255,255,255,.45); font-weight: 700; }
.cover { position: absolute; inset: 0; display: grid; place-items: center; }
.cover .disc { width: 760px; height: 760px; border-radius: 50%; display: grid; place-items: center; background: var(--yellow); color: var(--dark);
  box-shadow: 0 0 0 20px rgba(255,194,75,.14), 0 40px 140px rgba(255,194,75,.35); }
.cover .disc svg { width: 280px; height: 280px; }
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
