from bot import Echo
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = Echo()

bot.run(TOKEN)