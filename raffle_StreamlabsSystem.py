import os

ScriptName = 'Raffle'
Website = 'twitch.tv/blueboxfromspace'
Description = 'Add viewers to and select random viewer from a text file for a raffle draw.'
Creator = 'BlueBoxFromSpace'
Version = '1.0.0'
Command = '!raffle'


def Init():
    return


def ReloadSettings(jsonData):
    return


def Unload():
    return


def Execute(data):
    if data.IsChatMessage() and data.GetParam(0) == Command:
    # !raffle username adds user to a text file.
        if data.GetParam(1)
    
    # !raffle draw select random user from text file.
    # !raffle tells viewers what the current raffle is for.
    return


def addUserToTextFile():



def Tick():
    return


def OpenReadMe():
	os.startfile(readMeFile)
	return


def send_message(message):
    Parent.SendStreamMessage(message)
    return


def log(message):
    Parent.Log(Command, str(message))
    return
    