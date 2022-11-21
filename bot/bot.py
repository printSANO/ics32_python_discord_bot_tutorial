import discord
from discord.ui import Button, View

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        view = View()
        button1 = Button(label="Test", style=discord.ButtonStyle.gray)
        view.add_item(button1)
        async def buttons(interaction):
            button1.style = discord.ButtonStyle.red
            await interaction.response.edit_message(view=view)
        button1.callback = buttons
        await message.channel.send(view=view) 

client.run('Your Token for Discord')
