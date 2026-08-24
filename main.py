import os
import sys
import time
import json
import re
import ssl
import threading
import urllib.request
import yt_dlp
import imageio_ffmpeg

# colors and styles you can change it however you want to *farts cutely🎀*
YLW = "\033[93m"
GLD = "\033[33m"
BRGT = "\033[1m"
DIM = "\033[2m"
RST = "\033[0m"
GRN = "\033[92m"
RD = "\033[91m"

# made by nivoro (dc: jahudipic)

def nivo_clear():
    os.system("cls" if os.name == "nt" else "clear")

def nivo_banner():
    banner_lines = [
        r"  ███╗   ██╗  ██╗  ██╗   ██╗  ██████╗    ███╗   ███╗  ██████╗  ██████╗ ",
        r"  ████╗  ██║  ██║  ██║   ██║ ██╔═══██╗   ████╗ ████║  ██╔═══██╗ ╚════██╗",
        r"  ██╔██╗ ██║  ██║  ██║   ██║ ██║   ██║   ██╔████╔██║  ██████╔╝  █████╔╝",
        r"  ██║╚██╗██║  ██║  ╚██╗ ██╔╝ ██║   ██║   ██║╚██╔╝██║  ██╔═══╝   ╚═══██╗",
        r"  ██║ ╚████║  ██║   ╚████╔╝  ╚██████╔╝   ██║ ╚═╝ ██║  ██║      ██████╔╝",
        r"  ╚═╝  ╚═══╝  ╚═╝    ╚═══╝    ╚═════╝    ╚═╝     ╚═╝  ╚═╝      ╚═════╝ ",
        r"                                                                        ",
        r"  >> nivo mp3 [sp/yt] <<                                                "
    ]
    nivo_clear()
    sys.stdout.write(GLD)
    for line in banner_lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.0008)
        sys.stdout.write("\n")
    sys.stdout.write(f"{RST}\n")

class juicyspinningshit:
    def __init__(self, message="Downloading"):
        self.message = message
        self.running = False
        self.thread = None
        self.frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

    def spin_like_a_bitch(self):
        idx = 0
        while self.running:
            sys.stdout.write(f"\r{YLW}{self.frames[idx]} {self.message}...{RST}")
            sys.stdout.flush()
            idx = (idx + 1) % len(self.frames)
            time.sleep(0.08)

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.spin_like_a_bitch, daemon=True)
        self.thread.start()

    def stop_slave(self, success=True, msg="Done!"):
        self.running = False
        if self.thread:
            self.thread.join(timeout=0.2)
        
        symbol = f"{GRN}✔" if success else f"{RD}✖"
        sys.stdout.write(f"\r{symbol} {msg}{RST}\n")
        sys.stdout.flush()

def nivo_target(url):
    if "spotify.com" in url.lower():
        clean_url = url.split("?")[0]
        clean_url = re.sub(r"/intl-[a-zA-Z]{2}/", "/", clean_url)
        api_url = f"https://open.spotify.com/oembed?url={clean_url}"
        
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        req = urllib.request.Request(api_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx) as response:
            data = json.loads(response.read().decode("utf-8"))
            query = f"{data.get('title', '')} {data.get('author_name', '')}".strip()
            return f"ytsearch1:{query}"
    return url

def nivo_download(url, bitrate, output_folder):
    target = nivo_target(url)
    ffmpeg_binary = imageio_ffmpeg.get_ffmpeg_exe()
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'ffmpeg_location': ffmpeg_binary,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': str(bitrate),
        }],
        'quiet': True,
        'no_warnings': True,
        'default_search': 'ytsearch',
        'nocheckcertificate': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([target])

def nivo_bitrate():
    print(f"{YLW}{BRGT}[SELECT AUDIO QUALITY (KBPS)]{RST}")
    print(f"{GLD}[1] 320 kbps (Best Quality)")
    print(f"{GLD}[2] 256 kbps")
    print(f"{GLD}[3] 192 kbps")
    print(f"{GLD}[4] 128 kbps (Low Size)")
    print(f"{GLD}[5] Custom kbps{RST}")
    
    choice = input(f"\n{YLW}{BRGT}Choose option (1-5) [Default 320]: {RST}").strip()
    
    presets = {"1": "320", "2": "256", "3": "192", "4": "128"}
    if choice in presets:
        return presets[choice]
    elif choice == "5":
        custom = input(f"{YLW}Enter custom kbps (e.g. 320): {RST}").strip()
        return custom if custom.isdigit() else "320"
    return "320"

def main():
    while True:
        nivo_banner()
        
        output_dir = os.path.join(os.getcwd(), "Nivo_Downloads")
        os.makedirs(output_dir, exist_ok=True)
        
        print(f"{DIM}Output destination: {output_dir}{RST}\n")
        
        url = input(f"{YLW}{BRGT}[+] Enter Spotify or YouTube Link: {RST}").strip()
        if not url:
            print(f"{RD}No URL provided. Exiting.{RST}")
            break
            
        print()
        bitrate = nivo_bitrate()
        print(f"\n{YLW}Selected Bitrate: {BRGT}{bitrate} kbps{RST}\n")
        
        spinner = juicyspinningshit(f"Processing audio at {bitrate} kbps")
        spinner.start()
        
        try:
            nivo_download(url, bitrate, output_dir)
            spinner.stop_slave(True, f"Download and conversion complete! ({bitrate} kbps MP3)")
        except Exception as e:
            spinner.stop_slave(False, f"Download failed: {e}")
            
        print(f"\n{DIM}----------------------------------------{RST}")
        again = input(f"{YLW}Download another song senpai? (y/n): {RST}").strip().lower()
        if again != 'y':
            print(f"\n{GLD}Thank you for using this fucking mp3 downloader!{RST}\n")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{YLW}Process cancelled by user.{RST}\n")
        sys.exit(0)

# yes king
