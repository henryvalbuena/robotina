import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from bot_commands import COGS
from logger import logging


logger = logging.getLogger("robotina.start")


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents(messages=True, guilds=True)
bot = commands.Bot(command_prefix='!', intents=intents)

for cog in COGS:
    bot.add_cog(cog(bot))


@bot.event
async def on_ready():
    logger.info("Robonita is ready")


bot.run(TOKEN)
