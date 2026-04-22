# SpeedReader (RSVP)

A simple desktop application for RSVP reading built with Python and Tkinter.

## What is RSVP?

**RSVP** stands for **Rapid Serial Visual Presentation**. 

Instead of moving your eyes across lines of text, this tool displays words one by one in the center of the screen. This method reduces the need for eye movement, which can help some people read through text faster or with more focus.

## Features

- **Adjustable Speed:** Set your preferred Words Per Minute (WPM).
- **Navigation:** Buttons and shortcuts to pause or skip through the text.
- **Minimalist UI:** A basic text input and a display label for reading.

## How to Use

1. Paste your text into the text box.
2. Enter your desired speed in the "Wörter pro Minute" field.
3. Click **Start** or press `Enter`.

### Controls during reading:
| Key | Action |
| :--- | :--- |
| `Space` | **Pause / Play** |
| `Left Arrow` | **Back 5 words** |
| `Right Arrow` | **Forward 5 words** |
| `Escape` | **Quit** (return to menu) |

## Development

### Running from source:
1. Ensure you have Python installed.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Run the script:
   ```bash
   python SpeedReader.py
   ```

### Building the App (macOS):
The app is packaged using PyInstaller:
```bash
pip install pyinstaller
pyinstaller --windowed --name "Speedreader" --icon "icon.icns" SpeedReader.py
```

## Files

- `SpeedReader.py`: The main Python script.
- `Speedreader.spec`: Build configuration for PyInstaller.
- `icon.icns`: Application icon for macOS.
- `README.md`: Project documentation.
- `.gitignore`: Git exclusion rules.

---

**Disclaimer:** This project, including parts of its source code and this documentation, was generated with the assistance of AI.
