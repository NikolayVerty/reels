import os
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUR=33.63
caps=[(0.05,"«Отвратительная клиника."),(1.3,"Записалась на чистку зубов."),(3.0,"Случайно удалили пять зубов»"),
(7.08,"«Врачи неадекватные."),(8.0,"Втроём выдёргивали зубы руками»"),
(12.30,"«Врач не ожидал такой реакции"),(13.4,"и дал мне по лицу»"),
(18.68,"«Лишилась пяти зубов,"),(20.2,"получила два фингала»"),(22.25,"«Врачи — изверги."),(23.6,"Буду обращаться в органы»"),
(26.69,"А это на Зимний дворец:"),(28.5,"«При царе было лучше»")]
ends=[1.3,3.0,4.93,8.0,9.85,13.4,14.33,20.2,22.21,23.6,24.89,28.5,29.68]
CH=[];JS=[]
for i,((t,txt),e) in enumerate(zip(caps,ends)):
    CH.append(f'<div class="prow"><div class="plq" id="cp{i}">{txt}</div></div>')
    JS.append(f'tl.fromTo("#cp{i}",{{opacity:0,y:12,scale:.9}},{{opacity:1,y:0,scale:1,duration:.13,ease:"back.out(2.2)"}},{t});tl.set("#cp{i}",{{opacity:0}},{e});')
html=f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><style>
@font-face{{font-family:Manrope;font-weight:700;src:url(assets/fonts/manrope-cyrillic-700-normal.woff2)}}
@font-face{{font-family:Manrope;font-weight:800;src:url(assets/fonts/manrope-cyrillic-800-normal.woff2)}}
@font-face{{font-family:Manrope;font-weight:800;src:url(assets/fonts/manrope-latin-800-normal.woff2);unicode-range:U+0000-00FF}}
:root{{--y:#FFC24B;--ink:#0F0F12;--bad:#E5484D}}
html,body{{margin:0;background:#000}}
#root{{position:relative;width:1080px;height:1920px;overflow:hidden;background:var(--ink);font-family:Manrope,sans-serif}}
#base{{position:absolute;inset:0;width:1080px;height:1920px}}
#ov{{position:absolute;inset:0}}
#lbl{{position:absolute;left:60px;top:70px;font-weight:700;font-size:30px;color:#9a9aa3}} #lbl b{{color:var(--y)}}
#h{{position:absolute;left:60px;top:112px;width:960px;font-weight:800;font-size:70px;line-height:1.02;color:#fff}} #h span{{color:var(--y)}}
.rv{{position:absolute;left:30px;top:282px;width:1020px;height:590px;box-sizing:border-box;background:#fff;border-radius:28px;box-shadow:0 0 0 40px var(--ink);padding:44px 50px;opacity:0}}
.rv .who{{display:flex;align-items:center;gap:22px}}
.rv .av{{width:96px;height:96px;border-radius:50%;background:#c8c8cc;filter:blur(6px)}}
.rv .nm{{width:330px;height:34px;border-radius:8px;background:#d4d4d8;filter:blur(5px)}}
.rv .lv{{font-weight:700;font-size:30px;color:#888;margin-top:12px}}
.rv .st{{margin-top:34px;font-size:56px;letter-spacing:6px;color:#ddd}} .rv .st b{{color:#F5B400}}
.rv .tx{{margin-top:22px;font-weight:800;font-size:58px;line-height:1.15;color:var(--ink)}}
.w{{opacity:0}} .rv .tx.sm{{font-size:46px;line-height:1.18}} .rv .tx.big{{font-size:72px}}
#mtag{{position:absolute;left:40px;top:120px;background:var(--bad);color:#fff;font-weight:800;font-size:44px;padding:8px 22px;transform:rotate(-4deg);opacity:0}}
#stamp{{position:absolute;left:150px;top:640px;border:10px solid var(--bad);color:var(--bad);font-weight:800;font-size:96px;padding:6px 26px;border-radius:16px;background:rgba(255,255,255,.88);transform:rotate(-10deg);opacity:0}}
.prow{{position:absolute;left:0;right:0;top:1340px;display:flex;justify-content:center}}
.plq{{background:var(--y);color:var(--ink);font-weight:800;font-size:56px;line-height:1.1;padding:10px 26px 14px;white-space:nowrap;box-shadow:6px 6px 0 var(--ink);opacity:0}}
#cta{{position:absolute;left:30px;top:282px;width:1020px;height:590px;box-sizing:border-box;background:var(--ink);border:4px solid var(--y);border-radius:28px;box-shadow:0 0 0 40px var(--ink);display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;font-weight:800;font-size:64px;line-height:1.1;color:#fff;opacity:0}} #cta span{{display:inline-block;margin-top:16px;background:var(--y);color:var(--ink);padding:8px 24px}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
<video id="base" data-start="0" data-duration="{DUR}" data-track-index="0" src="assets/base.mp4" muted playsinline></video>
<audio id="voice" data-start="0" data-duration="{DUR}" data-track-index="1" src="assets/voice.wav" data-volume="1"></audio>
<div id="ov" class="clip" data-start="0" data-duration="{DUR}" data-track-index="2">
 <div id="lbl">Худшие отзывы · <b>выпуск 2</b></div>
 <div id="h">Пришла почистить зубы. <span>Ушла без пяти</span></div>
 <div class="rv" id="rv1"><div class="who"><div class="av"></div><div><div class="nm"></div><div class="lv">Знаток города 2 уровня</div></div></div>
  <div class="st"><b>★</b>★★★★</div>
  <div class="tx sm"><span class="w" id="a1">Отвратительная клиника. Записалась на чистку зубов — случайно удалили 5 зубов.</span> <span class="w" id="a2">Врачи втроём выдёргивали зубы руками.</span> <span class="w" id="a3">Врач дал мне по лицу.</span> <span class="w" id="a4">Два фингала и гематома. Буду обращаться в органы!</span></div></div>
 <div class="rv" id="rv2"><div class="who"><div class="av"></div><div><div class="nm"></div><div class="lv">Знаток города 13 уровня</div></div></div>
  <div class="st"><b>★</b>★★★★</div><div class="tx big">Зимний дворец.<br><span class="w" id="b1">«При царе было лучше»</span></div></div>
 <div id="cta">Скидывай самые смешные отзывы<br><span>в директ — разберу в выпуске</span></div>
 {"".join(CH)}
</div></div>
<script src="assets/gsap.min.js"></script><script>
window.__timelines=window.__timelines||{{}};
const tl=gsap.timeline({{paused:true}});
const TOP=["#lbl","#h"];
tl.fromTo("#h",{{opacity:0,scale:1.25}},{{opacity:1,scale:1,duration:.3,ease:"expo.out",transformOrigin:"0 0"}},0.02);
tl.fromTo("#lbl",{{opacity:0}},{{opacity:1,duration:.2}},0.02);
tl.fromTo("#rv1",{{opacity:0,scale:.92}},{{opacity:1,scale:1,duration:.25,ease:"power3.out"}},0.05);
tl.to("#a1",{{opacity:1,duration:.15}},0.3); tl.to("#a2",{{opacity:1,duration:.15}},7.1); tl.to("#a3",{{opacity:1,duration:.15}},12.3); tl.to("#a4",{{opacity:1,duration:.15}},18.7);
const M=[[4.93,7.03],[9.85,12.25],[14.33,18.63],[24.89,26.64],[29.68,31.63]];
for(const [a,b] of M){{tl.set([...TOP,"#rv1","#rv2"],{{opacity:0}},a);}}
tl.set([...TOP,"#rv1"],{{opacity:1}},7.03); tl.set([...TOP,"#rv1"],{{opacity:1}},12.25); tl.set([...TOP,"#rv1"],{{opacity:1}},18.63);
tl.set("#rv1",{{opacity:0}},26.64); tl.set(TOP,{{opacity:1}},26.64);
tl.fromTo("#rv2",{{opacity:0,scale:.92}},{{opacity:1,scale:1,duration:.25,ease:"power3.out"}},26.66); tl.to("#b1",{{opacity:1,duration:.15}},28.5);
tl.set(TOP,{{opacity:1}},31.63);
tl.fromTo("#cta",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.3,ease:"back.out(1.6)"}},31.63);
{chr(10).join(JS)}
window.__timelines["main"]=tl;
</script></body></html>'''
html=html.replace('<div id="stamp">ОТКРЫТАЯ ДВЕРЬ? НЕТ. ТЮРЬМА</div>','')
open(os.path.join(P,'index.html'),'w',encoding='utf-8').write(html)
