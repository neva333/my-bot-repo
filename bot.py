import discord
from discord.ext import commands
import re

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

# チャンネルIDを設定
source_channel_id = 123456789012345678  # URLを検出するチャンネルのID
destination_channel_id = 987654321098765432  # URLを転送するチャンネルのID

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.channel.id == source_channel_id:
        urls = re.findall(r'(https?://\S+)', message.content)
        if urls:
            destination_channel = bot.get_channel(destination_channel_id)
            await destination_channel.send(f'URL detected: {", ".join(urls)}')
            new_content = re.sub(r'(https?://\S+)', '', message.content).strip()
            await message.edit(content=new_content)
    await bot.process_commands(message)

bot.run('YOUR_BOT_TOKEN')
