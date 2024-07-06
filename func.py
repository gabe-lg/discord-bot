"""
Module containing helper functions for the bot
"""

import discord
from const import *
from datetime import datetime


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

    cmd = msg[1]
    if cmd == "echo":
        await _echo(c, msg, channel)
    elif cmd == "getKey":
        await _get_key(c, channel)
    elif cmd == "setKey":
        await _set_key(c, msg, channel)
    else:
        raise ValueError(f'"{cmd}" is not a valid command')


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
async def _echo(c: discord.Client, msg: list[str],
                channel: discord.TextChannel | discord.Thread):
    """
    Echos the message inputted by user.
    :param c:
    :param msg: list of words in message inputted by a user in Discord server.
    :param channel: Channel object corresponding to the channel in which the
     user sent the message.
    :raise ValueError: if no message is specified.
    """
    if len(msg) < 3:
        raise ValueError("echo: empty message")
    await send_msg(c, msg[2], channel)


async def _get_key(c, channel):
    """
    Displays current keyword and sends it as a message to user.
    :param c:
    :param channel:
    """
    await send_msg(c, "The keyword for this bot is currently set to "
                      f"`{c.cmd_key}`.", channel)


async def _set_key(c, msg, channel):
    """
    Changes the keyword for regular bot commands.
    :param c:
    :param msg:
    :param channel:
    :raise ValueError: if `key` contains more than `KEYWORD_LENGTH` characters.
    """
    if len(msg) < 3:
        raise ValueError("setKey: cannot set keyword to empty variable")

    key = msg[2]
    if len(key) > KEYWORD_LENGTH:
        raise ValueError("Provided keyword is too long")

    c.cmd_key = key
    await send_msg(c, f'Keyword has been set to {key}.\n'
                      "Run `$ getKey` to display current keyword.", channel)


# ===== HELPER FUNCTIONS ===== #
def msg_split(content: str) -> list[str]:
    """
    Splits message into a list of strings. The space character is the
    delimiter, except when it is wrapped between double quotation marks.

    If `content` contains an odd number of quotation marks, all remaining text
    after the last quotation mark will not be split and will be appended to the
    list of strings as a single entry.

    Treats multiple space characters in a row as a single space character, and
    ignores any trailing space characters.

    :param content: string to be split.
    :return: the list of strings containing words in `content`.
    """
    wrapped_in_quotes: bool = False
    curr_word: str = ""
    words: list[str] = []

    for char in content:
        if char == '"':
            wrapped_in_quotes = not wrapped_in_quotes
        elif char == " " and not wrapped_in_quotes:
            if curr_word != "":
                words.append(curr_word)
                curr_word = ""
        else:
            curr_word += char

    # for last word
    if curr_word != "":
        words.append(curr_word)

    return words
