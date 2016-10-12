import discord
from discord.ext import commands
from random import choice as rndchoice
from .utils.dataIO import fileIO
from .utils import checks
import os

defaults = [
    "Twentysix's Floppy Disk",
    "Eslyium's Hentai Collection",
    "A Nuke",
    "A Loaf Of Bread",
    "My Hand",
    "Will's SquidBot",
    "JennJenn's Penguin Army",
    "Red's Transistor",
    "Asu\u10e6's Wrath",
    "Skordy's Keyboard"]

class Burn:
    """Burn command."""

    def __init__(self, bot):
        self.bot = bot
        self.items = fileIO("data/burn/items.json", "load")

    def save_items(self):
        fileIO("data/burn/items.json", 'save', self.items)

    @commands.group(pass_context=True, invoke_without_command=True)
    async def burn(self, ctx, *, user : discord.Member=None):
        """Burn a user"""
        if ctx.invoked_subcommand is None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("Dont make me burn you instead " + user.mention)
                return
            await self.bot.say("-burns " + user.mention + " with " +
                               (rndchoice(self.items) + "-"))

    @burn.command()
    async def add(self, item):
        """Adds an item"""
        if item in self.items:
          await self.bot.say("That is already an item.")
        else:
          self.items.append(item)
          self.save_items()
          await self.bot.say("Item added.")

    @burn.command()
    @checks.is_owner()
    async def remove(self, item):
        """Removes item"""
        if item not in self.items:
          await self.bot.say("That is not an item")
        else:
            self.items.remove(item)
            self.save_items()
            await self.bot.say("item removed.")

def check_folders():
    if not os.path.exists("data/burn"):
        print("Creating data/burn folder...")
        os.makedirs("data/burn")

def check_files():
    f = "data/burn/items.json"
    if not fileIO(f, "check"):
        print("Creating empty items.json...")
        fileIO(f, "save", defaults)

def setup(bot):
    check_folders()
    check_files()
    n = Burn(bot)
    bot.add_cog(n)