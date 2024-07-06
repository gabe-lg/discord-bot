"""
Module containing helper functions for the bot
"""

import discord
from const import *
from datetime import datetime


def init(c: discord.Client):
    """
    Runs after the initialization of the bot.
    :param c: `Client` object passed from `bot.py`.
    """
    guild = discord.utils.get(c.guilds, name=GUILD)
    print(f"{c.user} is connected to the following guild:\n"
          f"{guild.name}(id: {guild.id})\n"
          f"Time: {datetime.now().strftime('%H:%M:%S')}"
    )


async def command(c: discord.Client, msg: list[str],
                  channel: discord.TextChannel | discord.Thread):
    """
    Runs upon receiving message starting with `c.cmd_key` from Discord server.
    Executes bot commands if message contains bot commands.
    :param c:
    :param msg: list of words in message inputted by a user in Discord server.
    :param channel: Channel object corresponding to the channel in which the
     user sent the message.
    :raise ValueError: if message does not contain any valid bot commands.
    """
    if len(msg) < 2:
        raise ValueError("Cannot execute empty command")
    if msg[1] == "echo":
        await echo(c, msg, channel)
    else:
        raise ValueError(f"{msg} is not a valid command")


async def send_msg(c: discord.Client, text: str,
                   channel: int | discord.TextChannel | discord.Thread):
    """
    Sends a message to the specified channel.
    :param c:
    :param text: text to be sent.
    :param channel: id or object of target channel. Requires the corresponding
     target channel is in the discord server the bot is active in.
     Default: `CHANNEL_DEFAULT`
    :raise ValueError: if `channel_id` is not a valid `id`.
    """
    # convert channel id to object
    if isinstance(channel, int):
        c.get_channel(channel)

    if not isinstance(channel, (discord.TextChannel, discord.Thread)):
        raise ValueError(
            f'Cannot send message to channel with id "{channel}": '
            "the specified channel was not found in discord server")
    await channel.send(text)


def send_user():
    raise NotImplementedError


# ===== COMMANDS ===== #
def change_command_keyword(c: discord.Client, key: str):
    """
    Changes the keyword for regular bot commands.
    :param c:
    :param key: new keyword.
    :raise ValueError: if `key` contains more than `KEYWORD_LENGTH` characters.
    """
    assert isinstance(key, str)
    if len(key) > KEYWORD_LENGTH:
        raise ValueError("Provided key is too long")
    c.cmd_key = key


async def echo(c, msg, channel):
    """
    Echos the message inputted by user.
    :param c:
    :param msg: list of words in message inputted by a user in Discord server.
    :param channel:
    :return:
    """
    if len(msg) < 3:
        raise ValueError("echo: empty message")
    await send_msg(c, msg[2], channel)
