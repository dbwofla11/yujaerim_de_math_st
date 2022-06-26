from token1 import token
import discord , asyncio 
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'{client.user} online!')

@client.command()
async def 안녕(ms):
    await ms.send("으으애으애ㅡ으응으응ㅇ애")

async def ping(ms):
    await ms.send("pong")





client.run(token) # 여기서 토큰을 받아 연결 
