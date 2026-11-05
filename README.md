# Reels

Генератор вертикальных рилсов (1080×1920, 30 fps, H.264 + AAC) из простого JSON-сценария. Нужны только `python3` и `ffmpeg`.

```bash
python3 render.py scenarios/example.json   # -> output/example.mp4
```

## Сценарий

```json
{
  "defaults": { "duration": 2.5, "size": 88, "color": "white" },
  "music": "../assets/music/track.mp3",
  "music_volume": 0.8,
  "scenes": [
    { "bg": "#0f172a", "text": "Заголовок" },
    { "bg": "../assets/media/photo.jpg", "text": "Текст поверх фото" },
    { "bg": "../assets/media/clip.mp4", "start": 4, "duration": 3, "text": "Текст поверх видео", "position": "bottom", "box": true }
  ]
}
```

Поля сцены (любое можно задать в `defaults`):

| Поле | Значение |
|---|---|
| `bg` | цвет `#RRGGBB`, путь к фото (с лёгким наездом камеры) или к видео |
| `text` | текст; переносится автоматически, `\n` — ручной перенос |
| `duration` | длительность сцены, сек |
| `start` | с какой секунды брать видео-фон |
| `size`, `color`, `font` | размер, цвет, путь к шрифту .ttf |
| `position` | `top`, `center`, `bottom` |
| `box`, `boxcolor` | плашка под текстом |
| `dim` | затемнение фото/видео-фона (0–1, по умолчанию 0.35) |
| `fade` | длительность появления/исчезновения сцены |

Пути к файлам указываются относительно файла сценария. Свои фото/видео кладите в `assets/media/`, музыку — в `assets/music/`. Готовые ролики появляются в `output/` (в git не попадают).
