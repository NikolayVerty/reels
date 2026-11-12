# index.html для ролика из выступления: 2ГИС — статистику даст менеджер.
import os
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUR=38.5
caps=[(0.08,"В 2ГИС статистику"),(1.86,"может дать менеджер"),(3.26,"Не бойтесь к ним обращаться"),(5.18,"у каждой карточки"),(6.12,"свой личный менеджер"),
(7.23,"«Мне нужно первое место —"),(8.95,"посмотреть трафик,"),(10.09,"сколько получает мой конкурент"),(11.63,"по нише, по городу»"),
(13.80,"Не бойтесь спрашивать"),(15.58,"и запрашивайте это"),(17.46,"перед тем, как"),(18.56,"оплачивать рекламу"),(20.90,"Смысл платить,"),(22.36,"если она не сработает?"),
(24.26,"Можно запросить статистику"),(26.18,"по рубрике в городе"),(28.18,"У менеджера:"),(29.46,"«Дай первое место —"),(31.10,"сколько показов, поисков,"),(32.76,"запросов по нише"),(34.60,"в нашем городе»"),
(35.41,"Так можно оценить"),(36.61,"потенциал и объём рынка")]
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
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
<video id="base" data-start="0" data-duration="{DUR}" data-track-index="0" src="assets/base.mp4" muted playsinline></video>
<audio id="voice" data-start="0" data-duration="{DUR}" data-track-index="1" src="assets/voice.wav" data-volume="1"></audio>
<div id="ov" class="clip" data-start="0" data-duration="{DUR}" data-track-index="2">
 <div id="lbl">Моё выступление · <b>Суровый Питерский форум</b></div>
 <div id="h">2ГИС бесплатно покажет <span>трафик конкурентов</span></div>
 <div id="bub"><small>Пишем личному менеджеру 2ГИС</small>«Сколько трафика у первого места в моей нише и городе?»</div>
 <div id="cmp"><div class="t">Статистика из 2ГИС от менеджера</div><div class="s">май–август 2025, с учётом медийной рекламы</div>
  <table><tr><th></th><th>10-е место</th><th>5–6-е место</th></tr>
  <tr id="r1"><td>Показы</td><td>26 981</td><td class="hi">63 321<span class="x">×2,3</span></td></tr>
  <tr id="r2"><td>Звонки</td><td>114</td><td class="hi">185</td></tr>
  <tr id="r3"><td>Маршруты</td><td>153</td><td class="hi">778<span class="x">×5</span></td></tr></table></div>
 <div id="pay"><div>СПРОСИ ДО ОПЛАТЫ РЕКЛАМЫ</div></div>
 <div id="fin"><div class="a">Сначала оцени рынок. <span>Потом плати.</span></div><div class="b">Разберу всё выступление по частям — подпишись</div></div>
 {"".join(CH)}
</div></div>
<script src="assets/gsap.min.js"></script><script>
window.__timelines=window.__timelines||{{}};
const tl=gsap.timeline({{paused:true}});
tl.fromTo("#lbl",{{opacity:0,y:-20}},{{opacity:1,y:0,duration:.3,ease:"power2.out"}},0.05);
tl.fromTo("#h",{{opacity:0,scale:1.25}},{{opacity:1,scale:1,duration:.35,ease:"expo.out",transformOrigin:"0 0"}},0.05);
tl.fromTo("#bub",{{opacity:0,y:60,rotation:-3}},{{opacity:1,y:0,rotation:-1.5,duration:.35,ease:"back.out(1.8)"}},7.15);
tl.set("#bub",{{opacity:0}},13.75);
tl.fromTo("#cmp",{{opacity:0,scale:.92}},{{opacity:1,scale:1,duration:.3,ease:"power3.out"}},13.80);
tl.from(["#r1","#r2","#r3"],{{opacity:0,x:-40,duration:.25,stagger:.35,ease:"power2.out"}},14.1);
tl.fromTo("#pay",{{opacity:0,scale:1.6}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},18.5);
tl.set(["#cmp","#pay"],{{opacity:0}},24.2);
tl.fromTo("#fin",{{opacity:0,scale:.9}},{{opacity:1,scale:1,duration:.3,ease:"expo.out"}},35.35);
{chr(10).join(JS)}
window.__timelines["main"]=tl;
</script></body></html>'''
open(os.path.join(P,'index.html'),'w',encoding='utf-8').write(html)
