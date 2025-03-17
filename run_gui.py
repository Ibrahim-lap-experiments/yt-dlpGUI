import sys
import subprocess
import platform
import tkinter as tk
import os
from tkinter import messagebox

# Check Python version
if sys.version_info < (3, 7):
    print("Python 3.7 or newer is required!")
    sys.exit(1)

def check_dependencies():
    """Check for required dependencies and install if missing"""
    try:
        # Check/Install yt-dlp
        subprocess.run(
            ["yt-dlp", "--version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Installing yt-dlp...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])

    # Check FFmpeg
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        show_ffmpeg_help()
        

def show_ffmpeg_help():
    """Show FFmpeg installation instructions"""
    system = platform.system()
    msg = "FFmpeg is required for audio conversion!\nDowenloading audio will not work.\n\nInstall instructions:\n"
    
    if system == "Windows":
        msg += "1. Download from https://www.gyan.dev/ffmpeg/builds\n"
        msg += "2. Unzip and add the 'bin' folder to your system PATH"
        
    elif system == "Darwin":
        msg += "1. Install Homebrew (https://brew.sh)\n"
        msg += "2. Run: brew install ffmpeg"
        
    elif system == "Linux":
        msg += "Run: sudo apt install ffmpeg  # Debian/Ubuntu"
        
    else:
        msg += "See https://ffmpeg.org/download.html"
        
    

    messagebox.showerror("FFmpeg Required", msg)

def main():
    # Check system requirements
    check_dependencies()
    
    # Import and start GUI after successful checks
    from ty_dlp_gui import YTDLPGUI  # Import your actual GUI file name
    
    root = tk.Tk()
    app = YTDLPGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()