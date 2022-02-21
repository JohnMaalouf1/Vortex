from urllib import response
import requests
from os.path import exists
import filecmp
import os
import sys
from Client_Transfer import send_file_driver
#from Client_Reciever import send_client_file_driver

BASE = "http://192.168.1.51:5000/"

def main():
    '''
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

    print("-----------Transfer----------")
    localFileTime = check_local_file_hierarchy()
    ServerFileTime = requests.get(BASE + "check_file_hierarchy")
    ServerFileTime = str(ServerFileTime.json())[9:-1]
    print("Local File Time: ",localFileTime)
    print("Server File Time: ",ServerFileTime)

    if (float(ServerFileTime) > localFileTime):
        print("Server has a newer save, sending over new file")
    else:
        print("Client has a newer save, sending over new file")

'''



    menu()


def check_if_local_file_exists():
    #print("Checking to see if File Exists on Client:")
    try:
        file_exists = exists(r'/Users/jackmaalouf/Desktop/ClientEmulationDirectory/Pokemon_Fire_Red.sav')
        #print("File Exists: " + str(file_exists))
        return file_exists
    except:
        # This is where you would need to send the file and the rom to the configured Directory
        print("File Does not Exist")
        return file_exists


def check_local_file_hierarchy():
        local_file_latest_update = os.path.getmtime(r'/Users/jackmaalouf/Projects/Vortex/Client/Pokemon_Fire_Red.sav')
        #print("File was last Modified at: "+str(local_file_latest_update))
        return local_file_latest_update


def menu():
    print("\n\nWelcome to Vortex, to get started Please Select an Option From the Menu:\n\n1): Check if Files are Present.\n2): Check for new Save Data.")
    userInput = input("> ")
    while(userInput != "0"):



        if userInput == "1":
            print("Checking Files...")
            response = requests.get(BASE + "check_file_exists")
            serverResponse = str(response.json())[9:-1]
            print("Server File Status: ",serverResponse)
            print("Local File Status: ", check_if_local_file_exists())


        elif userInput == "2":
            print("Comparing Files...")
            localFileTime = check_local_file_hierarchy()
            ServerFileTime = requests.get(BASE + "check_file_hierarchy")
            ServerFileTime = str(ServerFileTime.json())[9:-1]
            print("Local File Time: ",localFileTime)
            print("Server File Time: ",ServerFileTime)

            if(localFileTime > float(ServerFileTime)):
                print("New Local Save Data Found, uploading to Vortex")
                send_file_driver()
            elif (float(ServerFileTime) > localFileTime):
                print("New Server Save Data Found, Download to Local Machine")
                ServerFileTime = requests.get(BASE + "send_server_file")

        userInput = input("> ")
    print("Ending Program")

main()

# 1645058628.8383772

# First system to download the save data needs to upload save data again to open deadlock for downloading