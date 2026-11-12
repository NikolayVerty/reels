# index.html для ролика из выступления: 2ГИС — статистику даст менеджер.
import os
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUR=26.96
caps=[(0.04,"Что важно учесть с картами?"),(1.58,"Я выделил 9 пунктов"),(3.04,"Заниматься репутацией,"),(4.62,"рейтингом"),(4.88,"Не запускать рекламу"),(6.78,"на неподготовленную карточку"),
(7.96,"Делать фирменный стиль,"),(9.78,"упаковку"),(10.82,"Понятный прайс"),(11.84,"для клиента и для робота"),(14.28,"Актуальные данные:"),(15.32,"телефоны, сайты —"),(16.32,"всё указано корректно"),
(17.98,"Отслеживать результат —"),(19.60,"иначе не получится"),(21.62,"потом масштабироваться"),(24.20,"И работать с негативом"),(25.82,"и репутацией")]
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
#st{{position:absolute;left:30px;top:282px;width:1020px;height:590px;background:#fff;border-radius:28px;box-shadow:0 0 0 40px var(--ink);box-sizing:border-box;padding:20px 40px;opacity:0}}
#st .t{{font-weight:800;font-size:38px;color:var(--ink);margin-bottom:6px}}
#st .it{{display:flex;align-items:center;gap:16px;font-weight:700;font-size:31px;line-height:1.05;color:var(--ink);padding:3px 0;border-top:2px solid #eee}}
#st .it b{{flex:none;width:40px;height:40px;border-radius:50%;background:var(--y);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:26px}}
#pay2{{position:absolute;left:0;right:0;top:895px;display:flex;justify-content:center;opacity:0}}
#bub2{{position:absolute;left:70px;top:620px;width:820px;background:#fff;border:5px solid var(--ink);border-radius:36px 36px 36px 6px;padding:24px 32px;font-weight:700;font-size:46px;color:var(--ink);box-shadow:10px 10px 0 var(--y);opacity:0}}
#pay2 div{{background:var(--ink);color:var(--y);font-weight:800;font-size:40px;padding:12px 26px;border:4px solid var(--y);white-space:nowrap}}
#pay div{{background:var(--ink)!important;color:var(--y)!important;border-color:var(--y)!important;font-size:34px!important;white-space:nowrap}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
<video id="base" data-start="0" data-duration="{DUR}" data-track-index="0" src="assets/base.mp4" muted playsinline></video>
<audio id="voice" data-start="0" data-duration="{DUR}" data-track-index="1" src="assets/voice.wav" data-volume="1"></audio>
<div id="ov" class="clip" data-start="0" data-duration="{DUR}" data-track-index="2">
 <div id="lbl">Моё выступление · <b>Суровый Питерский форум</b></div>
 <div id="h">9 пунктов, без которых карты <span>не приведут клиентов</span></div>
 <div id="st"><div class="t">9 пунктов для Яндекс Карт</div><div class="it" id="i1"><b>1</b>Репутация и рейтинг</div><div class="it" id="i2"><b>2</b>Не запускать рекламу на неготовую карточку</div><div class="it" id="i3"><b>3</b>Фирменный стиль и упаковка</div><div class="it" id="i4"><b>4</b>Прайс для клиента и для Яндекса</div><div class="it" id="i5"><b>5</b>Актуальные данные: телефон, сайт</div><div class="it" id="i6"><b>6</b>Правильно настроенная реклама</div><div class="it" id="i7"><b>7</b>Отслеживать результат</div><div class="it" id="i8"><b>8</b>Отвечать на отзывы в течение дня</div><div class="it" id="i9"><b>9</b>Работать с негативом</div></div>
 <div id="pay2"><div>СОХРАНИ ЧЕК-ЛИСТ</div></div>
 {"".join(CH)}
</div></div>
<script src="assets/gsap.min.js"></script><script>
window.__timelines=window.__timelines||{{}};
const tl=gsap.timeline({{paused:true}});
tl.fromTo("#lbl",{{opacity:0,y:-20}},{{opacity:1,y:0,duration:.3,ease:"power2.out"}},0.05);
tl.fromTo("#h",{{opacity:0,scale:1.25}},{{opacity:1,scale:1,duration:.35,ease:"expo.out",transformOrigin:"0 0"}},0.05);
tl.fromTo("#st",{{opacity:0,scale:.92}},{{opacity:1,scale:1,duration:.3,ease:"power3.out"}},2.9);
const T={{i1:3.04,i2:4.88,i3:7.96,i4:10.82,i5:14.28,i6:17.7,i7:17.98,i8:24.0,i9:24.2}};
for(const k in T) tl.from("#"+k,{{opacity:0,x:-40,duration:.25,ease:"power2.out"}},T[k]);
tl.fromTo("#pay2",{{opacity:0,scale:1.5}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},25.4);
{chr(10).join(JS)}
window.__timelines["main"]=tl;
</script></body></html>'''
open(os.path.join(P,'index.html'),'w',encoding='utf-8').write(html)
