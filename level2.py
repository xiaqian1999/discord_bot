#For this level of bot, we want to work with random returns from the bot as user call the function

import random
from discord.ext.commands import Bot

with open("./TOKEN", 'r') as f:
    TOKEN = f.read().strip()

BOT_PREFIX = ("?", "!")

client = Bot(command_prefix=BOT_PREFIX)

@client.command()
async def eight_ball(ctx):
    possible_reponses = [
        'yeah',
        'maybe',
        'yeahmaybe',
        'definitely',
        'it is quite possible',
    ]
    await ctx.send(random.choice(possible_reponses))


client.run(TOKEN)
