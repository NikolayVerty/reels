# Нарезка фрагмента выступления «Суровый питерский форум» в вертикаль: слайд сверху, спикер снизу.
import json, wave, numpy as np, subprocess, sys, os
TALK, WAV, WORDS, OUT = sys.argv[1:5]
segs=[(440.10,441.98),(442.70,444.38),(445.38,450.92),(451.76,459.20),(462.76,472.36),(476.46,482.62),(482.98,487.72),(491.58,505.30)]
wf=wave.open(WAV); a=np.frombuffer(wf.readframes(wf.getnframes()),dtype=np.int16).astype(np.float32)/32768
db=20*np.log10(np.sqrt(np.convolve(a**2,np.ones(400)/400,'same'))[::160]+1e-9); thr=np.percentile(db,95)-30
def tight(s,e):
    i0,i1=int(s*100),int(e*100); idx=np.where(db[i0:i1]>thr)[0]
    return (s,e) if len(idx)==0 else (max(s,(i0+idx[0])/100-0.06), min(e+0.0,(i0+idx[-1])/100+0.10))
cuts=[tight(*x) for x in segs]
words=json.load(open(WORDS))['words']; nw=[]; off=0
for s,e in cuts:
    for x in words:
        if min(x['end'],e)-max(x['start'],s)>0.06: nw.append({'text':x['text'],'start':round(max(x['start'],s)-s+off,3),'end':round(min(x['end'],e)-s+off,3)})
    off+=e-s
os.makedirs(OUT,exist_ok=True)
json.dump({'source':'Николай Вертий Суровый питерский.mp4','cuts':[{'start':round(s,3),'end':round(e,3)} for s,e in cuts]},open(OUT+'/edit-decisions.json','w'),indent=1)
json.dump({'words':nw},open(OUT+'/transcript.json','w'),ensure_ascii=False,indent=0)
f=[]; n=len(cuts)
for i,(s,e) in enumerate(cuts):
    d=e-s
    f.append(f"[0:v]trim={s}:{e},setpts=PTS-STARTPTS[v{i}];[0:a]atrim={s}:{e},asetpts=PTS-STARTPTS,afade=t=in:d=0.015,afade=t=out:st={d-0.02:.3f}:d=0.02[a{i}]")
f.append(''.join(f"[v{i}][a{i}]" for i in range(n))+f"concat=n={n}:v=1:a=1[v][a]")
f.append("[v]split[v1][v2];[v1]crop=1162:660:44:352,scale=1080:613:flags=lanczos[sl];[v2]crop=640:600:1236:352,scale=1080:1012:flags=lanczos,unsharp=5:5:0.4[sp]")
f.append("color=c=0x0F0F12:s=1080x1920:r=30[bg];[bg][sl]overlay=0:270:shortest=1[b1];[b1][sp]overlay=0:908,fps=30,format=yuv420p[vo]")
f.append("[a]highpass=f=80,acompressor=threshold=-20dB:ratio=3:attack=5:release=80,loudnorm=I=-14:TP=-1.5:LRA=7,aresample=48000[ao]")
subprocess.run(['ffmpeg','-v','error','-y','-i',TALK,'-filter_complex',';'.join(f),'-map','[vo]','-map','[ao]','-c:v','libx264','-crf','17','-preset','medium','-c:a','aac','-b:a','192k',OUT+'/base.mp4'],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',OUT+'/base.mp4','-vn','-c:a','pcm_s16le',OUT+'/voice.wav'],check=True)
print([ (round(s,2),round(e,2)) for s,e in cuts], round(off,2))
print(' '.join(f"{x['text']}[{x['start']:.2f}]" for x in nw))
