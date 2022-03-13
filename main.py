# Import specific modules for the program
import random
import discord
from discord.ext import commands

# Enter curses in a python list order ex [curse1, curse2, curse3, curse4]
curse = ['CURSES']


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
# if a person curse . it automatically deletes it
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        for a in range(len(curse)):
            if curse[a] in message.content.lower():
                await message.delete()
        
             

client = MyClient()
# Enter The bot token
client.run('TOKEN')

