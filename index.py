import discord, datetime, random, asyncio
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("봇 실행 준비 완료")
    print(bot.user)
    game = discord.Game("!도움말")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def 연결(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("음성채팅방에 유저가 없습니다.")

@bot.command()
async def 끊기(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send("이미 연결이 끊겨있습니다.")

@bot.event
async def on_message(message):
    if message.content == "!테스트":
        await message.channel.send("ㅇㅋ")
    
    if message.content == "!제작자":
        embed = discord.Embed(colour=discord.Colour.blue(), title="티빈이 봇", description="제작자: 티빈이#0945")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/725881963092770916/824290401862549514/Tbinih3.png")
        await message.channel.send(embed=embed)

    if message.content == "!도움말":
        embed = discord.Embed(colour=discord.Colour.orange(), title="티빈이 봇 명령어")
        embed.add_field(name="!채널메세지 <채널ID> <내용>", value="봇이 <채널ID>에 <내용>을 보냅니다.", inline=False)
        embed.add_field(name="!내 정보", value="내 디스코드 정보를 알 수 있습니다.", inline=False)
        embed.add_field(name="!청소 <숫자>", value="<숫자>만큼 메세지가 지워집니다.", inline=False)
        embed.add_field(name="!초대코드", value="티빈이 봇 초대코드를 보여줍니다.", inline=False)
        embed.add_field(name="!봇 초대", value="서버에 유용한 봇 초대코드를 보여줍니다.", inline=False)
        embed.add_field(name="!타이머 <숫자>", value="<숫자>초 뒤에 메세지가 나타납니다.", inline=False)
        embed.add_field(name="!랜덤숫자", value="1~10까지의 랜덤 숫자가 나옵니다.", inline=False)
        await message.channel.send(embed=embed)

    if message.content == "!봇 초대":
        embed = discord.Embed(colour=discord.Colour.blue(), title="디스코드 봇 모음")
        embed.add_field(name="https://hydra.bot/", value="히드라 봇(음악 봇)을 추가합니다.", inline=False)
        embed.add_field(name="https://mee6.xyz/", value="미육 봇(관리 봇)을 추가합니다.", inline=False)
        embed.add_field(name="https://discord.com/oauth2/authorize?&client_id=218010938807287808&scope=bot+applications.commands&permissions=37014592", value="마냥 봇(미니게임 봇)을 추가합니다.", inline=False)
        await message.channel.send(embed=embed)

    if message.content == "!초대코드":
        embed = discord.Embed(colour=discord.Colour.blue(), title="티빈이 봇 초대코드", description="https://discord.com/oauth2/authorize?client_id=824281720781930537&permissions=8&scope=bot")
        await message.channel.send(embed=embed)

    if message.content.startswith(f"!채널메세지"):
        i = (message.author.guild_permissions.manage_messages)
        if i is True:
            ch = bot.get_channel(int(message.content[7:25]))
            await ch.send(message.content[26:])

        if i is False:
            await message.channel.send("{}, 당신은 이 명령어를 사용할 권한이 없습니다.".format(message.author.mention))

    if message.content == '!내 정보':
        user = message.author
        date= datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(colour=discord.Colour.green(), title="내 정보")
        embed.add_field(name="디스코드 가입일", value=f"{date.year}-{date.month}-{date.day}", inline=False)
        embed.add_field(name="디스코드 닉네임", value=f"서버 닉네임: {user.display_name},\n디스코드 닉네임: {user.name}", inline=False)
        embed.add_field(name="디스코드 아이디", value=f"{user.id}", inline=True)
        await message.channel.send(message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("!타이머"):
        number = int(message.content.split(" ")[1])
        await asyncio.sleep(number)
        await message.channel.send(f"{message.author.mention}, {number}초가 지났어요!")

    if message.content == "!랜덤숫자":
        await message.channel.send(random.randint(1,10))

    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        i = (message.author.guild_permissions.manage_messages)
        if i is True:
            await message.delete()
            await message.channel.purge(limit=number)

        if i is False:
            await message.channel.send("{}, 당신은 이 명령어를 사용할 권한이 없습니다.".format(message.author.mention))

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
