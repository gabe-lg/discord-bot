# discord-bot
A multipurpose discord bot for general purposes.

# Create an `.env` file
After cloning this repository, create a file with name `.env` inside the same directory as `bot.py`,
then copy the following code into the file.
<br>
```
; Discord token: private static token unique to the bot.
; get from dev portal: Settings > Bot > TOKEN
TOKEN={bot-token}

; Name of guild: the public name of target Discord server.
GUILD={guild-name}

; ===== Discord channels =====
; Channel id
; `None` if `getenv` does not return an `int`
; get from right-clicking channel > "Copy Server ID" with dev tools enabled
CHANNEL_0={channel-id}
```
Replace the placeholder names in curly braces with actual data as specified.

# Installation
These modules are required for running this project. Install as follows:
```
pip install -U discord.py
pip install -U python-dotenv
```

# Usage
In a terminal, run
<br>
```
python bot.py
```
