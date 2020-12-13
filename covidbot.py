#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import discord
import os
import requests
import json
import asyncio 

client = discord.Client()

# #will only actually need this if we implemented the @bot.command extension. For simplicity since we are just learning, 
# #we will save this for a future project expansion
# bot = commands.Bot(command_prefix = "$")
# #we will program our own $help command so we don't need discord's built-in help function this time.
# bot.remove_command("help")

#displays message when invoked via the CMD line to verify that it's working
@client.event
async def on_ready():
    print("{0.user} is now awake!".format(client))

#bot will appear online, wait, and listen for user commands in the discord server
@client.event
async def on_message(message):
    
    #if message sender is the bot, we do not want it to respond to itself
    if message.author == client.user:
        return
    
    #if user types $intro, bot will introduce itself
    if message.content.startswith('$intro'):
        await message.channel.send("My name is {0.user} and I'm ready for duty! Type $help to see all I can do!".format(client))

    #if user types $locate
    if message.content.startswith('$locate'):
        await message.channel.send("Were you looking for me? I'm right here!")
        
##########**[Walesia's assignment]
    #if user queries $covid US <state>
    if message.content.startswith('$covid US') or message.content.startswith('$covid us'):
        
        #change state query to all uppercase
        content = message.content.upper()
        
        #split entire message content into separate strings
        content = content.split(" ")
        
        #if user request is valid (request of one state)
        if len(content) == 3:
            
            #third argument will be the state request, so assign it to its own variable
            state_req = content[2]
            
            #get API data from covid tracking website
            api_response = requests.get(f'https://covidtracking.com/api/states?state={state_req}')
            
            #load JSON data into dictionary
            state_dict = json.loads(api_response.text)
            
            #if user's state request is not valid, ie. the dictionary did not store data from the API
            if state_req not in state_dict.values():
                await message.channel.send("Sorry, that doesn't seem to be a valid state in the U.S.")
                
            #otherwise, if valid, get covid data
            else: 
    
                await message.channel.send(f"Okay! Let me fetch the latest COVID-19 stats for you. Give me 3 seconds... ")

                #wait three seconds before sending another message
                await asyncio.sleep(3)

                #get API data from covid tracking website
                api_response = requests.get(f'https://covidtracking.com/api/states?state={state_req}')
                
                #load JSON data into dictionary
                state_dict = json.loads(api_response.text)

                #print formatting, relevant data accessed using dictionary keys
                state_stats = (f'''
                This is the latest information for {state_dict['state']}: 
                New positive tests: {state_dict['positiveIncrease']}
                Currently hospitalized: {state_dict['hospitalizedCurrently']}
                Cumulative deaths: {state_dict['death']}
                New deaths: {state_dict['deathIncrease']}
                *this data was last updated on {state_dict['lastUpdateEt']}
                ''')
                
                #bot to return above state statistics into the server channel
                await message.channel.send(state_stats) 
                
        #if user request is not valid (requests no state)
        elif len(content) > 3:
            await message.channel.send("Invalid request. Please check your formatting. Ask for $help if you need assistance.")
            
########**[Walesia and Bryce's assignment]
    #if user queries $covid check, bot will search for countries
    if message.content.startswith('$covid check'):
        
        #split content of message into separate strings
        content = message.content.split(" ")
        
        #join country query into one string (ie. United Kingdom)
        country = (" ").join(content[2:])
        
        #getting API request
        country_api = requests.get(f'https://api.covid19api.com/summary')
        
        #loading JSON dictionary
        c_dict = json.loads(country_api.text)
        
        #within the JSON dictionary is a **LIST** of country dictionaries
        c_dict = c_dict['Countries']
        
        #make dictionary to store country query
        got_country = {}
        
        #for checking if user's search is a valid country
        
            
        #for entries in the dictionary
        for x in c_dict:

            #if user search matches either the country, country code, or slug
            if x['Country'] == f'{country}' or x['CountryCode'] == f'{country}' or x['Slug'] == f'{country}':
                
                #add country's stats to dictionary
                got_country.update(x)
                
        #if the dictionary has the country in it, aka if the bot found it.
        if f'{country}' in got_country.values():
            
            #return message to server that bot is getting information
            await message.channel.send(f"Roger that! I'll be right back with those stats... ")

            #wait three seconds before sending another message
            await asyncio.sleep(3)


            #print statement, returning facts using new sub-dictionary keys
            country_facts = (f'''
            Today's COVID-19 stats for {got_country['Country']}:
            Total cases: {got_country['TotalConfirmed']}
            New confirmed cases: {got_country['NewConfirmed']}
            Cumulative deaths: {got_country['TotalDeaths']}
            New deaths: {got_country['NewDeaths']}
            This information was last updated on: {got_country['Date']}
            ''')
            
            #return stats to server
            await message.channel.send(country_facts)

        #if the dictionary does not have the queried country in it, aka bot couldn't find it.
        if f'{country}' not in got_country.values():
            
            #send error message back to server
            await message.channel.send(f'''Sorry, I don't recognize that one.\nPlease double check or try searching the country in another format.''')
            
            
#** Below are conditions for the bot's handling of US statistics, worldwide statistics, and creation of the help function **

    #if user queries $covid 
    if message.content.startswith('$covid'):
        
        #change message content to all lowercase
        content = message.content.lower()
        
        #split message content into separate strings strings
        content = content.split(" ")
      
    ############***[Chabi's assignment] 
        #if the content of the second argument is the united states
        if len(content) == 2 and content[1] == "us": 
                        
            #send message that bot is retrieving data
            await message.channel.send("Awesome, I'll be right back with the latest COVID-19 stats. Give me just a moment.")
            
            #wait three seconds before sending another message
            await asyncio.sleep(3)
            
            #api response for U.S. statistics
            us_api_response = requests.get('https://api.covidtracking.com/v1/us/current.json')
            
            #this particular API query is a list containing a dictionary, so we have to extract the dictionary first
            us_dict = json.loads(us_api_response.text)[0]
  
            #print formatting, accessing relevant data using dictionary keys
            us_stat_facts = f'''
            Today's COVID-19 stats for the United States: 
            New positive tests: {us_dict['positiveIncrease']}
            Currently hospitalized: {us_dict['hospitalizedCurrently']}
            Cumulative deaths: {us_dict['death']}
            New deaths: {us_dict['deathIncrease']}
            *this data was last updated on {us_dict['lastModified']}
            '''
            #print us statistics to the server
            await message.channel.send(us_stat_facts)
            
        #if user queries a country that is not the United States    
        elif len(content) == 2 and content[1] != "us" and content[1] != "all" and content[1] != "help":
            
            #send error message
            await message.channel.send('''
            Hmm, I'm not sure what you mean. Please check your formatting or request. Type '$covid help' for assistance.
            ''')
 
        #if the content of argument is empty
        if len(content) == 1:
            await message.channel.send("Empty request. Type '$covid help' if you need assistance.")

    ##########***[Gerson's assignment]
        #if content of the second argument is <world>, to return worldwide statistics
        elif content[1] == "all": 
            
            #send message that bot is retrieving data
            await message.channel.send("Alrighty then, let me go grab those latest COVID-19 stats. Be back in a jiffy.")
            
            #wait three seconds before sending another message
            await asyncio.sleep(3)
            
            #get worldwide data from API
            world_api_response = requests.get(f'https://api.covid19api.com/summary')
            
            #load to JSON
            world_dict = json.loads(world_api_response.text)
            
            #get sub-dictionary that corresponds to global stats and write to separate dictionary
            world_stats = (world_dict['Global'])
            
            #print statement, returning facts using new sub-dictionary keys
            global_facts = f'''
            Today's global COVID-19 stats:
            Total cases: {world_stats['TotalConfirmed']}
            New confirmed cases: {world_stats['NewConfirmed']}
            Cumulative deaths: {world_stats['TotalDeaths']}
            New deaths: {world_stats['NewDeaths']}
            '''
            #have bot send global stats to server
            await message.channel.send(global_facts)
            
            
##########***[Yafet's assignment]
        #if content of the second argument is help 
        elif content[1] == "help":
            
            #user guide for help function
            help_function = (f'''
            Hi! Welcome to the user guide menu. 
            Check out all of my available features!
            
            **$covid US <state>**: returns latest stats for U.S. states; *use two digit state codes*
            **$covid US**: returns latest stats for entire United States
            **$covid check <country>**: returns latest stats for countries; *use two digit country code, or full name*
            **$covid all**: returns latest global covid stats.
            
            More features coming soon!
            ''')
            
            #bot return user guide help menu to server
            await message.channel.send(help_function)
            
#bot token goes here
#run bot from command line to start
client.run('NzgxMzI1NTIzMDAyODUxMzU5.X78AGQ.KvPOcHZlxk8xZB4AaugCT48Dbs0')


# In[ ]:





# 
