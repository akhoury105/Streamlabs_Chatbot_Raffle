import os, codecs, json

ScriptName = 'Raffle'
Website = 'twitch.tv/blueboxfromspace'
Description = 'Add viewers to and select random viewer from a text file for a raffle draw.'
Creator = 'BlueBoxFromSpace'
Version = '1.0.0'
Command = '!raffle'

path = os.path.dirname(__file__)
settingsFile = os.path.join(path, 'setting.json')

respHowToBuy = ''
respWhatToWin = ''


def Init():
    loadSettings()
    return


def ReloadSettings(jsonData):
    loadSettings()
    return


def loadSettings():
    global respWhatToWin, respHowToBuy
    try:
        with codecs.open(settingsFile, encoding='utf-8-sig', mode='r') as file:
            settings = json.loads(file, encoding='utf-8-sig')
    except:
        log("Error Loading Settings. Loaded Default Instead")
        settings = {
            "HowToBuy" : "Use Channel Points to buy entries into this month's Raffle!",
            "WhatToWin" : "This months prize is TBD! The Drawing will be held TBD."
        }
    
    respHowToBuy = settings['HowToBuy']
    respWhatToWin = settings['WhatToWin']


def Unload():
    return


def Execute(data):
    if data.IsChatMessage() and data.GetParam(0).lower() == Command:
        # !raffle tells viewers what the current raffle is for.
        if data.GetParamCount() == 1:
            send_message(respHowToBuy)
            send_message(respWhatToWin)

        # !raffle draw select random user from text file.

        # !raffle username adds user to a text file.
    
    return


def drawRaffle():
    # generate random number for index
    # use that number to get a user from our list
    return


def addUserToTextFile():
    # open the file
    # check to see if its empty
    # add new line if its not empty
    # add new user to new line
    return


def Tick():
    return


def OpenReadMe():
	#os.startfile(readMeFile)
	return


def send_message(message):
    Parent.SendStreamMessage(message)
    return


def log(message):
    Parent.Log(Command, str(message))
    return
    