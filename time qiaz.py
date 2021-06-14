
######################################################
##### THIS BROJET IS MEAD BY : NORALDIM     ##########
##### GitHup : noraldim                     ##########
##### fallow the tips explane tiks to bater ##########
##### understan                             ##########
######################################################

# her we import tkinter to give us windows UI
# and also we import time

from tkinter import *
from tkinter.ttk import *
from time import strftime

# her we call the main function to costmize and creat border

root = Tk()
root.title('TIME by noraldim')

# this def to desply time in border
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

# her we stiling the lable wigit and color of front and back
# "ds-digital" its font come spratly from script you most downlod or tray ather font
lbl = Label(root,
            font = ('ds-digital', 70, 'bold'),
            background = 'black',
            foreground = 'white'
            )

# pot the clock in the center of bord 'tkintr'

lbl.pack(anchor = 'center')
time()
mainloop()
