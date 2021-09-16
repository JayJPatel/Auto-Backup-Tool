import os 
from backup import Backup  

#---------------------------------------------------------------------------
# CLASS - Tool

class Tool():  
    # Constructor 
    def __init__(self):  
        self.bTool = Backup() 
    
    # Main Menu loop, w/ options for user 
    def menu(self):  
        while(True): 
            os.system('cls')
            print("Auto Backup Tool\n") 
            print("Main Menu\n\n1. Run Backup\n2. Setup\n3. Help\n4. Exit")
            # Output msg if config.json not found 
            if (not self.bTool.config_Exists):  
                print ("config.json not detected! Please run setup before starting backup\n")
            
            # Try/Except for user input 
            try:  
                userInput = input()
                if (userInput not in ["1", "2", "3", "4"]):  
                    raise ValueError 
            except(ValueError):  
                print("Error: Please enter a number listed in the menu\n")
                input("Press Enter to continue...")
                continue 
            # Run Backup 
            if (userInput == "1"): 
                if (self.bTool.config_Exists):  
                    self.bTool.runBackup()
                else:  
                    print ("config.json not detected! Please run setup before starting backup\n")
                    input("\nPress Enter to return to the main menu...") 

            # Run setup
            if (userInput == "2"):  
                self.bTool.setup()

            # Open help menu 
            if (userInput == "3"):  
                self.helpMenu()

            # Exit 
            if (userInput == "4"):  
                exit() 

    # Opens help.txt and outputs help information
    def helpMenu(self):  
        os.system('cls')
        if (os.path.isfile('help.txt')):  
            print("---Help---\n")
            # Open help.txt (context manager) 
            with open('help.txt', 'r') as helpText:  
                print(helpText.read()) 
                input("\nPress Enter to return to the main menu...") 
        else:  
            print("Error: help.txt not found!")
            input("\nPress Enter to return to the main menu...") 
    
autoBackupTool = Tool() 

autoBackupTool.menu()
