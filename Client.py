from urllib import response
import requests
from os.path import exists
import filecmp
import os
import sys
from Client.Client_Transfer import send_file_driver


BASE = "http://172.20.10.3:5000/"

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
        local_file_latest_update = os.path.getmtime(r'/Users/jackmaalouf/Desktop/ClientEmulationDirectory/Pokemon_Fire_Red.sav')
        #print("File was last Modified at: "+str(local_file_latest_update))
        return local_file_latest_update


def menu():
    print("\n\nWelcome to Vortex, to get started Please Select an Option From the Menu:\n\n1): Check if Files are Present.\n2): Check if Files are the same.\n3): Send File to Server")
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

        elif userInput == "3":
            send_file_driver()

        userInput = input("> ")
    print("Ending Program")

main()

# 1645058628.8383772