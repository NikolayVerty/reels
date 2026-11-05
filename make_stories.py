#!/usr/bin/env python3
"""Рисует кадры сторис (1080x1920 PNG) и обложки хайлайтов из JSON.

    python3 make_stories.py instagram/highlights/highlights.json   # -> output/highlights/
"""
import json, os, subprocess, sys, tempfile, textwrap

W, H = 1080, 1920
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BG, ACCENT, TEXT, MUTED = "0x0F172A", "0xF97316", "white", "0x94A3B8"
HANDLE = "@nikolay_verty"


def esc(p):
    return p.replace("\\", "\\\\").replace(":", "\\:").replace("'", "\\'")


def wrap(text, chars):
    out = []
    for para in text.split("\n"):
        out.extend(textwrap.wrap(para, chars) or [""])
    return "\n".join(out)


def draw(tmp, name, text, font, size, color, y, chars):
    f = os.path.join(tmp, name)
    with open(f, "w", encoding="utf-8") as fh:
        fh.write(wrap(text, chars))
    return (f"drawtext=fontfile='{esc(font)}':textfile='{esc(f)}':fontsize={size}:fontcolor={color}"
            f":line_spacing={int(size*0.35)}:text_align=center:x=(w-text_w)/2:y={y}")


def render(filters, out):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c={BG}:s={W}x{H}:d=1",
                    "-vf", ",".join(filters), "-frames:v", "1", out], check=True)


def main():
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "highlights")
    tmp = tempfile.mkdtemp()
    for hl in data["highlights"]:
        d = os.path.join(root, hl["id"]); os.makedirs(d, exist_ok=True)
        # обложка: круг с акцентом и словом по центру
        render([f"drawbox=x=0:y=0:w={W}:h={H}:color={ACCENT}:t=fill",
                draw(tmp, "c.txt", hl["cover"], BOLD, 150 if len(hl["cover"]) <= 6 else 110, BG, "(h-text_h)/2", 20)],
               os.path.join(d, "00-cover.png"))
        n = len(hl["frames"])
        for i, fr in enumerate(hl["frames"], 1):
            body_len = len(fr["body"])
            bsize = 58 if body_len < 120 else 50
            render([f"drawbox=x=480:y=330:w=120:h=10:color={ACCENT}:t=fill",
                    draw(tmp, "l.txt", fr["label"], BOLD, 40, ACCENT, 380, 40),
                    draw(tmp, "t.txt", fr["title"], BOLD, 88, TEXT, 520, 16),
                    draw(tmp, "b.txt", fr["body"], REG, bsize, TEXT, 900, 30 if bsize == 58 else 34),
                    draw(tmp, "h.txt", f"{HANDLE}   {i}/{n}", REG, 36, MUTED, 1560, 60)],
                   os.path.join(d, f"{i:02d}.png"))
        print(f"{hl['id']}: обложка + {n} кадров")
    print("Готово:", root)


if __name__ == "__main__":
    main()
