import sys,os
S=sys.argv[1]
covers=[
 ('sp01',278,'Часть 1','2ГИС <mark>бесплатно</mark> покажет трафик конкурентов','<b>×2,3</b><i>показов у 5–6-го места против 10-го</i>'),
 ('sp02',468,'Часть 2','Почему клиент уходит к <mark>соседу</mark> ещё до звонка','<b>★4,9 vs ★4,2</b><i>куда пойдёшь ты?</i>'),
 ('sp03',480,'Часть 3','Яндекс <mark>сам опускает</mark> тебя в выдаче','<b>88% → 55%</b><i>отказов после работы с рейтингом</i>'),
 ('sp04',545,'Часть 4','Автосалон: лиды по <mark>439&nbsp;₽</mark> с&nbsp;карт','<b>2 318</b><i>лидов за 8 месяцев</i>'),
 ('sp05',595,'Часть 5','Чек-лист: <mark>9&nbsp;пунктов</mark> для Яндекс Карт','<b>Сохрани</b><i>чтобы не потерять</i>'),
 ('sp06',690,'Часть 6','Google ушёл. <mark>А&nbsp;его карты</mark> работают','<b>23 звонка</b><i>без продвижения, с нуля</i>'),
 ('sp07',750,'Часть 7','2ГИС работает <mark>не&nbsp;везде</mark>','<b>Восток ✓</b><i>там окупается, в центре — часто нет</i>'),
 ('sp08',1784,'Часть 8','Моё хобби — читать <mark>плохие отзывы</mark>','<b>25 000</b><i>просмотров одного плохого отзыва</i>'),
 ('sp09',1920,'Часть 9','Отзыв не прошёл? <mark>Виноват VPN</mark>','<b>Без VPN</b><i>и только с места — тогда пройдёт</i>'),
]
css='''@font-face{font-family:M;font-weight:800;src:url(manrope-cyrillic-800-normal.woff2)}
@font-face{font-family:M;font-weight:800;src:url(manrope-latin-800-normal.woff2);unicode-range:U+0000-00FF}
@font-face{font-family:M;font-weight:700;src:url(manrope-cyrillic-700-normal.woff2)}
@font-face{font-family:M;font-weight:700;src:url(manrope-latin-700-normal.woff2);unicode-range:U+0000-00FF}
html,body{margin:0}
.c{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:M;background-color:#ECEBE6;
background-image:linear-gradient(rgba(15,15,18,.07) 2px,transparent 2px),linear-gradient(90deg,rgba(15,15,18,.07) 2px,transparent 2px),linear-gradient(rgba(15,15,18,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(15,15,18,.035) 1px,transparent 1px);background-size:120px 120px,120px 120px,24px 24px,24px 24px}
.top{position:absolute;left:70px;top:270px;display:flex;gap:16px;align-items:center}
.tag{background:#0F0F12;color:#FFC24B;font-weight:800;font-size:34px;padding:8px 18px}
.ev{font-weight:700;font-size:30px;color:#55555c}
h1{position:absolute;left:70px;top:350px;width:940px;margin:0;font-weight:800;font-size:112px;line-height:1.02;color:#0F0F12;letter-spacing:-1px}
h1 mark{background:linear-gradient(transparent 20%,#FFC24B 20%,#FFC24B 90%,transparent 90%);color:#0F0F12;padding:0 8px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.sp{position:absolute;left:50%;bottom:150px;width:1240px;transform:translateX(-50%);filter:drop-shadow(0 0 0 #fff) drop-shadow(10px 0 0 #fff) drop-shadow(-10px 0 0 #fff) drop-shadow(0 10px 0 #fff) drop-shadow(0 -10px 0 #fff) drop-shadow(14px 18px 0 rgba(15,15,18,.18))}
.st{position:absolute;right:50px;bottom:290px;background:#fff;border:5px solid #0F0F12;box-shadow:10px 10px 0 #FFC24B;padding:18px 26px;transform:rotate(-4deg);max-width:440px}
.st b{display:block;white-space:nowrap;font-weight:800;font-size:68px;color:#16A34A;line-height:1}
.st i{display:block;font-style:normal;font-weight:700;font-size:28px;color:#0F0F12;margin-top:8px;line-height:1.15}
.bot{position:absolute;left:0;right:0;bottom:0;height:150px;background:#0F0F12}
'''
for code,t,tag,h,stat in covers:
    html=f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><div class="c"><div class="top"><span class="tag">{tag}</span><span class="ev">Моё выступление · Суровый Питерский форум</span></div><h1>{h}</h1><img class="sp" src="cut_{t}.png"><div class="bot"></div><div class="st">{stat}</div></div></body></html>'
    open(os.path.join(S,f'{code}.html'),'w',encoding='utf-8').write(html)
