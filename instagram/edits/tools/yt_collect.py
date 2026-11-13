import json, subprocess, sys
OUT=sys.argv[1]
Q={'narrow':['продвижение на яндекс картах','отзывы яндекс карты бизнес','2гис продвижение бизнеса','рейтинг на картах бизнес','локальный бизнес клиенты карты'],
   'broad':['маркетинг для бизнеса фишки','как продавать больше клиентам','продвижение бизнеса советы','маркетолог разбор бизнеса','ошибки предпринимателей маркетинг','как найти клиентов бизнесу','нейросеть для бизнеса маркетинг']}
rows={}
for bucket,qs in Q.items():
    for q in qs:
        r=subprocess.run([sys.executable,'-m','yt_dlp','--flat-playlist','--playlist-end','80','-J','https://www.youtube.com/results?search_query='+__import__('urllib.parse').parse.quote(q)+'&sp=EgIYAQ%253D%253D'],capture_output=True,text=True,timeout=300)
        try: d=json.loads(r.stdout)
        except Exception: print('fail',q,r.stderr[-200:]); continue
        n=0
        for e in d.get('entries',[]):
            if not e: continue
            dur=e.get('duration') or 999
            if dur>90 or not e.get('view_count'): continue
            vid=e['id']; n+=1
            rows[vid]={'id':vid,'bucket':bucket,'q':q,'title':e.get('title'),'views':e['view_count'],'dur':dur,'channel':e.get('channel'),'channel_url':e.get('channel_url')}
        print(bucket,q,n,flush=True)
json.dump(list(rows.values()),open(OUT,'w'),ensure_ascii=False,indent=0)
print('total',len(rows))
