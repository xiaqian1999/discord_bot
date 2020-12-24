#For this level of bot, we want to work with command handler and using weather API to retrieve the information

import discord
from discord.ext import tasks, commands #this import is needed to create commands
from pyowm import OWM #this import is needed to connect to weather API

#connection with token
with open("./TOKEN", 'r') as f:
    TOKEN = f.read().strip()

owm = OWM('09bc32477d66785773cfad8e2c5c04a2')
mgr = owm.weather_manager()

bot = commands.Bot(command_prefix = '-')

@bot.event
async def on_ready():
    print('logged on as {0}!'.format(bot))


@bot.command()
async def weather(ctx, *, arg): #arg is the city name
    place = str(arg)
    observation = mgr.weather_at_place(place)
    w = observation.weather
    await ctx.send('In {0}, now: {1} celsius'.format(place, str(w.temperature('celsius')["temp"])))


bot.run(TOKEN)
