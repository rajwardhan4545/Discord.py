import discord
from discord.ext import commands
from api import apikey,apij
from discord import FFmpegPCMAudio
from discord import Member
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions
import json
import asyncio
import openai
from discord import File
import time






intents = discord.Intents.all()
client = commands.Bot(command_prefix='&',intents=intents)

queues = {}

def check_queue(ctx,id):
    if queues[id] != []:
        voice = ctx.guild.voice_client
        source = queues[id].pop(0)
        player = voice.play(source)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.CustomActivity(name='Working for lucifer_3456...' ,emoji='🖥️'))
    print("bot is ready")
    print("-----------------------------------")


@client.command()
async def hello(ctx):
    await ctx.send("Hello , i am lucifers bot")

@client.command()
async def supporter(ctx):
    await ctx.send("if you want pic perms in server you have to put 'discord.gg/underrealm' in ur bio or status (u will get @supporters role and icon("
"<:zzz_Venti_Sip:1172810607507025960>) as well) ping <@750037398838182029> once u put this vanity link in ur bio")

@client.command()
async def ad(ctx):
    await ctx.send("lCome join UNDERWORLD\n\n"

"🍥It takes all sorts of people to make the underworld.  🍥\n\n"

"🍥We do giveaways monthly🍥\n\n"

"🍥If you're looking for a chill server to game in, make friends, talk about anime, k-pop and meet other PEOPLE, please consider joining!🍥\n\n"

"🍥We VC and have many fun bots🍥\n\n"

"🍥Please be at least 13 before joining this server for security purposes!🍥\n\n"

"🍥Also looking for Staff to come and help out our growing server🍥\n\n"

"🍡That should be all!\n"
"Please enjoy your stay!🍡\n"
"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||"
"https://discord.com/invite/underrealm")
    
@client.command()
async def dp(ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar.url
    await ctx.send(userAvatar)
@client.event
async def on_member_join(member):
    channel = client.get_channel(1192098301361791117)
    await channel.send(f"Hello {member.mention}")
    embed=discord.Embed(colour=discord.Colour.dark_purple(),title=f"Welcome To {member.guild.name}", description=f"Thanks for joining!\nPLEASE VISIT FOLLOWING CHANNELS :\n<#1047418272628346910>\n") # F-Strings!
    embed.set_thumbnail(url=member.avatar.url) # Set the embed's thumbnail to the member's avatar image!
    embed.set_image(url="https://media.tenor.com/x15S5rhHVscAAAAe/anime-purple.png")
    await channel.send(embed=embed)
@client.event
async def on_member_remove(member):
    channel = client.get_channel(1192098301361791117)
    await channel.send("good bye")
    
@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await member.kick(reason=reason)
    embed=discord.Embed(colour=discord.Colour.dark_purple(),title=f'User {member} has been kicked')
    await channel.send(embed=embed)
  

@kick.error
async def kick_error(ctx, error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("You dont have permissions to kick people!")

@client.command()
@has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason =None):
    await member.ban(reason=reason)
    embed=discord.Embed(colour=discord.Colour.dark_purple(),title=f'User {member} has been banned')
    await ctx.send(embed=embed)
    

@ban.error
async def ban_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("You dont have permissions to ban people!")


# =========================================================================
# music
from help_cog import help_cog
from music_cog import music_cog

client.remove_command("help")
async def setup(client):
    await client.add_cog(help_cog(client))
    await client.add_cog(music_cog(client))
coro = setup(client)
asyncio.run(coro)

# =========================================================================

# from openai import OpenAI





# bot = OpenAI(api_key=apij)
# @client.event
# async def on_message(message):
#     user_message = str(message.content)
#     channel = client.get_channel(1199690139488747641)
#     if message.channel.name == 'ai-bot':
#         response = bot.completions.create(
#         model="gpt-3.5-turbo-instruct",
#         prompt=user_message,
#         temperature=1,
#         max_tokens=50,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#         )
#         text_from_choice = response.choices[0].text.strip()
#         await channel.send(text_from_choice)

# ========================================================================
from pypresence import Presence
import time


client_id="1191692371524587520"
RPC = Presence(client_id)

RPC.connect()

RPC.update(
    state="working on my Demon",
    large_image='https://cdn.imgchest.com/files/pyq9c5g2nx4.png'

)



# ===================================================================
snipe_message_author = {}
snipe_message_content = {}
snipe_message_time = {}
from datetime import datetime
from pytz import timezone 
from datetime import datetime

ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')


@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     snipe_message_time[message.channel.id] = datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M %p')

     await asyncio.sleep(3600)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@client.command()
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(description = f"Last deleted message in #{channel.name}\n\n->  {snipe_message_content[channel.id]}")
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}\nToday at {snipe_message_time[channel.id]}")
        await ctx.send(embed = em)
    except KeyError: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")

@client.command()
async def membercount(ctx):
    guild_id = ctx.guild.id
    guild = client.get_guild(guild_id)
    embed=discord.Embed(colour=discord.Colour.dark_purple(),title="Members",description =len(guild.members))
    embed.set_footer(text = f"Today at {datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M %p')}")
    await ctx.send(embed=embed)

# =========================================================================
@commands.has_permissions(manage_messages=True)
@client.command(name='purge', brief='Deletes a specified number of messages from the current channel')
async def purge(ctx, amount: int):
  # Delete the specified number of messages
  deleted = await ctx.channel.purge(limit=amount)
  if len(deleted) == 0:
    # If no messages were deleted, create an embed message with a custom color and text
    embed = discord.Embed(title='Purge complete', color=discord.Colour.dark_purple())
    embed.description = 'No messages were deleted'
    # Set the user's profile picture as the thumbnail of the embed
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
    # Send the embed message
    await ctx.send(embed=embed,delete_after=10.0)
  else:
    # Create an embed message with a custom color and text
    embed = discord.Embed(title='Purge complete', color=discord.Colour.dark_purple())
    if len(deleted) == 1:
      # If only one message was deleted, use singular text
      embed.description = '1 message was deleted'
    else:
      # If more than one message was deleted, use plural text
      embed.description = f'{len(deleted)} messages were deleted'
    # Set the user's profile picture as the thumbnail of the embed
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
    # Send the embed message
    await ctx.send(embed=embed,delete_after=10.0)



# =========================================================================

client.run(apikey)