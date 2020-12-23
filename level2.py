import random
from discord.ext.commands import Bot

TOKEN = ''

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
