from pytube import YouTube
import tkinter as tk
import os

def Download():
    #we get the video link provided in the window
    link = title_entry.get()
    #we transform the string from link into an youtube link so that it can be passed further
    yt = YouTube(link)

    #we choose ".get_highest_resolution()" so the highest resolution available for the choosen video is downloaded
    video = yt.streams.get_highest_resolution()
    #we provide the "folder" inside the brackets so that is the path for the download
    video.download(folder)

    #destroy the window after the download of finished
    window.destroy()

#defining the path where the videos will be downloaded
folder = os.path.join(os.path.join(os.path.expanduser("~")),'desktop/YtDownload')

#creates the root of the window
window = tk.Tk()

#defines the tittle of the window
window.title("Youtube Downloader")

#defines the position on the grid of the label
label_entry = tk.Label(window,text="Link: ")
label_entry.grid(row=0,column=0)

#defines the local where we will paste the link of the desired video
title_entry = tk.Entry(window)
title_entry.grid(row=0,column=1)

#defines the button and it's position on the window
button = tk.Button(window,text="Download",command=Download)
button.grid(row=0,column=2)

#defines some customizations about the colors of the window
button.configure(bg="#445566", fg="white")
label_entry.configure(bg="#445566", fg="white")
window.configure(bg="#445566")

window.mainloop()