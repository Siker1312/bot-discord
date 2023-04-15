#from settings import settings
import discord
from discord.ext import commands
from bot_logic import *

import random
# import * - это тоже самое, что перечислить все файлы
#from bot_logic import *

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='$', intents=intents)

total=0
    
# Когда бот будет готов, он напишет в консоли свое название!
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def smile(ctx):
    await ctx.send(gen_emodji())

@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def password(ctx, count = 10):
    await ctx.send(gen_pass(count))

@bot.command()
async def help_1(ctx):
    await ctx.send(gen_help())

@bot.command()
async def blackjack(ctx,flag = "yes"):
    global total
    if flag == "yes":
        total += random.randint(1,11)
        await ctx.send(f"Ваш счёт {total}")
        if total >=21:
            await ctx.send("Вы проиграли")
            total=0
        else:
            await ctx.send("Если хотите продолжин введите - $blackjack yes, если остановиться $blackjack no")
    if flag == "no":
        if total >=21:
            await ctx.send("Вы проиграли")
            total=0
        else:
            await ctx.send("Вы выиграли!")
            total=0

bot.run("MTA5MjQ2MTU5NDcyNzk2MDY2Nw.GBsjb3.w95sQEb7PoOfFBuG5zke4U0JLFy2YVUsx4LjOY")



