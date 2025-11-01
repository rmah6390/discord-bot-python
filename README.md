![Python](https://img.shields.io/badge/Python-3.x-blue)
![discord.py](https://img.shields.io/badge/discord.py-2.x-informational)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

[Invite RidhaBot](https://discord.com/oauth2/authorize?client_id=1422055610240991232&scope=bot%20applications.commands&permissions=3072)


# Discord Bot (Python)

Tiny bot built with `discord.py` to practice event-driven Python and keeping secrets in `.env`.

## Commands

* `!ping` → Pong
* `!roll [sides]` → roll a die (default 6)
* `!addtodo <text>` / `!listtodos` / `!cleartodos` → per-server TODOs

## Setup

1. Create a bot in the **Discord Developer Portal** and enable **Message Content Intent**.
2. In the repo:

   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # macOS/Linux: source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Copy `.env.example` → `.env`, paste your token (`DISCORD_TOKEN`), or set it as an env var.
4. Run:

   ```bash
   python bot.py
   ```

## What I learned

* Enabling required intents (or commands won’t work)
* Loading secrets from `.env` (dotenv)
* Simple command handling + JSON storage

## How it works

* Commands handled by `discord.ext.commands.Bot` with prefix `!`
* Per-server TODOs saved in `todos.json` (keyed by guild ID, gitignored)
* Token loaded from `.env` via `python-dotenv`

## Project structure

```
.
├─ bot.py                # commands + JSON TODO storage
├─ requirements.txt      # deps
├─ .env.example          # token template
└─ LICENSE
```

## Troubleshooting

* `KeyError: DISCORD_TOKEN` → create `.env` from `.env.example` or set the env var
* No response → turn **Message Content Intent** ON in the portal and restart the bot
* Windows install issues → `python -m pip install -r requirements.txt` then `python bot.py`

## License

MIT — see `LICENSE`.

