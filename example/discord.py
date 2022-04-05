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
    #비속어 종류에 따라 1~9 없다면 0
        await message.delete()
        #메세지 삭제
        embed = discord.Embed(title = "메세지 삭제함", description = "")
        embed.set_footer(text = "디스코드 TNS 봇")
        #모듈 사용 여부 표기하기
        #봇 소개,도움,검열 메세지 등 유저가 볼수있는 원하는 곳에 모듈 사용 표기
    await bot.process_commads(msg)
    
    
@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency * 1000)}ms")
        
        
bot.run(TOKEN)
