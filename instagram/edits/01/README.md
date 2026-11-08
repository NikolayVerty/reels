# 01 · «Двадцать мест. Десять забирают всё» — рецепт монтажа

Исходник `1.MOV` (464×848, 103,7 с) → ролик 1080×1920, 35,7 с, −14 LUFS. Видео в git не храним.

1. `transcribe.py audio.wav words.json medium` — faster-whisper (модель с huggingface.co, окружение `reels`).
2. `cut.py <папка>` — нарезка: `edit-decisions.json` (оставлены последние дубли «вопрос» и «открой карты»), пересчёт таймкодов → `transcript.json`.
3. Склейка ffmpeg (масштаб до 1080×1920, компрессор, loudnorm −14) → `video-projects/01-dvadtsat-mest/assets/cut.mp4` + `voice.wav`.
4. `build.py` → `index.html` (HyperFrames + GSAP, стиль «редакционный коллаж» из `instagram/edit-style.md`), затем `npx hyperframes render --quality high`.
