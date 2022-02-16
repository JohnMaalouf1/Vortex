
from os.path import exists
import filecmp
import os



def main():
    print("Welcome to Vortex, to get started Please Select an Option From the Menu:\n\n1): Check if Files are Present.\n2): Check if Files are the same.\n3): Check File Times.\n0): Exit Program")
    userInput = input("> ")
    while(userInput != "0"):
        if userInput == "1":
            print("Checking Files...")
            check_if_file_exists()
        elif userInput == "2":
            compare_files()
            print("Comparing Files")
        elif userInput == "3":
            check_file_hierarchy()
            print("Comparing File Dates")
        userInput = input("> ")
    print("Ending Program")
    
def check_if_file_exists():
    print("Checking to see if File Exists")
    try:
        file_exists = exists(r'/home/ubuntu/Vortex/Pokemon_Fire_red2.sav')
        print("File Exists: " + str(file_exists))
        return True
    except:
        print("File Does not Exist")
        return False

def compare_files():
    try:
        file_status = filecmp.cmp(r'/home/ubuntu/Vortex/Pokemon - Fire Red Version (U) (V1.1).sav', r'/home/ubuntu/Vortex/Pokemon_Fire_red2.sav')
        if(file_status == True):
            print("File Sync up to date, no action required")
        elif(file_status == False):
            print("File Sync is out of date, checking most recent saves")
            check_file_hierarchy()
        return file_status
    except:
        print("File Does not Exist")
        return False

def check_file_hierarchy():
        localFile = os.path.getmtime(r'/home/ubuntu/Vortex/Pokemon_Fire_red2.sav')
        foreignFile = os.path.getmtime(r'/home/ubuntu/Vortex/Pokemon_Fire_red2.sav')
        if(localFile > foreignFile):
            print("You have new Data on your local machine, would you like to upload to Vortex?")
        elif(foreignFile > localFile):
            print("You have new Data on Vortex, would you like to download the latest Save?")
        print(localFile)
        print(foreignFile)
   

main()
