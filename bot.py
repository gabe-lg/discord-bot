"""
Starts up the bot, creates a connection with target server,
then prints out the server's name and id.

Credits:
adapted from https://realpython.com/how-to-make-a-discord-bot-python/
"""

from func import *

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    # coroutine has to be awaited
    await run(client)


client.run(TOKEN)
