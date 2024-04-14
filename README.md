
# Discord-Slash-Command V1

> `NOTE 📝:` This is a Discord bot built with Discord.py, as a template for slash commands and already a ping command. This project may not be completely finished yet, but I don't plan to add more at this moment, because I want it more as a template for others.


# Table of Contents
- [Features](#features)
- [Bot Usage](#bot-usage)
- [Commands](#commands)
  - [Sync Command](#sync-command)
  - [Ping Command](#ping-command)
- [Installation](#installation)
- [Configuration](#configuration)
- [Pictures](#pictures)


## Features

- **Slash Command sync:** Sync slash commands globally or in specific guilds.
- **Ping Command:** Check the bot's latency.

## Bot Usage
To use this bot, follow these steps: 
+ set up a bot on https://discord.com/developers/applications
+ get your bot token and put the token in the token.txt
+ Invite the bot to your Discord server 
+ Run the bot by putting your token in the `"token.txt"`, no other characters



## Commands

### Sync Command

- **Description:** Sync slash commands globally or in specific guilds.
- **Usage:** `.sync [guilds] [spec]` 
  - `guilds`: Optional list of guild IDs to sync commands to.
  - `spec`: Optional argument to specify syncing method: `"guild"`, `"global"`, or `"clear"`.
- **Permissions Required:** Bot owner



### Ping Command

- **Description:** Check the bot's latency.
- **Usage:** `/ping`

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/TrapstarJannik/Discord-Slash-Command.git
   cd your directory
   ```

4. Run the bot:
   ```sh
   python main.py
   ```

## Configuration

- The bot's prefix is set to `.` by default. You can change it in the `main.py` file.

## Pictures


![image](https://github.com/TrapstarJannik/images/blob/main/Screenshot_57.png)
![image](https://github.com/TrapstarJannik/images/blob/main/Screenshot_58.png)

