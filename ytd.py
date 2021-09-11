# Import 
from pytube import YouTube
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os.path

# Convert
def convert():

    # File store path setting
    dir_path = filedialog.askdirectory(parent=window,initialdir="/",title='Please select a directory for store')
    parsing = lnk.get()
    print(parsing)

    yt = YouTube(parsing)
    print("start!")

    # File convert start
    try:
        if(Radiovar.get() == 1):
            video = yt.streams.filter(only_audio=True).first()
            downloaded_file = video.download(dir_path)
            base, ext = os.path.splitext(downloaded_file)
            new_file = base + '.mp3'
            os.rename(downloaded_file, new_file)
        else:
            video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            downloaded_file = video.download(dir_path)
        messagebox.showinfo("success","finish converted!")
    except:
        messagebox.showinfo("fail","try again...")

# GUI 
window = Tk()
window.title("Youtube Convert")
window.geometry("500x300")
window.resizable(width=FALSE, height=False)

lbl = Label(window, text="YouTube Converter!")
lbl.pack()

lnk = Entry(window)
lnk.pack(fill="x")

st = StringVar() 
Radiovar = IntVar() 
Radio_button1 = Radiobutton(text="mp3",variable=Radiovar,value=1) 
Radio_button2 = Radiobutton(text="mp4",variable=Radiovar,value=2)
Radio_button1.pack()
Radio_button2.pack()

place = Label(window, text="\n")
place.pack()

btn = Button(window, text="convert",command=convert)
btn.pack()

window.mainloop()
