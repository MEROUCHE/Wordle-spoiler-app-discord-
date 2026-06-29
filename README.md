# WordleSpoilerBot

A lightweight, automated Python Discord bot that fetches the daily New York Times Wordle solution directly from the official API and posts it to a designated Discord channel at a specific time every day. 

To keep the game fun for everyone, the solution is automatically wrapped in Discord spoiler tags (`||WORD||`) so users only see it when they choose to click it.

## Features

* **100% Automated:** Runs on a daily background loop—no user slash commands required.
* **Direct API Integration:** Pulls clean JSON data directly from the New York Times servers instead of using brittle web scraping.
* **Smart Timezone Handling:** Dynamically detects the host machine's local timezone offset to ensure the post drops exactly when you expect it to.
* **Spoiler Protected:** Safeguards the daily answer behind interactive spoiler blocks.

---

## Prerequisites

Before running the bot, ensure you have Python 3.8+ installed along with the required libraries.

```bash
pip install discord.py requests
