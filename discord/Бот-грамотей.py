import discord
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='#!', intents=intents)


@bot.command(name='help_bot')
async def help_bot(ctx):
    await ctx.send(
        f'Commands:"#!numerals" for agreement with numerals\n'
        f'"#lalive" for define alive or not alive"\n'
        f'"#!noun" for noun case (nom, gen, dat, acc, a bit, lost) and number state(single, plural)\n'
        f'"#"#inf" for infinitive state"#"#morph" for full morphological analysis')


@bot.command(name='numerals')
async def help_bot(ctx):
    await ctx.send(
        f'Commands:"#!numerals" for agreement with numerals\n'
        f'"#lalive" for define alive or not alive"\n'
        f'"#!noun" for noun case (nom, gen, dat, acc, a bit, lost) and number state(single, plural)\n'
        f'"#"#inf" for infinitive state"#"#morph" for full morphological analysis')


bot.run("")
