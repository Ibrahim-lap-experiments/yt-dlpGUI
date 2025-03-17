## yt-dlpGUI
A simple cross-platform GUI wrapper for yt-dlp to download YouTube videos and audio tracks.


## Features
  * Download videos as MP4 or audio as MP3

  * Custom output folder selection

  * Real-time progress logging

  * Supports Windows, macOS, and Linux

## Requirements
  * Python 3.7 or newer
  * FFmpeg (for audio conversion)
  * yt-dlp (will be downloaded automatically)

## Installation
1. Clone repository
  ```
  git clone https://github.com/Ibrahim-lap-experiments/yt-dlpGUI.git
  cd yt-dlp-gui
  ```
2. Install FFmpeg<br />
   Windows:<br />
        A) Download from [FFmpeg](https://www.ffmpeg.org/)<br />
        b) Add the bin folder to your system PATH<br />
    
   Linux (Debian/Ubuntu):
    ```
    sudo apt install ffmpeg
    ```
## Usage<br />
* run the application<br />
    for Windows: <br />
        after installing the Requirements, double tap the win_run.bat file.<br />

    for Linux:<br />
    
      
        
        python run_gui.py
  
* Enter a YouTube URL

* Select format (Video MP4 or Audio MP3)

* Choose output folder (default: current directory)

* Click "Start Download"

## Credits
* Built using [yt-dlp](https://github.com/yt-dlp/yt-dlp)

* Audio conversion powered by [FFmpeg](https://www.ffmpeg.org/)
