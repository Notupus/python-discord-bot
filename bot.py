import os
import discord
try:
    import configparser
except:
    from six.moves import configparser

config = configparser.ConfigParser()
config.read('config.ini')
client = discord.Client()
if config['output'].getboolean('show_bot_identification'):

    print ("Attemping to log in as api",(config['api'].get('token')))
else:
    print("Attemping to log in to API")

class MyClient(discord.Client):
    async def on_ready(self):
        if config['output'].getboolean('show_bot_identification'):
         print('Logged on as {0}!'.format(self.user))
        else:
            print("Not showing any identifiction in output is disabled. Change the show_bot_identification parameter to true in config.ini to change that ")

    async def on_message(self, message):
       if config['output'].getboolean('show_incoming_messeges'):
          print('Message from {0.author}: {0.content}'.format(message))


    async def on_member_join(member):
        if config['actions'].getboolean('greet'):
           await member.create_dm()
           await member.dm_channel.send(
         f'Hi {member.name}, welcome to my Discord server!'
    )


    async def on_message(message):
      if message.author == client.user:
        return

      if message.content.startswith('$hello'):
        if config['actions'].getboolean('greet_back'):
         await message.channel.send('Hello!')



client = MyClient()
client.run(config['api'].get('token'))

