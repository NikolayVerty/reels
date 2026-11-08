import json, wave, numpy as np, subprocess, sys
W=sys.argv[1]
wf=wave.open(f"{W}/audio.wav"); a=np.frombuffer(wf.readframes(wf.getnframes()),dtype=np.int16).astype(np.float32)/32768
sr=16000; hop=160
rms=np.sqrt(np.convolve(a**2,np.ones(400)/400,'same'))[::hop]  # 10ms
db=20*np.log10(rms+1e-9)
thr=np.percentile(db,95)-30
def tighten(s,e):
    i0,i1=int(s*100),int(e*100)
    seg=db[i0:i1]; idx=np.where(seg>thr)[0]
    if len(idx)==0: return s,e
    return (i0+idx[0])/100-0.06, (i0+idx[-1])/100+0.10
segs=[(5.0,9.3),(10.25,15.4),(17.8,20.8),(23.75,27.4),(37.6,40.55),(69.8,73.3),(73.8,76.9),(77.8,79.9),(81.6,84.1),(85.1,85.95),(88.6,92.95),(96.2,100.8)]
out=[tighten(s,e) for s,e in segs]
for (s,e),(a2,b2) in zip(segs,out): print(f"{s:6.2f}-{e:6.2f} -> {a2:6.2f}-{b2:6.2f} ({b2-a2:.2f})")
print("total", sum(b-a for a,b in out))
json.dump({"source":"raw.mov","cuts":[{"start":round(a,3),"end":round(b,3)} for a,b in out]},open(f"{W}/edl.json","w"),indent=1)
# retime words
words=json.load(open(f"{W}/words.json"))["words"]; nw=[]; off=0
for a2,b2 in out:
    for x in words:
        mid=(x["start"]+x["end"])/2
        if min(x["end"],b2)-max(x["start"],a2)>0.08: nw.append({"text":x["text"],"start":round(max(x["start"],a2)-a2+off,3),"end":round(min(x["end"],b2)-a2+off,3)})
    off+=b2-a2
json.dump({"words":nw},open(f"{W}/words_cut.json","w"),ensure_ascii=False,indent=0)
print(" ".join(f"{x['text']}[{x['start']:.2f}]" for x in nw))
