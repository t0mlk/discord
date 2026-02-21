import discord
from discord.ext import commands, tasks
import random
import os
import datetime
import pytz
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is online!"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

EPIC_QUOTES = [
    "Ready your blades! The beast awakens in 1hr!",
    "The stars align... a dark presence is approaching in 60 minutes.",
    "Sharpen your steel, for the hunt begins in 1hr!",
    "The ground trembles. Something ancient stirs below. 60 minutes remain.",
    "Steel yourselves! Destiny calls upon the brave in 1hr.",
    "A shadow falls over the realm. The confrontation begins in 60 minutes.",
    "The whispers in the fog grow louder. The boss arrives in 1hr.",
    "Blood and glory await! The gates shall open in 60 minutes.",
    "Echoes of the past warn of the coming storm in 1hr!",
    "The fires of war are being kindled. Battle commences in 60 minutes.",
    "The ancient seal is cracking... only 1hr remains!",
    "Prepare for glory, for the battlefield crimson awaits in 60 minutes.",
    "The prophecy unfolds. The titan stirs in exactly 1hr.",
    "Gather your allies! The shadows are lengthening. Arrival in 60 minutes.",
    "A cold wind blows from the north. The boss emerges in 1hr.",
    "The gods watch in silence. The trial starts in 60 minutes.",
    "1hr until the eclipse. Don't lose your soul in the dark.",
    "The dragon's breath warms the air. Be ready in 60 minutes.",
    "Legends are born in fire. Your challenge begins in 1hr.",
    "The abyss stares back. Ready your hearts for war in 60 minutes.",
    "No mercy for the weak! The final stand is only 1hr away.",
    "The silver horn sounds. The boss appears in 60 minutes!",
    "The earth shall weep. The nightmare begins in 1hr.",
    "To arms, warriors of light! The darkness descends in 60 minutes.",
    "Fate is a cruel mistress. Face her in exactly 1hr.",
    "The kingdom's survival hangs by a thread. The threat arrives in 60 minutes.",
    "Feel the static in the air? The storm peaks in 1hr.",
    "Ancient eyes are opening. The beast rises in 60 minutes.",
    "The countdown to chaos has begun. 1hr left!",
    "Steel your nerves! The behemoth will be here in 60 minutes.",
    "The grand duel is set. The arena opens in 1hr.",
    "Vengeance has a name, and it arrives in 60 minutes.",
    "The gates of hell are creaking. 1hr until the breach.",
    "Rally to the banners! The siege begins in 60 minutes.",
    "The sky turns to blood. The master appears in 1hr.",
    "Valor will be tested. The reckoning is 60 minutes away.",
    "The chains are breaking. The prisoner escapes in 1hr.",
    "A legendary foe draws near. Prepare for battle in 60 minutes.",
    "The drums of war echo in the distance. Arrival in 1hr.",
    "May the gods have mercy. The boss awakens in 60 minutes."
]


@tasks.loop(minutes=10)
async def check_boss_time():
    berlin_tz = pytz.timezone('Europe/Berlin')
    now = datetime.datetime.now(berlin_tz)
    
    if now.hour in [6, 14, 22] and now.minute < 10:
        
        channel_id = 1472338412613795891
        role_id = 1472335046244307190
        
        channel = bot.get_channel(channel_id)
        if channel:
            quote = random.choice(EPIC_QUOTES)
            await channel.send(f"⚔️ <@&{role_id}> **BOSS ALERT:** {quote}")

@bot.event
async def on_ready():
    print(f'✅ Bot eingeloggt als {bot.user.name}')
    if not check_boss_time.is_running():
        check_boss_time.start()

if __name__ == "__main__":
    keep_alive()
    token = os.getenv('DISCORD_TOKEN')
    if token:
        bot.run(token)
    else:
        print("❌ FEHLER: DISCORD_TOKEN nicht in Render-Umgebungsvariablen gefunden!")
