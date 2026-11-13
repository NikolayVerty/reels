# Вставка из записи экрана: размыть название/адрес/контакты чужой карточки, пропустить ввод номера.
import subprocess, sys
SRC, OUT = sys.argv[1], sys.argv[2]
blur=[(4.6,6.75,95,200),(5.9,7.8,185,385),(7.5,8.35,40,250),(11.8,13.2,780,980)]  # (t0,t1,y0,y1) в исходнике
f=["[0:v]fps=30,scale=590:1280,setsar=1[s0]"]; cur='s0'
for i,(t0,t1,y0,y1) in enumerate(blur):
    f.append(f"[{cur}]split[m{i}][c{i}];[c{i}]crop=590:{y1-y0}:0:{y0},boxblur=luma_radius=18:luma_power=3:chroma_radius=10:chroma_power=3[b{i}];[m{i}][b{i}]overlay=0:{y0}:enable='between(t,{t0},{t1})'[s{i+1}]"); cur=f's{i+1}'
f.append(f"[{cur}]split=3[x][y][z];[x]trim=4.6:8.3,setpts=PTS-STARTPTS[pa];[y]trim=11.8:13.1,setpts=PTS-STARTPTS[pb];[z]trim=25.7:27.5,setpts=PTS-STARTPTS[pc];[pa][pb][pc]concat=n=3:v=1:a=0,format=yuv420p[vo]")
subprocess.run(['ffmpeg','-v','error','-y','-i',SRC,'-filter_complex',';'.join(f),'-map','[vo]','-an','-c:v','libx264','-crf','17',OUT],check=True)
