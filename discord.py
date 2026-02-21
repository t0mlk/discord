import discord
from discord.ext import commands, tasks
import random
import os
import asyncio
import datetime
import pytz
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is online!"

def run():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

EPIC_QUOTES = [
    "Ready your blades! The beast awakens in one hour!",
    "The stars align... a dark presence is approaching.",
    "Sharpen your steel, for the hunt begins soon!",
    "The ground trembles. Something ancient stirs below.",
    "Steel yourselves! Destiny calls upon the brave.",
    "A shadow falls over the realm. Who will stand against it?",
    "The whispers in the fog grow louder. Be prepared!",
    "Blood and glory await! The gates shall open in 60 minutes.",
    "Echoes of the past warn of the coming storm!",
    "The fires of war are being kindled. To arms!",
    "The ancient seal is cracking... one hour remains!",
    "Prepare for glory, for the battlefield crimson awaits.",
    "The prophecy unfolds. The titan stirs in sixty minutes.",
    "Gather your allies! The shadows are lengthening.",
    "A cold wind blows from the north. The hunt is near.",
    "The gods watch in silence. Show them your strength!",
    "One hour until the eclipse. Don't lose your soul in the dark.",
    "The dragon's breath warms the air. Arm yourselves!",
    "Legends are born in fire. Your trial starts soon.",
    "The abyss stares back. Ready your hearts for war.",
    "No mercy for the weak! The gates open in one hour.",
    "The silver horn sounds. To arms, warriors of light!",
    "Ancient ruins reveal a terrifying truth... stay alert.",
    "The moon turns red. A night of blood approaches.",
    "Steel and magic! One hour until the grand clash.",
    "Your ancestors guide your blades. Do not fail them.",
    "The mist is rising. The monsters are coming home.",
    "Final preparations! Destiny waits for no one.",
    "The king of shadows has sent his first warning.",
    "Honor or death! Choose your path in sixty minutes.",
    "The desert sands reveal a forgotten tomb.",
    "Ice and frost! The winter king demands a sacrifice.",
    "The volcano rumbles. Nature's wrath is coming.",
    "Shields up! The arrows will rain from the sky.",
    "A hero's journey starts with a single strike. Get ready.",
    "The cathedral bells toll for the fallen. And the living.",
    "The dark ritual is almost complete. Stop it or die.",
    "Beneath the waves, the kraken is moving.",
    "One hour of peace remains. Use it wisely.",
    "The final chapter begins. Are you the author of your victory?"
]

@tasks.loop(seconds=60)
async def automatic_epic_post():
    berlin_tz = pytz.timezone('Europe/Berlin')
    now_berlin = datetime.datetime.now(berlin_tz)
    current_time = now_berlin.strftime("%H:%M")

    TIMES_TO_POST = ["06:00", "14:00", "22:00"]

    if current_time in TIMES_TO_POST:
        CHANNEL_ID = 1472338412613795891
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            quote = random.choice(EPIC_QUOTES)
            await channel.send(f"**[RAID-WARNUNG]** {quote}")
            await asyncio.sleep(61)

@bot.event
async def on_ready():
    if not automatic_epic_post.is_running():
        automatic_epic_post.start()

keep_alive()
token = os.getenv('MTQ3MzA2Mz2NDM0ODA0MTQQQQ.GNon4N.ExhkD2zKaw0dPMhyfzPAs14dKVurIGWXp6s')
if token:
    bot.run(token)