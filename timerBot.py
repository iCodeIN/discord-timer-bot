import subprocess
import os
proc=subprocess.Popen('apt-get install -y python3-pip', shell=True, stdin=None, stdout=open(os.devnull,"wb"), executable="/bin/bash")
proc.wait()
proc=subprocess.Popen('apt-get install -y ffmpeg', shell=True, stdin=None, stdout=open(os.devnull,"wb"), executable="/bin/bash")
proc.wait()
os.system('pip install discord')
os.system('pip install PyNaCl')
os.system('pip install -U discord.py[voice]')
import discord
from discord import FFmpegPCMAudio
import time
import asyncio
from datetime import datetime
import nacl

token="REDACTED"
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
voice_clients = {}

os.system('pip install discord')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(msg):
    if msg.content.startswith('.timer'):
        FFMPEG_OPTIONS={'options': '-vn'}
        seconds=0
        number=0
        timeType=''
        try:
            number=(float((msg.content).split(" ")[1]))
        except ValueError:
            await msg.channel.send("🤨 That isn't a number.")
            handle_exception()
        try:
            timeType=(str((msg.content).split(" ")[2]))
            if (timeType == "seconds") or (timeType == "secs") or (timeType == "second"):
                seconds=number
                #print("Time type selected: "+str(timeType))
            elif (timeType == "minutes") or (timeType == "mins") or (timeType == "minute"):
                seconds=number*60
            else:
                await msg.channel.send("🤨 Try again [seconds or minutes].")
                handle_exception()
                seconds=0
        except:
            await msg.channel.send("🤨 Try again [seconds or minutes].")
            handle_exception()
            seconds=0
        print("["+str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))+"] "+str(msg.author)+" -> "+str(seconds)+" seconds")
        try:
            if seconds < 0:
                await msg.channel.send('🤨 No negative numbers.')
                handle_exception()
            elif seconds > 1200:
                await msg.channel.send('🤨 That is too long! (Less than 20 minutes).')
                handle_exception()
            else:
                message=await msg.channel.send(seconds)
                while seconds != 0:
                    seconds -= 1
                    await message.edit(content=("⏰ "+str(seconds)))
                    await asyncio.sleep(1)
                await message.edit(content="👍 Time's up!")
                global voice
                channel=client.get_channel("REDACTED")
                voice=await channel.connect()
                source=FFmpegPCMAudio('REDACTED')
                player=voice.play(source)
                while voice.is_playing():
                    continue
                await voice.disconnect()
        except:
            await msg.channel.send("🤨 Issue.")
            handle_exception()
    if msg.content.startswith('.stop'):
        await msg.channel.send("👋 Bye.")
        try:
            await voice.disconnect()
        except:
            handle_exception()
    if msg.content.startswith('.help'):
        await msg.channel.send("📚 'About Me' card section has command list")
def handle_exception():
    pass
client.run(token)
