
import discord
from discord import Client
import os
intents = discord.Intents.default()
intents.members=True
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



client.run(os.environ.get('TOKEN_SECRET'))

