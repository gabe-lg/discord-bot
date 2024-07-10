"""
Module containing helper functions for the bot
"""

import discord
from discord.ext import commands
from const import *
from datetime import datetime


async def command(c: discord.Client, msg: list[str],
                  ch: discord.TextChannel | discord.Thread,
                  author: discord.User | discord.Member):
    """
    Runs upon receiving message starting with `c.cmd_key` from Discord server.
    Executes bot commands if message contains bot commands.
    :param c:
    :param msg: list of words in message inputted by a user in Discord server.
    :param ch: Channel object corresponding to the channel in which the
     user sent the message.
    :param author: object representing the sender of the message.
    :raise ValueError: if message does not contain any valid bot commands.
    """
    if len(msg) < 2:
        raise ValueError("Cannot execute empty command")

    cmd = msg[1]
    if cmd == "echo":
        await _echo(c, msg, ch)
    elif cmd == "join":
        await _join(c, msg, ch)
    elif cmd == "setActivity":
        await _set_activity(c, msg, ch)
    elif cmd == "stopActivity":
        await _stop_activity(c, ch)
    elif cmd == "getKey":
        await _get_key(c, ch)
    elif cmd == "setKey":
        await _set_key(c, msg, ch)
    elif cmd == "kill":
        await _kill(c, ch, author)
    else:
        raise ValueError(f'"{cmd}" is not a valid command')


async def send_msg(c: discord.Client, text: str,
                   channel: int | discord.TextChannel | discord.Thread = CH_0):
    """
    Sends a message to the specified channel.
    :param c:
    :param text: text to be sent.
    :param channel: id or object of target channel. Requires the corresponding
     target channel is in the discord server the bot is active in.
     Default: `CH_0`
    :raise ValueError: if `channel_id` is not a valid `id`.
    """
    # convert channel id to object
    if isinstance(channel, int):
        channel = c.get_channel(channel)

    if not isinstance(channel, (discord.TextChannel, discord.Thread)):
        raise ValueError(
            f'Cannot send message to channel with id "{channel}": '
            "the specified channel was not found in discord server")
    await channel.send(text)


def send_user():
    raise NotImplementedError


# ===== COMMANDS ===== #
async def _echo(c: discord.Client, msg: list[str],
                ch: discord.TextChannel | discord.Thread):
    """
    Echos the message inputted by user.
    :param c:
    :param msg: list of words in message inputted by a user in Discord server.
    :param ch: Channel object corresponding to the channel in which the
     user sent the message.
    :raise ValueError: if no message is specified.
    """
    if len(msg) < 3:
        raise ValueError("`echo`: empty message")
    await send_msg(c, msg[2], ch)


async def _join(c, msg, ch):
    """ Instructs the bot to join a voice channel. If `channel-id` is not
    supplied, the bot will join the default voice channel. """
    # if -c supplied
    if len(msg) > 3 and msg[2] == "-c":
        try:
            vc_id = int(msg[3])
        except (TypeError, ValueError):
            raise ValueError("`join`: Channel ID must be an integer")
    else:
        vc_id = VC_DEFAULT

    vc = c.get_channel(vc_id)
    if not isinstance(vc, discord.VoiceChannel):
        raise ValueError(
            f'`join`: Cannot join voice channel with id "{vc_id}": '
            "the specified channel was not found in discord server")

    try:
        await vc.connect()
        await send_msg(c, f"Successfully joined `{vc.name}`.", ch)
    except discord.errors.ClientException:
        # if already in a vc
        await send_msg(c, "Error: `join`: bot is already in a voice channel",
                       ch)


async def _set_activity(c, msg, ch):
    """ Changes the activity of the bot. """
    if len(msg) < 4:
        raise ValueError("`setActivity`: invalid syntax\n"
                         "Usage: `$ setActivity [category] [name]`")

    valid_activities = ["play", "stream", "listen", "watch"]
    ctgy: str = msg[2].lower()

    if ctgy not in valid_activities:
        raise ValueError(f'`setActivity`: "{ctgy}" is an invalid category.\n'
                         "Valid categories: `play`, `stream`, `listen`, and "
                         "`watch`")

    name: str = msg[3]
    activities = [discord.Game(name=name),
                  discord.Streaming(name=name, url="https://github.com"),
                  discord.Activity(type=discord.ActivityType.listening, name=name),
                  discord.Activity(type=discord.ActivityType.watching, name=name)]

    for i in range(4):
        if ctgy == valid_activities[i]:
            await c.change_presence(activity=activities[i])

    await send_msg(c,
                   f"Successfully changed activity to `{name}`", ch)


async def _stop_activity(c, ch):
    """ Stops all activities of the bot. """
    await c.change_presence(activity=None)
    await send_msg(c,"Successfully stopped all activities", ch)


async def _get_key(c, ch):
    """ Displays current keyword and sends it as a message to user. """
    await send_msg(c, "The keyword for this bot is currently set to "
                      f"`{c.cmd_key}`.", ch)


async def _set_key(c, msg, ch):
    """
    Changes the keyword for regular bot commands.
    :raise ValueError: if `key` contains more than `KEYWORD_LENGTH` characters.
    """
    if len(msg) < 3:
        raise ValueError("`setKey`: cannot set keyword to empty variable")

    key = msg[2]
    if len(key) > KEYWORD_LENGTH:
        raise ValueError("Provided keyword is too long")

    c.cmd_key = key
    await send_msg(c, f"Keyword has been set to `{key}`.\n"
                      "Run `$ getKey` to display current keyword.", ch)


async def _kill(c, ch, author):
    """ If `author.id`==`USER_ID`, kills the bot. Otherwise, sends a text to
    `CH_ALERTS` and pass. """
    if author.id == USER_ID:
        await send_msg(c, "Bot killed.", ch)
        quit()
    else:
        await send_msg(c, "Unauthorized", ch)
        await send_msg(c, f"ALERT: user {author.name} attempted to kill "
                          f"the bot\n"
                          f"Time: {datetime.now().strftime('%H:%M:%S')}",
                       CH_ALERTS)


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
