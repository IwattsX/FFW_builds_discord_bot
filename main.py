import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('app_id')
intents = discord.Intents.default()
intents.message_content = True

client : commands.Bot = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_ready():
    # # Uncomment only if syncing a new slash command
    # try:
    #     synced = await client.tree.sync()
    #     print(f"Synced {len(synced)} command(s)")
    # except Exception as e:
    #     print(f"Error syncing commands: {e}")

    print(f'We have logged in as {client.user}')

# normal command with prefix .
# @client.command()
# async def ping(ctx : commands.Context):
#     await ctx.send('Pong!')

# implement slash command
@app_commands.command(name='ping', description='Bots test')
async def ping(interaction : discord.Interaction):
    latency = round(client.latency * 1000)
    await interaction.response.send_message(f"Pong Latency: {latency}ms")

client.tree.add_command(ping)

client.run(token)
