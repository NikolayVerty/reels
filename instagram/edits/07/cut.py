# Ролик 07: лучшие дубли из сырой записи, кадр без ладоней (crop 338x600 @ 46,20 → 1080x1920).
import json, wave, numpy as np, subprocess, sys, os
RAW, WAV, WORDS, OUT = sys.argv[1:5]
segs=[(32.10,35.30),(45.40,50.95),(51.70,53.60),(71.35,76.90),(81.65,83.78),(88.00,92.70),(100.85,104.90),
(114.25,116.85),(121.72,122.64),(124.02,127.45),(137.15,142.50),(168.35,170.22),(172.90,176.95),(185.30,189.10),(197.80,202.90),(208.70,212.40),(237.25,241.85)]
wf=wave.open(WAV); a=np.frombuffer(wf.readframes(wf.getnframes()),dtype=np.int16).astype(np.float32)/32768
db=20*np.log10(np.sqrt(np.convolve(a**2,np.ones(400)/400,'same'))[::160]+1e-9); thr=np.percentile(db,95)-30
def tight(s,e):
    i0,i1=int(s*100),int(e*100); idx=np.where(db[i0:i1]>thr)[0]
    return (s,e) if len(idx)==0 else (max(s,(i0+idx[0])/100-0.06), min(e,(i0+idx[-1])/100+0.12))
cuts=[tight(*x) for x in segs]+[(segs[-1][1],segs[-1][1]+0.5)]
words=json.load(open(WORDS))['words']; nw=[]; off=0
for s,e in cuts:
    for x in words:
        if min(x['end'],e)-max(x['start'],s)>0.06: nw.append({'text':x['text'],'start':round(max(x['start'],s)-s+off,3),'end':round(min(x['end'],e)-s+off,3)})
    off+=e-s
os.makedirs(OUT,exist_ok=True)
json.dump({'source':'IMG_3255.MOV','cuts':[{'start':round(s,3),'end':round(e,3)} for s,e in cuts]},open(OUT+'/edit-decisions.json','w'),indent=1)
json.dump({'words':nw},open(OUT+'/transcript.json','w'),ensure_ascii=False,indent=0)
f=[]; n=len(cuts)
for i,(s,e) in enumerate(cuts):
    d=e-s; vol=',volume=0' if i==n-1 else ''; fo=0.08 if i==n-2 else 0.02
    f.append(f"[0:v]trim={s}:{e},setpts=PTS-STARTPTS[v{i}];[0:a]atrim={s}:{e},asetpts=PTS-STARTPTS,afade=t=in:d=0.015,afade=t=out:st={d-fo:.3f}:d={fo}{vol}[a{i}]")
f.append(''.join(f"[v{i}][a{i}]" for i in range(n))+f"concat=n={n}:v=1:a=1[v][a]")
f.append("[v]crop=338:600:46:20,scale=1080:1920:flags=lanczos,unsharp=5:5:0.7,fps=30,format=yuv420p[vo]")
f.append("[a]highpass=f=80,acompressor=threshold=-20dB:ratio=3:attack=5:release=80,loudnorm=I=-14:TP=-1.5:LRA=7,aresample=48000[ao]")
subprocess.run(['ffmpeg','-v','error','-y','-i',RAW,'-filter_complex',';'.join(f),'-map','[vo]','-map','[ao]','-c:v','libx264','-crf','16','-preset','medium','-c:a','aac','-b:a','192k',OUT+'/cut.mp4'],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',OUT+'/cut.mp4','-vn','-c:a','pcm_s16le',OUT+'/voice.wav'],check=True)
print([(round(s,2),round(e,2)) for s,e in cuts], round(off,2))
