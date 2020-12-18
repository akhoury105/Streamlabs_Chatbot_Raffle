##########
# RAFFLE #
##########
## Version 1.2.0 ##
-Adds command for checking number of tickets and odd of winning.

## Version 1.1.0 ##
-Adds ability to add multiple tickets at once.
-Adds ability to clear the raffle_tickets.txt file with a command.

by: blueboxfromspace
twitch.tv/blueboxfromspace

This is a Streamlabs Chatbot script that will allow you
    to add viewers to a txt file and randomly pick from
    that file to select a winner.


##### Getting Started #####

## Python ##
Loading scripts into Streamlabs Chatbot requires the installation of 
    Python 2.7.13
    https://www.python.org/downloads/release/python-2713/

## Installing Script ##
-First open up Streamlabs Chatbot
-Navigate to the Scripts tab on the panel on the left side of the screen.
    If you don't see a scripts tab then you need to finish configuring the Chatbot. 
    Check online for help with that.
-If you haven't loaded any scripts before you probably won't see anything here.
-Click on the settings cog in the top right corner
-In here you need to locate python 2.7s Lib folder
-Click Pick folder and navigate to python 2.7s Lib folder
-You should now be ready to load your scripts

As with all Streamlabs Chatbot scripts you can install it one of two ways.

## The easy way ##
At the top right there will be 5 icons (reload scripts, import, log, errors, settings)
-Click on the import icon
-Navigate to the zipped script folder
-Select it and click open
There should be a prompt that your script was loaded.
The scripts should refresh and your script should be present.

## The preferred way ##
-Right click anywhere in the Scripts tab
-Select 'Open Script Folder'
-Place your unzipped script folder inside this folder
Placing all your scripts in this folder makes it easier if you plan on altering the scripts in the future


####################### Using the Script #########################

## Commands ##
- There are 5 commands associated with this script right now.
- Changing the Permission access in the UI will not affect the base
    !raffle and !raffle odds command as these do not require permission.

# !raffle #
- When this command is used the bot will send two messages.
- Theses messages in the UI are:
    How To Buy Raffle Ticket
    What To Win and When Is Draw
- You can make these messages whatever you want, of course.
    I just felt these were best suited for the command.
- These responses have no variables you can insert in them.

# !raffle <username> #
- Restricted by Permission
- This command will add a viewer to the raffle_tickets.txt file.
- Replace <username> with the viewer you wish to add.
- There is a confirmation message your bot will send back once the
    viewer is added.
- The confirmation message can be edited in the UI under:
    Viewer Added message
- The {0} is a variable for the viewer that is being added to the list.
- Adding a number after the username will add that many tickets to the list.
	example: !raffle blueboxfromspace 4 (will add 4 tickets)

# !raffle draw #
- Restricted by Permission
- This command will select a random viewer from the raffle_tickets.txt file.
- This will return a message with the viewer name selected from the list.
- The message returned from this command can be edited in the UI under:
    Draw Message
- The {0} variable is used for the randomly selected viewer i.e. the winner of the draw.


# !raffle clear #
- Restricted by Permission
- This command clears the list of tickets. (i.e. it removes all names from raffle_tickets.txt)
- The message returned from this command can be edited in the UI under:
    Clear Tickets Message


# !raffle odds #
- This command can return a message that tells the user of the command how many tickets they have
    and what their odds of winning are.
- The message returned from this command can be edited in the UI under:
    Odds Message
- The message has 3 variables:
    {0} = user of the command
    {1} = the number of tickers the user has
    {2} = the odds that user has of winning


## Errors ##

- There is a message that will be sent by your bot in the event certain errors
    are triggered.
- These errors will be logged in the script logs tab of Streamlabs Chatbot.
- This message is customizable in the UI under:
    Error Message
