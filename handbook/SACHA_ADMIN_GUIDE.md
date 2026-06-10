# Admin-Guide – Für Sacha
## Dynamis-Instapost | Technische Verwaltung

---

> Dieses Dokument ist nur für Sacha. Es erklärt alle technischen Einrichtungsschritte
> und wie häufige Probleme gelöst werden.

---

## 1. Checkliste für den Installations-Besuch bei Michelle

Vor dem Besuch sicherstellen:
- [ ] Anthropic API Key bereit (von console.anthropic.com)
- [ ] OpenAI API Key bereit (von platform.openai.com) – Michelle braucht ihren eigenen Account (siehe Abschnitt 3)
- [ ] GitHub-Repo bereits als privat erstellt und Link an Michelle geschickt
- [ ] Dynamis-Logo vorhanden (PNG mit transparentem Hintergrund, von Michelle besorgen)

Beim Besuch:
- [ ] Prüfen ob Michelle Kapitel 0 erledigt hat (Claude Code, Python, Ordner, Voicely)
- [ ] Ordnername korrekt: `~/Documents/dynamis-instapost` (ohne `-main` am Ende)
- [ ] In Ordner navigieren: `cd ~/Documents/dynamis-instapost`
- [ ] `.env`-Datei anlegen (siehe Abschnitt 2)
- [ ] Python-Pakete installieren: `pip3 install -r requirements.txt`
- [ ] Playwright installieren: `python3 -m playwright install chromium`
- [ ] `dynamis`-Alias in `.zshrc` einrichten (siehe Abschnitt 4)
- [ ] Voicely-Shortcut auf Ctrl+Cmd einrichten (in Voicely Einstellungen)
- [ ] Instagram-Login: Skript einmal starten, Michelle loggt sich selbst ein
- [ ] Logo in `assets/logo/` ablegen
- [ ] Test-Post gemeinsam durchführen (Kategorie 2, Thomas Müller)
- [ ] Handbuch als PDF drucken oder per E-Mail schicken

---

## 2. .env-Datei anlegen

```bash
cd ~/Documents/dynamis-instapost
cp .env.example .env
```

Dann `.env` im Texteditor öffnen und die Keys eintragen:

```bash
open -e .env
```

Eintragen:
```
ANTHROPIC_API_KEY=sk-ant-...   # aus console.anthropic.com
OPENAI_API_KEY=sk-...          # aus Michelles OpenAI-Account
```

> ⚠️ Michelles Keys sind ihre eigenen – nicht Quinsa-Keys verwenden.

---

## 3. OpenAI Account für Michelle einrichten

Michelle braucht einen eigenen OpenAI-Account für die Bildgenerierung (DALL-E).
Sacha übernimmt die Kosten NICHT.

**Einmalig beim Besuch:**
1. Gehe zu: https://platform.openai.com/signup
2. Account mit Michelles E-Mail erstellen
3. Zahlungsmittel hinterlegen (Kreditkarte oder Prepaid)
4. Ca. 10 USD Guthaben aufladen (reicht für viele Bilder)
5. API-Key erstellen: https://platform.openai.com/api-keys → "Create new secret key"
6. Key in die `.env`-Datei eintragen

**Kosten-Info für Michelle:**
- Ca. 0.04 USD pro generiertem KI-Bild (bei `gpt-image-1`, medium quality)
- 10 USD Guthaben reicht für etwa 250 Bilder
- Guthaben läuft nicht ab, nur bei Nutzung verbraucht

**Wenn Guthaben aufgebraucht ist:**
Michelle geht selbst auf https://platform.openai.com/billing und lädt auf.
Im Handbuch Kapitel 5 ist das erklärt.

---

## 4. "dynamis"-Alias in .zshrc einrichten

```bash
echo 'function dynamis() { cd ~/Documents/dynamis-instapost && claude; }' >> ~/.zshrc
source ~/.zshrc
```

Testen: neues Terminal-Fenster öffnen, `dynamis` eintippen.
Claude Code sollte direkt starten.

> Falls Claude Code nicht im PATH ist: `which claude` prüfen.
> Wenn leer: `export PATH="$PATH:/usr/local/bin"` in `.zshrc` hinzufügen.

---

## 5. Instagram-Session einrichten

Das Skript speichert die Login-Session in `instagram_session/`.
Michelle muss sich nur **einmal** einloggen.

**Erstmalig:**
```bash
cd ~/Documents/dynamis-instapost
python3 scripts/post_to_instagram.py --image assets/logo/*.png --caption "Test"
```
→ Browser öffnet sich → Michelle loggt sich selbst ein → Enter drücken → Session gespeichert.

**Wenn Session abläuft** (nach Wochen bis Monaten):
Das Login-Fenster erscheint automatisch beim nächsten Posting-Versuch.
Michelle loggt sich erneut ein. Kein Handlungsbedarf von Sacha.

> Sacha hat kein Instagram-Passwort von Michelle und braucht es nicht.

---

## 6. Häufige technische Probleme

### "python3 not found" oder "command not found: python3"

```bash
# Python-Pfad prüfen:
which python3

# Falls leer, in .zshrc ergänzen:
echo 'export PATH="/Library/Frameworks/Python.framework/Versions/3.x/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
Versionsnummer (3.x) entsprechend anpassen.

---

### "pip3 not found"

```bash
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
```

---

### "anthropic: command not found" oder "module not found"

```bash
cd ~/Documents/dynamis-instapost
pip3 install -r requirements.txt
```

---

### Playwright-Browser öffnet sich nicht

```bash
python3 -m playwright install chromium
# Falls Fehler: auch die Abhängigkeiten installieren:
python3 -m playwright install-deps
```

---

### "claude: command not found" im Terminal

Claude Code ist nicht im PATH. Prüfen:
```bash
ls /usr/local/bin/claude
# oder:
ls ~/Library/Application\ Support/Claude/
```

Claude Code neu installieren wenn nicht gefunden.

---

### OpenAI Error 429 (Rate Limit) oder Insufficient Credits

Michelle muss Guthaben aufladen: https://platform.openai.com/billing
Oder: Sacha prüft den Account-Status online.

---

### Instagram "suspicious login" Meldung

Instagram hat die Session aus Sicherheitsgründen beendet.
Michelle bekommt eine E-Mail oder SMS von Instagram zur Bestätigung.
Nach Bestätigung: Session-Ordner löschen und neu einloggen:

```bash
rm -rf ~/Documents/dynamis-instapost/instagram_session/
python3 scripts/post_to_instagram.py --image [bild] --caption "Test"
```

---

## 7. Neuen Redner hinzufügen

1. Neue JSON-Datei in `assets/speaker_templates/` erstellen:
   ```bash
   cp assets/speaker_templates/_default.json assets/speaker_templates/neuer_name.json
   ```
2. Datei bearbeiten (Name, Stil, Hashtags, Farben)
3. In `SKILL.md` unter "Schritt 2 → Kategorie 2 → Redner-Auswahl" einen neuen Punkt hinzufügen

---

## 8. Updates einspielen

Wenn du Änderungen am Skill oder Skript machst:
```bash
cd ~/Documents/dynamis-instapost
git pull
```

Falls Michelle keine Git-Kenntnisse hat: Dateien manuell ersetzen oder persönlich vorbeikommen.

---

## 9. Skill-Pfad in SKILL.md aktualisieren

Das Bash-Kommando im Skill enthält `/Users/[USERNAME]/` als Platzhalter.
Beim Besuch ersetzen:

```bash
# Michelles Benutzernamen herausfinden:
whoami
# z.B. "michelle" → Pfad wird: /Users/michelle/Documents/dynamis-instapost
```

In `.claude/skills/dynamis-insta-post/SKILL.md` alle `[USERNAME]` durch Michelles echten Benutzernamen ersetzen.

---

*Quinsa Consulting | Internes Dokument*
