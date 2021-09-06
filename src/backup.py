import os
import json 
import tkinter as tk 
from tkinter import filedialog

tkWin = tk.Tk() 
tkWin.withdraw() 

#---------------------------------------------------------------------------
# CLASS - Backup

class Backup() : 
    def __init__(self) : 
        if (os.path.isfile('config.json')) :
            self.config_Exists = True 
            self.parse()
        else :
            self.config_Exists = False  
            print("\n config.json Not detected! Run setup before running backup")

    def check(self) : 
        pass

    def run(self) : 
        pass 

    def parse(self) : 
        pass 

    def setup(self) : 
        pass
