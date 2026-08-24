# NIVO MP3 [SP/YT]

Open-source command-line audio extractor and converter for Spotify and YouTube links.

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

## 📌 Overview

Nivo MP3 is a lightweight Python terminal utility designed to fetch and convert audio tracks from YouTube and Spotify into standard MP3 format.

The project is fully open-source and can either be executed directly via Python or compiled into a standalone Windows executable.

## ✨ Features

- **YouTube Support**: Direct audio extraction from YouTube video links.
- **Spotify Support**: Resolves Spotify track metadata via oEmbed and fetches matching audio.
- **No External FFmpeg Setup**: Uses `imageio-ffmpeg` to automatically manage the FFmpeg binary.
- **Bitrate Presets**: Configurable quality presets (128, 192, 256, 320 kbps) or custom values.
- **Automatic Output**: Saves converted `.mp3` files directly into a local `Nivo_Downloads/` folder.
- **Interactive CLI**: Terminal UI featuring animated status indicators and color-coded logging.

## 🚀 Installation & Running from Source

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)

### 1. Download the Project

**Option A: Download as ZIP (Easiest)**
1. Go to the [GitHub repository](https://github.com/your-username/nivo-mp3)
2. Click the **"Code"** button → **"Download ZIP"**
3. Extract the ZIP file to a folder of your choice

**Option B: Clone with Git**
```bash
git clone https://github.com/your-username/nivo-mp3.git
cd nivo-mp3
```

### 2. Install Dependencies

Open a terminal/command prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install yt-dlp imageio-ffmpeg
```

### 3. Run the Script

```bash
python main.py
```

## 🏗️ Building Standalone Executable (.exe)

To bundle the application into a single standalone `.exe` without requiring Python on target systems:

```bash
pip install pyinstaller
pyinstaller --onefile --name "Nivo-MP3" main.py
```

The compiled binary will be placed inside the `dist/` directory.

## 📖 Usage

1. Start the script via `python main.py` (or launch the compiled `.exe`).
2. Paste a valid Spotify or YouTube track URL.
3. Select your target audio bitrate (1–5).
4. Completed files will appear automatically inside `Nivo_Downloads/`.

## 💻 System Requirements

- **OS**: Windows 10/11, Linux, or macOS (Python script is cross-platform)
- **Internet**: Active connection required for metadata resolution and audio stream fetching

## ⚠️ System Notices (Compiled Binary Only)

If running as a PyInstaller-compiled binary without a commercial code-signing certificate, Windows SmartScreen may trigger a warning:

> *"Windows protected your PC"*

To proceed, click **More info** → **Run anyway**.

## 🔒 Security

For security guidelines, please refer to [SECURITY.md](SECURITY.md).

## 📜 Disclaimer

This utility is distributed for educational and personal use only. Users are responsible for complying with intellectual property rights, local laws, and the terms of service of upstream platforms (YouTube, Spotify). The author does not endorse or encourage copyright infringement.

## 👨‍💻 Author

Made by **nivoro** (Discord: jahudipic)
