# Вторая проверка речи по ГОТОВОМУ ролику: расшифровка финального mp4 + громкость на стыках.
# python3 -I instagram/edits/tools/check_speech.py <final.mp4> <edit-decisions.json>
import sys, json, subprocess, tempfile, os, wave, numpy as np
mp4, edl = sys.argv[1], sys.argv[2]
tmp = tempfile.mkdtemp(); wav = os.path.join(tmp, 'a.wav')
subprocess.run(['ffmpeg','-v','error','-y','-i',mp4,'-vn','-ac','1','-ar','16000',wav],check=True)
subprocess.run([sys.executable,'-I',os.path.join(os.path.dirname(__file__),'transcribe.py'),wav,os.path.join(tmp,'w.json'),'medium'],env={**os.environ,'HF_HUB_DISABLE_XET':'1'})
wf = wave.open(wav); a = np.frombuffer(wf.readframes(wf.getnframes()),dtype=np.int16).astype(float); sr=16000
t = 0
print('\nСтыки (дБ за 60 мс до/после склейки; >60 с обеих сторон — риск обрыва слова):')
for c in json.load(open(edl))['cuts'][:-1]:
    t += c['end'] - c['start']; i = int(t*sr); w = int(0.06*sr)
    db = lambda s: int(20*np.log10(np.sqrt((s**2).mean())+1))
    print(f'  {t:6.2f} c: {db(a[i-w:i]):3d} | {db(a[i:i+w]):3d}')
