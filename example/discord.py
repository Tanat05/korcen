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
    if korcen.check(message.content):
        await message.delete()
        embed = discord.Embed(title = "메세지 삭제함", description = "")
        embed.set_footer(text = "디스코드 TNS 봇")
    
        
        
bot.run(TOKEN)
