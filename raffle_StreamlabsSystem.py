import os, codecs, json

ScriptName = 'Raffle'
Website = 'twitch.tv/blueboxfromspace'
Description = 'Add viewers to and select random viewer from a text file for a raffle draw.'
Creator = 'BlueBoxFromSpace'
Version = '1.0.1'
Command = '!raffle'

path = os.path.dirname(__file__)
settingsFile = os.path.join(path, 'settings.json')
raffleTicketFile = os.path.join(path, 'raffle_tickets.txt')
readMeFile = os.path.join(path, 'README.txt')

settings = {}
respHowToBuy = ''
respWhatToWin = ''
respWinner = ''
respAddedTicket = ''
respClearTickets = ''
permission = 'Caster'
error = ''

# TODO: Add sound effect for draw.
# TODO: Add delay to winner reveal.
# TODO: Later verion create variables in UI to change prize and draw date.
# TODO: Add command to clear text file.

def Init():
    loadSettings()
    return


def ReloadSettings(jsonData):
    loadSettings()
    return


def loadSettings():
    global respWhatToWin, respHowToBuy, permission, error, respWinner, respAddedTicket, settings, respClearTickets
    try:
        with codecs.open(settingsFile, encoding='utf-8-sig', mode='r') as file:
            settings = json.load(file, encoding='utf-8-sig')
    except:
        log("Error Loading Settings. Loaded Default Instead")
        settings = {
            "Permission":"Caster",
            "HowToBuy" : "Use Channel Points to buy entries into this month's Raffle!",
            "WhatToWin" : "This month's prize is TBD! The Drawing will be held TBD.",
            "WinMessage": "This raffle's winner is @{0}!",
            "ErrorMessage": "Error Occurred. Please check the logs.",
            "AddedMessage": "@{0} has been added to the list.",
            "ClearMessage": "The ticket list has been cleared."
        }

    permission = settings['Permission']
    respHowToBuy = settings['HowToBuy']
    respWhatToWin = settings['WhatToWin']
    respWinner = settings['WinMessage']
    error = settings['ErrorMessage']
    respAddedTicket = settings['AddedMessage']
    respClearTickets = settings['ClearMessage']


def Unload():
    return


def Execute(data):
    if data.IsChatMessage() and data.GetParam(0).lower() == Command:
        # !raffle tells viewers what the current raffle is for.
        if data.GetParamCount() == 1:
            send_message(respHowToBuy)
            send_message(respWhatToWin)

        # !raffle clear clears the text file.
        elif data.GetParam(1) == 'clear' and Parent.HasPermission(data.User, permission, ''):
            clearTickets()

        # !raffle draw select random viewer from text file.
        elif data.GetParam(1).lower() == "draw" and Parent.HasPermission(data.User,permission,''):
            drawRaffle()

        # !raffle odds tells viewer odds of winning and how many tickets they have.
        elif data.GetParam(1).lower() == "odds":
            raffleOdds(data.UserName)

        # !raffle username adds viewer to a text file.
        elif data.GetParamCount() > 1 and Parent.HasPermission(data.User,permission,''):
            if data.GetParamCount() == 2:
                addViewerToTextFile(data.GetParam(1), 1)
            elif data.GetParam(2).isnumeric():
                addViewerToTextFile(data.GetParam(1), int(data.GetParam(2)) )
        
    return


# Calculates odds and returns message with odds, and num of tickets for the user
def raffleOdds(user):
    totalTickets = len(getTickets())
    userTickets = getUserTickets(user)
    odds = float(userTickets)/float(totalTickets)
    odds = odds * 100
    resp = '{}, you have {} tickets. Your odds of winning are {}%.'.format(user, userTickets, odds)
    send_message(resp)


# Returns the number of tickets a user has purchased.
def getUserTickets(user):
    tickets = getTickets()
    tickets = formatTickets(tickets)
    tickets = lowerNamesInList(tickets)
    numOfUserTickets = tickets.count(user.lower())
    return numOfUserTickets


# Updates the ticket list from our text file.
def getTickets():
    try:
        with open(raffleTicketFile, 'r') as file:
            tickets = file.readlines()
    except:
        send_message(error)
        log("Error loading tickets from raffle_tickets.txt")
    return tickets


def drawRaffle():
    # open our text file and store it in list
    tickets = getTickets()
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


# Returns a useable list of tickets
def formatTickets(tickets):
    newTickets = []
    for x in tickets:
        x = x.replace('\n','')
        newTickets.append(x)
    return newTickets


# Returns a list where the tickets are all lower case for counting tickets
def lowerNamesInList(tickets):
    newTickets = []
    for x in tickets:
        x = x.replace(x,x.lower())
        newTickets.append(x)
    return newTickets


def addViewerToTextFile(viewer, num):
    viewer = sanitizeUser(viewer)
    for i in range(num):
        try:
            # open the file
            with open(raffleTicketFile, 'a+') as file:
                # check to see if its empty
                file.seek(0)
                data = file.read(100)
                # add new line if its not empty
                if len(data) > 0:
                    file.write('\n')
                # add new viewer to new line
                file.write(viewer)
        except:
            send_message(error)
            log("Couldn't add viewer to raffle_tickets.txt")
            return
    send_message(respAddedTicket.format(viewer))
    return


def clearTickets():
    try:
        with open(raffleTicketFile, 'w+') as file:
            file.write('')
    except:
        send_message(error)
        log("Couldn't clear raffle_tickets.txt")
        return
    send_message(respClearTickets)


# Removes the @ symbol from the name
def sanitizeUser(user):
    user = user.replace('@','')
    return user


def Tick():
    return


def OpenReadMe():
	os.startfile(readMeFile)
	return


def send_message(message):
    Parent.SendStreamMessage(str(message))
    return


def log(message):
    Parent.Log(Command, str(message))
    return
    