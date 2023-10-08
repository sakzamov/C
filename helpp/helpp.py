import discord
from discord.ext import commands
import random
import tjr
import os
import requests
import time
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.command()
async def mem(ctx):
    ls = os.listdir('images')
    rand_img = random.choice(ls)
    with open('images/' + rand_img, 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
@bot.command()
async def meme(ctx):
    l2 = os.listdir('meme')
    rand_im = random.choice(l2)
    with open('meme/' + rand_im, 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
        await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send(f"he" * count_heh)

@bot.command()
async def bye(ctx):
        await ctx.send(f"Поки споки")

@bot.command()
async def password(ctx, count=8):
    await ctx.send(f'Ваш пароль - {gen_pass(count)} ')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def helpp(ctx):
    hl = os.listdir('help')
    for i in range(1, 8):
        with open('help/help' + str(i) + '.jpg', 'rb') as f:
            # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
            picture = discord.File(f)
        # Можем передавать файл как параметр!
        await ctx.send(file=picture)
        time.sleep(5)

bot.run(tjr.TOKEN)
