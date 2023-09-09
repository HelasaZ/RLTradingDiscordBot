from main import Read
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
token = "###### TOKEN HERE ######"

mtext = Read().get_mtext()
itext = Read().get_itext()
otext = Read().get_otext()
ztext = Read().get_ztext()
ftext = Read().get_ftext()


@bot.event
async def on_ready():
    print("Le bot est prêt")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Searching prices..."))


@bot.command()
async def test(ctx):
    await ctx.send("test")


@bot.command()
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

    for each_message in messages:
        await each_message.delete()


@bot.command()
async def fennec(ctx):
    await ctx.send(ftext)


@bot.command()
async def mainframe(ctx):
    await ctx.send(mtext)


@bot.command()
async def interstellar(ctx):
    await ctx.send(itext)


@bot.command()
async def zomba(ctx):
    await ctx.send(ztext)


@bot.command()
async def octane(ctx):
    await ctx.send(otext)


bot.run(token)
