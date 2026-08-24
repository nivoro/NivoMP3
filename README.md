# NIVO MP3 [SP/YT]

```text
  ███╗   ██╗  ██╗  ██╗   ██╗  ██████╗    ███╗   ███╗  ██████╗  ██████╗ 
  ████╗  ██║  ██║  ██║   ██║ ██╔═══██╗   ████╗ ████║  ██╔═══██╗ ╚════██╗
  ██╔██╗ ██║  ██║  ██║   ██║ ██║   ██║   ██╔████╔██║  ██████╔╝  █████╔╝
  ██║╚██╗██║  ██║  ╚██╗ ██╔╝ ██║   ██║   ██║╚██╔╝██║  ██╔═══╝   ╚═══██╗
  ██║ ╚████║  ██║   ╚████╔╝  ╚██████╔╝   ██║ ╚═╝ ██║  ██║      ██████╔╝
  ╚═╝  ╚═══╝  ╚═╝    ╚═══╝    ╚═════╝    ╚═╝     ╚═╝  ╚═╝      ╚═════╝ 
```

```text
  >> nivo mp3 [sp/yt] <<
```

## What it does

Downloads audio from YouTube or Spotify and converts it to MP3.  
Paste a link, pick quality, done.

## Features

- YouTube & Spotify support
- No manual FFmpeg install
- Bitrate presets (128-320 kbps)
- Saves to `Nivo_Downloads/`
- Colorful CLI with spinner animation

## Installation

**You need Python 3.8 or higher.**  
Download it here: [python.org/downloads](https://www.python.org/downloads/)

### 1. Get the files

**Download as ZIP:**  
Click "Code" → "Download ZIP" → extract.

**Or clone:**
```bash
git clone https://github.com/your-username/nivo-mp3.git
cd nivo-mp3
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run it

```bash
python main.py
```

## Build EXE (optional, Windows only)

If you want a standalone .exe file:

```bash
pip install pyinstaller
pyinstaller --onefile --name "Nivo-MP3" main.py
```

The EXE will be in `dist/`.

## How to use

1. Run `python main.py`
2. Paste a Spotify or YouTube link
3. Choose bitrate (1-5)
4. MP3 appears in `Nivo_Downloads/`

## Disclaimer

For personal and educational use only.  
Respect copyright and platform terms.

## Author

nivoro (dc: jahudipic)
