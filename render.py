#!/usr/bin/env python3
"""Рендер вертикальных рилсов (1080x1920) из JSON-сценария с помощью ffmpeg.

Использование:
    python3 render.py scenarios/example.json            # -> output/example.mp4
    python3 render.py scenarios/example.json -o my.mp4
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import textwrap

W, H = 1080, 1920
FPS = 30
DEFAULT_FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
VIDEO_EXT = {".mp4", ".mov", ".m4v", ".webm", ".mkv", ".avi"}


def run(cmd):
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-3000:])
        sys.exit(f"ffmpeg завершился с ошибкой: {' '.join(cmd[:6])} ...")


def wrap(text, size):
    # примерная ширина символа ~0.6 от размера шрифта, поля по 80px
    max_chars = max(8, int((W - 160) / (size * 0.6)))
    lines = []
    for para in text.split("\n"):
        lines.extend(textwrap.wrap(para, max_chars) or [""])
    return "\n".join(lines)


def esc(path):
    # экранирование пути для аргументов фильтра ffmpeg
    return path.replace("\\", "\\\\").replace(":", "\\:").replace("'", "\\'")


def render_scene(scene, idx, base_dir, defaults, tmp):
    dur = float(scene.get("duration", defaults.get("duration", 3)))
    bg = scene.get("bg", defaults.get("bg", "#111111"))
    fade = float(scene.get("fade", defaults.get("fade", 0.3)))
    out = os.path.join(tmp, f"scene_{idx:03d}.mp4")

    cover = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1"
    if bg.startswith("#"):
        inputs = ["-f", "lavfi", "-i", f"color=c=0x{bg[1:]}:s={W}x{H}:r={FPS}:d={dur}"]
        chain = "setsar=1"
    else:
        path = bg if os.path.isabs(bg) else os.path.join(base_dir, bg)
        if not os.path.exists(path):
            sys.exit(f"Файл фона не найден: {path}")
        ext = os.path.splitext(path)[1].lower()
        if ext in IMAGE_EXT:
            inputs = ["-loop", "1", "-framerate", str(FPS), "-t", str(dur), "-i", path]
            # лёгкий наезд камеры (zoom ~ +8% за сцену)
            frames = int(dur * FPS)
            chain = (f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
                     f"zoompan=z='1+0.08*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                     f":d=1:s={W}x{H}:fps={FPS},setsar=1")
        elif ext in VIDEO_EXT:
            start = float(scene.get("start", 0))
            inputs = ["-stream_loop", "-1", "-ss", str(start), "-t", str(dur), "-i", path]
            chain = f"{cover},fps={FPS}"
        else:
            sys.exit(f"Неизвестный тип фона: {path}")
        if scene.get("dim", defaults.get("dim", 0.35)):
            d = float(scene.get("dim", defaults.get("dim", 0.35)))
            chain += f",drawbox=x=0:y=0:w={W}:h={H}:color=black@{d}:t=fill"

    text = scene.get("text", "")
    if text:
        size = int(scene.get("size", defaults.get("size", 84)))
        color = scene.get("color", defaults.get("color", "white"))
        font = scene.get("font", defaults.get("font", DEFAULT_FONT))
        pos = scene.get("position", defaults.get("position", "center"))
        y = {"top": "h*0.15", "center": "(h-text_h)/2", "bottom": "h*0.78-text_h"}.get(pos, pos)
        tf = os.path.join(tmp, f"text_{idx:03d}.txt")
        with open(tf, "w", encoding="utf-8") as f:
            f.write(wrap(text, size))
        draw = (f"drawtext=fontfile='{esc(font)}':textfile='{esc(tf)}':fontsize={size}"
                f":fontcolor={color}:line_spacing={int(size*0.25)}:text_align=center"
                f":x=(w-text_w)/2:y={y}:shadowcolor=black@0.6:shadowx=3:shadowy=3")
        if scene.get("box", defaults.get("box", False)):
            draw += f":box=1:boxcolor={scene.get('boxcolor', defaults.get('boxcolor', 'black@0.55'))}:boxborderw=30"
        # появление текста с небольшой задержкой
        draw += f":alpha='min(1,max(0,(t-0.15)/0.35))'"
        chain += "," + draw

    if fade > 0:
        chain += f",fade=t=in:st=0:d={fade},fade=t=out:st={max(0, dur-fade)}:d={fade}"
    chain += ",format=yuv420p"

    run(["ffmpeg", "-y", "-hide_banner", *inputs, "-vf", chain, "-t", str(dur), "-an",
         "-r", str(FPS), "-c:v", "libx264", "-preset", "medium", "-crf", "20", out])
    return out, dur


def main():
    ap = argparse.ArgumentParser(description="Рендер рилса из JSON-сценария")
    ap.add_argument("scenario")
    ap.add_argument("-o", "--output")
    args = ap.parse_args()

    with open(args.scenario, encoding="utf-8") as f:
        sc = json.load(f)
    base_dir = os.path.dirname(os.path.abspath(args.scenario))
    root = os.path.dirname(os.path.abspath(__file__))
    out = args.output or os.path.join(root, "output",
                                      os.path.splitext(os.path.basename(args.scenario))[0] + ".mp4")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    defaults = sc.get("defaults", {})

    tmp = tempfile.mkdtemp(prefix="reel_")
    try:
        clips, total = [], 0.0
        for i, scene in enumerate(sc["scenes"]):
            print(f"Сцена {i+1}/{len(sc['scenes'])}...", flush=True)
            clip, d = render_scene(scene, i, base_dir, defaults, tmp)
            clips.append(clip)
            total += d
        lst = os.path.join(tmp, "list.txt")
        with open(lst, "w") as f:
            f.writelines(f"file '{c}'\n" for c in clips)
        video = os.path.join(tmp, "video.mp4")
        run(["ffmpeg", "-y", "-hide_banner", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", video])

        music = sc.get("music")
        if music:
            mpath = music if os.path.isabs(music) else os.path.join(base_dir, music)
            vol = float(sc.get("music_volume", 1.0))
            audio = ["-stream_loop", "-1", "-ss", str(sc.get("music_start", 0)), "-i", mpath]
            af = f"volume={vol},afade=t=in:d=0.5,afade=t=out:st={max(0, total-1.5)}:d=1.5"
        else:
            # тихая дорожка — соцсети лучше принимают видео со звуком
            audio = ["-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo"]
            af = "anull"
        run(["ffmpeg", "-y", "-hide_banner", "-i", video, *audio, "-map", "0:v", "-map", "1:a",
             "-af", af, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", str(total),
             "-movflags", "+faststart", out])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print(f"Готово: {out} ({total:.1f} с)")


if __name__ == "__main__":
    main()
