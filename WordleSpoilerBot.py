#!/usr/bin/env python3

from datetime import datetime, time
import discord
from discord.ext import tasks
import requests

# 1. Double check your timezone! 
# If your computer clock says 19:38, make sure you DO NOT have tzinfo=timezone.utc here,
# otherwise it will wait for London time.
LOCAL_TZ = datetime.now().astimezone().tzinfo

POST_TIME = time(hour=0, minute=20, second=0, tzinfo=LOCAL_TZ)

# Make sure this is your exact channel ID (no quotes)
CHANNEL_ID = 1519769041584259134 


class WordleBot(discord.Client):

    def __init__(self):
        super().__init__(intents=discord.Intents.default())

    async def setup_hook(self):
        self.daily_wordle_loop.start()
        print("⏰ Background task loop has been scheduled.")

    async def on_ready(self):
        print(f"✅ Logged in successfully as {self.user.name}")
        print(f"Target execution time is set to: {POST_TIME}")

    @tasks.loop(time=POST_TIME)
    async def daily_wordle_loop(self):
        # FIX 1: Force the loop to wait until Discord completely loads the bot connection
        await self.wait_until_ready()
        
        print(f"⏳ [{datetime.now().strftime('%H:%M:%S')}] Loop triggered! Attempting to send Wordle...")

        # FIX 2: Use fetch_channel() instead of get_channel(). 
        # fetch_channel makes a direct API call to Discord, bypassing empty cache bugs.
        try:
            channel = await self.fetch_channel(CHANNEL_ID)
            print(f"🎯 Successfully connected to channel: #{channel.name}")
        except Exception as e:
            print(f"❌ Error finding channel: {e}")
            return

        # Fetch today's word
        print("🌐 Contacting New York Times API...")
        today = datetime.now().strftime("%Y-%m-%d")
        url = f"https://www.nytimes.com/svc/wordle/v2/{today}.json"
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                word = data["solution"].upper()
                message = f"📅 **Wordle Solution for {today}:** {word}"
                
                # Send message
                await channel.send(message)
                print("🎉 Wordle successfully posted to Discord!")
            else:
                print(f"❌ NYT API returned an error code: {response.status_code}")
        except Exception as e:
            print(f"❌ Network error while fetching Wordle: {e}")


client = WordleBot()
client.run("MTUxOTc2NTY1MDM2MzM4Mzk2MA.GotkMO.R8yxEG9S2HLDqmHHtQ8FMH5hCGwZDEyhdK3_Fg")