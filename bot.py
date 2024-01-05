import discord
import asyncio
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

class Echo(discord.Client):

    def __init__(self, *args, **kwargs):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True

        super().__init__(intents=intents, *args, **kwargs)
        self.channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        await self.announce_gbm()

    async def on_member_join(self, member):
        channel_id_str = os.getenv('DISCORD_CHANNEL_ID')
        channel_id = int(channel_id_str) if channel_id_str else None

        if channel_id:
            channel = self.get_channel(channel_id)
            if channel:
                welcome_message = (
                    f"Welcome to the official discord server of Drexel AI, {member.mention}! "
                    "Feel free to introduce yourself. If you are interested in being part of any of our current projects, "
                    "you can type `projects` to get more information."
                )
                await channel.send(welcome_message)

    async def announce_gbm(self):
        channel = self.get_channel(self.channel_id)

        while True:
            now = datetime.now()
            day_of_week = now.weekday()

            if day_of_week == 2:  # Wednesday
                # First announcement at 10 AM
                announce_time = now.replace(hour=10, minute=0, second=0, microsecond=0)
                time_difference = announce_time - now

                await asyncio.sleep(time_difference.total_seconds())

                try:
                    await channel.send("@everyone Hey everyone! Our weekly GBM will be today at 5:00 PM. Don't miss it!")
                except:
                    pass

                # Second announcement at 4.50 PM
                announce_time = now.replace(hour=16, minute=50, second=0, microsecond=0)
                time_difference = announce_time - now

                await asyncio.sleep(time_difference.total_seconds())

                try:
                    await channel.send("@everyone Hey everyone! Our weekly GBM will be in 10 minutes. Don't miss it!")
                except:
                    pass

            # Sleep for a week before checking again
            await asyncio.sleep(60 * 60 * 24 * 7)

    async def on_message(self, message):
        content = message.content.lower()

        if message.author == self.user:
            return

        if any(prefix in content for prefix in ['$hi', '$hello']):
            await message.channel.send("Hello")

        if content.startswith('$projects'):
            
            project_info = "We have various projects this quarter"
            await message.channel.send(project_info)



