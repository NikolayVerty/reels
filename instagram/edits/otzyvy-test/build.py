import os
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUR=15.01
caps=[(0.10,"Ужасная автошкола."),(1.80,"Инструктор заставил сбить бабку"),(4.54,"Сижу в тюрьме уже 2 года"),(8.85,"Ну типа… ну класс"),(11.0,"По отзыву можно снимать"),(12.6,"Тарантино")]
ends=[1.76,3.0,5.64,10.53,12.6,14.51]
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
#rv{{position:absolute;left:30px;top:282px;width:1020px;height:590px;box-sizing:border-box;background:#fff;border-radius:28px;box-shadow:0 0 0 40px var(--ink);padding:44px 50px;opacity:0}}
#rv .who{{display:flex;align-items:center;gap:22px}}
#rv .av{{width:96px;height:96px;border-radius:50%;background:#c8c8cc;filter:blur(6px)}}
#rv .nm{{width:330px;height:34px;border-radius:8px;background:#d4d4d8;filter:blur(5px)}}
#rv .lv{{font-weight:700;font-size:30px;color:#888;margin-top:12px}}
#rv .st{{margin-top:34px;font-size:56px;letter-spacing:6px;color:#ddd}} #rv .st b{{color:#F5B400}}
#rv .tx{{margin-top:22px;font-weight:800;font-size:58px;line-height:1.15;color:var(--ink)}}
.w{{opacity:0}}
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
 <div id="lbl">Худшие отзывы · <b>выпуск 1</b></div>
 <div id="h">Отзыв, по которому <span>можно снимать кино</span></div>
 <div id="rv"><div class="who"><div class="av"></div><div><div class="nm"></div><div class="lv">Знаток города 4 уровня</div></div></div>
  <div class="st"><b>★</b>★★★★</div>
  <div class="tx"><span class="w" id="w1">Ужастная автошкола.</span> <span class="w" id="w2">Инструктор заставил сбить бабку,</span> <span class="w" id="w3">сижу в тюрьме уже 2 года</span></div></div>
 <div id="stamp">ОТКРЫТАЯ ДВЕРЬ? НЕТ. ТЮРЬМА</div>
 <div id="cta">Скидывай самые смешные отзывы<br><span>в директ — разберу в выпуске</span></div>
 {"".join(CH)}
</div></div>
<script src="assets/gsap.min.js"></script><script>
window.__timelines=window.__timelines||{{}};
const tl=gsap.timeline({{paused:true}});
const HIDE=["#lbl","#h","#rv"];
tl.fromTo("#h",{{opacity:0,scale:1.25}},{{opacity:1,scale:1,duration:.3,ease:"expo.out",transformOrigin:"0 0"}},0.02);
tl.fromTo("#lbl",{{opacity:0}},{{opacity:1,duration:.2}},0.02);
tl.fromTo("#rv",{{opacity:0,scale:.92}},{{opacity:1,scale:1,duration:.25,ease:"power3.out"}},0.05);
tl.to("#w1",{{opacity:1,duration:.15}},0.7); tl.to("#w2",{{opacity:1,duration:.15}},1.80);
tl.set(HIDE,{{opacity:0}},3.0);
tl.set(HIDE,{{opacity:1}},4.48); tl.to("#w3",{{opacity:1,duration:.15}},4.54);
tl.set(HIDE,{{opacity:0}},5.64);
tl.set(HIDE,{{opacity:1}},8.73);
tl.set("#rv",{{opacity:0}},13.2);
tl.fromTo("#cta",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.3,ease:"back.out(1.6)"}},13.25);
{chr(10).join(JS)}
window.__timelines["main"]=tl;
</script></body></html>'''
html=html.replace('<div id="stamp">ОТКРЫТАЯ ДВЕРЬ? НЕТ. ТЮРЬМА</div>','')
open(os.path.join(P,'index.html'),'w',encoding='utf-8').write(html)
