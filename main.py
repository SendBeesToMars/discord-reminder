import bs4, requests, threading
from discord import guild
from discord.ext import commands
import discord
import os

res = requests.get("https://www.overclockers.co.uk/amd-ryzen-9-5900x-twelve-core-4.8ghz-socket-am4-processor-retail-cp-3ca-am.html")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
soup = soup.select("#comingsoonDetails")

def check_website():
    res = requests.get("https://www.overclockers.co.uk/amd-ryzen-9-5900x-twelve-core-4.8ghz-socket-am4-processor-retail-cp-3ca-am.html")
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    soup = soup.select("#comingsoonDetails")
    
    threading.Timer(300, check_website).start()
    
    if soup:
        return False
    else:
        return True


TOKEN = os.environ.get('DOOTDOOT_TOKEN')

bot = commands.Bot(command_prefix=",")

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command(name="dm")
async def dm(ctx, user: discord.Member):
    if check_website():
        await user.send("cpu is available :)")
    else:
        print("checking...")

bot.run(TOKEN)

