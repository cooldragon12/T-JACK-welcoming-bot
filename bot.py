
import discord
from discord.message import Message
from discord.utils import get
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
    channel = client.get_channel(900665979812589588)
    emoji_selection = [":school_satchel:", ":1251squidwardawake:", ":mechanical_arm:", ":1000hahaa:", ":5724duck:", ":8793beluga:"]

    message = await client.send_message(channel, '''
Welcome to our server T-AJACK

To get your role click the following emojis:

    🎒 = Classmates - if you're are classmates 

    :1251squidwardawake: = Iyah's Katoto - if you're friend of Iyah

    🦾 = Karl's Katoto - if you're friend of Karl

    :1000hahaa: = Shawn's Katoto - if you're friend of Shawn

    :5724duck: = Johndel's Katoto - if you're friend of Johndel

    :8793beluga: = Cassandra's Katoto  - if you're friend of Cassandra

Enjoy the server 
    ''')
    await client.add_reaction(message, emoji=emoji_selection[0])
    await client.add_reaction(message, emoji=emoji_selection[1])
    await client.add_reaction(message, emoji=emoji_selection[2])
    await client.add_reaction(message, emoji=emoji_selection[3])
    await client.add_reaction(message, emoji=emoji_selection[4])
    await client.add_reaction(message, emoji=emoji_selection[5])

@client.event
async def on_reaction_add(reaction,user):
        reaction = await client.wait_for_reaction(emoji="🏃", message=message)
        emoji_selection = [":school_satchel:", ":1251squidwardawake:", ":mechanical_arm:", ":1000hahaa:", ":5724duck:", ":8793beluga:"]
        channel = client.get_channel(900665979812589588)
        if reaction.message.channel.id != channel:
            return
        emoji = reaction.emoji
        if emoji == emoji_selection[0]:
            role = get(user.server.roles, name="Classmates")
            
        elif emoji == emoji_selection[1]:
            role = get(user.server.roles, name="IYAH's Katoto")
            
        elif emoji == emoji_selection[2]:
            role = get(user.server.roles, name="KARL's Katoto")
                
        elif emoji == emoji_selection[3]:
            role = get(user.server.roles, name="SHAWN's Katoto")
                
        elif emoji == emoji_selection[4]:
            role = get(user.server.roles, name="JOHNDEL's Katoto")
        elif emoji == emoji_selection[5]:
            role = get(user.server.roles, name="CASSANDRA's Katoto")
        await client.add_roles(reaction.message.author, role)    
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


client.run(os.environ.get('TOKEN_SECRET'))

