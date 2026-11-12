# index.html для ролика из выступления: 2ГИС — статистику даст менеджер.
import os
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUR=50.67
caps=[(0.04,"Как репутация влияет на бизнес?"),(1.92,"Где репутация меньше —"),(4.92,"там меньше трафика"),(6.04,"Большой процент отказов:"),(8.04,"люди просто уходят"),
(9.14,"Из-за этого Яндекс"),(11.76,"может пессимизировать карточку —"),(13.76,"понижать,"),(14.44,"понимая, что это неинтересно"),
(16.58,"Изменение рейтинга"),(18.18,"повлияло на отказы"),(20.22,"Отказ — это люди зашли,"),(21.90,"посмотрели, что-то не устроило"),(23.00,"и быстро ушли"),(24.12,"И карточку сразу понижают"),
(26.14,"Мне недавно позвонили:"),(27.84,"«Не хотите купить франшизу?»"),(29.08,"Покупать я не собирался —"),(30.66,"спортивный интерес"),
(32.38,"Зашёл в их магазины на картах"),(34.52,"а там репутация"),(35.86,"не очень хорошая"),(37.08,"Это влияет на масштабирование:"),
(39.34,"покупатель франшизы зайдёт,"),(41.28,"увидит плохую репутацию"),(43.86,"и продажа франшизы"),(45.60,"будет затруднена"),(46.86,"или продаж будет мало"),(49.40,"Доверия будет немного")]
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
#st{{position:absolute;left:30px;top:282px;width:1020px;height:590px;background:#fff;border-radius:28px;box-shadow:0 0 0 40px var(--ink);box-sizing:border-box;padding:34px 46px;opacity:0}}
#st .t{{font-weight:800;font-size:44px;color:var(--ink)}} #st .s{{font-weight:500;font-size:24px;color:#777;margin:4px 0 22px}}
#st .row{{display:flex;align-items:center;gap:26px;padding:14px 0;border-top:2px solid #eee}}
#st .k{{width:250px;font-weight:700;font-size:40px;color:#555}} #st .v{{font-weight:800;font-size:96px;color:var(--ink);font-variant-numeric:tabular-nums}}
#st .v.g{{color:var(--ok)}} #st .v.r{{color:#E5484D}} #st .ar{{font-weight:800;font-size:70px;color:#bbb}}
#st .def{{margin-top:14px;font-weight:700;font-size:32px;background:var(--y);display:inline-block;padding:8px 18px;color:var(--ink)}}
#bub2{{position:absolute;left:70px;top:620px;width:820px;background:#fff;border:5px solid var(--ink);border-radius:36px 36px 36px 6px;padding:24px 32px;font-weight:700;font-size:46px;color:var(--ink);box-shadow:10px 10px 0 var(--y);opacity:0}}
#pay2{{position:absolute;left:0;right:0;top:790px;display:flex;justify-content:center;opacity:0}}
#pay2 div{{background:#E5484D;color:#fff;font-weight:800;font-size:33px;padding:12px 22px;border:4px solid #fff;white-space:nowrap}}
#pay div{{background:#E5484D!important;color:#fff!important;border-color:#fff!important}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
<video id="base" data-start="0" data-duration="{DUR}" data-track-index="0" src="assets/base.mp4" muted playsinline></video>
<audio id="voice" data-start="0" data-duration="{DUR}" data-track-index="1" src="assets/voice.wav" data-volume="1"></audio>
<div id="ov" class="clip" data-start="0" data-duration="{DUR}" data-track-index="2">
 <div id="lbl">Моё выступление · <b>Суровый Питерский форум</b></div>
 <div id="h">Плохой рейтинг — и Яндекс <span>сам опускает тебя в выдаче</span></div>
 <div id="st"><div class="t">Кейс: автосалон</div><div class="s">рейтинг и отказы в карточке, слайд выступления</div>
  <div class="row"><div class="k">Рейтинг</div><div class="v">4,4</div><div class="ar">→</div><div class="v g">5,0</div></div>
  <div class="row"><div class="k">Отказы</div><div class="v r">88%</div><div class="ar">→</div><div class="v g">55%</div></div>
  <div class="def" id="def">Отказ = зашёл, посмотрел, не понравилось — ушёл</div></div>
 <div id="pay"><div>КАРТОЧКУ ОПУСКАЮТ В ВЫДАЧЕ</div></div>
 <div id="bub2">«Не хотите купить нашу франшизу?»</div>
 <div id="pay2"><div>ПЛОХАЯ РЕПУТАЦИЯ РЕЖЕТ ДАЖЕ ПРОДАЖУ ФРАНШИЗЫ</div></div>
 {"".join(CH)}
</div></div>
<script src="assets/gsap.min.js"></script><script>
window.__timelines=window.__timelines||{{}};
const tl=gsap.timeline({{paused:true}});
tl.fromTo("#lbl",{{opacity:0,y:-20}},{{opacity:1,y:0,duration:.3,ease:"power2.out"}},0.05);
tl.fromTo("#h",{{opacity:0,scale:1.25}},{{opacity:1,scale:1,duration:.35,ease:"expo.out",transformOrigin:"0 0"}},0.05);
tl.fromTo("#st",{{opacity:0,scale:.92}},{{opacity:1,scale:1,duration:.3,ease:"power3.out"}},16.5);
tl.from("#st .row",{{opacity:0,x:-40,duration:.25,stagger:.5,ease:"power2.out"}},16.8);
tl.fromTo("#def",{{opacity:0,y:20}},{{opacity:1,y:0,duration:.25,ease:"back.out(2)"}},20.22);
tl.set("#def",{{opacity:0}},24.3);
tl.fromTo("#pay",{{opacity:0,scale:1.6}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},24.3);
tl.set(["#st","#pay"],{{opacity:0}},26.05);
tl.fromTo("#bub2",{{opacity:0,y:60,rotation:-3}},{{opacity:1,y:0,rotation:-1.5,duration:.35,ease:"back.out(1.8)"}},27.7);
tl.set("#bub2",{{opacity:0}},32.3);
tl.fromTo("#pay2",{{opacity:0,scale:1.5}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},45.6);
{chr(10).join(JS)}
window.__timelines["main"]=tl;
</script></body></html>'''
open(os.path.join(P,'index.html'),'w',encoding='utf-8').write(html)
