import os
import json
import discord
from dotenv import load_dotenv
from discord.ext import commands

import alias

# Variables
__version__ = str("1.2")
dirname = os.path.dirname(__file__)
imglink = str("https://absolver.dev/assets/images/")


# Functions
def get_move(move_name):
    filepath = dirname + "/movelist.json"
    with open(filepath) as movelist_file:
        contents = movelist_file.read()
    movelist_json = json.loads(contents)

    move_details = list(filter(lambda x: (x['Attack'].lower() == move_name), movelist_json))

    return move_details[0]


def move_embed(move):
    imgname = move['Attack'].replace(" ", "-")
    imgname = imgname.lower()

    embed = discord.Embed(title=move['Attack'], colour=0x1f3c80)
    if imgname == "faejin-stopper" or imgname == "faejin-parry":
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/c/ca/Bruce_Lee_1973.jpg")
    elif imgname == "back-stagger" or imgname == "front-stagger" or imgname == "side-stagger":
        embed.set_thumbnail(
            url="https://thumbs.dreamstime.com/z/drunk-business-man-wasted-drinking-whiskey-alcoholism-attractive-lying-desk-bottle-problem-alcohol-abuse-addiction-42684912.jpg"
        )
    else:
        embed.set_thumbnail(url=imglink + imgname + ".png")

    # Shut the fuck up I know it's ugly i cbf to make it nicer
    embed.add_field(name='Start Up \u200B', value=move['Start up frame'],)
    embed.add_field(name='Hit \u200B', value=move['Adv. on hit'])
    embed.add_field(name='Block \u200B', value=move['Adv. on block'])
    embed.add_field(name='Height', value=move['Target Area'])
    embed.add_field(name='Type', value=move['Attack Type'])
    embed.add_field(name='Parry Direction', value=move['Target Side'])
    embed.add_field(name='Impact', value=move['Impact'])
    embed.add_field(name='Special', value=move['Special properties'])
    embed.add_field(name='Transition', value=move['Stance Transition'])
    embed.add_field(name='Notes', value=move['Notes'])

    return embed


# Main
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='b! ')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord! Running version {__version__}\n'
          f'----------------------------------------'
          )


@bot.command(name="get", help="Acquires the frame data of the named move. Aliases accepted, swords not yet available.")
async def getmove(ctx):
    user_message = ctx.message.content
    user_message = user_message.replace("b! get ", "")

    move_name = user_message.lower()

    # Searches alias.py for aliases
    move_alias = list(filter(lambda x: (move_name in x["alias"]), alias.MOVE_NAMES))
    if move_alias:
        move_name = move_alias[0]["name"]
        # I know using try except is lazy and bad but i am lazy and bad
        try:
            move = get_move(move_name)
            embed = move_embed(move)
            response = embed
        except IndexError:
            response = discord.Embed(title="Attack data not found, sword attacks unavailable", colour=0x1f3c80)

    else:
        response = discord.Embed(title="Attack not found", colour=0x1f3c80)

    await ctx.send(embed=response, delete_after=20)


@bot.command(name="sneak", help="I wonder what this does...")
async def sneak(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/350772748013928458/849339089668276244/deckfinder.png")


@bot.command(name="terms", help="Defines cis/trans terminology")
async def terms(ctx):
    await ctx.send("**Cis** - Same\n**Trans** - Opposite\nIf an attack hits cis then it strikes from the side you are facing\nSide Kick hits cis, Hook hits trans\nIf an attack's movement is cis it maintains left/right direction.\nWobble's movement is Front to Back Cis. Inside Kick is Front to Back Trans.")


# Runs bot
bot.run(TOKEN)
