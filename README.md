# discord-bot
A multipurpose discord bot for general purposes.

# Commands
`$ echo [message]`: echos the message inputted by user.<br>
`$ join -c [channel-id]`: instructs the bot to join a voice channel. If 
`channel-id` is not supplied, the bot will join the default voice channel.<br>
`$ setActivity [category] [name]`: changes the activity of the bot.<br>
`$ stopActivity`: stops all activities of the bot.<br>
`$ getKey`: displays current keyword and sends it as a message to user.<br>
`$ setKey [key]`: changes the keyword for regular bot commands.<br>
`$ kill`: kills the bot.<br>

# Usage
Follow the link in the "About" section of this repository to add this bot to 
your server.<br>
<i>Note: Discord requires that you have <b>Manage server</b> permission in the 
server.</i>

# Setup
Follow these steps to create a new bot.
1. Create a Discord bot. <br><i> See
https://realpython.com/how-to-make-a-discord-bot-python/#creating-a-bot for 
detailed instructions.</i>
2. Run `git clone https://github.com/gabe-lg/discord-bot.git` to clone this 
repository.
3. In the home directory, rename `env.txt` into `.env`.
4. Inside `.env`, replace the placeholder names in curly braces with actual 
data as specified.
5. Install modules required for the basic functionality of this app:
```
pip install -U discord.py
pip install -U python-dotenv
pip install -U pynacl
```
6. In a terminal, run
<br>
```
python bot.py
```
