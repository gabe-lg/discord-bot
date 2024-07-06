"""

"""
from func import *

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
c = discord.Client(intents=intents)

# set command keyword
c.cmd_key = KEYWORD_DEFAULT


@c.event
async def on_ready():
    """
    Starts up the bot, creates a connection with target server,
    then prints out the server's name and id.

    Credits:
    adapted from https://realpython.com/how-to-make-a-discord-bot-python/
    """
    init(c)


@c.event
async def on_message(message):
    """

    """
    # print(message.content, c.cmd_key)
    msg = message.content.split(" ")
    if message.author == c.user:
        return
    if msg[0] == c.cmd_key:
        try:
            await command(c, msg, message.channel)
        except ValueError as e:
            await send_msg(c,
                           f"Error: {e.args[0]}",
                           message.channel)


c.run(TOKEN)
