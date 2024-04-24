from pytube import YouTube
import tkinter as tk
import os

def Download():
    link = title_entry.get()
    yt = YouTube(link)

    video = yt.streams.get_highest_resolution()
    video.download(folder)

    window.destroy()


folder = os.path.join(os.path.join(os.path.expanduser("~")),'desktop/YtDownload')



window = tk.Tk()
window.title("Youtube Downloader")
label_entry = tk.Label(window,text="Link: ")
label_entry.grid(row=0,column=0)
title_entry = tk.Entry(window)
title_entry.grid(row=0,column=1)
button = tk.Button(window,text="Download",command=Download)
button.grid(row=0,column=2)
button.configure(bg="#445566", fg="white")
label_entry.configure(bg="#445566", fg="white")
window.configure(bg="#445566")
window.mainloop()