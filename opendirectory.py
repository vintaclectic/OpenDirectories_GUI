import os
import webbrowser
from Tkinter import *

root = Tk() 
root.wm_title("OpenURL") 
root.resizable(0,0)
entry_text=StringVar() 
drop_text1=StringVar()
label = Label(root, text='File name')
entry = Entry(root, width=30, textvariable=entry_text)
drop_text1.set("E-book")
drop1 = OptionMenu(root,drop_text1,'Music','Video','E-book','Kindle','Images','Archive','Torrent')

def open_url():
    global drop_text1
    title=entry_text.get()
    options_dictionary = {
    'Music':'(.ogg|.mp3|.flac|.wma|.m4a) ',
    'Video':'(.mkv|.mp4|.avi|.mov|.mpg|.wmv) ',
    'E-book':'(.MOBI|.CBZ|.CBR|.CBC|.CHM|.EPUB|.FB2|.LIT|.LRF|.ODT|.PDF|.PRC|.PDB|.PML|.RB|.RTF|.TCR) ',
    'Kindle':'(.MOBI|.EPUB|.LIT) ',
    'Images':'(.jpg|.gif|.png|.tif|.tiff|.psd) ',
    'Archive':'(.rar|.tar|.zip|.sit) ',
    'Torrent':'.torrent '
    }
    url = 'https://www.google.com/search?q='+options_dictionary[drop_text1.get()]+title+' intitle:"index of" -inurl:(listen77|mp3raid|mp3toss|mp3drug|index_of|wallywashis)'
    if drop_text1.get()!='Torrent': url+=' -inurl:(jsp|pl|php|html|aspx|htm|cf|shtml)'
    webbrowser.open(url)

button_1=Button(root, text='GO', command=open_url, width=4) 
label.grid(row=0) 
entry.grid(row=0, column=1,columnspan=3) 
button_1.grid(row=0, column=4)
drop1.grid(row=1, column=1)

root.mainloop()
