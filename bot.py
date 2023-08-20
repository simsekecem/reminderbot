import discord
import asyncio
import os

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

    # Bu kısım botun belirli bir zaman aralığında çalışmasını sağlar
    while True:
        channel_id = int(os.environ.get('CHANNEL_ID'))  # Kanal ID'sini environment değişkeninden al
        await client.wait_until_ready()
        channel = client.get_channel(channel_id)
        await channel.send("@everyone 🆘 Hourly reminder 🆘 Increase the gap! https://shiningawards.com/best-kpop-rapper-2023/")

        # 1 saat beklemek için
        await asyncio.sleep(3600)

token = os.environ.get('DISCORD_TOKEN')  # Token'ı environment değişkeninden al
client.run(token)
