# Dynamis-Instapost

Instagram-Assistent für Dynamis-Zentrum Basel (@dynamiszentrum).

## Für Michelle

Lies das **Handbuch** unter `handbook/Handbuch_Dynamis_Instagram.md`.

Kurzversion:
1. Terminal öffnen (Cmd + Leertaste → "Terminal")
2. `cd ~/Documents/dynamis-instapost` → Enter
3. `claude` → Enter
4. `/dynamis-insta-post` → Enter

## Für Entwickler (Sacha)

### Struktur
```
.claude/skills/dynamis-insta-post/SKILL.md   ← Claude Code Skill
scripts/generate_image.py                     ← Bildgenerator
assets/speaker_templates/*.json               ← Redner-Konfigurationen
assets/logo/                                  ← Dynamis Logo hier ablegen
assets/fonts/                                 ← werden automatisch heruntergeladen
output/                                       ← generierte Bilder
```

### Setup
```bash
cp .env.example .env          # API-Keys eintragen
pip3 install -r requirements.txt
python3 -m playwright install chromium
```

### Logo hinzufügen
Lege das Dynamis-Zentrum Logo (PNG mit transparentem Hintergrund) in `assets/logo/` ab.

### Neuen Redner hinzufügen
Erstelle eine neue JSON-Datei in `assets/speaker_templates/`:
```json
{
  "name": "Vorname Nachname",
  "sprache": "de",
  "stil_erweiterung": "Schlüsselwörter für Stil",
  "standard_hashtags": ["#Hashtag1", "#Hashtag2"],
  "hashtags_ohne": ["Wort1", "Wort2"],
  "bild_hintergrund_stil": "Englischer DALL-E Prompt für Hintergrund",
  "layout_farbe_akzent": [R, G, B],
  "layout_farbe_text": [R, G, B],
  "gradient_c1": [R, G, B],
  "gradient_c2": [R, G, B],
  "gradient_alpha": 170
}
```
Dateiname = Key, den Michelle im Skill eintippt (z.B. `neuer_redner.json`).