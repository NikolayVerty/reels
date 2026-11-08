# Генерирует index.html для рилса 01 «Двадцать мест. Десять забирают всё».
import json, os
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUR = 35.70

# Плашки-субтитры: (start, end_group, text, zone)
groups = [
  [(0.11,"Если ты 11-й в Яндекс Картах —"),(2.01,"поздравляю, клиентов у тебя почти нет")],
  [(3.82,"В Картах 20 мест"),(5.84,"первые 10 забирают 86% трафика")],
  [(8.67,"И это не я придумал —"),(9.99,"это данные Яндекса")],
  [(11.21,"Остальные 10 мест забирают 14% трафика"),(13.73,"по сути — крошки")],
  [(14.56,"А теперь вопрос,"),(15.40,"от которого у половины владельцев сжалась жопа")],
  [(17.36,"Открой Карты прямо сейчас"),(19.03,"вбей свою услугу и район"),(20.71,"Не название — услугу")],
  [(22.15,"Посчитай, на каком ты месте")],
  [(23.66,"Одиннадцатый? Поздравляю —"),(24.94,"ты работаешь на первую десятку")],
  [(31.27,"Напиши в комментах, какое у тебя место"),(32.77,"или слово «КАРТЫ» —"),(33.75,"подскажу, как попасть в первую десятку")],
]
group_end = [3.82,8.60,11.17,14.56,17.36,22.15,23.62,27.00,DUR]
# зона плашек: speaker -> низ кадра, collage -> над стикером
zone = ["spk","col","spk","col","spk","col","spk","col","spk"]

plaques_html=[]; js=[]
for gi,g in enumerate(groups):
    top = 1120 if zone[gi]=="spk" else 1000
    if gi==8: top=1090
    left = 70 if zone[gi]=="spk" else 450
    if gi in (5,): left=70
    items=[]
    for k,(t,txt) in enumerate(g):
        pid=f"p{gi}_{k}"
        items.append(f'<div class="plq" id="{pid}" style="margin-left:{(k%2)*36}px">{txt}</div>')
        js.append(f'tl.fromTo("#{pid}",{{opacity:0,y:18,scale:.92}},{{opacity:1,y:0,scale:1,duration:.18,ease:"back.out(2)"}},{t});')
        js.append(f'tl.set("#{pid}",{{opacity:0}},{group_end[gi]});')
    w = 900 if left==70 else 560
    plaques_html.append(f'<div class="pgrp" style="top:{top}px;left:{left}px;width:{w}px">{"".join(items)}</div>')

# Рейтинг 20 мест
rows=[]
for i in range(1,21):
    w = 520 - (i*9)
    rows.append(f'<div class="row" id="r{i}"><span class="rk">{i}</span><span class="pin"></span><span class="bar" style="width:{w}px"></span><span class="st">★ 4,{9-(i%5)}</span></div>')
rows_html="\n".join(rows)

html = f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8">
<style>
@font-face{{font-family:Manrope;font-weight:500;src:url(assets/fonts/manrope-cyrillic-500-normal.woff2)}}
@font-face{{font-family:Manrope;font-weight:700;src:url(assets/fonts/manrope-cyrillic-700-normal.woff2)}}
@font-face{{font-family:Manrope;font-weight:800;src:url(assets/fonts/manrope-cyrillic-800-normal.woff2)}}
@font-face{{font-family:Manrope;font-weight:800;src:url(assets/fonts/manrope-latin-800-normal.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:Play;font-style:italic;font-weight:800;src:url(assets/fonts/playfair-display-cyrillic-800-italic.woff2)}}
@font-face{{font-family:Play;font-style:italic;font-weight:800;src:url(assets/fonts/playfair-display-latin-800-italic.woff2);unicode-range:U+0000-00FF}}
:root{{--y:#FFC24B;--y2:#F5A623;--ink:#0F0F12;--gr:#1A1A1F;--ok:#16A34A;--bad:#E5484D;--paper:#ECEBE6}}
html,body{{margin:0;background:#000}}
#root{{position:relative;width:1080px;height:1920px;overflow:hidden;background:var(--paper);font-family:Manrope,sans-serif}}
#bg{{position:absolute;inset:0;background-color:var(--paper);
 background-image:linear-gradient(rgba(15,15,18,.07) 2px,transparent 2px),linear-gradient(90deg,rgba(15,15,18,.07) 2px,transparent 2px),
 linear-gradient(rgba(15,15,18,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(15,15,18,.035) 1px,transparent 1px);
 background-size:120px 120px,120px 120px,24px 24px,24px 24px}}
#camwrap{{position:absolute;left:0;top:0;width:1080px;height:1920px;transform-origin:0 0;z-index:2;overflow:hidden}}
#camzoom{{position:absolute;inset:0;transform-origin:50% 35%}}
#cam{{width:1080px;height:1920px;object-fit:cover;display:block}}
#camshade{{position:absolute;inset:0;background:rgba(10,10,14,.72);opacity:0}}
#camframe{{position:absolute;inset:0;border:30px solid #fff;box-sizing:border-box;opacity:0}}
#ov{{position:absolute;inset:0;z-index:3}}
.pgrp{{position:absolute;display:flex;flex-direction:column;align-items:flex-start;gap:12px}}
.plq{{position:relative;max-width:100%;box-sizing:border-box;background:var(--y);color:var(--ink);font-weight:800;font-size:46px;line-height:1.12;padding:10px 20px 12px;
 box-shadow:6px 6px 0 var(--ink);opacity:0}}
.big{{position:absolute;font-weight:800;color:#fff;text-shadow:0 6px 30px rgba(0,0,0,.45);opacity:0}}
.acc{{position:absolute;font-family:Play;font-style:italic;font-weight:800;opacity:0}}
#list{{position:absolute;left:60px;top:250px;width:760px;opacity:0}}
.row{{display:flex;align-items:center;gap:16px;height:34px;margin-bottom:5px;padding:0 14px;background:#fff;border:2px solid rgba(15,15,18,.12);border-radius:8px;font-weight:800;font-size:24px;color:var(--ink)}}
.rk{{width:40px;font-variant-numeric:tabular-nums}}
.pin{{width:18px;height:18px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);background:var(--gr)}}
.bar{{height:10px;border-radius:5px;background:#CFCFCA}}
.st{{margin-left:auto;font-size:20px;color:#6b6b66}}
.row.top{{background:var(--y);border-color:var(--ink)}}
.row.top .bar{{background:var(--ink);opacity:.25}}
.row.low{{opacity:.45}}
.row.me{{background:var(--bad);color:#fff;border-color:var(--ink);opacity:1}}
.row.me .bar{{background:#fff;opacity:.5}} .row.me .st{{color:#fff}}
#brk{{position:absolute;left:830px;top:250px;width:22px;height:385px;border:5px solid var(--ink);border-left:none;opacity:0}}
#brk2{{position:absolute;left:830px;top:640px;width:22px;height:385px;border:5px solid #8a8a85;border-left:none;opacity:0}}
#n86{{left:470px;top:1270px;font-size:230px;color:var(--ok)}}
#n14{{left:470px;top:1270px;font-size:230px;color:#8a8a85}}
#crumbs{{left:470px;top:1560px;font-size:110px;color:var(--ink)}}
#me{{position:absolute;left:640px;top:640px;opacity:0;background:var(--bad);color:#fff;font-weight:800;font-size:44px;padding:6px 18px;box-shadow:5px 5px 0 var(--ink)}}
.coin{{position:absolute;width:64px;height:64px;border-radius:50%;background:var(--y);border:5px solid var(--ink);font-weight:800;font-size:38px;color:var(--ink);display:flex;align-items:center;justify-content:center;opacity:0}}
#onten{{left:450px;top:1360px;font-size:92px;color:var(--ink);width:560px;line-height:1.05}}
/* телефон */
#phone{{position:absolute;left:250px;top:240px;width:580px;height:720px;background:#fff;border:10px solid var(--ink);border-radius:56px;opacity:0;box-shadow:16px 16px 0 rgba(15,15,18,.15)}}
#sbar{{position:absolute;left:36px;right:36px;top:60px;height:96px;border-radius:48px;background:#F2F2EF;border:3px solid var(--ink);display:flex;align-items:center;padding:0 30px;font-size:40px;font-weight:700;color:var(--ink);overflow:hidden;white-space:nowrap}}
#typed{{display:inline-block;overflow:hidden;white-space:nowrap;vertical-align:bottom}}
#caret{{display:inline-block;width:4px;height:44px;background:var(--ink);margin-left:4px}}
.res{{position:absolute;left:36px;right:36px;height:92px;border-radius:18px;background:#F7F7F4;border:2px solid rgba(15,15,18,.12);opacity:0}}
.res i{{position:absolute;left:24px;top:22px;width:40px;height:40px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);background:var(--y2)}}
.res b{{position:absolute;left:90px;top:26px;height:14px;width:300px;border-radius:7px;background:#CFCFCA}}
.res u{{position:absolute;left:90px;top:54px;height:12px;width:180px;border-radius:6px;background:#E2E2DD}}
.chip{{position:absolute;font-weight:800;font-size:50px;padding:10px 24px;border:4px solid var(--ink);opacity:0;box-shadow:6px 6px 0 var(--ink)}}
#chipNo{{left:110px;top:1010px;background:#fff;color:#8a8a85;text-decoration:line-through;text-decoration-thickness:6px;text-decoration-color:var(--bad)}}
#chipYes{{left:560px;top:1010px;background:var(--ok);color:#fff}}
#h1{{left:70px;top:250px;font-size:150px;line-height:1}}
#hPlace{{left:70px;top:250px;font-size:104px;line-height:1.02;width:900px}}
#ss1{{left:70px;top:560px;font-size:92px;line-height:1.05;width:940px}}
#ss2{{left:70px;top:820px;font-size:108px;white-space:nowrap;line-height:1;color:var(--y)}}
#ss3{{left:70px;top:1000px;font-size:64px;color:#fff;width:900px;line-height:1.1}}
#kw{{left:70px;top:300px;font-family:Manrope;font-style:normal;font-size:96px;color:var(--ink);background:var(--y);padding:6px 28px;border:5px solid var(--ink);box-shadow:8px 8px 0 var(--ink)}}
#sub{{position:absolute;left:340px;top:1560px;width:400px;height:84px;border-radius:16px;background:#0095F6;color:#fff;font-weight:800;font-size:38px;display:flex;align-items:center;justify-content:center;opacity:0}}
#sub2{{position:absolute;left:340px;top:1560px;width:400px;height:84px;border-radius:16px;background:#EFEFEF;color:var(--ink);font-weight:800;font-size:38px;display:flex;align-items:center;justify-content:center;opacity:0}}
</style></head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
  <div id="bg"></div>
  <div id="camwrap"><div id="camzoom">
    <video id="cam" class="" data-start="0" data-duration="{DUR}" data-track-index="0" src="assets/cut.mp4" muted playsinline></video>
    <div id="camshade"></div></div><div id="camframe"></div>
  </div>
  <audio id="voice" data-start="0" data-duration="{DUR}" data-track-index="1" src="assets/voice.wav" data-volume="1"></audio>
  <div id="ov" class="clip" data-start="0" data-duration="{DUR}" data-track-index="2">
    <div class="big" id="h1">ТЫ 11-Й?</div>
    <div id="list">{rows_html}</div>
    <div id="brk"></div><div id="brk2"></div>
    <div class="acc" id="n86">86%</div>
    <div class="acc" id="n14">14%</div>
    <div class="acc" id="crumbs">крошки</div>
    <div id="me">← ТЫ</div>
    <div class="coin" id="c1" style="left:880px;top:700px">₽</div>
    <div class="coin" id="c2" style="left:930px;top:690px">₽</div>
    <div class="coin" id="c3" style="left:890px;top:640px">₽</div>
    <div class="acc" id="onten">на первую десятку</div>
    <div id="phone"><div id="sbar"><span id="typed">кофейня Хамовники</span><span id="caret"></span></div>
      <div class="res" id="res1" style="top:200px"><i></i><b></b><u></u></div>
      <div class="res" id="res2" style="top:310px"><i></i><b></b><u></u></div>
      <div class="res" id="res3" style="top:420px"><i></i><b></b><u></u></div>
      <div class="res" id="res4" style="top:530px"><i></i><b></b><u></u></div></div>
    <div class="chip" id="chipNo">«Кофе Хаус»</div>
    <div class="chip" id="chipYes">кофейня ✓</div>
    <div class="big" id="hPlace">КАКОЕ У ТЕБЯ МЕСТО?</div>
    <div class="big" id="ss1">КАРТЫ — НЕ СПРАВОЧНИК.</div>
    <div class="big" id="ss2">КАРТЫ = КАССА</div>
    <div class="big" id="ss3">и к тебе должна стоять очередь</div>
    <div class="acc" id="kw">КАРТЫ</div>
    <div id="sub">Подписаться</div><div id="sub2">Вы подписаны</div>
    {"".join(plaques_html)}
  </div>
</div>
<script src="assets/gsap.min.js"></script>
<script>
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{paused:true}});
const STK = {{x:60,y:1170,scale:.34,rotation:-3}};
const FULL = {{x:0,y:0,scale:1,rotation:0}};
function toSticker(t){{ tl.to("#camwrap",{{...STK,duration:.32,ease:"power3.inOut"}},t); tl.to("#camframe",{{opacity:1,duration:.15}},t+.1); }}
function toFull(t){{ tl.to("#camwrap",{{...FULL,duration:.28,ease:"power3.inOut"}},t); tl.to("#camframe",{{opacity:0,duration:.1}},t); }}
const rows=[...Array(20)].map((_,i)=>"#r"+(i+1));
const TOP={{backgroundColor:"#FFC24B",borderColor:"#0F0F12",opacity:1}}, LOW={{opacity:.4}}, ME={{backgroundColor:"#E5484D",color:"#fff",borderColor:"#0F0F12",opacity:1}};

// 0 Хук: панч-зум + заголовок
tl.fromTo("#camzoom",{{scale:1.18}},{{scale:1.04,duration:.5,ease:"expo.out"}},0);
tl.fromTo("#h1",{{opacity:0,scale:1.6,rotation:-4}},{{opacity:1,scale:1,rotation:-2,duration:.3,ease:"back.out(2.2)"}},0.05);
tl.to("#h1",{{x:-8,duration:.05,yoyo:true,repeat:5}},2.55);
tl.set("#h1",{{opacity:0}},3.82);

// 3.82 Коллаж: 20 мест
toSticker(3.70);
tl.to("#list",{{opacity:1,duration:.15}},3.82);
tl.from(rows,{{x:-60,opacity:0,duration:.22,stagger:.035,ease:"power2.out"}},3.85);
tl.set(rows.slice(0,10),TOP,5.84);
tl.from(rows.slice(0,10),{{scale:1.06,duration:.2,stagger:.02,ease:"back.out(3)"}},5.84);
tl.fromTo("#brk",{{opacity:0,scaleY:0,transformOrigin:"0 0"}},{{opacity:1,scaleY:1,duration:.25,ease:"power2.out"}},6.12);
tl.fromTo("#n86",{{opacity:0,scale:.3,rotation:-12}},{{opacity:1,scale:1,rotation:-4,duration:.35,ease:"back.out(1.8)"}},6.88);
toFull(8.55); tl.set(["#list","#brk","#n86"],{{opacity:0}},8.62);

// 11.21 Коллаж: остальные 10
toSticker(11.10);
tl.set("#list",{{opacity:1}},11.21);
tl.set(rows.slice(0,10),TOP,11.21);
tl.set(rows.slice(10),LOW,11.57);
tl.fromTo("#brk2",{{opacity:0,scaleY:0,transformOrigin:"0 0"}},{{opacity:1,scaleY:1,duration:.25}},11.83);
tl.fromTo("#n14",{{opacity:0,y:-200}},{{opacity:1,y:0,duration:.4,ease:"bounce.out"}},12.43);
tl.fromTo("#crumbs",{{opacity:0,scale:2.2,rotation:8}},{{opacity:1,scale:1,rotation:-3,duration:.3,ease:"expo.out"}},14.05);
toFull(14.50); tl.set(["#list","#brk2","#n14","#crumbs"],{{opacity:0}},14.56);

// 14.56 Повторная зацепка: резкий зум ближе
tl.to("#camzoom",{{scale:1.22,duration:.35,ease:"power4.out"}},14.56);
tl.to("#camzoom",{{scale:1.3,duration:1.8,ease:"none"}},14.95);

// 17.36 Телефон: поиск услуги
toSticker(17.25); tl.set("#camzoom",{{scale:1.04}},17.6);
tl.fromTo("#phone",{{opacity:0,y:120,rotation:4}},{{opacity:1,y:0,rotation:-2,duration:.35,ease:"back.out(1.6)"}},17.40);
tl.set("#typed",{{clipPath:"inset(0 100% 0 0)"}},0);
tl.fromTo("#typed",{{clipPath:"inset(0 100% 0 0)"}},{{clipPath:"inset(0 0% 0 0)",duration:1.1,ease:"steps(17)"}},19.03);
tl.to("#caret",{{opacity:0,duration:.01,repeat:9,yoyo:true,repeatDelay:.25}},17.5);
tl.fromTo(["#res1","#res2","#res3","#res4"],{{opacity:0,x:40}},{{opacity:1,x:0,duration:.2,stagger:.08,ease:"power2.out"}},20.15);
tl.fromTo("#chipNo",{{opacity:0,scale:1.5,rotation:-8}},{{opacity:1,scale:1,rotation:-4,duration:.25,ease:"back.out(2)"}},20.81);
tl.fromTo("#chipYes",{{opacity:0,scale:1.5,rotation:8}},{{opacity:1,scale:1,rotation:3,duration:.25,ease:"back.out(2)"}},21.71);
toFull(22.08); tl.set(["#phone","#chipNo","#chipYes"],{{opacity:0}},22.15);

// 22.15 Какое место
tl.fromTo("#hPlace",{{opacity:0,y:-60}},{{opacity:1,y:0,duration:.25,ease:"power3.out"}},22.18);
tl.set("#hPlace",{{opacity:0}},23.62);

// 23.66 Коллаж: ты 11-й
toSticker(23.55);
tl.set("#list",{{opacity:1}},23.66);
tl.set(rows.slice(0,10),TOP,23.66);
tl.set(rows.slice(10),LOW,23.66);
tl.set("#r11",ME,23.70);
tl.from("#r11",{{scale:1.15,duration:.25,ease:"back.out(3)"}},23.70);
tl.fromTo("#me",{{opacity:0,x:60}},{{opacity:1,x:0,duration:.2,ease:"power2.out"}},23.80);
tl.fromTo(["#c1","#c2","#c3"],{{opacity:0,y:0}},{{opacity:1,y:-420,duration:.9,stagger:.18,ease:"power1.inOut"}},25.10);
tl.fromTo("#onten",{{opacity:0,scale:1.8}},{{opacity:1,scale:1,duration:.3,ease:"expo.out"}},25.70);
toFull(26.90); tl.set(["#list","#me","#c1","#c2","#c3","#onten"],{{opacity:0}},27.0);

// 27.04 Фраза-скриншот
tl.to("#camshade",{{opacity:1,duration:.2}},27.0);
tl.to("#camzoom",{{scale:1.12,duration:4,ease:"none"}},27.0);
tl.fromTo("#ss1",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.25,ease:"power3.out"}},27.06);
tl.fromTo("#ss2",{{opacity:0,scale:1.7}},{{opacity:1,scale:1,duration:.3,ease:"expo.out"}},28.62);
tl.fromTo("#ss3",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.25,ease:"power2.out"}},29.36);
tl.set(["#ss1","#ss2","#ss3"],{{opacity:0}},31.2); tl.to("#camshade",{{opacity:0,duration:.15}},31.18);
tl.set("#camzoom",{{scale:1.04}},31.2);

// 31.27 Призыв
tl.fromTo("#kw",{{opacity:0,scale:2,rotation:-10}},{{opacity:1,scale:1,rotation:-4,duration:.3,ease:"back.out(2)"}},33.25);
tl.fromTo("#sub",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.25,ease:"power2.out"}},34.30);
tl.set("#sub",{{opacity:0}},35.0); tl.set("#sub2",{{opacity:1}},35.0);
tl.from("#sub2",{{scale:.9,duration:.15}},35.0);

{chr(10).join(js)}
window.__timelines["main"] = tl;
</script>
</body></html>'''
open(os.path.join(P,"index.html"),"w",encoding="utf-8").write(html)
print("ok")
