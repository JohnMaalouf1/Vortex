'''
@Author - John Maalouf

Server Program

Will have Directories to store ROM and Save data.
Requires Client to configure Emulation Directory
Will check to see if rom and save file are present in emulation directory, if not send rom and save file
If they are present, check timestamp of save file, if it is old, try to update it

'''

from os.path import exists
import filecmp
import os
    
def check_if_file_exists():
    # Need to setup Emulation Directory
    print("Checking to see if File Exists on Client")
    try:
        file_exists = exists(r'C:\Users\jackm\Vortex\Server\Pokemon_Fire_Red.sav')
        print("File Exists: " + str(file_exists))
        return file_exists
    except:
        # This is where you would need to send the file and the rom to the configured Directory
        print("File Does not Exist")
        return file_exists

def compare_files():
    try:
        file_status = filecmp.cmp(r'C:\Users\jackm\Projects\Vortex/Pokemon_Fire_Red.sav', r'/Users/jackmaalouf/Projects/Vortex/ServerEmulationDirectory/Pokemon_Fire_Red.sav')
        if(file_status == True):
            print("File Sync up to date, no action required")
        elif(file_status == False):
            print("File Sync is out of date, checking most recent saves")
            check_file_hierarchy()
        return file_status
    except:
        print("File Does not Exist")
        return False

def check_server_file_hierarchy():
        server_file_latest_update = os.path.getmtime(r'C:\Users\jackm\Vortex\Server\Pokemon_Fire_Red.sav')
        print("File was last Modified at: "+str(server_file_latest_update))
        return server_file_latest_update

   



#def main():
#    print("Welcome to Vortex, to get started Please Select an Option From the Menu:\n\n1): Check if Files are Present.\n2): Check if Files are the same.\n3): Check File Times.\n0): Exit Program")
#    userInput = input("> ")
#    while(userInput != "0"):
#        if userInput == "1":
#            print("Checking Files...")
#            check_if_file_exists()
#        elif userInput == "2":
#            compare_files()
#            print("Comparing Files")
#        elif userInput == "3":
#            check_file_hierarchy()
#            print("Comparing File Dates")
#        userInput = input("> ")
#    print("Ending Program")

#main()
