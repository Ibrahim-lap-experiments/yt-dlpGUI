import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
import subprocess
import threading
import os

class YTDLPGUI:
    def __init__(self, root):
        self.root = root
        root.title("yt-dlp GUI")
        root.geometry("600x400")

        # URL Input
        ttk.Label(root, text="Video URL:").pack(pady=5)
        self.url_entry = ttk.Entry(root, width=60)
        self.url_entry.pack(pady=5)

        # Format Selection
        ttk.Label(root, text="Download Format:").pack(pady=5)
        self.format_var = tk.StringVar(value="video")
        ttk.Radiobutton(root, text="Video (mp4)", variable=self.format_var, value="video").pack()
        ttk.Radiobutton(root, text="Audio (mp3)", variable=self.format_var, value="audio").pack()

        # Output Path
        ttk.Label(root, text="Output Folder:").pack(pady=5)
        
        
        self.output_path = tk.StringVar(value=os.getcwd())
        ttk.Entry(root, textvariable=self.output_path, width=60).pack(pady=5)
        ttk.Button(root, text="Browse", command=self.select_output).pack()

        # Download Button
        ttk.Button(root, text="Start Download", command=self.start_download).pack(pady=10)

        # Log Console
        self.log = scrolledtext.ScrolledText(root, height=10)
        self.log.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def select_output(self):
        path = filedialog.askdirectory()
        if path:
            self.output_path.set(path)

    def start_download(self):
        url = self.url_entry.get()
        output_path = self.output_path.get()
        format_type = self.format_var.get()

        if not url:
            self.update_log("Error: Please enter a URL")
            return

        thread = threading.Thread(target=self.run_ytdlp, args=(url, output_path, format_type))
        thread.start()

    def run_ytdlp(self, url, output_path, format_type):
        cmd = [
            "yt-dlp",
            "-o", f"{output_path}/%(title)s.%(ext)s",
            "--progress", "--newline"
        ]

        if format_type == "audio":
            cmd += ["-x", "--audio-format", "mp3"]
        else:
                cmd += [
                    "--format", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                    "--merge-output-format", "mp4"
                ]

        self.update_log(f"Starting download...\nCommand: {' '.join(cmd)}\n")

        try:
            process = subprocess.Popen(
                cmd + [url],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )

            for line in process.stdout:
                self.update_log(line)

            process.wait()
            self.update_log("\nDownload completed!" if process.returncode == 0 else "\nDownload failed!")

        except Exception as e:
            self.update_log(f"Error: {str(e)}")

    def update_log(self, message):
        self.log.insert(tk.END, message)
        self.log.see(tk.END)
        self.log.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = YTDLPGUI(root)
    root.mainloop()