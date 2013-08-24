#!/user/bin/python
# -*- coding: utf-8 -*-
# CryptoGui.py
# This file contains the GUI for the CryptoCheat Project

import ttk
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'CryptoCheat'))
import LetterFreq
from threading import Thread
from LetterFreq import *
from Tkinter import *
from ttk import *


class CryptoGui:

    def __init__(self):
        self.__CreateAndShowGUI()
        print 'hello'

    def __CreateAndShowGUI(self):
        root = Tk()
        root.title("CryptoCheat")
        content = ttk.Frame(root, padding=(3,3,12,12))
        self.textTop = Text(content, width=40, height=10)
        self.textBottom= Text(content, width=40, height=10)
        self.progress = ttk.Progressbar(content, orient=HORIZONTAL, length =200, mode='indeterminate')
        ok = ttk.Button(content, text="Decrypt", command=self.__OkAction)
        content.grid(column=0, row=0, sticky=(N, S, E, W))
        self.textTop.grid(column=0, row=0, columnspan=3, rowspan=1, sticky=(N, S, E, W), pady=5)
        self.textBottom.grid(column=0, row=1, columnspan=3, rowspan=1, sticky=(N, S, E, W), pady=5)
        self.progress.grid(column=0, row=2, columnspan =2)
        ok.grid(column=2, row=2, sticky=(E))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.mainloop()

    def __OkAction(self):
        self.progress.start()
        Thread(target=self.textBottom.insert(1.0, LetterFreq(str(self.textTop.get(1.0, END)).strip('\n')).get())).start()
        Thread.join()
        #textBottom.insert(1.0, LetterFreq(str(textTop.get(1.0, END)).strip('\n')).get())
        progress.stop()