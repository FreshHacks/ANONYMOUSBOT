import discord
import asyncio
from discord import *
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix = '!')

@Bot.event
async def on_ready():
	await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="!help | By Kostya#3533"))
	print("Logged in!")
#@Bot.event
#async def on_message(message):
#	print('MSGLog: {0.author} => {0.content}'.format(message))

@Bot.command(pass_context = True)
async def hello(ctx, *args):
	text = ''
	for item in args:
		text = text + item + ' '
	emb = discord.Embed(title = "test title", colour = 0x7800c2)
	emb.add_field(name = "WARNING!", value = "@everyone")
	emb.add_field(name = ":", value = text)
	if not args:
		await ctx.send('Необходимо ввести текст сообщения')
	await ctx.send(embed = emb) 

@Bot.command(pass_context = True)
async def info(ctx, user: discord.User):
	await ctx.send()

@Bot.command()
async def say(ctx, channel : discord.TextChannel, *args):
	await ctx.message.delete()
	text = ''
	if not channel:
		await ctx.send('Введите канал, в который вы хотите отправить сообщение')
		return
	if not args:
		await ctx.send('Необходимо ввести текст сообщения')
	for item in args:
		text = text + item + ' '
	await channel.send(text)

token = os.environ.get('BOT_TOKEN')