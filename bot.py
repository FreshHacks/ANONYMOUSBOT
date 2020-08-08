import discord
import datetime
import asyncio
import requests
from datetime import timedelta
from discord.ext import commands


client = commands.Bot(command_prefix = '/', self_bot=True) # Префикс бота


@client.event
async def on_ready():
	print('Bot Loaded!')


@client.command()
async def stream(ctx, *, text):
	activity = discord.Streaming(name=text, url='https://twitch.tv/olbaeb')
	await client.change_presence(status=discord.Status.online, activity=activity)
	await ctx.message.delete()

@client.command()
async def play(ctx, *, text):
	activity = discord.Game(name=text, type = 3)
	await client.change_presence(status=discord.Status.online, activity=activity)
	await ctx.message.delete()

@client.command()
async def watch(ctx, *, text):
	activity = discord.Activity(type=discord.ActivityType.watching, name=text)
	await client.change_presence(activity=activity)
	await ctx.message.delete()

@client.command()
async def listen(ctx, *, text):
	activity = discord.Activity(type=discord.ActivityType.listening, name=text)
	await client.change_presence(activity=activity)
	await ctx.message.delete()

#Информация об пользователе
@client.command(pass_context= True)
async def info(ctx, user: discord.Member):
	emb = discord.Embed(title= "Информация об {}".format(user.name), colour= 0x63009c)
	emb.add_field(name= 'Имя', value= user.name)
	emb.add_field(name= 'Присоединился', value= user.joined_at)
	emb.add_field(name= 'Айди', value= user.id)
	emb.set_thumbnail(url= user.avatar_url)
	emb.set_author(name= client.user.name, url= "https://discord.com/api/oauth2/authorize?client_id=725379044845027329&permissions=8&scope=bot")
	emb.set_footer(text= "Вызвано: {}".format(user.name), icon_url= user.avatar_url)
	await ctx.send(embed= emb)
	await ctx.message.delete()

@client.command() 
async def stat(ctx, channel: discord.TextChannel = None):
    if not channel: #проверяем ввели ли канал
        channel = ctx.channel
        text = 'в данном канале'
    else:
        text = f'в #{channel.name}'
    await ctx.send(f"{ctx.author.mention}, я начинаю вычисления, подождите немного...") #отправляем сообщение о начале отсчёта
    counter = 0
    yesterday = datetime.datetime.today() - timedelta(days = 1)
    #начинаем считать сообщения
    async for message in channel.history(limit=None, after=yesterday):
        counter += 1
    counter2 = 0
    weekago = datetime.datetime.today() - timedelta(weeks = 1)
    async for message in channel.history(limit=None, after=weekago):
        counter2 += 1
    counter3 = 0
    monthago = datetime.datetime.today() - timedelta(weeks = 4)
    async for message in channel.history(limit=None, after=monthago):
        counter3 += 1
    embed = discord.Embed(title = f'Статиститка сообщений {text}', colour= 0x63009c) #создаём embed-сообщение о подсчётах 
    embed.add_field(name = 'За сегодня', value = f'{counter}', inline = False) #добавляем поле "За сегодня"
    embed.add_field(name = 'За неделю', value = f'{counter2}', inline = False) #добавляем поле "За неделю" 
    embed.add_field(name = 'За месяц', value = f'{counter3}', inline = False) #добавляем поле "За месяц" 
    await ctx.send(f'{ctx.author.mention}', embed = embed) #вывод сообщения с информацией о подсчётах

#Инфо Серв
@client.command()
async def serverinfo(ctx):
	channels = len(ctx.guild.channels)
	text_channels = len(ctx.guild.text_channels)
	voice_channels = len(ctx.guild.voice_channels)
	categories = len(ctx.guild.categories)
	members = len(ctx.guild.members)
	embed = discord.Embed(title = 'Информация о сервере:', description = f'Название сервера: ``{ctx.guild.name}``\nАйди сервера: ``{ctx.guild.id}``\nВсего участников: ``{members}``\nВсего каналов и категорий: ``{channels}``\nТекстовые каналы: ``{text_channels}``\nГолосовые каналы: ``{voice_channels}``\nКатегорий: ``{categories}``', colour= 0x63009c)
	await ctx.send(embed = embed)

@client.command(aliases=['bitcoin'])
async def btc(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`', colour= 0x63009c)
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)

@client.command()
async def fox(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Рандомное фото лисы", color=0x63009c)
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image']) 

@client.command()
async def duck(ctx):
	await ctx.message.delete()
	r = requests.get('https://random-d.uk/api/random').json()
	em = discord.Embed(title="Рандомное фото или гифка гуся", color=0x63009c)
	em.set_image(url=r["url"])
	try:
		await ctx.send(embed=em)
	except:
		await ctx.send(r['url'])

@client.command()
async def дошик(ctx):
	await ctx.message.delete()
	emb = discord.Embed(title="Вы заварили Ролтон? Отличный выбор!", description="\n \n У вас получилось:", color=0x63009c)
	emb.set_author(name='Ролтон', icon_url='https://cdn140.picsart.com/261815732025212.png?type=webp&to=min&r=640')
	emb.set_image(url = 'https://pngimg.com/uploads/noodle/noodle_PNG59.png')
	embed = discord.Embed(title="Инструкция", description="1. Откройте пачку ароматного Ролтона\n \n 2. Высыпите содержимое в тарелку \n \n 3. Залейте Ролтон кипятком \n \n 4. Накройте крышкой и подождите 4-5 минут \n \n 5. Наслаждайтесь вкусом вашего Ролтона", color=0x63009c)
	embed.set_author(name='Ролтон', icon_url='https://cdn140.picsart.com/261815732025212.png?type=webp&to=min&r=640')
	await ctx.send(embed = embed)
	await ctx.send(embed = emb)

@client.command()
async def spam_ls(ctx, *, args):
	await ctx.message.delete()
	for member in ctx.guild.members:
		try:
			await member.send(args)
		except:
			continue

token = os.environ.get('BOT_TOKEN')
client.run(str(token), bot=False)
