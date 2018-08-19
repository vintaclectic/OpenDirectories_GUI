import os
import webbrowser
from Tkinter import *

root = Tk() 
root.wm_title("OpenURL") 
root.resizable(100,100)
entry_text=StringVar() 
drop_text1=StringVar()
label = Label(root, text='File name')
entry = Entry(root, width=50, textvariable=entry_text)
drop_text1.set("Video")
drop1 = OptionMenu(root,drop_text1,'Video','Music','Ebook','Software','Images','Compressed','Torrent')

def open_url():
    global drop_text1
    title=entry_text.get()
    options_dictionary = {
    'Video':'(.mkv|.mp4|.avi|.mov|.mpg|.wmv) ',
    'Music':'(.ogg|.mp3|.flac|.wma|.m4a|.ac3|.wav) ',
    'Ebook':'(.MOBI|.CBZ|.CBR|.CBC|.CHM|.EPUB|.FB2|.LIT|.LRF|.ODT|.PDF|.PRC|.PDB|.PML|.RB|.RTF|.TCR) ',
    'Software':'(.apk|.exe|.iso|.rar|.tar|.zip) ',
    'Images':'(.jpg|.gif|.png|.tif|.tiff|.psd) ',
    'Compressed':'(.7z|.bz2|.gz|.iso|.rar|.zip.tar|.sit) ',
    'Torrent':'.torrent '
    }
    url = 'https://www.google.com/search?q='+options_dictionary[drop_text1.get()]+title+' intitle:"index of" -inurl:(listen77|mp3raid|mp3toss|mp3drug|index_of|wallywashis)'
    if drop_text1.get()!='Torrent': url+=' -inurl:(jsp|pl|php|html|aspx|htm|cf|shtml)'
    webbrowser.open(url)

button_1=Button(root, text='GO', command=open_url, width=4) 
label.grid(row=0) 
entry.grid(row=0, column=1,columnspan=3) 
button_1.grid(row=0, column=5)
drop1.grid(row=0, column=4)

root.mainloop()
