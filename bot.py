"""
Main script for the bot

Credits:
adapted from https://realpython.com/how-to-make-a-discord-bot-python/
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
    """
    guild = discord.utils.get(c.guilds, name=GUILD)
    print(f"{c.user} is connected to the following guild:\n"
          f"{guild.name}(id: {guild.id})\n"
          f"Time: {datetime.now().strftime('%H:%M:%S')}")


@c.event
async def on_message(message: discord.Message):
    """
    Executes upon receiving a message in any Discord channel the bot has access
    to. Searches for `c.cmd_key` and runs relevant commands.
    """
    msg = msg_split(message.content)

    # bot should not react to its own messages
    if message.author == c.user:
        return

    if msg[0] == c.cmd_key:
        try:
            await command(c, msg, message.channel)
        except ValueError as e:
            await send_msg(c, f"Error: {e.args[0]}", message.channel)


c.run(TOKEN)
