# index.html для ролика из выступления: 2ГИС — статистику даст менеджер.
import os
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUR=42.87
caps=[(0.05,"Куда вы пойдёте?"),(1.92,"Предугадаю: вариант слева"),(4.42,"Почему?"),(5.18,"Понятный, высокий рейтинг"),(6.86,"много оценок"),
(8.78,"Понятная упаковка"),(9.86,"есть сторис,"),(10.84,"скидка, лид-магнит"),(13.68,"можно сразу забронировать столик"),
(15.67,"Справа рейтинг ниже,"),(17.27,"мало оценок,"),(17.73,"непонятная упаковка"),(18.97,"нет форм захвата"),
(21.72,"Конечно, выберем левый"),(23.82,"Не занимаешься геосервисами —"),(26.26,"клиенты просто уходят"),
(27.87,"Клиент перед покупкой"),(31.41,"точно проверит"),(32.39,"вашу репутацию в сети"),
(34.02,"Поэтому я всем говорю:"),(35.98,"даже если у вас Яндекс Директ,"),(37.66,"даже если таргет ВК —"),(40.04,"люди будут смотреть"),(41.06,"репутацию организации")]
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
.hl{{position:absolute;left:24px;top:286px;width:300px;height:545px;border:8px solid var(--ok);border-radius:18px;opacity:0}}
.hl2{{position:absolute;left:736px;top:286px;width:312px;height:545px;border:8px solid #E5484D;border-radius:18px;opacity:0}}
#cmp2{{position:absolute;left:30px;top:282px;width:1020px;height:590px;background:#fff;border-radius:28px;box-sizing:border-box;padding:34px 30px;display:flex;gap:24px;opacity:0}}
#cmp2 .col{{flex:1;border-radius:20px;padding:22px 24px}}
#cmp2 .good{{background:#EAF7EE}} #cmp2 .bad{{background:#F4F4F2}}
#cmp2 .hd{{font-weight:800;font-size:44px;margin-bottom:18px}} #cmp2 .good .hd{{color:var(--ok)}} #cmp2 .bad .hd{{color:#8a8a85}}
#cmp2 .it{{font-weight:700;font-size:36px;line-height:1.15;color:var(--ink);padding:14px 0 14px 46px;position:relative}}
#cmp2 .it:before{{content:"";position:absolute;left:0;top:20px;width:26px;height:26px;border-radius:50%}}
#cmp2 .good .it:before{{background:var(--ok)}} #cmp2 .bad .it:before{{background:#E5484D}}
#pay2{{position:absolute;left:0;right:0;top:790px;display:flex;justify-content:center;opacity:0}}
#pay2 div{{background:var(--ink);color:var(--y);font-weight:800;font-size:44px;padding:12px 26px;border:4px solid var(--y)}}
#pay div{{background:#E5484D!important;color:#fff!important;border-color:#fff!important}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
<video id="base" data-start="0" data-duration="{DUR}" data-track-index="0" src="assets/base.mp4" muted playsinline></video>
<audio id="voice" data-start="0" data-duration="{DUR}" data-track-index="1" src="assets/voice.wav" data-volume="1"></audio>
<div id="ov" class="clip" data-start="0" data-duration="{DUR}" data-track-index="2">
 <div id="lbl">Моё выступление · <b>Суровый Питерский форум</b></div>
 <div id="h">Почему клиент уходит к соседу <span>ещё до звонка</span></div>
 <div id="hlL" class="hl"></div><div id="hlR" class="hl2"></div>
 <div id="cmp2"><div class="col good"><div class="hd">Слева · ★ 4,9</div>
   <div class="it" id="g1">Высокий рейтинг</div><div class="it" id="g2">Много оценок</div><div class="it" id="g3">Сторис и скидка</div><div class="it" id="g4">Бронь в один клик</div></div>
  <div class="col bad"><div class="hd">Справа · ★ 4,2</div>
   <div class="it" id="b1">Рейтинг ниже</div><div class="it" id="b2">Мало оценок</div><div class="it" id="b3">Непонятная упаковка</div><div class="it" id="b4">Нет захвата заявки</div></div></div>
 <div id="pay"><div>КЛИЕНТЫ УХОДЯТ К СОСЕДУ</div></div>
 <div id="pay2"><div>РЕКЛАМА ПРИВОДИТ — КАРТОЧКА РЕШАЕТ</div></div>
 {"".join(CH)}
</div></div>
<script src="assets/gsap.min.js"></script><script>
window.__timelines=window.__timelines||{{}};
const tl=gsap.timeline({{paused:true}});
tl.fromTo("#lbl",{{opacity:0,y:-20}},{{opacity:1,y:0,duration:.3,ease:"power2.out"}},0.05);
tl.fromTo("#h",{{opacity:0,scale:1.25}},{{opacity:1,scale:1,duration:.35,ease:"expo.out",transformOrigin:"0 0"}},0.05);
tl.fromTo("#hlL",{{opacity:0,scale:1.08}},{{opacity:1,scale:1,duration:.25,ease:"back.out(2)"}},3.5);
tl.set("#hlL",{{opacity:0}},4.4);
tl.fromTo("#cmp2",{{opacity:0,scale:.92}},{{opacity:1,scale:1,duration:.3,ease:"power3.out"}},4.42);
const T={{g1:5.18,g2:6.86,g3:9.86,g4:13.68,b1:15.67,b2:17.27,b3:17.73,b4:18.97}};
for(const k in T) tl.from("#"+k,{{opacity:0,x:-30,duration:.22,ease:"power2.out"}},T[k]);
tl.from(".bad",{{opacity:0,duration:.25}},15.6);
tl.set("#cmp2",{{opacity:0}},21.7);
tl.fromTo("#hlR",{{opacity:0,scale:1.08}},{{opacity:1,scale:1,duration:.25,ease:"back.out(2)"}},23.82);
tl.fromTo("#pay",{{opacity:0,scale:1.6}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},26.26);
tl.set(["#hlR","#pay"],{{opacity:0}},27.8);
tl.fromTo("#pay2",{{opacity:0,scale:1.6}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},40.0);
{chr(10).join(JS)}
window.__timelines["main"]=tl;
</script></body></html>'''
open(os.path.join(P,'index.html'),'w',encoding='utf-8').write(html)
