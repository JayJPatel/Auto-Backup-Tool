import os
import json
import shutil 
import tkinter as tk
from tkinter import filedialog
from datetime import datetime 

#---------------------------------------------------------------------------
# CLASS - Backup

class Backup():  

    def __init__(self):  
        if (os.path.isfile('config.json')): 
            self.config_Exists = True 
            self.parse()
        else: 
            self.config_Exists = False  
            print("\nconfig.json Not detected! Run setup before running backup")
            self.destination_Flag = False 
            self.source_Flag = False 

    '''
    runBackup: Backs up source to directory w/ label of current time
    @param: None 
    @return: None 
    '''
    def runBackup(self):  
        print("Backing up...")
        # Grab current time, format, then store str to directory  
        RightNow = str(datetime.now()) 
        RightNow = RightNow.replace(" ", "_")
        RightNow = RightNow.replace(":", ".")
        RightNow = RightNow[:-7] # Removes milliseconds in str
        print(RightNow) 
        D = self.destination + RightNow # Backup folder w/ time 
        try : 
            shutil.copytree(self.source, D)
            print("Backup successful! ")
        except(FileNotFoundError) : 
            print("Error: Source directory not found!")
        input("Press Enter to continue...")
        return 
    
    '''
    parse: Reads info + stores data from config.json 
    @param: None
    @return: None 
    '''
    def parse(self):
        # Open config.json
        with open('config.json', 'r') as parse: 
            data = json.load(parse)
        # Store destination and source paths & update flags 
        self.dest_Path = data["Destination"]
        self.destination = self.dest_Path["Destination"]
        self.src_Path = data["Source"]
        self.source = self.src_Path["Source"]
        self.source_Flag = True 
        self.destination_Flag = True   
        return  
    
    '''
    setup: Prompt user for backup type, location, and files to backup
    @param: None 
    @return: None
    '''
    def setup(self):  
        # Loop for setting folder paths 
        while(True): 
            # Output menu 
            os.system('cls')
            print("---Setup---")
            print("\n1. Choose file path for destination folder", end = "")
            if (self.destination_Flag):  
                print(" [SET]", end = "")
                print("\n\t", self.destination, end = "")
            print("\n2. Choose file path for source folder", end = "")
            if (self.source_Flag):  
                print(" [SET]", end = "")
                print("\n\t", self.source, end = "")
            print("\n3. Return to main menu\n")

            # Try/Except for user input 
            try:  
                userInput = input()
                if (userInput not in ["1", "2", "3"]):  
                    raise ValueError
            except(ValueError):  
                print("Error: Please enter a number listed in the menu\n")
                input("Press Enter to continue...")
                continue
        
            # Choose backup folder destination
            if (userInput == "1"): 
                # If destination folder has already been set, prompt if user wants to update location  
                if (self.destination_Flag):  
                    while(True):  
                        print("\nDestination folder has already been set. Change destination directory location? Y/N")
                        try:  
                            destInput = input()
                            if (destInput not in ["y", "Y", "n", "N"]):  
                                raise ValueError 
                        except (ValueError): 
                            print("Error: Please enter either Y or N")
                            continue 
                        # User wants to update location 
                        if (destInput == "y" or destInput == "Y"):  
                            self.destination = self.setupLocation("destination", "/Backup/")
                            self.dest_Path = {"Destination": self.destination}
                            break
                        # User doesn't want to update location -- return to setup menu 
                        else:  
                            break 
                # If destination folder hasn't already been set, call setupLocation
                else:  
                    self.destination = self.setupLocation("destination", "/Backup/")
                    self.dest_Path = {"Destination": self.destination}

            # Choose source folder location
            # TODO - ADD MULTIPLE PATHS / REMOVE PATHS TO SOURCE 
            if (userInput == "2"):  
                self.source = self.setupLocation("source", "")
                self.src_Path = {"Source": self.source}

            # Return to main menu
            if (userInput == "3"):  
                # TODO Do not export if no changes have been made
                # Run export if both flags are set 
                if (self.destination_Flag and self.source_Flag) : 
                    self.export()
                break 
        return 

    '''
    getPath: Method that grabs file path by open file explorer dialog. Called in setupLocation
    @param: String to be concatenated to end of the path 
    @return: String containing file path 
    '''
    def getPath(self, dirFolder):  
        # Create + hide tkinter window
        tkWin = tk.Tk()
        tkWin.wm_attributes("-topmost", 1) # Move window to front
        tkWin.withdraw() 
        # Open file dialog to retrieve path 
        path = filedialog.askdirectory() + dirFolder
        # Destroy tkinter window, and return path
        tkWin.destroy()
        return path 

    '''
    setupLocation: Method used to retrieve a file path and update bool flags that are used in setup. 
    @param type: String specifying whether to set destination or source path 
    @param locStr: String to be concatenated to end of path 
    @return: String containing file path 
    '''
    def setupLocation(self, type, locStr):  
        print("Press Enter to choose file path for", type, "folder")
        input()
        location = self.getPath(locStr)

        # TODO -- Check for errors 
        print("Target", type, "directory:", location)

        # Update flags, then return 
        if (type == "destination"):  
            if (not self.destination_Flag):  
                self.destination_Flag = True
        else:  
            if (not self.source_Flag):  
                self.source_Flag = True
        input("Press Enter to continue...\n")
        return location

    '''
    export: Exports file paths in setup to json file 
    @param: None 
    @return: None
    '''
    def export(self) :
        # Move source and destination to a single object (to export)
        exportDict = {} 
        exportDict.update(Destination = self.dest_Path)
        exportDict.update(Source = self.src_Path)
        # Open file and export data
        with open('config.json', 'w') as config: 
            config.seek(0) # Move to line 1 
            json.dump(exportDict, config, indent=2)
            config.truncate()
        # Update bool config_exists
        if (not self.config_Exists): 
            self.config_Exists = True
        return 