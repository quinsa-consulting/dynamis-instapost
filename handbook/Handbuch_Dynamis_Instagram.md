# Instagram-Assistent – Handbuch
## Dynamis-Zentrum Basel

**Version 1.1 | Erstellt von Quinsa Consulting**

---

> Dieses Handbuch erklärt Schritt für Schritt, wie du deinen Instagram-Assistenten bedienst.
> Bei technischen Problemen wende dich an Sacha.

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

> Du kannst diese Schritte ganz alleine machen.
> Nimm dir ca. 30 Minuten Zeit und folge den Anweisungen genau.

---

### 0.1 Claude Code herunterladen und installieren

Claude Code ist das Programm, mit dem du deinen Assistenten bedienst.

**Schritte:**
1. Öffne Safari oder Chrome
2. Gehe zu: **https://claude.ai/download**
3. Klicke auf den Download-Knopf für Mac

> 📸 *Hier Screenshot einfügen: Claude-Download-Seite mit Knopf für Mac*

4. Die Datei `Claude.dmg` erscheint unten im Browser (oder in deinen Downloads)
5. Doppelklicke auf `Claude.dmg`

> 📸 *Hier Screenshot einfügen: Das Installations-Fenster mit Claude-Symbol und Pfeil in den Anwendungen-Ordner*

6. Ziehe das Claude-Symbol in den **Anwendungen**-Ordner
7. Öffne **Anwendungen** im Finder und doppelklicke auf **Claude**
8. Falls eine Warnung erscheint ("von unbekanntem Entwickler"):
   - Klicke **nicht** auf Abbrechen
   - Gehe zu **Systemeinstellungen → Datenschutz & Sicherheit**
   - Klicke unten auf **"Trotzdem öffnen"**

> ✅ **Fertig!** Claude Code zeigt ein Chat-Fenster.

---

### 0.2 Python installieren

Python ist eine Programmiersprache, die das Bildgenerator-Programm braucht.

**Schritte:**
1. Gehe zu: **https://www.python.org/downloads/**
2. Klicke auf den grossen gelben Knopf **"Download Python 3.x.x"**

> 📸 *Hier Screenshot einfügen: Python-Webseite mit dem gelben Download-Knopf*

3. Die Datei `python-3.x.x-macos.pkg` erscheint in deinen Downloads
4. Doppelklicke auf die Datei
5. Klicke immer auf **"Fortfahren"** und dann **"Installieren"**
6. Gib dein Mac-Passwort ein wenn gefragt
7. Klicke am Ende auf **"Schliessen"**

> ✅ **Fertig!** Python ist installiert.

---

### 0.3 Den Assistenten-Ordner herunterladen

**Schritte:**
1. Öffne deinen Browser und gehe zum Link, den dir Sacha geschickt hat (GitHub-Link)
2. Klicke auf den grünen Knopf **"Code"**
3. Klicke auf **"Download ZIP"**

> 📸 *Hier Screenshot einfügen: GitHub-Seite mit grünem "Code"-Knopf und Download ZIP Option*

4. Die ZIP-Datei erscheint in deinen Downloads
5. Doppelklicke auf die ZIP-Datei – sie entpackt sich automatisch
6. Du siehst jetzt einen Ordner namens `dynamis-instapost-main`
7. Benenne ihn in **`dynamis-instapost`** um:
   - Rechtsklick auf den Ordner → **"Umbenennen"**
   - Tippe `dynamis-instapost` → Enter
8. Ziehe den Ordner in deinen **Dokumente**-Ordner

> ✅ **Fertig!** Der Ordner liegt jetzt unter: **Dokumente → dynamis-instapost**

---

### 0.4 Voicely registrieren (Spracherkennung – empfohlen)

Mit Voicely kannst du sprechen statt tippen. Das spart viel Zeit!

**Schritte:**
1. Gehe zu: **https://www.voicely.de/affiliate?via=sacha-bourquin-b98344**
2. Klicke auf **"Registrieren"** oder **"Kostenlos starten"**

> 📸 *Hier Screenshot einfügen: Voicely-Webseite mit Registrierungsknopf*

3. Erstelle ein Konto mit deiner E-Mail-Adresse
4. Lade Voicely für Mac herunter und installiere es (gleich wie Claude Code oben)
5. Öffne Voicely – ein kleines Symbol erscheint oben in der Menüleiste

> ✅ **Fertig!** Voicely ist bereit. Weitere Einrichtung in Kapitel 4.

---

## Kapitel 1: Deinen Mac verstehen {#kapitel-1}

### 1.1 Versteckte Dateien und Ordner anzeigen

Manche wichtigen Dateien auf deinem Mac sind normalerweise unsichtbar.
So machst du sie sichtbar:

1. Öffne den **Finder** (das blaue Gesicht-Symbol unten im Dock)
2. Halte diese Tasten gleichzeitig gedrückt: **Cmd ⌘ + Shift ⇧ + Punkt (.)**

> 📸 *Hier Screenshot einfügen: Finder mit sichtbaren versteckten Dateien (grau dargestellt)*

Um sie wieder zu verstecken: dieselbe Tastenkombination nochmals drücken.

---

### 1.2 Das Terminal öffnen

Das Terminal ist ein Fenster, in das du kurze Befehle eintippen kannst.

**Methode (einfachste):**
1. Drücke gleichzeitig: **Cmd ⌘ + Leertaste**
   → Ein Suchfeld erscheint (Spotlight)
2. Tippe: `Terminal`
3. Drücke **Enter**

> 📸 *Hier Screenshot einfügen: Spotlight mit "Terminal" eingegeben*

> Das Terminal-Fenster sieht aus wie ein schwarzes Textfenster mit einer Zeile wie:
> `michelles-mac:~ michelle$`
> Das ist normal. Hier kannst du Befehle eintippen.

---

### 1.3 Den Assistenten starten – Kurzbefehl "dynamis"

Sacha richtet beim Besuch einen Kurzbefehl ein. Danach reicht ein einziges Wort:

1. Öffne das Terminal (Cmd ⌘ + Leertaste → "Terminal" → Enter)
2. Tippe: `dynamis`
3. Drücke **Enter**

> ✅ Der Assistenten-Ordner wechselt automatisch und Claude Code startet. Fertig!

Du musst dir keine langen Befehle merken. **Nur: `dynamis` eintippen.**

---

### 1.4 Tastenkürzel-Übersicht

| Aktion | Tasten |
|--------|--------|
| Spotlight (Suche) öffnen | Cmd ⌘ + Leertaste |
| Versteckte Dateien zeigen/verstecken | Cmd ⌘ + Shift ⇧ + . |
| Kopieren | Cmd ⌘ + C |
| Einfügen | Cmd ⌘ + V |
| Voicely aktivieren/deaktivieren | Ctrl + Cmd ⌘ |
| Befehl im Terminal abbrechen | Ctrl + C |

---

## Kapitel 2: Installation (mit Sacha zusammen) {#kapitel-2}

> Diese Schritte erledigt **Sacha beim ersten Besuch**.
> Du musst nur dabei sein – und einmal dein Instagram-Passwort eingeben.

### Was Sacha beim Besuch einrichtet:

- [ ] Claude Code mit API-Key verbinden (Sacha trägt ihn direkt ein)
- [ ] Python-Pakete installieren
- [ ] Zugangsdaten-Datei anlegen (`.env`)
- [ ] Instagram einmalig einloggen (du tippst dein Passwort selbst)
- [ ] Den `dynamis`-Kurzbefehl einrichten
- [ ] Voicely-Tastenkürzel (Ctrl + Cmd ⌘) einrichten
- [ ] Test-Post gemeinsam erstellen

---

### 2.1 Instagram einmalig einloggen

Beim ersten Mal öffnet Sacha das Programm und ein Browser-Fenster erscheint:

> 📸 *Hier Screenshot einfügen: Instagram-Login-Seite im Browser*

**Was du tust:**
1. Du tippst deinen Instagram-Benutzernamen ein
2. Du tippst dein Passwort ein
3. Du klickst auf **"Anmelden"**
4. Danach drückst du im Terminal **Enter**

Nach diesem ersten Login merkt sich das Programm deinen Account automatisch.
Du musst dich **nicht mehr bei jedem Post einloggen**.

> ⚠️ Nur du gibst dein Passwort ein. Es wird nirgends gespeichert oder weitergegeben.

---

## Kapitel 3: Einen Post erstellen – Schritt für Schritt {#kapitel-3}

### 3.1 Den Assistenten starten

1. Öffne das Terminal (Cmd ⌘ + Leertaste → "Terminal" → Enter)
2. Tippe: `dynamis` → Enter

> 📸 *Hier Screenshot einfügen: Terminal mit "dynamis" eingegeben, Claude Code startet*

3. Warte bis Claude Code startet (ca. 5 Sekunden)
4. Tippe: `/dynamis-insta-post` → Enter

> 📸 *Hier Screenshot einfügen: Claude Code zeigt die Kategorien-Auswahl*

---

### 3.2 Kategorie wählen

Du siehst 5 Optionen:

```
1 – SEMINAR oder WORKSHOP
2 – VORTRAG (mit Gastredner)
3 – INSPIRATIONSABEND
4 – RÜCKBLICK (Fotos nach dem Event)
5 – SPIRITUELL (Zitat, Gedanke)
```

Tippe die gewünschte **Zahl** ein und drücke **Enter**.

---

### 3.3 Informationen eingeben

Der Assistent fragt dich der Reihe nach nach Titel, Datum, Ort, Highlights usw.

**Tipp:** Nutze Voicely – einfach **Ctrl + Cmd ⌘** drücken und sprechen (siehe Kapitel 4).

Beispiel was du sprechen kannst:
> *"Thomas Müller. Thema: Wesenspsychologie. Datum: Freitag 15. August 2026 um 19 Uhr. Kosten: 40 Franken."*

---

### 3.4 Bild-Option wählen

- **A** eingeben → Du lädst ein eigenes Bild direkt ins Chat-Fenster (Drag & Drop)
- **B** eingeben → Der Assistent erstellt ein KI-Bild (dauert ca. 30 Sekunden)

> 📸 *Hier Screenshot einfügen: Chat-Fenster mit der Bild-Frage und Option A/B*

---

### 3.5 Caption prüfen und freigeben

Der Assistent zeigt dir den fertigen Text mit Emojis und Hashtags.

> 📸 *Hier Screenshot einfügen: Generierte Caption im Chat-Fenster*

- Wenn alles passt: Tippe `ja` → Enter
- Wenn etwas geändert werden soll: Schreib es einfach, z.B.:
  `Ändere das Datum auf 20. August`

---

### 3.6 Post auf Instagram veröffentlichen

Nach der Freigabe:
1. Das Programm bereitet alles automatisch vor
2. Ein Browser-Fenster öffnet sich mit deinem Instagram

> 📸 *Hier Screenshot einfügen: Instagram im Browser mit vorausgefülltem Bild und Text*

3. Überprüfe den Post kurz (Bild, Text, alles korrekt?)
4. Wähle optional Musik: Suche in Instagram nach dem Suchbegriff, den dir der Assistent genannt hat
5. Klicke auf **"Teilen"**

> Das Browser-Fenster schliesst sich automatisch nach 5 Minuten.
> ✅ Dein Post ist jetzt auf Instagram!

---

## Kapitel 4: Voicely nutzen – sprechen statt tippen {#kapitel-4}

### 4.1 Registrierung

**Link:** https://www.voicely.de/affiliate?via=sacha-bourquin-b98344

---

### 4.2 Tastenkürzel

Das Tastenkürzel für Voicely ist: **Ctrl + Cmd ⌘**

Das richtet Sacha beim Besuch ein. Du kannst es in den Voicely-Einstellungen ändern.

---

### 4.3 Voicely verwenden

1. Klicke ins Texteingabefeld in Claude Code
2. Drücke **Ctrl + Cmd ⌘** – Voicely ist jetzt aktiv

> 📸 *Hier Screenshot einfügen: Voicely-Mikrofon-Symbol aktiv*

3. Sprich deutlich:
   *"Thomas Müller. Thema: Meditation. Datum: 15. August um 19 Uhr."*
4. Drücke wieder **Ctrl + Cmd ⌘** zum Beenden
5. Prüfe den Text kurz, dann **Enter** drücken

**Tipps:**
- Ruhige Umgebung hilft
- Deutlich und nicht zu schnell sprechen
- Zahlen ausschreiben: "fünfzehnter August" statt "15.8."

---

## Kapitel 5: Häufige Fragen und Probleme {#kapitel-5}

### "dynamis" funktioniert nicht

Das Terminal zeigt: `command not found: dynamis`

**Was tun:** Terminal schliessen (rotes X), neu öffnen, nochmals versuchen.
Falls es wieder passiert: Sacha anrufen.

---

### Claude Code reagiert nicht

**Was tun:** Drücke **Ctrl + C** (bricht ab). Tippe dann `/dynamis-insta-post` nochmals.

---

### Das KI-Bild wird nicht erstellt

Mögliche Ursache: OpenAI-Guthaben aufgebraucht.

**Was tun:**
1. Gehe zu: **https://platform.openai.com/**
2. Logge dich in deinen Account ein
3. Gehe zu **"Billing"** und lade Guthaben auf (z.B. 10 USD)

> Sacha zeigt dir beim ersten Besuch, wo du das findest.

---

### Instagram fragt nach Passwort

Das passiert alle paar Wochen – die Login-Session ist abgelaufen.

**Was tun:**
1. Das Passwort-Fenster öffnet sich automatisch
2. Gib deinen Benutzernamen und dein Passwort ein
3. Klicke auf "Anmelden"
4. Drücke im Terminal **Enter**
5. Alles läuft weiter wie gewohnt

---

### Mac startet neu oder Programm öffnet sich nicht

**Was tun:** Mac neu starten. Dann nochmals `dynamis` eintippen.

---

*Dieses Handbuch wurde erstellt von Quinsa Consulting | quinsa.ch*
