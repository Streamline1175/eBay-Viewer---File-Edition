import discord
from discord.ext import commands
import asyncio
import random
import re

# Create a bot instance
intents = discord.Intents.default()
intents.message_content=True
#bot = discord.Client(intents=intents)

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Define a dictionary to store progress for each user
progress = {}

@bot.command()
async def ebaylist(ctx):
    # Check if a .txt file is attached
    if ctx.message.attachments and ctx.message.attachments[0].filename.endswith('.txt'):
        # Read the content of the attached .txt file
        file = ctx.message.attachments[0]
        contents_bytes = await file.read()
        contents = contents_bytes.decode('utf-8')
        message_list = contents.splitlines()
    else:
        await ctx.send("Please attach a .txt file with eBay URLs.")
        return

    user_id = ctx.author.id

    if user_id not in progress:
        progress[user_id] = 0

    total_items = len(message_list)
    progress[user_id] = 0

    # Send messages and update progress
    for url in message_list:
        progress[user_id] += 1
        random_watch = random.randint(1, 10)
        random_view = random.randint(50, 500)
        progress_percentage = (progress[user_id] / total_items) * 100
        
        username = ctx.author.name

        # Calculate the number of spaces needed to overwrite the line
        spaces_to_clear = 150  # Adjust as needed for your terminal width
        spaces_to_clear -= len(f"Progress: [{'#' * int(progress_percentage / 2):50}] {progress_percentage:.2f}% - {username}")

        # Print the progress bar in the terminal with clearing spaces
        print(f"Progress: [{'#' * int(progress_percentage / 2):50}] {progress_percentage:.2f}% - {username}" + ' ' * spaces_to_clear, end='\r')

        await ctx.send(f"$ebay watch {url} {random_watch}")
        await asyncio.sleep(2)  # Adjust the delay between messages
        await ctx.send(f"$ebay view {url} {random_view}")
        await asyncio.sleep(2)  # Adjust the delay between messages

    # Clear the line by printing spaces, then print the completed status
    print(' ' * 150, end='\r')  # Clears the line
    print(f"Completed - Total Items: {total_items} - {username}")

# Replace 'YOUR_BOT_TOKEN' with your bot's token
bot.run('MTE2MDA4OTkxMDEwNDAzOTUxNw.GPtM9Y.pDdY8cPaOfHhUER-6XZj5Dmh7fZTq6PsrwxO3k')