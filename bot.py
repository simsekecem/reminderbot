import discord
import asyncio

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

    # Bu kısım botun belirli bir zaman aralığında çalışmasını sağlar
    while True:
        channel = client.get_channel(1123444669708238900)  # Kanal ID'sini buraya girin
        await channel.send("@everyone 🆘 Hourly reminder 🆘 Increase the gap! https://shiningawards.com/best-kpop-rapper-2023/")

        # 1 saat beklemek için
        await asyncio.sleep(3600)


client.run('MTE0Mjg1NTQxOTg1Nzk5Mzc5MA.GtHmOr.h-qsSLMW9X3jV_Cqi2ZLilhJuRGNNvizzJmtvg')
