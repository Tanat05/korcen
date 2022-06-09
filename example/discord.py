#discord.py
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
    print(korcen.check(message.content))
    if korcen.check(message.content):
        await message.delete()
        embed = nextcord.Embed(title = "메세지 삭제함", description = "", color=0xFF2424)
        embed.set_footer(text = "디스코드 TNS 봇")
        await message.channel.send(embed=embed)
    
        
        
bot.run(TOKEN)


#disnake(추천)
import disnake
from disnake.ext import commands, tasks
from korcen import korcen

korcen = korcen.korcen()

intents = disnake.Intents.default()
intents.message_content = True

bot = commands.AutoShardedBot(shard_count=3, command_prefix=commands.when_mentioned, intents=intents)


@bot.event
async def on_ready():
    print(f"[!] 다음으로 로그인에 성공했습니다.")
    print(f"[!] 다음 : {bot.user.name}")
    print(f"[!] 다음 : {bot.user.id}")
    bot.remove_command("help")


@bot.event
async def on_message(message):
    text = message.content
    사유 = ""
    검열 = 0
    if korcen.general(text):
        사유 += "욕설\n"
        await message.delete()
        검열 = 1
    if korcen.minor(text):
        사유 += "사소한 욕설\n"
        if 검열 == 0:
            await message.delete()
        검열 = 1
    if korcen.sexual(text):
        사유 += "섹드립\n"
        if 검열 == 0:
            await message.delete()
        검열 = 1
    if korcen.belittle(text):
        사유 += "비하\n"
        if 검열 == 0:
            await message.delete()
        검열 = 1
    if korcen.race(text):
        사유 += "인종 차별\n"
        if 검열 == 0:
            await message.delete()
        검열 = 1
    if korcen.parent(text):
        사유 += "패드립\n"
        if 검열 == 0:
            await message.delete()
        검열 = 1
    if korcen.foreign(text):
        사유 += "외국 욕설\n"
        if 검열 == 0:
            await message.delete()
        검열 = 1
    if korcen.special(text):
        사유 += "특수(이모지 등)\n"
        if 검열 == 0:
            await message.delete()
        검열 = 1
    if korcen.politics(text):
        사유 += "정치\n"
        if 검열 == 0:
            await message.delete()
        검열 = 1
    if 검열 == 1:
        embed = disnake.Embed(
            title=f"{message.author}님의 채팅을 검열했습니다.", description=f"메시지가 검열이 되었습니다.", color=0xFF2424)
        embed.add_field(
            name="검열된 메세지", value=f"```{message.content}```", inline=False)
        embed.add_field(
            name="검열 사유", value=f"`{사유}`", inline=False)
        embed.set_footer(text = "디스코드 TNS 봇")
        await message.channel.send(embed=embed)


bot.run("토큰을 넣으세요")
