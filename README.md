# testudo-covid-discord-bot

This is a Discord bot, named 'Testudo Covid Patrol', coded in Python using discord.py that returns recent COVID-19 statistics. 

## About
-------------------------

After being invited into a Discord server, our bot will operate within the channel(s) where it is allowed base permissions send messages and read messages. The bot will listen to the server chat until it detects that a “$covid” command has been made. If the request is valid, it will then retrieve the requested information from the relevant API(s) and return the statistics to the server channel it was requested from. If the request is invalid, the bot will return an error message guiding the user to proper syntax. 

Data is retrieved from The [COVID Tracking Project](https://covidtracking.com/data/api) and [COVID19 API](https://covid19api.com/).

To integrate with Discord and our command line, we imported the discord and asyncio libraries along with the os modules. We also imported the requests library and the built-in JSON package in order to interact with the APIs and retrieve the necessary data. 

## Current features for our bot: 
------------------

**$covid US (state)**: bot will return the latest statistics for the queried US state to include: new positive cases, current hospitalizations, cumulative deaths, new daily deaths, and how recently the data was last updated.

**$covid check (country)**: bot will return the latest statistics for the queried country to include: total cases, new confirmed cases, cumulative deaths, new daily deaths, and how recently the data was last updated.
Country queries are supported as both two digit country codes and by formal name. 

**$covid all**: bot will return the latest worldwide statistics.


**$covid help:** bot will return a user menu that displays available features and provides notes on proper syntax.


## Error handling:
Our bot’s code also supports input validation. If the user makes a query that is not recognized, the bot will return an error message and direct the user to double check their syntax or consult the ‘$covid help’ documentation.
Empty command: 

>Invalid state query:

>Too many arguments: 

>Incorrect syntax: 

>Invalid two-digit country code:

## Creating your own Discord Bot: 

- First you need to download the latest version of Python, as of December 2020 which is version 3.9 . To do so, navigate to the downloads section of  Python’s website. Select the 3.9 version and run it. Go to your menu after and click IDLE Python 3.9 64-bit. This is the new coding space.

- Now you need to set up a discord.py library. You can get the library directly from PyPI. Into the command terminal type:
  - python 3 -m install -U discord.py
  - If you are using windows type : py -3 -m pip install, -U discord.py

- Next, create a simple Bot using code similar to our bot here:

- Generate your bot token from your Discord’s Developer Portal, where you can also customize your bot’s description, picture, and name.



- Once you run your bot and it is logged in and ready, it should display the on_ready message in your console. In this case, *“It’s {bot name} here!”*

- Finally invite your bot to the Discord server. Change any necessary channel permissions if you wish to isolate which channels the bot can read messages/operate in. 

