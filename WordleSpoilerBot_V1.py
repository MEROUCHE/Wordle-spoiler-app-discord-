#!/usr/bin/env python3

from datetime import datetime
import discord
from discord import app_commands
import requests

# 1. Setup the Discord Client and Command Tree (for Slash Commands)
class WordleBot(discord.Client):

    def __init__(self):
        # Default intents are fine for a basic slash command bot
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # This syncs your commands globally with Discord's servers
        await self.tree.sync()


client = WordleBot()


# 2. Event that fires when the bot successfully logs in
@client.event
async def on_ready():
    print(f"Logged in successfully as {client.user.name}")


# 3. Create the /wordle Slash Command
@client.tree.command(name="wordle", description="Get today's Wordle solution")
async def wordle(interaction: discord.Interaction):
    # --- Your original logic goes here ---
    today = datetime.now().strftime("%Y-%m-%d")
    url = f"https://www.nytimes.com/svc/wordle/v2/{today}.json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        word = data["solution"].upper()
        message = f"Today's Wordle solution ({today}) is: **{word}**"
    else:
        message = "⚠️ Failed to fetch today's data from the NYT servers."

    # --- Discord specific response ---
    # Setting ephemeral=True makes the response invisible to everyone else in the server.
    # This prevents you from spoiling the answer for your friends!
    await interaction.response.send_message(message)


# 4. Run the bot using the token you got from the Developer Portal
client.run("MTUxOTc2NTY1MDM2MzM4Mzk2MA.GotkMO.R8yxEG9S2HLDqmHHtQ8FMH5hCGwZDEyhdK3_Fg")