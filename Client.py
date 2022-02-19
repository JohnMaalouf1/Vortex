from urllib import response
import requests
from os.path import exists
import filecmp
import os

BASE = "http://192.168.1.54:5000/"

def main():
    print()
    clientEmulationDirectory = '/Users/jackmaalouf/Desktop/ClientEmulationDirectory'
    serverEmulationDirectory = '/Users/jackmaalouf/Desktop/ServerEmulationDirectory'


    print("-----------Client----------")
    print("Client Emulation Directory: "+str(clientEmulationDirectory))
    check_if_local_file_exists()
    check_local_file_hierarchy()
    #else:
        #download file from Server

    print("-----------Server----------")
    print("Server Emulation Directory: "+str(serverEmulationDirectory))
    print("Checking Files...")
    response = requests.get(BASE + "check_file_exists")
    print(response.json())

    print("Comparing Files...")
    response = requests.get(BASE + "check_file_hierarchy")
    print(response.json())

    print("--------File Transfer--------")
    def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=True)

    menu()


def check_if_local_file_exists():
    print("Checking to see if File Exists on Client:")
    try:
        file_exists = exists(r'/Users/jackmaalouf/Desktop/ClientEmulationDirectory/Pokemon_Fire_Red.sav')
        print("File Exists: " + str(file_exists))
        return file_exists
    except:
        # This is where you would need to send the file and the rom to the configured Directory
        print("File Does not Exist")
        return file_exists


def check_local_file_hierarchy():
        local_file_latest_update = os.path.getmtime(r'/Users/jackmaalouf/Desktop/ClientEmulationDirectory/Pokemon_Fire_Red.sav')
        print("File was last Modified at: "+str(local_file_latest_update))


def menu():
    print("\n\nWelcome to Vortex, to get started Please Select an Option From the Menu:\n\n1): Check if Files are Present.\n2): Check if Files are the same.\n3): Check File Times.\n0): Exit Program")
    userInput = input("> ")
    while(userInput != "0"):



        if userInput == "1":
            print("Checking Files...")
            response = requests.get(BASE + "check_file_exists")
            print(response.json())


        elif userInput == "2":
            print("Comparing Files...")
            response = requests.get(BASE + "check_file_hierarchy")
            print(response.json())

        elif userInput == "3":
            check_file_hierarchy()
            print("Comparing File Dates")
        userInput = input("> ")
    print("Ending Program")

main()

# 1645058628.8383772