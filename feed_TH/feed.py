import discord
from discord.ext import commands
from random import choice as rndchoice
from .utils.dataIO import fileIO
import os

defaults = [
    ":cookie:",
    ":sushi:",
    ":fries:",
    ":pizza:",
    ":rice:",
    ":grapes:",
    ":strawberry:",
    ":hamburger:",
    ":cake:",
    ":mushroom:",
    ":dango:",
    ":curry:",
    ":cactus:",
    ":ramen:",
    ":corn:",
    ":sake:",
    ":eggplant:",
    ":banana:",
    ":candy:",
    ":lemon:",
    ":tropical_drink:",
    ":spaghetti:",
    ":custard:",
    ":birthday:",
    ":green_apple:",
    ":melon:",
    ":sweet_potato:",
    ":coffee:",
    ":beer:",
    ":wine_glass:",
    ":fish_cake:",
    ":egg:",
    ":ice_cream:",
    ":lollipop:",
    ":tangerine:",
    ":watermelon:",
    ":bread:",
    ":pineapple:",
    ":rice_cracker:",
    ":shaved_ice:",
    ":crab:",
    ":meat_on_bone: ",
    ":stew:",
    ":shallow_pan_of_food:",
    ":oden:",
    ":taco:",
    ":burrito:",
    ":bento:",
    ":champagne:",
    ":bacon:",
    ":tea:",
    ":pancakes:",
    ":croissant:",
    ":tumbler_glass:",
    ":kiwi:",
    ":stuffed_flatbread:",
    ":avocado:",
    ":milk:",
    ":cucumber:",
    ":lizard:",
    ":four_leaf_clover:",
    ":cocktail:",
    ":icecream:",
    ":cheese: ",
    ":carrot:",
    ":crocodile:",
    ":fried_shrimp:",
    ":poultry_leg:",
    ":egg:",
    ":potato:",
    ":popcorn:",
    ":peanuts:",]

class Feed:
    """Feeding command."""

    def __init__(self, bot):
        self.bot = bot
        self.items = fileIO("data/feed/items.json", "load")

    @commands.command()
    async def feed(self, user : discord.Member=None):
        """Force A food Item Down A Users Throat"""
        if user.id == self.bot.user.id:
            await self.bot.say("เลเวียจะรับ {} จากคุณค่ะ".format(rndchoice(self.items)))
                                             
            return
        await self.bot.say("- เลเวียเสิร์ฟ {} ให้คุณ {} "
                           " ค่ะ -".format(rndchoice(self.items),
                                             user.name))

def check_folders():
    if not os.path.exists("data/feed"):
        print("Creating data/feed folder...")
        os.makedirs("data/feed")

def check_files():
    f = "data/feed/items.json"
    if not fileIO(f, "check"):
        print("Creating empty items.json...")
        fileIO(f, "save", defaults)


def setup(bot):
    check_folders()
    check_files()
    n = Feed(bot)
    bot.add_cog(n)