from doctest import IGNORE_EXCEPTION_DETAIL
import pandas as pd
import discord
from dotenv import load_dotenv
import os
import sys
import numpy as np

async def get_messages(num_messages, client, channel_id, na_prefixes):
    channel = client.get_channel(int(channel_id))
    msg_hist = [['Content', 'time', 'author', 'id']]
    
    i = 1
    async for message in channel.history(limit=num_messages):

        if (message.author != client.user) and (message.author.id != 228537642583588864) and not (str(message.content).startswith(na_prefixes))  and (len(str(message.content)) >= 1 ):
            msg_hist.append([message.content, message.created_at, message.author.name, message.author.id])

        progress = (i/num_messages) * 100
        sys.stdout.write('\r')
        sys.stdout.write('[%-20s] %.1f%%' %(int(progress/5)*'=', progress))
        i += 1

    sys.stdout.write('\n')
    pd.DataFrame(msg_hist).to_csv('discord_message_hist.csv')
    print('Complete!')
    

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

bad_prefixes = ("#", "!", "?", "http", "+") # Bot will not collect messages with these prefixes

common_emoji = "\U0001F60E"

intents = discord.Intents.all()
client = discord.Client(intents=intents) #instance of the bot itself

@client.event
async def on_ready():
    print("Logged in as %s" %client.user)

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    elif message.content.startswith('#'):
        
        channel = str(message.channel.name)
        cmd = message.content.split()[0].replace('#', '')  # Getting command from first string
        parameters = []

        if len(message.content.split()) > 1:
            parameters = message.content.split()[1:] # Getting parameters if included

        '''
        CHANGE THIS: Need to replace all of the if statements below a function dictionary (lookup table)
        '''
        if cmd.lower() == 'hi':
            await message.channel.send(f'Hello')
            return
       
        elif cmd.lower() == 'bye':
            await message.channel.send(f'Bye bye! {common_emoji}', file=discord.File("C:/Users/liam/OneDrive/Documents/python projects/discord/shared resources/bot_profile_picture.jpg"))
            client.close()
            exit()

        elif cmd.lower() == 'get_messages': # Want to get messages
            #need to check if the second parameter is a number and if in acceptable range

            if len(parameters) > 1 or len(parameters) < 1:
                await message.channel.send(f'Error: Incorrect arguments provided')
                return
            
            elif len(parameters) == 1:
                #insert function
                await get_messages(int(parameters[0]), client, CHANNEL_ID, bad_prefixes)
                return

client.run(TOKEN)