
import discord
from discord.ext import commands
from discord.utils import get
from discord import Client
import os
import environ_var
intents = discord.Intents.default()
intents.members=True
intents.reactions=True

client= Client(intents=intents)
bot = commands.Bot(command_prefix=">>")

@client.event
async def on_ready():
    print("We are Ready!!!")
    channel = client.get_channel(900665979812589588)
    emoji_selection = [899104958845157416, 899104959201677373, 899104960443220009, 899104959260422145]

    # emoji_selection = ["school_satchel", "1251squidwardawake", "mechanical_arm", "1000hahaa", "5724duck", "8793beluga"]
    emoji_id = []
    for emoji_name in emoji_selection:
        emoji = client.get_emoji(emoji_name)
        emoji_id.append(emoji)
    message = await channel.send(f'''
Welcome to our server T-AJACK

To get your role click the following emojis:

    🎒 = Classmates - if you're are classmates 

    {emoji_id[0]} = Iyah's Katoto - if you're friend of Iyah

    🦾 = Karl's Katoto - if you're friend of Karl

    {emoji_id[1]} = Shawn's Katoto - if you're friend of Shawn

    {emoji_id[2]} = Johndel's Katoto - if you're friend of Johndel

    {emoji_id[3]} = Cassandra's Katoto  - if you're friend of Cassandra

Enjoy the server 
    ''')
 
    await message.add_reaction( emoji=str('🎒'))
    await message.add_reaction( emoji=emoji_id[0])
    await message.add_reaction( emoji=str('🦾'))
    await message.add_reaction( emoji=emoji_id[1])
    await message.add_reaction( emoji=emoji_id[2])
    await message.add_reaction( emoji=emoji_id[3])
# For The Role Selection
emoji_selection1 = [":school_satchel:", ":1251squidwardawake:", ":mechanical_arm:", ":1000hahaa:", ":5724duck:", ":8793beluga:"]
emoji_selection = [899104958845157416, 899104959201677373, 899104960443220009, 899104959260422145]
roles = ["IYAH's Katoto", "SHAWN's Katoto","JOHNDEL's Katoto", "CASSANDRA's Katoto","Classmates", "KARL's Katoto"]
channel_id = 900665979812589588
selected = []
@client.event
async def on_reaction_remove(reaction,user):
        
        # channel = client.get_channel(channel)
        emoji_id = []
        for emoji_name in emoji_selection:
            emoji = client.get_emoji(emoji_name)
            emoji_id.append(emoji)
        emoji_id.append(str('🎒')) # 4
        emoji_id.append(str('🦾')) # 5
        
        if reaction.message.channel.id ==channel_id:
            selected.remove(user.id)
            for i in range(len(emoji_selection1)):
                    emoji = reaction.emoji
                    if emoji == emoji_id[i]:
                        role = get(user.guild.roles, name=roles[i])
            await user.remove_roles(role)    


@client.event
async def on_reaction_add(reaction,user):
    if user.id != 900002914943238174:
        # channel = client.get_channel(channel)
        emoji_id = []
        for emoji_name in emoji_selection:
            emoji = client.get_emoji(emoji_name)
            emoji_id.append(emoji)
        emoji_id.append(str('🎒')) # 4
        emoji_id.append(str('🦾')) # 5
        
       
            
        
        if reaction.message.channel.id ==channel_id:
            
            if user.id not in selected:
                print("reacted")
                selected.append(user.id)
                print(selected)
                for i in range(len(emoji_selection1)):
                    emoji = reaction.emoji
                    if emoji == emoji_id[i]:
                        role = get(user.guild.roles, name=roles[i])
                        
                await user.add_roles(role, reason=None)    
@client.event
async def on_member_join(member):
    guild = member.guild
    user = member.name
    mention = member.mention
    members = len(list(member.guild.members))

    print(f"{user} has join")
    msg = f'''
Hello {mention}! 
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

