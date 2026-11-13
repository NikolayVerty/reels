import sys, json
from faster_whisper import WhisperModel
audio, out, size = sys.argv[1], sys.argv[2], sys.argv[3]
m = WhisperModel(size, device="cpu", compute_type="int8")
import numpy as np, wave
wf=wave.open(audio); a=np.frombuffer(wf.readframes(wf.getnframes()),dtype=np.int16).astype(np.float32)/32768
segs, info = m.transcribe(a, language="ru", word_timestamps=True, vad_filter=False, beam_size=5,
    initial_prompt="Яндекс Карты, топ-10, восемьдесят шесть процентов, четырнадцать процентов, заново.")
words=[]; lines=[]
for s in segs:
    lines.append(f"[{s.start:6.2f}-{s.end:6.2f}] {s.text.strip()}")
    for w in s.words: words.append({"text": w.word.strip(), "start": round(w.start,3), "end": round(w.end,3), "p": round(w.probability,3)})
json.dump({"words": words}, open(out,"w"), ensure_ascii=False, indent=0)
print("\n".join(lines))
