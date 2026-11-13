import json, subprocess, sys, time, statistics
OUT=sys.argv[1]
names_old={'direct':['Geo Leads Клиенты с Яндекс Карт','Дмитрий Пекный Продвижение через карты','Геомаркетинг для бизнеса','Агентство Репутация отзывы','Сергейкин про Маркетинг','Дядя Волк Денис Иванов'],
 'adjacent':['Трафикмолл маркетинг b2b','МРАКЕТПЛЕЙСЫ wildberries','Александр Кушков бизнес','маркетолог Ирина Пинчук','Сергей Абдульманов книги про бизнес'],
 'outsized':['Оскар Хартманн','Михаил Гребенюк','Аяз Шабутдинов','Игорь Рыбаков','Маргулан Сейсембай','Бизнес Молодость Осипов']}
names={'direct':['Geo Leads Яндекс Карты','геомаркетинг яндекс карты shorts'],
 'adjacent':['Трафикмолл','продажи маркетинг shorts Антон Власов'],
 'outsized':['Михаил Гребенюк shorts','Оскар Хартманн shorts','Аяз Шабутдинов shorts','Игорь Рыбаков shorts','Дмитрий Портнягин shorts','Бизнес секреты shorts']}
def run(args):
    r=subprocess.run([sys.executable,'-m','yt_dlp','--flat-playlist','-J']+args,capture_output=True,text=True,timeout=300)
    try: return json.loads(r.stdout)
    except Exception: return None
res=[]
for kind,ns in names.items():
    for n in ns:
        d=run(['ytsearch3:'+n])
        time.sleep(6)
        if not d: print('search fail',n); time.sleep(5); continue
        ch=next((e for e in d['entries'] if e and e.get('channel_url')),None)
        if not ch: print('no channel',n); continue
        url=ch['channel_url'].rstrip('/')+'/shorts'
        s=run(['--playlist-end','40',url]); time.sleep(3)
        if not s or not s.get('entries'): print('no shorts',n,ch.get('channel')); continue
        E=[e for e in s['entries'] if e and e.get('view_count')]
        if len(E)<5: print('few',n,len(E)); continue
        med=statistics.median([e['view_count'] for e in E])
        for e in E: res.append({'kind':kind,'channel':ch.get('channel'),'url':'https://www.youtube.com/shorts/'+e['id'],'id':e['id'],'title':e.get('title'),'views':e['view_count'],'median':med,'x':round(e['view_count']/med,1) if med else 0})
        print(kind,ch.get('channel'),len(E),'median',int(med),'max',max(e['view_count'] for e in E),flush=True)
old=json.load(open(OUT)) if __import__('os').path.exists(OUT) else []
seen={r['id'] for r in old}
res=old+[r for r in res if r['id'] not in seen]
json.dump(res,open(OUT,'w'),ensure_ascii=False,indent=0)
