import discord
try:
    import configparser
except:
    from six.moves import configparser

config = configparser.ConfigParser()
config.read('config.ini')
print ("Logged in as api",(config['api'].get('token')))

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(config['api'].get('token'))