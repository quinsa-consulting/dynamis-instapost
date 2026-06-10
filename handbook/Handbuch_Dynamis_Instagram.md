# Instagram-Assistent – Handbuch
## Dynamis-Zentrum Basel

**Version 1.0 | Erstellt von Quinsa Consulting**

---

> Dieses Handbuch erklärt Schritt für Schritt, wie du deinen Instagram-Assistenten bedienst.
> Bei Fragen wende dich an Sacha: [Handynummer eintragen]

---

## Inhaltsverzeichnis

0. [Was du VOR dem Treffen mit Sacha erledigen kannst](#kapitel-0)
1. [Deinen Mac verstehen](#kapitel-1)
2. [Installation (mit Sacha zusammen)](#kapitel-2)
3. [Einen Post erstellen – Schritt für Schritt](#kapitel-3)
4. [Voicely nutzen – sprechen statt tippen](#kapitel-4)
5. [Häufige Fragen und Probleme](#kapitel-5)

---

## Kapitel 0: Was du VOR dem Treffen mit Sacha erledigen kannst {#kapitel-0}

> Du kannst diese Schritte ganz alleine machen, auch ohne Sacha dabei.
> Nimm dir 20–30 Minuten Zeit und folge den Anweisungen genau.

### 0.1 Claude Code herunterladen und installieren

Claude Code ist das Programm, mit dem du deinen Assistenten bedienst.

**Schritte:**
1. Öffne deinen Browser (Safari oder Chrome)
2. Gehe zu: **https://claude.ai/download**
3. Klicke auf "Download für Mac"
4. Die Datei `Claude.dmg` wird heruntergeladen (du siehst sie unten im Browser)
5. Doppelklicke auf die heruntergeladene Datei
6. Ziehe das Claude-Symbol in den Programme-Ordner (Anwendungen)
7. Öffne Claude aus dem Programme-Ordner

> ✅ **Fertig!** Du siehst jetzt das Claude-Fenster.

---

### 0.2 Python installieren

Python ist eine Programmiersprache, die das Bildgenerator-Programm braucht.

**Schritte:**
1. Gehe zu: **https://www.python.org/downloads/**
2. Klicke auf den grossen gelben Knopf "Download Python 3.x.x"
3. Die Datei `python-3.x.x-macos.pkg` wird heruntergeladen
4. Doppelklicke auf die Datei
5. Klicke immer auf "Weiter" und dann auf "Installieren"
6. Gib dein Mac-Passwort ein wenn gefragt

> ✅ **Fertig!** Python ist installiert.

---

### 0.3 Den Projektordner herunterladen

**Schritte:**
1. Öffne deinen Browser und gehe zum Link, den dir Sacha geschickt hat
   (GitHub-Repository-Link)
2. Klicke auf den grünen Knopf "Code"
3. Klicke auf "Download ZIP"
4. Die ZIP-Datei wird heruntergeladen
5. Doppelklicke auf die ZIP-Datei – sie entpackt sich automatisch
6. Verschiebe den entpackten Ordner in deinen **Dokumente**-Ordner

> ✅ **Fertig!** Der Ordner heisst `dynamis-instapost` und liegt jetzt in Dokumenten.

---

### 0.4 Voicely registrieren (für Spracherkennung)

Voicely ist ein Schweizer Programm, mit dem du sprechen statt tippen kannst.
Das ist sehr praktisch, um dem Assistenten die Post-Informationen zu geben.

**Schritte:**
1. Gehe zu: **https://www.voicely.de/affiliate?via=sacha-bourquin-b98344**
2. Klicke auf "Kostenlos testen" oder "Registrieren"
3. Erstelle ein Konto mit deiner E-Mail-Adresse
4. Lade Voicely für Mac herunter und installiere es

> ✅ **Fertig!** Voicely ist eingerichtet.

---

## Kapitel 1: Deinen Mac verstehen {#kapitel-1}

### 1.1 Versteckte Ordner anzeigen

Manche wichtigen Ordner auf deinem Mac sind normalerweise unsichtbar.
So machst du sie sichtbar:

1. Öffne den **Finder** (das blaue Gesicht-Symbol im Dock)
2. Halte die Tasten **Cmd + Shift + .** gleichzeitig gedrückt
   (Cmd = die Taste mit dem ⌘ Symbol)
3. Du siehst jetzt grau dargestellte Ordner – das sind die versteckten

> Um sie wieder zu verstecken: dieselbe Tastenkombination nochmals drücken.

---

### 1.2 Das Terminal öffnen

Das Terminal ist ein Fenster, in das du Befehle eintippen kannst.

**Methode 1 (einfachste):**
1. Drücke **Cmd + Leertaste** gleichzeitig (Spotlight öffnet sich)
2. Tippe: `Terminal`
3. Drücke **Enter**

**Methode 2:**
1. Öffne Programme (Anwendungen)
2. Öffne den Ordner "Dienstprogramme"
3. Doppelklicke auf "Terminal"

> Das Terminal sieht aus wie ein schwarzes (oder weisses) Fenster mit Text.

---

### 1.3 Ordnerpfade verstehen

- `~` bedeutet: dein persönlicher Ordner (z.B. `/Users/michelle`)
- `~/Documents` bedeutet: dein Dokumente-Ordner
- `~/Downloads` bedeutet: dein Downloads-Ordner
- Schrägstrich `/` trennt Ordner-Ebenen

---

### 1.4 Rechtsklick auf dem Mac

- Mit Maus: halte **Ctrl** und klicke
- Mit Trackpad: klicke mit zwei Fingern gleichzeitig

---

## Kapitel 2: Installation (mit Sacha zusammen) {#kapitel-2}

> Diese Schritte machst du **zusammen mit Sacha** beim ersten Treffen.

### 2.1 Claude Code mit API-Key einrichten

1. Öffne Claude Code
2. Du wirst nach einem API-Key gefragt
3. Sacha gibt dir deinen persönlichen API-Key
4. Tippe ihn ein und drücke Enter

---

### 2.2 Den Projektordner in Claude Code öffnen

1. Öffne das Terminal (siehe Kapitel 1.2)
2. Tippe folgenden Befehl und drücke Enter:
   ```
   cd ~/Documents/dynamis-instapost
   ```
3. Tippe dann:
   ```
   claude
   ```
4. Claude Code öffnet sich für diesen Ordner

---

### 2.3 Python-Pakete installieren

1. Im Terminal (im Ordner `dynamis-instapost`), tippe:
   ```
   pip3 install -r requirements.txt
   ```
2. Drücke Enter und warte (ca. 1–2 Minuten)
3. Du siehst viel Text – das ist normal

> Falls die Meldung erscheint "pip3 not found": Sacha hilft dir beim Beheben.

---

### 2.4 Die .env-Datei einrichten (API-Keys)

Die `.env`-Datei enthält deine geheimen Zugangscodes. Sie ist unsichtbar, aber wichtig.

1. Zeige versteckte Dateien: **Cmd + Shift + .** im Finder
2. Im `dynamis-instapost`-Ordner siehst du jetzt `.env.example`
3. Mache eine Kopie davon und nenne sie `.env` (ohne "example")
4. Öffne `.env` mit dem Texteditor
5. Sacha trägt die API-Keys ein

> ⚠️ **Wichtig:** Gib diese Datei niemals weiter und lade sie nicht hoch!

---

### 2.5 Environment-Einstellungen (falls Python nicht gefunden wird)

Falls das Terminal sagt "python3 not found" oder "command not found":

1. Öffne das Terminal
2. Tippe folgenden Befehl:
   ```
   echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
   ```
3. Drücke Enter
4. Tippe:
   ```
   source ~/.zshrc
   ```
5. Drücke Enter
6. Versuche nochmals

> Sacha hilft dir dabei beim ersten Treffen.

---

### 2.6 Playwright installieren (für Instagram-Posting)

1. Im Terminal, tippe:
   ```
   python3 -m playwright install chromium
   ```
2. Drücke Enter und warte (ca. 2–3 Minuten)

---

## Kapitel 3: Einen Post erstellen – Schritt für Schritt {#kapitel-3}

### 3.1 Claude Code starten

**Jeden Tag so starten:**

1. Öffne das Terminal (Cmd + Leertaste → "Terminal" → Enter)
2. Tippe:
   ```
   cd ~/Documents/dynamis-instapost
   ```
3. Drücke Enter
4. Tippe:
   ```
   claude
   ```
5. Drücke Enter
6. Claude Code ist jetzt bereit

---

### 3.2 Den Post-Assistenten starten

1. Im Claude Code Fenster, tippe:
   ```
   /dynamis-insta-post
   ```
2. Drücke Enter
3. Der Assistent begrüsst dich und fragt nach der Post-Kategorie

---

### 3.3 Beispiel: Einen Vortrag ankündigen

**Du gibst ein:** `2`
*(für VORTRAG)*

**Assistent fragt:** Welcher Redner?
**Du gibst ein:** `A`
*(für Thomas Müller)*

**Assistent fragt:** Was ist das Thema?
**Du gibst ein** (oder sprichst per Voicely):
*"Wesenspsychologie und inneres Wachstum – wie wir unsere verborgenen Anteile integrieren"*

**Assistent fragt:** Datum und Uhrzeit?
**Du gibst ein:** *"Freitag, 15. August 2026 um 19:00 Uhr"*

**Assistent fragt:** Hast du ein Bild?
**Du gibst ein:** `A` *(wenn du einen Flyer hast)* oder `B` *(für KI-Bild)*

→ Der Assistent erstellt die Caption und zeigt sie dir.

**Du prüfst den Text** und sagst entweder:
- "Passt so" – und bekommst alles zum Kopieren
- "Ändere [was auch immer]" – der Assistent passt es an

---

### 3.4 Den fertigen Post an Sacha schicken

1. Kopiere die Caption (markieren → Cmd + C)
2. Schicke sie per WhatsApp oder E-Mail an Sacha
3. Schicke auch das Bild (liegt im Ordner `output/`)
4. Schreib dazu welche Musik du möchtest (Tipp aus dem Assistenten)

---

## Kapitel 4: Voicely nutzen – sprechen statt tippen {#kapitel-4}

> Voicely wandelt deine Sprache in Text um. So sparst du noch mehr Zeit!

### 4.1 Voicely einrichten

1. Öffne Voicely
2. Link für Registrierung: **https://www.voicely.de/affiliate?via=sacha-bourquin-b98344**
3. Wähle "Schweizerdeutsch" oder "Deutsch" als Sprache
4. Stelle sicher, dass dein Mikrofon erlaubt ist

### 4.2 Voicely im Alltag nutzen

1. Starte Voicely (kleines Symbol oben in der Menüleiste)
2. Klicke ins Claude Code Textfeld
3. Aktiviere Voicely mit der Tastenkombination (z.B. Fn + F5)
4. Sprich deutlich: *"Thema: Meditation und innere Ruhe. Datum: Samstag 20. September 2026."*
5. Voicely schreibt mit
6. Prüfe den Text kurz, dann drücke Enter

---

## Kapitel 5: Häufige Fragen und Probleme {#kapitel-5}

### "Python wurde nicht gefunden"

**Lösung:**
```
/usr/local/bin/python3 scripts/generate_image.py ...
```
Oder sage Sacha Bescheid, er richtet den PATH ein.

---

### "API-Key ungültig" oder "Authentication error"

**Lösung:**
1. Öffne die Datei `.env` (versteckte Dateien einblenden: Cmd+Shift+.)
2. Prüfe, ob der API-Key vollständig ist (beginnt mit `sk-ant-...`)
3. Kopiere den Key aus der E-Mail von Sacha nochmals

---

### "Das Bild wird nicht erstellt" / OpenAI Fehler

**Mögliche Ursachen:**
- OpenAI API-Guthaben aufgebraucht → Sacha aufladen lassen
- Internetverbindung prüfen

---

### "command not found: claude"

**Lösung:**
1. Schliesse das Terminal-Fenster
2. Öffne ein neues Terminal
3. Versuche nochmals

---

### Claude Code friert ein oder reagiert nicht

**Lösung:**
- Drücke **Ctrl + C** (bricht den aktuellen Vorgang ab)
- Tippe dann `/dynamis-insta-post` nochmals

---

### Ich brauche Hilfe

Kontaktiere Sacha:
- **WhatsApp:** [Nummer eintragen]
- **E-Mail:** sacha@quinsa.ch

---

*Dieses Handbuch wurde erstellt von Quinsa Consulting*
*quinsa.ch | sacha@quinsa.ch*
