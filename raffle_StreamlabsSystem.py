import os, codecs, json

ScriptName = 'Raffle'
Website = 'twitch.tv/blueboxfromspace'
Description = 'Add viewers to and select random viewer from a text file for a raffle draw.'
Creator = 'BlueBoxFromSpace'
Version = '1.0.0'
Command = '!raffle'

path = os.path.dirname(__file__)
settingsFile = os.path.join(path, 'setting.json')
raffleTicketFile = os.path.join(path, 'raffle_tickets.txt')

respHowToBuy = ''
respWhatToWin = ''
respWinner = ''
permission = 'Caster'
error = ''

# TODO: Add sound effect for draw.
# TODO: Add delay to winner reveal.
# TODO: Later verion create variables in UI to change prize and draw date.

def Init():
    loadSettings()
    return


def ReloadSettings(jsonData):
    loadSettings()
    return


def loadSettings():
    global respWhatToWin, respHowToBuy, permission, error, respWinner
    try:
        with codecs.open(settingsFile, encoding='utf-8-sig', mode='r') as file:
            settings = json.loads(file, encoding='utf-8-sig')
    except:
        log("Error Loading Settings. Loaded Default Instead")
        settings = {
            "Permission":"Caster",
            "HowToBuy" : "Use Channel Points to buy entries into this month's Raffle!",
            "WhatToWin" : "This month's prize is TBD! The Drawing will be held TBD.",
            "WinMessage": "This raffle's winner is @{0}!",
            "ErrorMessage": "Error Occurred. Please check the logs."
        }

    permission = settings['Permission']
    respHowToBuy = settings['HowToBuy']
    respWhatToWin = settings['WhatToWin']
    respWinner = settings['WinMessage']
    error = settings['ErrorMessage']


def Unload():
    return


def Execute(data):
    if data.IsChatMessage() and data.GetParam(0).lower() == Command:
        # !raffle tells viewers what the current raffle is for.
        if data.GetParamCount() == 1:
            send_message(respHowToBuy)
            send_message(respWhatToWin)

        # !raffle draw select random viewer from text file.
        elif data.GetParam(1).lower() == "draw" and Parent.HasPermission(data.User,permission,''):
            drawRaffle()

        # !raffle username adds viewer to a text file.
    
    return


def drawRaffle():
    # open our text file and store it in list
    try:
        with open(raffleTicketFile, 'r') as file:
            tickets = file.readlines()
    except:
        send_message(error)
        log("Error loading tickets from raffle_tickets.txt")
    # generate random number for index
    # use that number to get a viewer from our list
    if len(tickets) == 0:
        send_message(error)
        log("No tickets found in raffle_tickets.txt")
        return
    tickets = formatTickets(tickets)
    winner = tickets[Parent.GetRandom(0,len(tickets))]
    send_message(respWinner.format(winner))
    return


def addUserToTextFile():
    # open the file
    # check to see if its empty
    # add new line if its not empty
    # add new viewer to new line
    return

def formatTickets(tickets):
    newTickets = []
    for x in tickets:
        x = x.replace('\n','')
        newTickets.append(x)
    return newTickets



def Tick():
    return


def OpenReadMe():
	#os.startfile(readMeFile)
	return


def send_message(message):
    Parent.SendStreamMessage(str(message))
    return


def log(message):
    Parent.Log(Command, str(message))
    return
    