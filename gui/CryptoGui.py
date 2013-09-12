#!/user/bin/python
# -*- coding: utf-8 -*-
# CryptoGui.py
# This file contains the GUI for the CryptoCheat Project

import ttk
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'CryptoCheat'))
import LetterFreq
import threading
import thread
from LetterFreq import *
from Tkinter import *
from ttk import *




class CryptoGui:
    """
    This class is in charge of creating the gui. 
    """

    def __init__(self):
        self.__CreateAndShowGUI()

    def __ClearBottomTextBox(self):
        self.textBottom.delete(1.0, END)

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
        self.__ClearBottomTextBox()
        DecryptThread(self)
        print "after threading is done"

class DecryptThread(threading.Thread):
    """
    This class threads the individual tasks. 

    In future this class will be demoted and a DecryptThread will be create that will start many thraeds
    """

    def __init__(self, GuiAddress):
        threading.Thread.__init__(self)
        self.gui = GuiAddress
        print "Going to start the progress bar from the threaded class right before I start the class"
        self.start()

    def run(self):
        self.gui.progress.start()
        textFromTop = self.gui.textTop.get(1.0, END).strip('\n')
        decryptedText = LetterFreq(textFromTop).get()
        self.gui.textBottom.insert(1.0, decryptedText)
        self.gui.progress.stop()


if __name__ == '__main__':
    try:
        CryptoGui()
    except Exception, e:
        print e