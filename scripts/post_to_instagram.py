#!/usr/bin/env python3
"""
post_to_instagram.py - Dynamis-Zentrum Basel Instagram Posting-Automation
Playwright öffnet Instagram, füllt Bild + Caption vor.
Michelle klickt selbst auf Teilen.
"""
import argparse
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

SESSION_DIR = Path(__file__).parent.parent / "instagram_session"


def post_to_instagram(image_path: str, caption: str):
    path = Path(image_path).resolve()
    if not path.exists():
        print(f"Fehler: Bild nicht gefunden: {path}")
        sys.exit(1)

    SESSION_DIR.mkdir(exist_ok=True)
    print("Öffne Instagram im Browser...")
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            str(SESSION_DIR),
            headless=False,
            channel="chromium",
        )
        page = context.new_page()

        page.goto("https://www.instagram.com/")
        page.wait_for_load_state("domcontentloaded", timeout=30000)
        page.wait_for_timeout(3000)

        # Login prüfen
        if "accounts/login" in page.url or "auth_platform" in page.url:
            print("\n" + "=" * 55)
            print("  Bitte bei Instagram einloggen.")
            print("  Gib deinen Benutzernamen und dein Passwort ein.")
            print("  Danach hier im Terminal Enter drücken.")
            print("=" * 55)
            input()
            page.wait_for_load_state("domcontentloaded", timeout=30000)
            page.wait_for_timeout(2000)

        # Schritt 1: "New post" Link anklicken
        print("Klicke auf 'Neuer Beitrag'...")
        page.get_by_role("link", name="New post").click()
        page.wait_for_timeout(1000)

        # Schritt 2: "Post" im Dropdown wählen
        print("Wähle 'Beitrag' aus dem Menü...")
        page.get_by_role("link", name="Post Post").click()
        page.wait_for_timeout(2000)

        # Schritt 3: Bild hochladen
        print("Lade Bild hoch...")
        select_btn = page.get_by_role("button", name="Select From Computer")
        select_btn.wait_for(timeout=10000)

        with page.expect_file_chooser(timeout=10000) as fc_info:
            select_btn.click()
        file_chooser = fc_info.value
        file_chooser.set_files(str(path))

        # Durch Crop und Filter navigieren (2x "Weiter")
        for step in range(2):
            print(f"Schritt {step + 1} von 2...")
            next_btn = page.get_by_role("button", name="Next")
            next_btn.wait_for(state="visible", timeout=15000)
            page.wait_for_timeout(500)
            next_btn.click()
            page.wait_for_timeout(2000)

        # Caption einfügen
        print("Füge Text ein...")
        caption_box = page.get_by_role("textbox", name="Write a caption...")
        caption_box.wait_for(timeout=10000)
        caption_box.click()
        caption_box.fill(caption)
        page.wait_for_timeout(500)

        print("\n" + "=" * 55)
        print("  Dein Post ist bereit!")
        print("  Überprüfe den Beitrag im Browser.")
        print("  Klicke auf 'Teilen' wenn alles passt.")
        print("  Das Fenster schliesst sich nach 5 Minuten.")
        print("=" * 55)

        time.sleep(300)

        print("Fertig! Browser wird geschlossen.")
        try:
            context.close()
        except Exception:
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image",        required=True, help="Pfad zum PNG-Bild")
    parser.add_argument("--caption",      default=None,  help="Caption als Text")
    parser.add_argument("--caption-file", default=None,  help="Pfad zur Caption-Textdatei")
    args = parser.parse_args()
    if args.caption_file:
        caption = Path(args.caption_file).read_text(encoding="utf-8")
    elif args.caption:
        caption = args.caption
    else:
        print("Fehler: --caption oder --caption-file angeben.")
        sys.exit(1)
    post_to_instagram(args.image, caption)
