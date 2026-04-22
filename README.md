# ⚡ SpeedReader (RSVP)

Ein minimalistisches, hochperformantes Tool für effizientes Lesen direkt auf deinem Desktop.

## 📖 Was ist RSVP?

**RSVP** steht für **Rapid Serial Visual Presentation**. 

Anstatt deine Augen von links nach rechts über eine Zeile zu bewegen (was Zeit kostet), präsentiert RSVP dir jedes Wort einzeln an derselben Stelle. Das eliminiert die Zeit, die deine Augen für die Fokussierung und das Springen zwischen Wörtern benötigen, und verhindert das "Subvokalisieren" (das Mitsprechen im Kopf). Dadurch kannst du deine Lesegeschwindigkeit massiv steigern – oft auf über 500 oder 600 Wörter pro Minute!

---

## 🚀 Features

- **Einstellbare Geschwindigkeit:** Wähle deine WPM (Words Per Minute) selbst.
- **Volle Kontrolle:** Pause, Play und Navigation per Tastatur.
- **Präzises Springen:** Springe 5 Wörter vor oder zurück, um nichts zu verpassen.
- **Ablenkungsfrei:** Ein sauberes, fokussiertes Interface.

---

## 🛠 Nutzung & Steuerung

### Starten der App
1. Kopiere deinen Text in das Textfeld.
2. Gib deine gewünschte Geschwindigkeit (WPM) ein.
3. Drücke **Start** (oder `Enter`).

### Während des Lesens (Tastenkürzel)
| Taste | Aktion |
| :--- | :--- |
| `Leertaste` | **Pause / Play** |
| `Pfeil links` | **5 Wörter zurück** |
| `Pfeil rechts` | **5 Wörter vor** |
| `Escape` | **Beenden** (zurück zum Menü) |

---

## 🏗 Installation (Entwickler)

Falls du die App aus dem Quellcode starten möchtest:

1. **Repository klonen**
2. **Virtuelle Umgebung erstellen:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. **Starten:**
   ```bash
   python SpeedReader.py
   ```

### Als App builden (macOS)
Um die eigenständige `.app` zu erstellen, wurde PyInstaller verwendet:
```bash
pyinstaller --windowed --name "Speedreader" --icon "icon.icns" SpeedReader.py
```

---

## 🎨 Icon
Das Projekt nutzt ein individuelles `icon.icns`, um sich nahtlos in dein macOS-Dock einzufügen.

---

Viel Spaß beim schnellen Lesen! 🚀
