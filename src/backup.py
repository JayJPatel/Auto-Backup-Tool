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
        # Check if config exists 
        if (self.config_Exists) : 
            self.parse()
        else : 
            # If config doesnt exist, set false flags 
            self.destination_Flag = False 
            self.source_Flag = False

        # Loop for setting folder paths 
        while(True) :
            # Output menu 
            os.system('cls')
            print("---Setup---")
            print("\n1. Choose file path for destination folder", end = "")
            if (self.destination_Flag) : 
                print(" [SET]", end = "")
            print("\n2. Choose file path for source folder", end = "")
            if (self.source_Flag) : 
                print(" [SET]", end = "")
            print("\n3. Return to main menu\n")

            # Try/Except for user input 
            try : 
                userInput = input()
                if (userInput not in ["1", "2", "3"]) : 
                    raise ValueError
            except(ValueError) : 
                print("Error: Please enter a number listed in the menu\n")
                input("Press Enter to continue...")
                continue
        
            # Choose backup folder destination
            if (userInput == "1") :
                # If destination folder has already been set, prompt if user wants to update location  
                if (self.destination_Flag) : 
                    while(True) : 
                        print("\nDestination folder has already been set. Change destination directory location? Y/N")
                        try : 
                            destInput = input()
                            if (destInput not in ["y", "Y", "n", "N"]) : 
                                raise ValueError 
                        except (ValueError) :
                            print("Error: Please enter either Y or N")
                            continue 
                        # User wants to update location 
                        if (destInput == "y" or destInput == "Y") : 
                            self.destination = self.setupLocation("destination", "/Backup/")
                            break
                        # User doesn't want to update location -- return to setup menu 
                        else : 
                            break 
                # If destination folder hasn't already been set, call setupLocation
                else : 
                    self.destination = self.setupLocation("destination", "/Backup/")
            
            # Choose source folder location
            # TODO - ADD MULTIPLE PATHS / REMOVE PATHS TO SOURCE 
            if (userInput == "2") : 
                self.source = self.setupLocation("source", "")

            # Return to main menu
            if (userInput == "3") : 
                break 

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

    # Method used to set location in setup
    def setupLocation(self, type, locStr) : 
        print("Press Enter to choose file path for", type, "folder")
        input()
        location = self.getPath(locStr)

        # TODO -- Check for errors 
        print("Target", type, "directory:", location)

        # Update flags, then return 
        if (type == "destination") : 
            if (not self.destination_Flag) : 
                self.destination_Flag = True
        else : 
            if (not self.source_Flag) : 
                self.source_Flag = True
        input("Press Enter to continue...\n")
        return location