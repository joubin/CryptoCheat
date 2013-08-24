#!/user/bin/python
# -*- coding: utf-8 -*-
#The gui code will go here Suckaaaaaaa
import ttk
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'CryptoCheat'))
import LetterFreq
from LetterFreq import *
from Tkinter import *
from ttk import *

def OkAction():
    progress.start()
    textBottom.insert(1.0, LetterFreq(str(textTop.get(1.0, END)).strip('\n')).get())
    progress.stop()

root = Tk()
root.title("CryptoCheat")
content = ttk.Frame(root, padding=(3,3,12,12))
textTop = Text(content, width=40, height=10)
textBottom= Text(content, width=40, height=10)
progress = ttk.Progressbar(content, orient=HORIZONTAL, length =200, mode='indeterminate')
ok = ttk.Button(content, text="Decrypt", command=OkAction)
content.grid(column=0, row=0, sticky=(N, S, E, W))
textTop.grid(column=0, row=0, columnspan=3, rowspan=1, sticky=(N, S, E, W), pady=5)
textBottom.grid(column=0, row=1, columnspan=3, rowspan=1, sticky=(N, S, E, W), pady=5)
progress.grid(column=0, row=2, columnspan =2)
ok.grid(column=2, row=2, sticky=(E))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()

