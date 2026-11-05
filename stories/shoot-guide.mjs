// Схема съёмки: node stories/shoot-guide.mjs -> output/shoot-guide.png
import { createRequire } from 'node:module';
import path from 'node:path'; import { fileURLToPath } from 'node:url';
const { chromium } = createRequire(import.meta.url)('playwright');
const here = path.dirname(fileURLToPath(import.meta.url));
const font = [400,600,800].map(w=>['cyrillic','latin'].map(s=>`@font-face{font-family:'Manrope';font-weight:${w};src:url('file://${here}/fonts/manrope-${s}-${w}-normal.woff2')}`).join('')).join('');

// силуэт человека в кадре 9:16 (кадр 270x480)
const person = (x, chest, mic) => `
  <g transform="translate(${x} 0)">
    <circle cx="135" cy="${chest-150}" r="52" fill="#3a3a44"/>
    <path d="M40 480 C 40 ${chest-40}, 80 ${chest-75}, 135 ${chest-75} C 190 ${chest-75}, 230 ${chest-40}, 230 480Z" fill="#3a3a44"/>
    ${mic ? `<rect x="150" y="${chest-40}" width="34" height="70" rx="17" fill="#FFC24B"/><rect x="163" y="${chest+30}" width="8" height="130" fill="#FFC24B"/>` : ''}
  </g>`;
const frame = (inner, bg) => `<svg viewBox="0 0 270 480" class="phone">
  <rect width="270" height="480" rx="26" fill="${bg}"/>${inner}
  <rect x="0" y="0" width="270" height="68" fill="rgba(255,60,60,.10)"/><rect x="0" y="384" width="270" height="96" fill="rgba(255,60,60,.10)"/><rect x="212" y="68" width="58" height="316" fill="rgba(255,60,60,.10)"/>
  <line x1="0" y1="160" x2="270" y2="160" stroke="#FFC24B" stroke-dasharray="6 6" stroke-width="2"/>
  <text x="10" y="153" fill="#FFC24B" font-size="17" font-family="Manrope, Inter" font-weight="800">глаза — на этой линии</text>
  <rect x="2" y="2" width="266" height="476" rx="25" fill="none" stroke="#555" stroke-width="3"/></svg>`;

// вид сверху
const top = (items) => `<svg viewBox="0 0 300 300" class="topv"><rect width="300" height="220" rx="20" fill="#1A1A1F"/>${items}</svg>`;
const cam = (x,y,r,l)=>`<g transform="translate(${x} ${y}) rotate(${r})"><rect x="-14" y="-9" width="28" height="18" rx="4" fill="#FFC24B"/><path d="M14 -6 L28 -12 L28 12 L14 6Z" fill="#FFC24B"/></g><text x="${x-22}" y="${y+30}" fill="#FFC24B" font-size="17" font-family="Manrope, Inter" font-weight="800">${l}</text>`;
const you = (x,y)=>`<circle cx="${x}" cy="${y}" r="20" fill="#fff"/><text x="${x-12}" y="${y+5}" font-size="17" font-family="Manrope, Inter" font-weight="800">Вы</text>`;
const light = (x,y,l)=>`<circle cx="${x}" cy="${y}" r="16" fill="#fff8" /><text x="${x-30}" y="${y-22}" fill="#ccc" font-size="16" font-family="Manrope, Inter" font-weight="600">${l}</text>`;

const cols = [
 { t:'Кухня, днём', s:'Рилсы 01 и 02', bg:'#2b2620', f: person(0,330,false),
   top: top(`<rect x="0" y="0" width="300" height="14" fill="#7dd3fc88"/><text x="110" y="34" fill="#7dd3fc" font-size="17" font-family="Manrope, Inter" font-weight="800">окно</text>${you(150,90)}${cam(150,185,-90,'телефон')}<line x1="150" y1="110" x2="150" y2="165" stroke="#555" stroke-dasharray="4 4"/><text x="160" y="145" fill="#999" font-size="16" font-family="Manrope, Inter">1–1,2 м</text>`),
   li:['Окно спереди-сбоку, не за спиной','Телефон на штативе на уровне глаз','Основная камера, не фронталка, 4K','Кадр по грудь, сзади видно кухню','Петличка или микрофон за кадром','Первый кадр с движением: 01 ставишь кружку, 02 кусаешь шаурму'] },
 { t:'Студия-подкаст', s:'Рилс 03 (и будущий кейс 05)', bg:'#15151a', f: person(0,330,true),
   top: top(`<rect x="70" y="90" width="160" height="40" rx="8" fill="#25252C"/><text x="128" y="115" fill="#888" font-size="16" font-family="Manrope, Inter">стол</text>${you(150,60)}${cam(150,190,-90,'камера 1')}${cam(255,150,-140,'2')}${light(40,170,'свет 45°')}${light(150,14,'контр')}`),
   li:['Сидишь за столом, кадр по пояс','Подкастный микрофон в кадре','Камера 1 анфас, камера 2 сбоку 30–45°','Свет: софтбокс спереди-сбоку + контровой','Фон тёмный, жёлтая подсветка — цвет сайта','Первый кадр: жест «стоп» рукой'] },
 { t:'Экран + голос', s:'Рилс 04', bg:'#0F0F12', f: `<rect x="20" y="90" width="230" height="200" rx="14" fill="#fff"/><rect x="36" y="110" width="120" height="14" rx="7" fill="#ddd"/><rect x="36" y="140" width="198" height="60" rx="10" fill="#FFF6E0"/><rect x="36" y="214" width="60" height="60" rx="8" fill="#FFC24B"/><rect x="104" y="214" width="60" height="60" rx="8" fill="#eee"/><rect x="172" y="214" width="60" height="60" rx="8" fill="#eee"/><circle cx="200" cy="330" r="34" fill="#3a3a44" stroke="#FFC24B" stroke-width="4"/><text x="150" y="380" fill="#999" font-size="16" font-family="Manrope, Inter">лицо кружком</text>`,
   top: top(`<rect x="90" y="40" width="120" height="70" rx="8" fill="#25252C"/><text x="118" y="80" fill="#888" font-size="16" font-family="Manrope, Inter">ноутбук</text>${you(150,160)}<text x="20" y="230" fill="#999" font-size="16" font-family="Manrope, Inter">экран + голос в петличку</text>`),
   li:['Запись экрана кабинета Яндекс Бизнеса','Масштаб 150–200%, курсор двигается с первой секунды','Голос — петличка, тихая комната','Последние 3 строки — лицом в камеру (кухня или студия)','Если есть — снять на телефон, как наводят камеру на QR','Чужие данные в кабинете не показывать'] },
];
const html = `<!doctype html><html><head><meta charset="utf-8"><style>${font}
*{margin:0;padding:0;box-sizing:border-box} body{width:1800px;font-family:'Manrope','Inter',sans-serif;background:#0F0F12;color:#fff;padding:60px}
h1{font-size:56px;font-weight:800;letter-spacing:-1px} .sub{color:#94949E;font-size:24px;margin:10px 0 40px;font-weight:600}
.row{display:grid;grid-template-columns:repeat(3,1fr);gap:40px}
.c{background:#1A1A1F;border-radius:32px;padding:34px;border:2px solid rgba(255,255,255,.07)}
.k{color:#F5A623;font-weight:800;font-size:18px;text-transform:uppercase;letter-spacing:2px} h2{font-size:38px;font-weight:800;margin:6px 0 24px}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:start} .phone{width:100%} .topv{width:100%}
.cap{color:#94949E;font-size:15px;font-weight:600;margin:8px 0 0} ul{margin-top:24px;list-style:none;display:grid;gap:12px}
li{font-size:21px;line-height:1.35;padding-left:30px;position:relative;font-weight:600} li:before{content:'';position:absolute;left:0;top:8px;width:14px;height:14px;border-radius:4px;background:#FFC24B}
.legend{margin-top:34px;color:#94949E;font-size:20px;font-weight:600} .legend b{color:#ff8a8a}
</style></head><body><h1>Как и где снимаем</h1><div class="sub">3 локации · вертикально 9:16 · каждая строка текста — отдельный дубль</div>
<div class="row">${cols.map(c=>`<div class="c"><div class="k">${c.s}</div><h2>${c.t}</h2><div class="pair"><div>${frame(c.f,c.bg)}<div class="cap">Кадр в телефоне</div></div><div>${c.top}<div class="cap">Вид сверху</div></div></div><ul>${c.li.map(x=>`<li>${x}</li>`).join('')}</ul></div>`).join('')}</div>
<div class="legend"><b>Красные зоны</b> в кадре закрывают кнопки и подпись Instagram — туда не ставим лицо и важное. Жёлтая линия — уровень глаз.</div>
</body></html>`;
const b = await chromium.launch(); const p = await b.newPage({ viewport:{width:1800,height:1000}, deviceScaleFactor: 1 });
await p.setContent(html); await p.waitForTimeout(200);
await p.screenshot({ path: path.join(here,'..','output','shoot-guide.png'), fullPage: true }); await b.close(); console.log('ok');
