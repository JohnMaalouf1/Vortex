from urllib import response
import requests

BASE = "http://192.168.1.54:5000/"

def main():
    clientEmulationDirectory = '/Users/jackmaalouf/Desktop/EmulationDirectory'
    #input("Please configure your Emulation Directory:")
    print(clientEmulationDirectory)
    print("Welcome to Vortex, to get started Please Select an Option From the Menu:\n\n1): Check if Files are Present.\n2): Check if Files are the same.\n3): Check File Times.\n0): Exit Program")
    userInput = input("> ")
    while(userInput != "0"):
        if userInput == "1":
            print("Checking Files...")
            response = requests.get(BASE + "check_files")
            print(response.json())
        elif userInput == "2":
            compare_files()
            print("Comparing Files")
        elif userInput == "3":
            check_file_hierarchy()
            print("Comparing File Dates")
        userInput = input("> ")
    print("Ending Program")

main()



