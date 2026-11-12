# index.html для ролика из выступления: 2ГИС — статистику даст менеджер.
import os
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUR=53.64
caps=[(0.04,"Кейс автосалона:"),(0.90,"автосалоны в Минводах,"),(3.48,"Пятигорске"),(4.10,"На входе — плохая упаковка,"),(6.42,"так себе фотографии,"),(7.96,"прайс без SEO"),
(9.72,"Очень много негатива,"),(11.44,"проблемы с репутацией"),(12.82,"и никакой рекламы"),(14.98,"Слева — как было до:"),(18.58,"к упаковке много вопросов,"),(20.68,"товары навалены как попало"),
(22.58,"Справа — уже есть магниты,"),(25.04,"сторис, которые захватывают"),(26.94,"и ведут на предложение"),(29.64,"Есть шапка, понятная витрина"),
(31.20,"Что сделали:"),(31.48,"внедрили SEO в прайс,"),(33.30,"переписали с SEO-ключами,"),(36.42,"внедрили сквозную аналитику —"),(37.72,"видеть, что работает,"),(40.56,"переработали рекламу"),
(42.20,"И на выходе такие цифры:"),(44.50,"лид до 500 рублей,"),(47.66,"статистика постоянно растёт"),(49.32,"В итоге —"),(51.44,"хорошая работающая система")]
CH=[]; JS=[]
for i,(t,txt) in enumerate(caps):
    end=caps[i+1][0] if i+1<len(caps) else DUR
    CH.append(f'<div class="prow"><div class="plq" id="c{i}">{txt}</div></div>')
    JS.append(f'tl.fromTo("#c{i}",{{opacity:0,y:12,scale:.9}},{{opacity:1,y:0,scale:1,duration:.14,ease:"back.out(2.2)"}},{t});tl.set("#c{i}",{{opacity:0}},{end});')
html=f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><style>
@font-face{{font-family:Manrope;font-weight:500;src:url(assets/fonts/manrope-cyrillic-500-normal.woff2)}}
@font-face{{font-family:Manrope;font-weight:700;src:url(assets/fonts/manrope-cyrillic-700-normal.woff2)}}
@font-face{{font-family:Manrope;font-weight:800;src:url(assets/fonts/manrope-cyrillic-800-normal.woff2)}}
@font-face{{font-family:Manrope;font-weight:800;src:url(assets/fonts/manrope-latin-800-normal.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:Manrope;font-weight:700;src:url(assets/fonts/manrope-latin-700-normal.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:Play;font-style:italic;font-weight:800;src:url(assets/fonts/playfair-display-cyrillic-800-italic.woff2)}}
:root{{--y:#FFC24B;--ink:#0F0F12;--gr:#1A1A1F;--ok:#16A34A}}
html,body{{margin:0;background:#000}}
#root{{position:relative;width:1080px;height:1920px;overflow:hidden;background:var(--ink);font-family:Manrope,sans-serif}}
#base{{position:absolute;inset:0;width:1080px;height:1920px}}
#ov{{position:absolute;inset:0}}
#lbl{{position:absolute;left:60px;top:58px;font-weight:700;font-size:28px;color:#9a9aa3;letter-spacing:.5px}}
#lbl b{{color:var(--y)}}
#h{{position:absolute;left:60px;top:100px;width:960px;font-weight:800;font-size:66px;line-height:1.02;color:#fff}}
#h span{{color:var(--y)}}
.prow{{position:absolute;left:0;right:0;top:1340px;display:flex;justify-content:center}}
.plq{{background:var(--y);color:var(--ink);font-weight:800;font-size:56px;line-height:1.1;padding:10px 26px 14px;white-space:nowrap;box-shadow:6px 6px 0 var(--ink);opacity:0}}
#bub{{position:absolute;left:70px;top:600px;width:860px;background:#fff;border:5px solid var(--ink);border-radius:36px 36px 36px 6px;padding:26px 34px;font-weight:700;font-size:44px;line-height:1.2;color:var(--ink);box-shadow:10px 10px 0 var(--y);opacity:0}}
#bub small{{display:block;font-size:26px;color:#777;margin-bottom:8px}}
#cmp{{position:absolute;left:30px;top:282px;width:1020px;height:590px;background:#fff;border-radius:28px;box-sizing:border-box;padding:34px 40px;opacity:0}}
#cmp .t{{font-weight:800;font-size:40px;color:var(--ink)}}
#cmp .s{{font-weight:500;font-size:24px;color:#777;margin-top:4px}}
#cmp table{{width:100%;margin-top:26px;border-collapse:collapse;font-variant-numeric:tabular-nums}}
#cmp th{{font-size:28px;color:#777;font-weight:700;text-align:right;padding:6px 0}}
#cmp th:first-child,#cmp td:first-child{{text-align:left}}
#cmp td{{font-size:44px;font-weight:800;color:var(--ink);text-align:right;padding:12px 0;border-top:2px solid #eee}}
#cmp td.hi{{color:var(--ok)}}
#cmp td .x{{display:inline-block;margin-left:12px;font-size:28px;background:var(--y);padding:2px 10px;border-radius:8px;color:var(--ink);vertical-align:middle}}
#pay{{position:absolute;left:0;right:0;top:780px;display:flex;justify-content:center;opacity:0}}
#pay div{{background:var(--ink);color:var(--y);font-weight:800;font-size:46px;padding:12px 28px;border:4px solid var(--y)}}
#fin{{position:absolute;left:30px;top:282px;width:1020px;height:590px;background:var(--ink);border:4px solid var(--y);border-radius:28px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:center;padding:0 50px;opacity:0}}
#fin .a{{font-family:Play;font-style:italic;font-weight:800;font-size:96px;line-height:1.02;color:#fff}}
#fin .a span{{color:var(--y)}}
#fin .b{{margin-top:30px;font-weight:700;font-size:34px;color:#c9c9d1}}
#st,#res{{position:absolute;left:30px;top:282px;width:1020px;height:590px;background:#fff;border-radius:28px;box-shadow:0 0 0 40px var(--ink);box-sizing:border-box;padding:34px 46px;opacity:0}}
#st .t,#res .t{{font-weight:800;font-size:44px;color:var(--ink)}} #st .s,#res .s{{font-weight:500;font-size:24px;color:#777;margin:4px 0 18px}}
#st .it{{font-weight:800;font-size:48px;line-height:1.1;color:var(--ink);padding:16px 0 16px 64px;position:relative;border-top:2px solid #eee}}
#st .it:before{{content:"";position:absolute;left:0;top:24px;width:38px;height:38px;border-radius:50%;background:var(--ok)}}
#res .row{{display:flex;align-items:baseline;gap:24px;padding:16px 0;border-top:2px solid #eee}}
#res .v{{font-weight:800;font-size:130px;line-height:1;color:var(--ok);font-variant-numeric:tabular-nums}} #res .k{{font-weight:700;font-size:40px;color:#555}}
.hl{{position:absolute;left:24px;top:410px;width:470px;height:460px;border:8px solid #E5484D;border-radius:18px;opacity:0}}
.hl2{{position:absolute;left:530px;top:410px;width:478px;height:460px;border:8px solid var(--ok);border-radius:18px;opacity:0}}
#pay{{position:absolute;left:0;right:0;top:790px;display:flex;justify-content:center;opacity:0}}
#bub2{{position:absolute;left:70px;top:620px;width:820px;background:#fff;border:5px solid var(--ink);border-radius:36px 36px 36px 6px;padding:24px 32px;font-weight:700;font-size:46px;color:var(--ink);box-shadow:10px 10px 0 var(--y);opacity:0}}
#pay2{{position:absolute;left:0;right:0;top:790px;display:flex;justify-content:center;opacity:0}}
#pay2 div{{background:#E5484D;color:#fff;font-weight:800;font-size:33px;padding:12px 22px;border:4px solid #fff;white-space:nowrap}}
#pay div{{background:var(--ink)!important;color:var(--y)!important;border-color:var(--y)!important;font-size:34px!important;white-space:nowrap}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
<video id="base" data-start="0" data-duration="{DUR}" data-track-index="0" src="assets/base.mp4" muted playsinline></video>
<audio id="voice" data-start="0" data-duration="{DUR}" data-track-index="1" src="assets/voice.wav" data-volume="1"></audio>
<div id="ov" class="clip" data-start="0" data-duration="{DUR}" data-track-index="2">
 <div id="lbl">Моё выступление · <b>Суровый Питерский форум</b></div>
 <div id="h">Как автосалон получает лиды <span>по 439 ₽ с карт</span></div>
 <div id="pay"><div>НА СТАРТЕ: С КАРТ 4–5% РЫНКА, У КОНКУРЕНТА 23%</div></div>
 <div id="hlL" class="hl"></div><div id="hlR" class="hl2"></div>
 <div id="st"><div class="t">Что сделали</div><div class="s">слайд выступления</div>
  <div class="it" id="i1">SEO в прайсе</div><div class="it" id="i2">SEO-ключи в описаниях</div><div class="it" id="i3">Сквозная аналитика + CRM</div><div class="it" id="i4">Новая рекламная кампания</div></div>
 <div id="res"><div class="t">Результат за 8 месяцев</div><div class="s">статистика Яндекса, слайд выступления</div>
  <div class="row"><div class="v g">2 318</div><div class="k">лидов</div></div>
  <div class="row"><div class="v g">439 ₽</div><div class="k">средняя цена лида</div></div></div>
 <div id="pay2"><div>РАБОТАЮЩАЯ СИСТЕМА, А НЕ РАЗОВАЯ РЕКЛАМА</div></div>
 {"".join(CH)}
</div></div>
<script src="assets/gsap.min.js"></script><script>
window.__timelines=window.__timelines||{{}};
const tl=gsap.timeline({{paused:true}});
tl.fromTo("#lbl",{{opacity:0,y:-20}},{{opacity:1,y:0,duration:.3,ease:"power2.out"}},0.05);
tl.fromTo("#h",{{opacity:0,scale:1.25}},{{opacity:1,scale:1,duration:.35,ease:"expo.out",transformOrigin:"0 0"}},0.05);
tl.fromTo("#pay",{{opacity:0,scale:1.5}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},5.0);
tl.set("#pay",{{opacity:0}},14.9);
tl.fromTo("#hlL",{{opacity:0,scale:1.06}},{{opacity:1,scale:1,duration:.25,ease:"back.out(2)"}},14.98);
tl.set("#hlL",{{opacity:0}},22.5);
tl.fromTo("#hlR",{{opacity:0,scale:1.06}},{{opacity:1,scale:1,duration:.25,ease:"back.out(2)"}},22.58);
tl.set("#hlR",{{opacity:0}},31.1);
tl.fromTo("#st",{{opacity:0,scale:.92}},{{opacity:1,scale:1,duration:.3,ease:"power3.out"}},31.15);
const T={{i1:31.48,i2:33.30,i3:36.42,i4:40.56}};
for(const k in T) tl.from("#"+k,{{opacity:0,x:-40,duration:.25,ease:"power2.out"}},T[k]);
tl.set("#st",{{opacity:0}},44.4);
tl.fromTo("#res",{{opacity:0,scale:.92}},{{opacity:1,scale:1,duration:.3,ease:"power3.out"}},44.45);
tl.from("#res .row",{{opacity:0,x:-40,duration:.3,stagger:.9,ease:"power2.out"}},44.7);

tl.fromTo("#pay2",{{opacity:0,scale:1.5}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},51.4);
{chr(10).join(JS)}
window.__timelines["main"]=tl;
</script></body></html>'''
open(os.path.join(P,'index.html'),'w',encoding='utf-8').write(html)
