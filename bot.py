
import discord
from discord.message import Message
from discord.util import get
from discord import Client
import os
import environ_var
intents = discord.Intents.default()
intents.members=True
intents.reactions=True
client= Client(intents=intents)


@client.event
async def on_ready():
    print("We are Ready!!!")
    # welcomechannel = await client.fetch_channel("897640623669116968")

@client.event
async def on_member_join(member):
    guild = member.guild
    user = member.name
    mention = member.mention
    members = len(list(member.guild.members))

    print(f"{user} has join")
    msg = f'''Hello {mention}! 
    Welcome to {guild} and thank you for joining enjoy
    Current population of this guild is {members}.
    '''
    channel = client.get_channel(897640623669116968)
    
    embed = discord.Embed(color=discord.Colour.random(), description=msg)
    embed.set_thumbnail(url=f'{member.avatar_url}')
    
    await channel.send(embed=embed)
# async def get_emoji(guild: discord.Guild, arg):
#     return get(ctx.guild.emojis, name=arg)
@client.event
async def on_reaction_add(reaction, user):
    emoji_selection = [":school_satchel:", ":1251squidwardawake:", ":mechanical_arm:", ":1000hahaa:", ":5724duck:", ":8793beluga:"]

    channel = client.get_channel(900665979812589588)
    emoji = reaction.emoji

    if reaction.message.id == (900669947770970122):
        if emoji == emoji_selection[0]:
            role = get(user.server.roles, name="Classmates")
            await client.add_roles(user, role)
        elif emoji == emoji_selection[1]:
            role = get(user.server.roles, name="IYAH's Katoto")
            await client.add_roles(user, role)
        elif emoji == emoji_selection[2]:
            role = get(user.server.roles, name="KARL's Katoto")
            await client.add_roles(user, role)    
        elif emoji == emoji_selection[3]:
            role = get(user.server.roles, name="SHAWN's Katoto")
            await client.add_roles(user, role)    
        elif emoji == emoji_selection[4]:
            role = get(user.server.roles, name="JOHNDEL's Katoto")
            await client.add_roles(user, role)    
        elif emoji == emoji_selection[5]:
            role = get(user.server.roles, name="CASSANDRA's Katoto")
            await client.add_roles(user, role)    

client.run(os.environ.get('TOKEN_SECRET'))

