import requests
import os
import json


def getStartAddress():
    return input("Please Enter the Starting Address:")


def getStartCity():
    return input("Please Enter the Starting City(Ex. City,ST):")


def getDestinationAddress():
    return input("Please Enter your Destination Address:")


def getDestinationCity():
    return input("Please Enter your Destination City(Ex. City,ST):")


def validDir():
    startAddress = getStartAddress()
    startCity = getStartCity()
    destinationAddress = getDestinationAddress()
    destinationCity = getDestinationCity()

    dir = 'http://www.mapquestapi.com/directions/v2/route?key=koBSx5A8tI3GQVXABdi6F7vGNdhwiESn&from='\
          + startAddress + startCity + '&to=' + destinationAddress + destinationCity

    dlDir(dir)


def dlDir(dl):
    res = requests.get(dl)

    writeMap = open('temp.json', 'wb')

    for chunk in res.iter_content(100000):
        writeMap.write(chunk)

    writeMap.close()
    parseDir('temp.json')


def parseDir(dir):
    test = open(dir, 'r')
    data = test.read()
    dirData = json.loads(data)

    writeDir = open(input("Enter File Name:") + '.txt', 'w')

    for item in dirData['route']['legs'][0]['maneuvers']:
        writeDir.write(item['narrative'])
        writeDir.write('\n')

    writeDir.close()
    test.close()


def main():
    validDir()
    os.remove('temp.json')


main()