# Тест рубрики «Худшие отзывы»: фрагменты выступления (слайд сверху, спикер снизу) + мем-вставки Cutzo на весь экран.
import subprocess, sys, json
TALK, MEM, OUT = sys.argv[1:4]
seq=[('t',1779.80,1782.80),('m','da-eto-zhestko.mp4',0.85,2.33),('t',1782.81,1783.97),('m','vot.mp4',2.85,5.94),('t',1784.58,1786.38),('t',1788.42,1792.40),('s',0.5)]
inputs=['-i',TALK]; mi={}
for x in seq:
    if x[0]=='m' and x[1] not in mi: mi[x[1]]=len(mi)+1; inputs+=['-i',f'{MEM}/{x[1]}']
f=[];labels=[];t=0;timeline=[]
for i,x in enumerate(seq):
    if x[0]=='t':
        s,e=x[1],x[2]; d=e-s
        f.append(f"[0:v]trim={s}:{e},setpts=PTS-STARTPTS,split[a{i}][b{i}];[a{i}]crop=1162:660:44:352,scale=1080:613[sl{i}];[b{i}]crop=640:600:1236:352,scale=1080:1012,unsharp=5:5:0.4[sp{i}];color=c=0x0F0F12:s=1080x1920:r=30:d={d}[bg{i}];[bg{i}][sl{i}]overlay=0:270[x{i}];[x{i}][sp{i}]overlay=0:908,fps=30,format=yuv420p,setsar=1[v{i}]")
        f.append(f"[0:a]atrim={s}:{e},asetpts=PTS-STARTPTS,afade=t=in:d=0.015,afade=t=out:st={d-0.05:.3f}:d=0.05,aresample=48000,aformat=channel_layouts=stereo[au{i}]")
        timeline.append(('talk',round(t,2),round(t+d,2)))
    elif x[0]=='m':
        k=mi[x[1]]; s,e=x[2],x[3]; d=e-s
        f.append(f"[{k}:v]trim={s}:{e},setpts=PTS-STARTPTS,split[a{i}][b{i}];[a{i}]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:3[bg{i}];[b{i}]scale=1080:1500:force_original_aspect_ratio=decrease[fg{i}];[bg{i}][fg{i}]overlay=(W-w)/2:(H-h)/2,fps=30,format=yuv420p,setsar=1[v{i}]")
        f.append(f"[{k}:a]atrim={s}:{e},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={d-0.06:.3f}:d=0.06,aresample=48000,aformat=channel_layouts=stereo[au{i}]")
        timeline.append(('meme',round(t,2),round(t+d,2)))
    else:
        d=x[1]
        f.append(f"[v{i-1}]trim=0:0.04,loop=loop={int(d*30)}:size=1:start=0,setpts=N/30/TB,trim=0:{d}[v{i}]") if False else None
        f.append(f"color=c=0x0F0F12:s=1080x1920:r=30:d={d},format=yuv420p,setsar=1[v{i}];anullsrc=r=48000:cl=stereo,atrim=0:{d}[au{i}]")
    t+=d; labels.append(f"[v{i}][au{i}]")
f=[x for x in f if x]
f.append(''.join(labels)+f"concat=n={len(seq)}:v=1:a=1[v][a];[a]loudnorm=I=-14:TP=-1.5:LRA=9[ao]")
subprocess.run(['ffmpeg','-v','error','-y',*inputs,'-filter_complex',';'.join(f),'-map','[v]','-map','[ao]','-c:v','libx264','-crf','17','-c:a','aac','-b:a','192k',OUT+'/base.mp4'],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',OUT+'/base.mp4','-vn','-c:a','pcm_s16le',OUT+'/voice.wav'],check=True)
json.dump({'timeline':timeline,'dur':round(t,2)},open(OUT+'/timeline.json','w'))
print(timeline, round(t,2))
