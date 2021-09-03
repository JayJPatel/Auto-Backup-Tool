#---------------------------------------------------------------------------
# CLASS - Tool

class Tool() : 
    # Constructor 
    def __init__(self) : 
        # TODO : Parse & store relevant information on app start 
        pass
    
    # Main Menu loop, w/ options for user 
    def menu(self) : 
        while(True) : 
            print("Auto Backup Tool\n")
            print("Main Menu\n1. Run Manual Backup\n2. Setup\n3. Help\n4. Exit")
            #TODO TRY/CATCH IN THIS BLOCK
            userInput = input()    

            if (userInput == "1") :
                break 
            if (userInput == "2") : 
                break 
            if (userInput == "3") : 
                self.setup()
            
            if (userInput == "4") : 
                exit() 

autoBackupTool = Tool() 

autoBackupTool.menu()


