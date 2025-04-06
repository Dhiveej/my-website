import tkinter as tk
from tkinter import messagebox
import yt_dlp

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a YouTube URL")
        return

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'D:/Project/%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            messagebox.showinfo("Success", "Download completed successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create and place the widgets
tk.Label(root, text="YouTube URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)
download_button = tk.Button(root, text="Download", command=download_video)
download_button.grid(row=1, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
