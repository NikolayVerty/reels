# Ролик 07 «Любой может поменять тебе телефон»: полноэкранная голова + коллажи (стиль ролика 01), запись экрана в телефоне.
import json, os, re
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUR=58.49
caps=[(0.0,"Любой человек может зайти"),(1.12,"к тебе в карточку"),(1.78,"и поменять телефон"),(2.88,"Да, любой"),
(3.76,"В Картах есть кнопка"),(5.38,"«Исправить»"),(6.30,"можно исправить"),(7.30,"любую информацию:"),(8.16,"сайт, контакты —"),(9.26,"всё что угодно"),
(10.10,"Правку может предложить"),(11.04,"кто угодно:"),(11.96,"бывший сотрудник,"),(13.22,"обиженный клиент"),(14.60,"или твой конкурент"),
(15.68,"Если ты не следишь —"),(16.60,"правку могут принять"),
(17.70,"Поменяли сайт —"),(18.58,"клиент уходит к другому"),(19.74,"Поменяли телефон —"),(20.82,"звонки не поступают"),(22.44,"Поставили «закрыто»"),(23.42,"в твой хлебный день —"),(24.74,"клиенты не приходят"),
(26.18,"Ты теряешь деньги"),(27.08,"и не понимаешь почему"),(28.22,"Узнаёшь, только когда"),(30.16,"клиент скажет:"),(31.16,"«Я звонил —"),(31.70,"никто не ответил»"),
(32.74,"А вторая беда — галочка"),(33.40,"«Информация подтверждена»"),(34.70,"Не обновлял 3 месяца —"),(36.36,"её просто снимают"),
(37.42,"Без неё ты падаешь"),(39.70,"в выдаче"),(40.42,"и клиенты уходят"),(41.14,"к тем, у кого она есть"),
(42.80,"Зайди в Яндекс Бизнес"),(44.20,"→ «История изменений»"),(45.32,"Посмотри, кто что менял"),(46.68,"Сверь телефон, сайт,"),(47.86,"график работы"),(48.94,"Всё ли актуально?"),(50.30,"Пять минут"),
(50.88,"Не следишь за карточкой ты —"),(52.26,"за тебя её правят другие"),
(53.70,"Пиши «КАРТЫ» под роликом"),(54.96,"или в директ —"),(55.54,"пришлю, что проверять"),(57.24,"каждый месяц")]
CH=[];JS=[]
for i,(t,txt) in enumerate(caps):
    end=caps[i+1][0] if i+1<len(caps) else DUR
    CH.append(f'<div class="prow"><div class="plq" id="cp{i}">{txt}</div></div>')
    JS.append(f'tl.fromTo("#cp{i}",{{opacity:0,y:12,scale:.9}},{{opacity:1,y:0,scale:1,duration:.13,ease:"back.out(2.2)"}},{t});tl.set("#cp{i}",{{opacity:0}},{end});')
html=f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><style>
@font-face{{font-family:Manrope;font-weight:500;src:url(assets/fonts/manrope-cyrillic-500-normal.woff2)}}
@font-face{{font-family:Manrope;font-weight:700;src:url(assets/fonts/manrope-cyrillic-700-normal.woff2)}}
@font-face{{font-family:Manrope;font-weight:800;src:url(assets/fonts/manrope-cyrillic-800-normal.woff2)}}
@font-face{{font-family:Manrope;font-weight:800;src:url(assets/fonts/manrope-latin-800-normal.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:Play;font-style:italic;font-weight:800;src:url(assets/fonts/playfair-display-cyrillic-800-italic.woff2)}}
:root{{--y:#FFC24B;--ink:#0F0F12;--gr:#1A1A1F;--ok:#16A34A;--bad:#E5484D;--paper:#ECEBE6}}
html,body{{margin:0;background:#000}}
#root{{position:relative;width:1080px;height:1920px;overflow:hidden;background:var(--paper);font-family:Manrope,sans-serif}}
#bg{{position:absolute;inset:0;background-image:linear-gradient(rgba(15,15,18,.07) 2px,transparent 2px),linear-gradient(90deg,rgba(15,15,18,.07) 2px,transparent 2px),linear-gradient(rgba(15,15,18,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(15,15,18,.035) 1px,transparent 1px);background-size:120px 120px,120px 120px,24px 24px,24px 24px}}
#camwrap{{position:absolute;left:0;top:0;width:1080px;height:1920px;transform-origin:0 0;z-index:2;overflow:hidden}}
#camzoom{{position:absolute;inset:0;transform-origin:50% 30%}}
#cam{{width:1080px;height:1920px;object-fit:cover;display:block}}
#shade{{position:absolute;inset:0;background:rgba(10,10,14,.72);opacity:0}}
#frame{{position:absolute;inset:0;border:34px solid #fff;box-sizing:border-box;opacity:0}}
#ov{{position:absolute;inset:0;z-index:3}}
.prow{{position:absolute;left:0;right:0;top:1330px;display:flex;justify-content:center}}
.plq{{background:var(--y);color:var(--ink);font-weight:800;font-size:56px;line-height:1.1;padding:10px 26px 14px;white-space:nowrap;box-shadow:6px 6px 0 var(--ink);opacity:0}}
.hd{{position:absolute;left:60px;top:240px;width:960px;font-weight:800;font-size:92px;line-height:1.02;color:#fff;text-shadow:0 6px 30px rgba(0,0,0,.5);opacity:0}}
.hd span{{color:var(--y)}}
#h1{{text-shadow:none}} #h1 i{{font-style:normal;display:inline-block;background:var(--ink);color:#fff;padding:6px 20px;margin-bottom:10px;box-shadow:8px 8px 0 var(--y)}} #h1 i.y{{background:var(--y);color:var(--ink);box-shadow:8px 8px 0 var(--ink)}}
.sec{{position:absolute;left:50px;top:250px;width:980px;opacity:0}}
.ttl{{font-weight:800;font-size:80px;line-height:1.05;color:var(--ink);margin-bottom:26px}}
.ttl span{{background:linear-gradient(transparent 20%,var(--y) 20%,var(--y) 90%,transparent 90%);padding:0 8px}}
#phone{{position:absolute;left:300px;top:230px;width:480px;height:1041px;border:12px solid var(--ink);border-radius:56px;overflow:hidden;background:#fff;box-shadow:16px 16px 0 rgba(15,15,18,.18);opacity:0}}
#scr{{width:480px;height:1041px;object-fit:cover;display:block}}
#tagBtn{{position:absolute;left:40px;top:330px;background:var(--y);border:5px solid var(--ink);box-shadow:8px 8px 0 var(--ink);font-weight:800;font-size:46px;padding:10px 22px;transform:rotate(-5deg);opacity:0}}
.who{{display:flex;align-items:center;gap:24px;background:#fff;border:5px solid var(--ink);box-shadow:8px 8px 0 var(--ink);padding:26px 32px;margin-bottom:38px;font-weight:800;font-size:64px;color:var(--ink)}}
.who b{{flex:none;width:76px;height:76px;border-radius:50%;background:var(--bad);color:#fff;display:flex;align-items:center;justify-content:center;font-size:44px}}
.row{{display:flex;flex-direction:column;align-items:flex-start;gap:4px;background:#fff;border:5px solid var(--ink);box-shadow:8px 8px 0 var(--ink);padding:22px 30px;margin-bottom:34px}}
.row .k{{font-weight:800;font-size:62px;color:var(--ink);white-space:nowrap}}
.row .ar{{display:none}}
.row .v{{font-weight:800;font-size:50px;color:var(--bad);line-height:1.1}}
#badge{{display:inline-flex;align-items:center;gap:18px;background:#fff;border:5px solid var(--ink);box-shadow:8px 8px 0 var(--ink);padding:26px 30px;font-weight:800;font-size:56px;color:var(--ink);line-height:1.1}}
#badge i{{font-style:normal;width:60px;height:60px;border-radius:50%;background:#2F6BFF;color:#fff;display:flex;align-items:center;justify-content:center;font-size:36px}}
#cross{{position:absolute;left:-20px;top:150px;width:1000px;height:12px;background:var(--bad);transform:rotate(-6deg);opacity:0}}
#m3{{display:inline-block;margin-top:50px;background:var(--ink);color:var(--y);font-weight:800;font-size:64px;padding:10px 26px}}
.rk{{display:flex;align-items:center;gap:18px;font-weight:800;font-size:60px;color:var(--ink);background:#fff;border:4px solid rgba(15,15,18,.15);border-radius:14px;padding:18px 26px;margin-bottom:20px}}
.rk.me{{background:var(--bad);color:#fff;border-color:var(--ink)}}
.rk.top{{background:var(--y);border-color:var(--ink)}}
.st{{display:flex;align-items:center;gap:22px;background:#fff;border:5px solid var(--ink);box-shadow:8px 8px 0 var(--ink);padding:22px 28px;margin-bottom:34px;font-weight:800;font-size:56px;line-height:1.1;color:var(--ink)}}
.st b{{flex:none;width:64px;height:64px;border-radius:50%;background:var(--y);display:flex;align-items:center;justify-content:center;font-size:36px}}
#five{{display:inline-block;background:var(--ok);color:#fff;font-weight:800;font-size:72px;padding:10px 28px;transform:rotate(-3deg)}}
#bub{{position:absolute;left:60px;top:300px;width:900px;background:#fff;border:5px solid var(--ink);border-radius:40px 40px 40px 8px;padding:26px 34px;font-weight:700;font-size:52px;line-height:1.2;color:var(--ink);box-shadow:10px 10px 0 var(--y);opacity:0}}
#bub small{{display:block;font-size:30px;color:#777;margin-bottom:6px}}
#ss1{{left:60px;top:560px;font-size:100px}} #ss2{{left:60px;top:800px;font-size:100px;color:var(--y)}}
#kw{{position:absolute;left:60px;top:300px;font-weight:800;font-size:110px;color:var(--ink);background:var(--y);padding:6px 30px;border:6px solid var(--ink);box-shadow:10px 10px 0 var(--ink);transform:rotate(-4deg);opacity:0}}
#sub,#sub2{{position:absolute;left:60px;top:500px;width:420px;height:90px;border-radius:18px;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center;opacity:0}}
#sub{{background:#0095F6;color:#fff}} #sub2{{background:#EFEFEF;color:var(--ink)}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
<div id="bg"></div>
<div id="camwrap"><div id="camzoom"><video id="cam" data-start="0" data-duration="{DUR}" data-track-index="0" src="assets/cut.mp4" muted playsinline></video><div id="shade"></div></div><div id="frame"></div></div>
<audio id="voice" data-start="0" data-duration="{DUR}" data-track-index="1" src="assets/voice.wav" data-volume="1"></audio>
<div id="phwrap" style="position:absolute;inset:0;z-index:3"><div id="phone"><video id="scr" data-start="3.6" data-duration="6.8" data-track-index="3" src="assets/screen.mp4" muted playsinline></video></div></div>
<div id="ov" class="clip" data-start="0" data-duration="{DUR}" data-track-index="2">
 <div class="hd" id="h1"><i>ТВОЙ ТЕЛЕФОН</i><br><i class="y">ПОМЕНЯЛ КОНКУРЕНТ?</i></div>
 <div id="tagBtn">кнопка «Исправить»</div>
 <div class="sec" id="sWho"><div class="ttl">Правку может предложить <span>кто угодно</span></div>
  <div class="who" id="w1"><b>!</b>Бывший сотрудник</div><div class="who" id="w2"><b>!</b>Обиженный клиент</div><div class="who" id="w3"><b>!</b>Конкурент</div></div>
 <div class="sec" id="sLoss"><div class="ttl">Если правку <span>приняли</span></div>
  <div class="row" id="l1"><span class="k">Сайт</span><span class="ar">→</span><span class="v">клиент уходит к другому</span></div>
  <div class="row" id="l2"><span class="k">Телефон</span><span class="ar">→</span><span class="v">звонков нет</span></div>
  <div class="row" id="l3"><span class="k">«Закрыто»</span><span class="ar">→</span><span class="v">в твой хлебный день</span></div></div>
 <div id="bub"><small>клиент — через неделю</small>«Я вам звонил, а никто не ответил»</div>
 <div class="sec" id="sBadge"><div class="ttl">Вторая беда — <span>галочка владельца</span></div>
  <div style="position:relative"><div id="badge"><i>✓</i>Информация подтверждена владельцем</div><div id="cross"></div></div>
  <div id="m3">не обновлял 3 месяца → сняли</div></div>
 <div class="sec" id="sRank"><div class="ttl">Без галочки — <span>ниже в выдаче</span></div>
  <div class="rk top">1 · Сосед с галочкой ✓</div><div class="rk top">2 · Ещё сосед ✓</div><div class="rk">3 · …</div><div class="rk me" id="rme">7 · ТЫ ↓</div></div>
 <div class="sec" id="sDo"><div class="ttl">Что сделать <span>за 5 минут</span></div>
  <div class="st" id="d1"><b>1</b>Яндекс Бизнес → История изменений</div><div class="st" id="d2"><b>2</b>Сверь телефон, сайт, график</div><div class="st" id="d3"><b>3</b>Подтверди данные</div>
  <div id="five">5 минут</div></div>
 <div class="hd" id="ss1">НЕ СЛЕДИШЬ ТЫ —</div><div class="hd" id="ss2">ПРАВЯТ ДРУГИЕ</div>
 <div id="kw">КАРТЫ</div><div id="sub">Подписаться</div><div id="sub2">Вы подписаны</div>
 {"".join(CH)}
</div></div>
<script src="assets/gsap.min.js"></script><script>
window.__timelines=window.__timelines||{{}};
const tl=gsap.timeline({{paused:true}});
const STK={{x:40,y:1440,scale:.25,rotation:-3}}, FULL={{x:0,y:0,scale:1,rotation:0}};
function toS(t){{tl.to("#camwrap",{{...STK,duration:.32,ease:"power3.inOut"}},t);tl.to("#frame",{{opacity:1,duration:.15}},t+.1);}}
function toF(t){{tl.to("#camwrap",{{...FULL,duration:.28,ease:"power3.inOut"}},t);tl.to("#frame",{{opacity:0,duration:.1}},t);}}
function sec(id,a,b){{tl.fromTo(id,{{opacity:0,y:30}},{{opacity:1,y:0,duration:.25,ease:"power3.out"}},a);tl.set(id,{{opacity:0}},b);}}
// хук
tl.fromTo("#camzoom",{{scale:1.2}},{{scale:1.03,duration:.5,ease:"expo.out"}},0);
tl.fromTo("#h1",{{opacity:0,scale:1.4}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)",transformOrigin:"0 0"}},0.05);
tl.set("#h1",{{opacity:0}},2.85);
// запись экрана
toS(3.45); tl.fromTo("#phone",{{opacity:0,y:120,rotation:4}},{{opacity:1,y:0,rotation:-2,duration:.35,ease:"back.out(1.6)"}},3.5);
tl.fromTo("#tagBtn",{{opacity:0,scale:1.5}},{{opacity:1,scale:1,duration:.25,ease:"back.out(2)"}},5.3);
tl.set(["#phone","#tagBtn"],{{opacity:0}},10.05);
// кто угодно
sec("#sWho",10.05,15.55); tl.from("#w1",{{opacity:0,x:-60,duration:.22}},11.96); tl.from("#w2",{{opacity:0,x:-60,duration:.22}},13.22); tl.from("#w3",{{opacity:0,x:-60,duration:.22}},14.6);
toF(15.5); tl.fromTo("#camzoom",{{scale:1.03}},{{scale:1.18,duration:.3,ease:"power4.out"}},16.6); tl.set("#camzoom",{{scale:1.03}},17.6);
// потери
toS(17.55); sec("#sLoss",17.62,26.1); tl.from("#l1",{{opacity:0,x:-60,duration:.22}},17.7); tl.from("#l2",{{opacity:0,x:-60,duration:.22}},19.74); tl.from("#l3",{{opacity:0,x:-60,duration:.22}},22.44);
toF(26.05);
tl.fromTo("#bub",{{opacity:0,y:60,rotation:-3}},{{opacity:1,y:0,rotation:-1.5,duration:.35,ease:"back.out(1.8)"}},30.1); tl.set("#bub",{{opacity:0}},32.6);
// галочка
toS(32.6); sec("#sBadge",32.68,37.35); tl.fromTo("#cross",{{opacity:0,scaleX:0,transformOrigin:"0 50%"}},{{opacity:1,scaleX:1,duration:.3}},36.5); tl.from("#m3",{{opacity:0,scale:1.4,duration:.25,ease:"back.out(2)"}},35.5);
sec("#sRank",37.4,42.7); tl.fromTo("#rme",{{y:-120}},{{y:0,duration:.6,ease:"bounce.out"}},38.0);
// что делать
sec("#sDo",42.75,50.8); tl.from("#d1",{{opacity:0,x:-60,duration:.22}},43.1); tl.from("#d2",{{opacity:0,x:-60,duration:.22}},46.68); tl.from("#d3",{{opacity:0,x:-60,duration:.22}},48.9); tl.from("#five",{{opacity:0,scale:1.6,duration:.25,ease:"back.out(2)"}},50.3);
toF(50.8);
// фраза-скриншот
tl.to("#shade",{{opacity:1,duration:.2}},50.85); tl.fromTo("#ss1",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.25}},50.88); tl.fromTo("#ss2",{{opacity:0,scale:1.6}},{{opacity:1,scale:1,duration:.3,ease:"expo.out"}},52.26);
tl.set(["#ss1","#ss2"],{{opacity:0}},53.6); tl.to("#shade",{{opacity:0,duration:.15}},53.58);
// призыв
tl.fromTo("#kw",{{opacity:0,scale:2,rotation:-12}},{{opacity:1,scale:1,rotation:-4,duration:.3,ease:"back.out(2)"}},54.0);
tl.fromTo("#sub",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.25}},56.3); tl.set("#sub",{{opacity:0}},57.3); tl.set("#sub2",{{opacity:1}},57.3);
{chr(10).join(JS)}
window.__timelines["main"]=tl;
</script></body></html>'''
open(os.path.join(P,'index.html'),'w',encoding='utf-8').write(html)
print(len(caps)); print(caps)
