#!/usr/bin/env python3
"""
generate_image.py - Dynamis-Zentrum Basel Instagram Bildgenerator
1080x1080px, 5 Kategorien mit warmem spirituellem Design.
"""
import argparse, base64, io, json, urllib.request
from datetime import datetime
from pathlib import Path

import openai
from PIL import Image, ImageDraw, ImageFilter, ImageFont

LOGO_PATH    = Path("assets/logo")
OUTPUT_DIR   = Path("output")
FONT_DIR     = Path("assets/fonts")
SPEAKER_DIR  = Path("assets/speaker_templates")

# Dynamis Brand Farben (von dynamis-zentrum.ch)
DYNAMIS_GOLD   = (196, 134,  30)   # warmes Gold aus dem Logo
DYNAMIS_ORANGE = (210, 120,  45)   # warmes Orange
DYNAMIS_DARK   = ( 20,  12,  35)   # tiefes Dunkelviolett
DYNAMIS_WARM   = (165, 120,  80)   # warmes Bernstein
DYNAMIS_WHITE  = (255, 248, 235)   # warmes Weiss

CATEGORY_CONFIGS = {
    "SEMINAR": {
        "label": "SEMINAR",
        "gradient_c1": (15, 8, 30), "gradient_c2": (60, 35, 10), "gradient_alpha": 175,
        "dalle_prompt": "mystical ancient forest, golden light rays through trees, spiritual transformation, warm amber tones, no text, no people",
    },
    "VORTRAG": {
        "label": "VORTRAG",
        "gradient_c1": (20, 12, 35), "gradient_c2": (80, 45, 15), "gradient_alpha": 170,
        "dalle_prompt": "warm mystical light, spiritual wisdom atmosphere, golden glow, deep shadows, no text, no people",
    },
    "INSPIRATIONSABEND": {
        "label": "INSPIRATIONSABEND",
        "gradient_c1": (25, 10, 10), "gradient_c2": (90, 40, 10), "gradient_alpha": 160,
        "dalle_prompt": "cozy candlelight atmosphere, warm golden and amber tones, intimate and inviting, soft bokeh, no text, no people",
    },
    "RÜCKBLICK": {
        "label": "RÜCKBLICK",
        "gradient_c1": (18, 12, 8), "gradient_c2": (70, 50, 20), "gradient_alpha": 150,
        "dalle_prompt": "warm golden memories, soft autumn light, gratitude and warmth, gentle bokeh, no text, no people",
    },
    "SPIRITUELL": {
        "label": "SPIRITUELL",
        "gradient_c1": (8, 5, 25), "gradient_c2": (35, 25, 60), "gradient_alpha": 145,
        "dalle_prompt": "ethereal cosmic light, meditation, soft purple and gold, transcendent atmosphere, no text, no people",
    },
}


def download_fonts():
    FONT_DIR.mkdir(parents=True, exist_ok=True)
    url = "https://github.com/googlefonts/roboto/raw/main/src/hinted/"
    for f in ["Roboto-Light.ttf", "Roboto-Regular.ttf", "Roboto-Bold.ttf", "Roboto-Black.ttf"]:
        p = FONT_DIR / f
        if not p.exists():
            print(f"Lade {f}...")
            try:
                urllib.request.urlretrieve(url + f, p)
            except Exception as e:
                print(f"  Warnung: {e}")

_FB = {"Roboto-Black.ttf": "Roboto-Bold.ttf", "Roboto-Light.ttf": "Roboto-Regular.ttf"}

def _font(name, size):
    for c in [name, _FB.get(name)]:
        if c:
            try:
                return ImageFont.truetype(str(FONT_DIR / c), size)
            except:
                pass
    return ImageFont.load_default(size=size)

def wrap_text(text, font, max_w):
    words, lines, cur = text.split(), [], []
    for w in words:
        t = " ".join(cur + [w])
        width = font.getlength(t) if hasattr(font, "getlength") else len(t) * 14
        if width <= max_w:
            cur.append(w)
        else:
            if cur:
                lines.append(" ".join(cur))
            cur = [w]
    if cur:
        lines.append(" ".join(cur))
    return lines


def _find_logo():
    """Sucht das Dynamis-Logo im assets/logo Ordner."""
    for ext in ["*.png", "*.jpg", "*.jpeg", "*.PNG", "*.JPG"]:
        matches = list(LOGO_PATH.glob(ext))
        if matches:
            return matches[0]
    return None

def _logo(h):
    p = _find_logo()
    if not p:
        return None
    im = Image.open(p).convert("RGBA")
    r = h / im.height
    return im.resize((int(im.width * r), h), Image.LANCZOS)

def _paste_logo(img, logo, x, y, white=True):
    if logo is None:
        return
    r, g, b, a = logo.split()
    color = (255, 255, 255) if white else DYNAMIS_DARK
    bg = Image.new("RGB", logo.size, color)
    bg.putalpha(a)
    img.paste(bg, (x, y), bg)


def _header(img, draw, label, accent=DYNAMIS_GOLD):
    """Standard Header: Logo links, Kategorie-Label rechts, goldene Trennlinie."""
    _paste_logo(img, _logo(65), 48, 36, white=True)
    draw.text((1032, 68), label, font=_font("Roboto-Bold.ttf", 26),
              fill=(*accent, 210), anchor="rm")
    draw.rectangle([(48, 122), (1032, 125)], fill=(*accent, 100))


def generate_background(prompt):
    client = openai.OpenAI()
    r = client.images.generate(
        model="gpt-image-1",
        prompt=f"Abstract photorealistic background, no text, no letters, no people, no faces, cinematic lighting, spiritual atmosphere: {prompt}",
        size="1024x1024", quality="medium", n=1,
    )
    data = base64.b64decode(r.data[0].b64_json)
    return Image.open(io.BytesIO(data)).convert("RGBA").resize((1080, 1080), Image.LANCZOS)


def apply_gradient_overlay(img, c1, c2, alpha):
    ov = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    for y in range(1080):
        t = y / 1080
        r = int(c1[0] + (c2[0] - c1[0]) * t)
        g = int(c1[1] + (c2[1] - c1[1]) * t)
        b = int(c1[2] + (c2[2] - c1[2]) * t)
        d.line([(0, y), (1080, y)], fill=(r, g, b, alpha))
    return Image.alpha_composite(img, ov)


def _darken(img, start_y=680, strength=80):
    ov = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    for y in range(start_y, 1080):
        t = (y - start_y) / (1080 - start_y)
        d.line([(0, y), (1080, y)], fill=(0, 0, 0, int(strength * t ** 1.4)))
    return Image.alpha_composite(img, ov)


def _soft_glow(img, color, cx, cy, radius, alpha):
    """Weiches Leuchten für spirituelle Atmosphäre."""
    glow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse(
        [(cx - radius, cy - radius), (cx + radius, cy + radius)],
        fill=(*color, alpha)
    )
    return Image.alpha_composite(img, glow.filter(ImageFilter.GaussianBlur(radius // 2)))


def _decorative_lines(img, color, alpha=40):
    """Dezente horizontale Zierlinien unten."""
    ov = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    for y, w in [(940, 800), (960, 600), (978, 400)]:
        x0 = (1080 - w) // 2
        d.line([(x0, y), (x0 + w, y)], fill=(*color, alpha), width=1)
    return Image.alpha_composite(img, ov)


def draw_layout_standard(img, title, subtitle, cfg_label, accent):
    """Standard Layout für SEMINAR, INSPIRATIONSABEND, RÜCKBLICK, SPIRITUELL."""
    img = _soft_glow(img, accent, 540, 400, 400, 18)
    img = _darken(img, 660, 90)

    draw = ImageDraw.Draw(img)
    _header(img, draw, cfg_label, accent)

    ft = _font("Roboto-Black.ttf", 72)
    fs = _font("Roboto-Light.ttf", 40)

    lines = wrap_text(title, ft, 920)
    y = 185
    for l in lines:
        draw.text((80, y), l, font=ft, fill=(*DYNAMIS_WHITE, 255))
        y += 88

    max_w = max(int(ft.getlength(l)) for l in lines)
    draw.rectangle([(80, y + 12), (80 + max_w, y + 16)], fill=(*accent, 220))

    if subtitle:
        draw.text((80, y + 42), subtitle, font=fs, fill=(*accent, 200))

    return _decorative_lines(img, accent, 45)


def draw_layout_vortrag(img, title, subtitle, speaker_cfg, accent):
    """Speaker-Layout für VORTRAG mit Redner-Stil."""
    img = _soft_glow(img, accent, 540, 380, 380, 22)
    img = _darken(img, 640, 95)

    draw = ImageDraw.Draw(img)
    _header(img, draw, "VORTRAG", accent)

    ft_name  = _font("Roboto-Black.ttf", 64)
    ft_theme = _font("Roboto-Light.ttf", 44)
    ft_sub   = _font("Roboto-Regular.ttf", 36)

    speaker_name = speaker_cfg.get("name", "")
    y = 185

    if speaker_name:
        draw.text((80, y), speaker_name, font=ft_name, fill=(*accent, 255))
        y += 80
        name_w = int(ft_name.getlength(speaker_name))
        draw.rectangle([(80, y + 4), (80 + name_w, y + 7)], fill=(*accent, 180))
        y += 30

    lines = wrap_text(title, ft_theme, 900)
    for l in lines:
        draw.text((80, y), l, font=ft_theme, fill=(*DYNAMIS_WHITE, 235))
        y += 60

    if subtitle:
        y += 12
        draw.text((80, y), subtitle, font=ft_sub, fill=(*accent, 185))

    return _decorative_lines(img, accent, 50)


def load_speaker_config(speaker_key):
    path = SPEAKER_DIR / f"{speaker_key}.json"
    if not path.exists():
        path = SPEAKER_DIR / "_default.json"
    try:
        with open(path, encoding="utf-8") as f:
            cfg = json.load(f)
        return cfg
    except Exception:
        return {"name": "", "layout_farbe_akzent": list(DYNAMIS_GOLD)}


def generate_post(title, subtitle, category, speaker=None, dalle_prompt=None):
    download_fonts()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    cfg = CATEGORY_CONFIGS.get(category, CATEGORY_CONFIGS["SEMINAR"])
    speaker_cfg = load_speaker_config(speaker) if speaker else {}

    # Akzentfarbe: aus Speaker-Config oder Kategorie-Default
    if speaker_cfg and "layout_farbe_akzent" in speaker_cfg:
        accent = tuple(speaker_cfg["layout_farbe_akzent"])
        c1 = tuple(speaker_cfg.get("gradient_c1", cfg["gradient_c1"]))
        c2 = tuple(speaker_cfg.get("gradient_c2", cfg["gradient_c2"]))
        alpha = speaker_cfg.get("gradient_alpha", cfg["gradient_alpha"])
        prompt = speaker_cfg.get("bild_hintergrund_stil", cfg["dalle_prompt"])
    else:
        accent = DYNAMIS_GOLD
        c1, c2, alpha = cfg["gradient_c1"], cfg["gradient_c2"], cfg["gradient_alpha"]
        prompt = cfg["dalle_prompt"]

    if dalle_prompt:
        prompt = dalle_prompt

    print(f"Kategorie: {cfg['label']}")
    print("Generiere Hintergrundbild...")
    bg = generate_background(prompt)
    print("Wende Gradient an...")
    img = apply_gradient_overlay(bg, c1, c2, alpha)
    print("Erstelle Layout...")

    if category == "VORTRAG":
        img = draw_layout_vortrag(img, title, subtitle, speaker_cfg, accent)
    else:
        img = draw_layout_standard(img, title, subtitle, cfg["label"], accent)

    out = OUTPUT_DIR / f"{datetime.now().strftime('%Y-%m-%d')}_post.png"
    img.convert("RGB").save(out, "PNG", dpi=(300, 300))
    print(f"Gespeichert: {out}")
    return out


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Dynamis Instagram Bildgenerator")
    p.add_argument("--title",    required=True,  help="Titel oder Redner-Name")
    p.add_argument("--subtitle", default="",     help="Untertitel oder Thema")
    p.add_argument("--category", default="SEMINAR",
                   choices=["SEMINAR", "VORTRAG", "INSPIRATIONSABEND", "RÜCKBLICK", "SPIRITUELL"])
    p.add_argument("--speaker",  default=None,
                   help="Redner-Key: thomas_mueller | raffaela | mychael_shane | custom")
    p.add_argument("--prompt",   default=None,   help="Eigener DALL-E Prompt (Englisch)")
    a = p.parse_args()
    generate_post(a.title, a.subtitle, a.category, a.speaker, a.prompt)
