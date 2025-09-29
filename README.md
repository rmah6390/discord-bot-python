# Discord Bot (Python)

Small practice bot while learning Python + Discord API. Commands:
- `!ping` → "Pong!"
- `!roll [sides]` → roll a die (default 6)
- `!addtodo <text>` / `!listtodos` / `!cleartodos` → JSON todos per server

## Setup
1) Create a bot in Discord Developer Portal and enable **Message Content Intent**.
2) Create `.env` from `.env.example` with your token (do not commit `.env`).
3) `pip install -r requirements.txt`
4) `python bot.py`

## What I learned
- Enabling intents or commands won’t work
- Loading secrets from `.env` (dotenv)
- Simple command handling + JSON storage

## Next steps
- Add `!remindme`
- Switch JSON → SQLite if list grows
