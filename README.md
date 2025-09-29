![Python](https://img.shields.io/badge/Python-3.x-blue)
![discord.py](https://img.shields.io/badge/discord.py-2.x-informational)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

# Discord Bot (Python)

**Commands**
- `!ping` → Pong!
- `!roll [sides]` → roll a die (default 6)
- `!addtodo <text>` / `!listtodos` / `!cleartodos`

I built this to practice Python events. I also learned to keep secrets in \.env`.`

## Setup
1) Create a bot in Discord Developer Portal and enable **Message Content Intent**.
2) Create `.env` from `.env.example` with your token (do not commit `.env`).
3) python -m pip install -r requirements.txt
4) python bot.py

## What I learned
- Enabling intents or commands won’t work
- Loading secrets from `.env` (dotenv)
- Simple command handling + JSON storage

## How it works
- Commands handled by `discord.ext.commands.Bot` with prefix `!`.
- Per-server TODOs saved in `todos.json` (keyed by guild ID, ignored by Git).
- Secrets come from `.env` via `python-dotenv`.

## Project structure
.
├─ bot.py            # commands + JSON TODO storage
├─ requirements.txt  # deps
├─ .env.example      # token template
└─ LICENSE

## Troubleshooting
- `KeyError: DISCORD_TOKEN` → create `.env` from `.env.example` and paste your token.
- Bot doesn’t respond → enable **Message Content Intent** in the Developer Portal.
- Windows: use `python -m pip install -r requirements.txt` then `python bot.py`.

