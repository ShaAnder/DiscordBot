### --- IMPORTS --- ###

#main imports
from dotenv import load_dotenv
import os
import nextcord
from nextcord.ext import commands
import logging
#importing classes

### --- LOGGER --- ###

#setting up a logger, will output the logs from nextcord to a file for viewing instead of leaving them in the console
logger = logging.getLogger('nextcord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

### --- ENV SETUP --- ###

#we want to setup dotenv so we can call our env variables
load_dotenv()

#define our API variable
DISCORD_API = os.getenv('DISC_TOKEN', default=None)

### --- BOT SETUP --- ###

#we want to setup our bots intents (discord mandatory, or else it won't catch commands)
intents = nextcord.Intents.default()
intents.message_content = True

#define our bot variable + the prefix to use, feeding intents in to run bot)
bot = commands.Bot(command_prefix="s!", intents=intents) 

#bot ready up message
@bot.event
async def on_ready():
    print("Spooky bot is good to go!")

### --- COGS --- ###

#cog setup, it will look in cogs directory for python files and load them with the extension sliced off and then feed it into the extensions 
for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.{fn[:-3]}")

# allows us to unload and reload as needed and in realtime, updated a file, just reload, buggy module? just unload
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send("Loaded Cog!")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send("Unloaded Cog!")

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")
    await ctx.send("Reloaded Cog!")


### --- RUN THE BOT --- ###

#run the bot
bot.run(DISCORD_API)

