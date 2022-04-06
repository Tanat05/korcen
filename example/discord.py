import discord
from discord.ext import commads
from korcen import korcen

TOKEN = "봇 토큰 넣기"
bot = commands.Bot(command_prefix = "!")
korcen = korcen.korcen()


@bot.event
async def on_ready():
    print(f"[!] 다음으로 로그인에 성공했습니다.")
    print(f"[!] 다음 : {bot.user.name}")
    print(f"[!] 다음 : {bot.user.id}")


@bot.event
async def on_message(message):
    a = korcen.check(message.content)
    if a == True:
    #비속어가 있다면 True 없다면 False
        await message.delete()
        #메세지 삭제
        embed = discord.Embed(title = "메세지 삭제함", description = "")
        embed.set_footer(text = "디스코드 TNS 봇")
        #모듈 사용 여부 표기하기
        #봇 소개,도움,검열 메세지 등 유저가 볼수있는 곳중 원하는 곳에 모듈 사용 표기
    await bot.process_commads(msg)
    
        
        
bot.run(TOKEN)
