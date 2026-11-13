# index.html для ролика из выступления: 2ГИС — статистику даст менеджер.
import os
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUR=40.51
caps=[(0.00,"Как удалить негативный отзыв?"),(1.28,"Мы работаем с негативом"),(3.18,"через ИИ"),(4.90,"ИИ изучает массив данных"),(7.42,"и формирует жалобу"),(8.26,"по правилам Яндекса"),
(11.34,"Как это делаем:"),(13.90,"загружаем сам отзыв,"),(15.48,"загружаем правила Яндекса —"),(18.00,"ИИ помогает составить жалобу,"),(21.06,"отправляем её в Яндекс"),(23.70,"и шанс удаления выше,"),(25.74,"чем если писать самому"),
(26.74,"Вот так выглядит удаление:"),(29.24,"«Мы рассмотрели вашу жалобу,"),(32.08,"отзыв снят с публикации»"),(34.40,"Если не получилось —"),(36.82,"конечно, пишем ответ"),(38.58,"Отзыв не может висеть без ответа")]
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
#no,#res{{position:absolute;left:30px;top:282px;width:1020px;height:590px;background:#fff;border-radius:28px;box-shadow:0 0 0 40px var(--ink);box-sizing:border-box;padding:34px 46px;opacity:0}}
#no .t,#res .t{{font-weight:800;font-size:44px;color:var(--ink)}} #no .s,#res .s{{font-weight:500;font-size:24px;color:#777;margin:4px 0 18px}}
.card{{position:absolute;left:30px;top:282px;width:1020px;height:590px;background:#fff;border-radius:28px;box-shadow:0 0 0 40px var(--ink);box-sizing:border-box;padding:30px 44px;opacity:0}}
.card .t{{font-weight:800;font-size:42px;color:var(--ink);margin-bottom:18px}}
.card .st{{display:flex;align-items:center;gap:22px;font-weight:800;font-size:46px;color:var(--ink);padding:12px 0;border-top:2px solid #eee}}
.card .st b{{flex:none;width:58px;height:58px;border-radius:50%;background:var(--y);display:flex;align-items:center;justify-content:center;font-size:32px}}
.card .ft2{{margin-top:16px;display:inline-block;background:var(--ok);color:#fff;font-weight:800;font-size:34px;padding:8px 18px}}
#stamp{{position:absolute;left:250px;top:560px;border:8px solid var(--ok);color:var(--ok);font-weight:800;font-size:62px;padding:10px 26px;border-radius:14px;background:rgba(255,255,255,.85);transform:rotate(-8deg);opacity:0}}
#res .row{{display:flex;align-items:baseline;gap:24px;padding:6px 0;border-top:2px solid #eee}}
#res .v{{font-weight:800;font-size:100px;line-height:1;color:var(--ok);font-variant-numeric:tabular-nums}} #res .k{{font-weight:700;font-size:40px;color:#555}}
.hl{{position:absolute;left:24px;top:410px;width:470px;height:460px;border:8px solid #E5484D;border-radius:18px;opacity:0}}
.hl2{{position:absolute;left:530px;top:410px;width:478px;height:460px;border:8px solid var(--ok);border-radius:18px;opacity:0}}
#pay{{position:absolute;left:0;right:0;top:790px;display:flex;justify-content:center;opacity:0}}
#bub2{{position:absolute;left:70px;top:620px;width:820px;background:#fff;border:5px solid var(--ink);border-radius:36px 36px 36px 6px;padding:24px 32px;font-weight:700;font-size:46px;color:var(--ink);box-shadow:10px 10px 0 var(--y);opacity:0}}
#pay2{{position:absolute;left:0;right:0;top:800px;display:flex;justify-content:center;opacity:0}}
#pay2 div{{background:#E5484D;color:#fff;font-weight:800;font-size:33px;padding:12px 22px;border:4px solid #fff;white-space:nowrap}}
#pay div{{background:var(--ink)!important;color:var(--y)!important;border-color:var(--y)!important;font-size:38px!important;white-space:nowrap}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
<video id="base" data-start="0" data-duration="{DUR}" data-track-index="0" src="assets/base.mp4" muted playsinline></video>
<audio id="voice" data-start="0" data-duration="{DUR}" data-track-index="1" src="assets/voice.wav" data-volume="1"></audio>
<div id="ov" class="clip" data-start="0" data-duration="{DUR}" data-track-index="2">
 <div id="lbl">Моё выступление · <b>Суровый Питерский форум</b></div>
 <div id="h">Как удалить негативный отзыв <span>с помощью ИИ</span></div>
 <div class="card" id="cd1"><div class="t">Жалоба на отзыв через ИИ</div>
  <div class="st" id="s1"><b>1</b>Загружаем отзыв</div><div class="st" id="s2"><b>2</b>Загружаем правила Яндекса</div>
  <div class="st" id="s3"><b>3</b>ИИ составляет жалобу</div><div class="st" id="s4"><b>4</b>Отправляем в Яндекс</div>
  <div class="ft2" id="sf">шанс удаления выше, чем написать самому</div></div>
 <div id="stamp">СНЯТ С ПУБЛИКАЦИИ</div>
 <div id="pay2"><div>НЕ УДАЛИЛИ — ОТВЕТЬ</div></div>
 {"".join(CH)}
</div></div>
<script src="assets/gsap.min.js"></script><script>
window.__timelines=window.__timelines||{{}};
const tl=gsap.timeline({{paused:true}});
tl.fromTo("#lbl",{{opacity:0,y:-20}},{{opacity:1,y:0,duration:.3,ease:"power2.out"}},0.05);
tl.fromTo("#h",{{opacity:0,scale:1.25}},{{opacity:1,scale:1,duration:.35,ease:"expo.out",transformOrigin:"0 0"}},0.05);
tl.fromTo("#cd1",{{opacity:0,scale:.92}},{{opacity:1,scale:1,duration:.3,ease:"power3.out"}},11.3);
const T={{s1:13.9,s2:15.48,s3:18.0,s4:21.06,sf:23.7}};
for(const k in T) tl.from("#"+k,{{opacity:0,x:-40,duration:.25,ease:"power2.out"}},T[k]);
tl.set("#cd1",{{opacity:0}},26.7);
tl.fromTo("#stamp",{{opacity:0,scale:2.2}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},32.08);
tl.set("#stamp",{{opacity:0}},34.35);
tl.fromTo("#pay2",{{opacity:0,scale:1.5}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},38.5);
{chr(10).join(JS)}
window.__timelines["main"]=tl;
</script></body></html>'''
open(os.path.join(P,'index.html'),'w',encoding='utf-8').write(html)
