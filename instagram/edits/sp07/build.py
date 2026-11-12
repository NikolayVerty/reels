# index.html для ролика из выступления: 2ГИС — статистику даст менеджер.
import os
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUR=45.33
caps=[(0.00,"В отличие от Яндекса,"),(2.20,"2ГИС продаёт места"),(3.38,"в любом городе"),(4.22,"Можно быть в топе,"),(5.36,"на втором-третьем месте"),(7.80,"Все места в выдаче продаются"),
(9.34,"Я провёл такую черту"),(11.06,"по карте России:"),(13.36,"где 2ГИС работает хорошо,"),(14.92,"где плохо — по опыту"),
(17.00,"Мы запускали много городов"),(19.44,"В ЦФО, в центре"),(21.84,"2ГИС работает не очень"),(23.40,"часто даже не окупается"),
(24.96,"А в восточной части —"),(26.68,"Новосиб, Омск,"),(27.56,"Томск, Красноярск —"),(28.78,"2ГИС работает изумительно"),(30.30,"один из топовых инструментов"),
(31.26,"Если клиенты на востоке —"),(34.28,"обязательно запускайте"),(35.20,"рекламу в 2ГИС"),
(36.38,"Красноярск, ритуальные услуги:"),(38.86,"проплачена реклама 2ГИС,"),(40.34,"топ-3 места"),(41.62,"Очень много трафика,"),(42.62,"звонков и маршрутов"),(44.16,"И это за месяц")]
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
.tag{{position:absolute;font-weight:800;font-size:38px;padding:10px 20px;border:4px solid #fff;box-shadow:6px 6px 0 var(--ink);opacity:0}}
.tag.bad{{left:40px;top:700px;background:#E5484D;color:#fff}} .tag.good{{right:30px;top:560px;background:var(--ok);color:#fff}}
#res .grid{{display:grid;grid-template-columns:1fr 1fr;gap:6px 30px;margin-top:6px}}
#res .c{{border-top:2px solid #eee;padding-top:6px}}
#res .c .v{{font-size:96px!important}} #res .c .k{{font-size:32px!important}}
#res .t{{font-size:36px!important}}
#res .row{{display:flex;align-items:baseline;gap:24px;padding:6px 0;border-top:2px solid #eee}}
#res .v{{font-weight:800;font-size:100px;line-height:1;color:var(--ok);font-variant-numeric:tabular-nums}} #res .k{{font-weight:700;font-size:40px;color:#555}}
.hl{{position:absolute;left:24px;top:410px;width:470px;height:460px;border:8px solid #E5484D;border-radius:18px;opacity:0}}
.hl2{{position:absolute;left:530px;top:410px;width:478px;height:460px;border:8px solid var(--ok);border-radius:18px;opacity:0}}
#pay{{position:absolute;left:0;right:0;top:790px;display:flex;justify-content:center;opacity:0}}
#bub2{{position:absolute;left:70px;top:620px;width:820px;background:#fff;border:5px solid var(--ink);border-radius:36px 36px 36px 6px;padding:24px 32px;font-weight:700;font-size:46px;color:var(--ink);box-shadow:10px 10px 0 var(--y);opacity:0}}
#pay2{{position:absolute;left:0;right:0;top:790px;display:flex;justify-content:center;opacity:0}}
#pay2 div{{background:#E5484D;color:#fff;font-weight:800;font-size:33px;padding:12px 22px;border:4px solid #fff;white-space:nowrap}}
#pay div{{background:var(--ink)!important;color:var(--y)!important;border-color:var(--y)!important;font-size:38px!important;white-space:nowrap}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
<video id="base" data-start="0" data-duration="{DUR}" data-track-index="0" src="assets/base.mp4" muted playsinline></video>
<audio id="voice" data-start="0" data-duration="{DUR}" data-track-index="1" src="assets/voice.wav" data-volume="1"></audio>
<div id="ov" class="clip" data-start="0" data-duration="{DUR}" data-track-index="2">
 <div id="lbl">Моё выступление · <b>Суровый Питерский форум</b></div>
 <div id="h">2ГИС работает не везде. <span>Вот где он окупается</span></div>
 <div id="pay"><div>В 2ГИС МЕСТА В ВЫДАЧЕ ПРОДАЮТСЯ</div></div>
 <div class="tag bad" id="tb">ЦФО: часто не окупается</div>
 <div class="tag good" id="tg">Восток: работает изумительно</div>
 <div id="res"><div class="t">Красноярск · ритуальные услуги · реклама 2ГИС</div><div class="s">результаты за месяц, слайд выступления</div>
  <div class="grid"><div class="c"><div class="v g">352</div><div class="k">открыли карточку</div></div><div class="c"><div class="v g">48</div><div class="k">звонков</div></div>
  <div class="c"><div class="v g">32</div><div class="k">маршрута</div></div><div class="c"><div class="v g">70</div><div class="k">переходов на сайт</div></div></div></div>
 <div id="pay2"><div>ВОСТОК — 2ГИС ОКУПАЕТСЯ</div></div>
 {"".join(CH)}
</div></div>
<script src="assets/gsap.min.js"></script><script>
window.__timelines=window.__timelines||{{}};
const tl=gsap.timeline({{paused:true}});
tl.fromTo("#lbl",{{opacity:0,y:-20}},{{opacity:1,y:0,duration:.3,ease:"power2.out"}},0.05);
tl.fromTo("#h",{{opacity:0,scale:1.25}},{{opacity:1,scale:1,duration:.35,ease:"expo.out",transformOrigin:"0 0"}},0.05);
tl.fromTo("#pay",{{opacity:0,scale:1.5}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},7.8);
tl.set("#pay",{{opacity:0}},9.3);
tl.fromTo("#tb",{{opacity:0,scale:1.4,rotation:-6}},{{opacity:1,scale:1,rotation:-3,duration:.3,ease:"back.out(2)"}},23.4);
tl.fromTo("#tg",{{opacity:0,scale:1.4,rotation:6}},{{opacity:1,scale:1,rotation:3,duration:.3,ease:"back.out(2)"}},28.78);
tl.set(["#tb","#tg"],{{opacity:0}},36.3);
tl.fromTo("#res",{{opacity:0,scale:.92}},{{opacity:1,scale:1,duration:.3,ease:"power3.out"}},36.38);
tl.from("#res .c",{{opacity:0,y:30,duration:.3,stagger:.45,ease:"power2.out"}},41.5);
tl.fromTo("#pay2",{{opacity:0,scale:1.5}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},44.1);
{chr(10).join(JS)}
window.__timelines["main"]=tl;
</script></body></html>'''
open(os.path.join(P,'index.html'),'w',encoding='utf-8').write(html)
