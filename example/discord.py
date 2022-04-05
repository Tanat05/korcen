import discord
from discord.ext import commads
from korcen import check

TOKEN = "봇 토큰 넣기"
bot = commands.Bot(command_prefix = "!")


@bot.event
async def on_ready():
    print(f"[!] 다음으로 로그인에 성공했습니다.")
    print(f"[!] 다음 : {bot.user.name}")
    print(f"[!] 다음 : {bot.user.id}")


@bot.event
async def on_message(message):
    a = check.check(message.content)
    if a != 0:
        await message.delete()
    await bot.process_commads(msg)
    
    
@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency * 1000)}ms")
        
        
bot.run(TOKEN)
