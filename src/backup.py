import os
import json
import tkinter as tk
from tkinter import filedialog

#---------------------------------------------------------------------------
# CLASS - Backup

class Backup() : 
    def __init__(self) : 
        if (os.path.isfile('config.json')) :
            self.config_Exists = True 
            self.parse()
        else :
            self.config_Exists = False  
            print("\nconfig.json Not detected! Run setup before running backup")

    def check(self) : 
        pass

    def run(self) : 
        pass 

    def parse(self) : 
        pass 

    # Prompt user for backup type, location, and files to backup
    def setup(self) : 
        os.system('cls')
        print("---Setup---")

        # Choose backup folder destination 
        input("\nPress Enter to choose file path for destination folder")
        #self.destination = filedialog.askdirectory() + "/Backup/"
        self.destination = self.getPath("/Backup/")
        print("Target destination directory: ", self.destination)

        #TODO Ask if this directory is correct 

        # Choose source folder location 
        input("\nPress Enter to choose file path for source folder")
        self.source = self.getPath("")

        print("Target source directory: ", self.source)

        input("\nPress Enter to return to the main menu...")

    # Method that grabs file path -- used in setup 
    def getPath(self, dirFolder) : 
        # Create + hide tkinter window
        tkWin = tk.Tk()
        tkWin.wm_attributes("-topmost", 1) # Move window to front
        tkWin.withdraw() 

        # Open file dialog to retrieve path 
        path = filedialog.askdirectory() + dirFolder

        # Destroy tkinter window, and return path
        tkWin.destroy()
        return path 
