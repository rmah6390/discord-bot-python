import os, json, random
from dotenv import load_dotenv
import discord
from discord.ext import commands

DATA_FILE = "todos.json"

def load_todos():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

def save_todos(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print("Logged in as " + str(bot.user))

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def roll(ctx, sides: int = 6):
   if sides < 2:
        await ctx.send("Please pick 2 or more sides (try 6).")
        return
    value = random.randint(1, sides)
    await ctx.send("You rolled: " + str(value))

@bot.command()
async def addtodo(ctx, *, item: str):
    data = load_todos()
    key = str(ctx.guild.id)
    if key not in data:
        data[key] = []
    data[key].append(item)
    save_todos(data)
    await ctx.send("Added: " + item)

@bot.command()
async def listtodos(ctx):
    data = load_todos()
    items = data.get(str(ctx.guild.id), [])
    if len(items) == 0:
        await ctx.send("No todos yet.")
        return
    text = "Your todos:\n"
    i = 1
    for it in items:
        text = text + str(i) + ". " + it + "\n"
        i = i + 1
    await ctx.send(text)

@bot.command()
async def cleartodos(ctx):
    data = load_todos()
    data[str(ctx.guild.id)] = []
    save_todos(data)
    await ctx.send("Cleared todos.")

@bot.command()
async def help(ctx):
    msg = (
        "**Commands**\n"
        "!ping\n!roll [sides]\n!addtodo <text>\n!listtodos\n!cleartodos\n"
    )
    await ctx.send(msg)

if __name__ == "__main__":
    if TOKEN is None or len(TOKEN.strip()) == 0:
        raise RuntimeError("DISCORD_TOKEN missing in .env")
    bot.run(TOKEN)
