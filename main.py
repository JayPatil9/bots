import os
import discord
from discord.ext import commands, tasks
from discord_components import DiscordComponents, Button, Select, SelectOption , ButtonStyle



client = discord.Client()
client = commands.Bot(command_prefix='ue!')
client.remove_command("help")

@client.event
async def on_ready():
	DiscordComponents(client)
	print(f"Logged in as {client.user}!")

@client.command()
async def button(ctx):
	await ctx.send(
		"Hello, World!",
		components = [
			Button(label = "WOW button!"), 
			Button(style = ButtonStyle.URL
			,label = "Register Now"
			,url = "https://www.urbanesports.ml/")
			]
		)
	interaction = await client.wait_for("button_click")
	
	await interaction.respond(content = "Button clicked!")

@client.command()
async def select(ctx):
	await ctx.send(
		"Hello, World!",
		components = [
			Select(placeholder="select something!", options=[SelectOption(label="a", value="A"), SelectOption(label="b", value="B")])
			]
		)
		
	interaction = await client.wait_for("select_option", check = lambda i: i.component[0].value == "A")
		
	await interaction.respond(content = f"{interaction.component[0].label} selected!")

token = os.environ["token"]
client.run(token)
