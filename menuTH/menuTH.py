from random import choice as randchoice
from discord.ext import commands

menus = {
    1: ':green_apple: :apple:',
    2: ':tea:',
    3: ':pear: :',
    4: ':tangerine: :peach:',
    5: ':lemon: :sake:',
    6: ':banana: :pineapple:',
    7: ':watermelon: ',
    8: ':grapes: ',
    9: ':strawberry: ',
    10: ":melon: ",
    11: ':cherries: ',
    2: ':fries:',
    13: ':spaghetti:',
    14: ':stuffed_flatbread: ',
    15: ':salad: ',
    16: ':bento:',
    17: ':rice_ball:',
    18: ':ramen:',
    19: ':dango:',
    20: 'doughnut',
    21: ':ice_cream:',
    22: ':cake:',
    23: ':candy:',
    24: ':rice:',
    25: ':beer:',
    26: ':tropical_drink:',
    27: ":pizza: 112",
    28: ":poultry_leg:",
    29: ':curry:',
    30: ':sushi:',
    31: ':rice_cracker:',
    32: ':stew:',
    33: ":egg:",
    34: ':custard:',
    35: ':shaved_ice:',
    36: ':cookie:',
    37: ':lollipop:',
    38: ':potato: :sweet_potato:',
    39: ':wine_glass:',
    40: ':meat_on_bone:',
    41: ":fried_shrimp:",
    42: ':fish_cake:',
    43: ':oden:',
    44: ':icecream:',
    45: ':honey_pot:',
    46: ':eggplant:',
    47: ':fish:',
    49: ':cocktail: ',
    50: ':crab: ',
    51: ':crocodile: ',
    52: ':hotdog: ',
    53: ':burrito:  ',
}


class Menus:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def menu(self, num: int=None):
        """Menu for you"""
        if num:
            if num < 1:
                await self.bot.say(':exclamation: ไม่มีรายการอาหารที่ท่านเลือกค่ะ')
                return
            if num > 53:
                await self.bot.say(':warning: เลขรายการอาหารมีแค่ `53` รายการค่ะ')
                return
            await self.bot.say(":fork_knife_plate: ท่านเลือกรายการอาหารลำดับที่ {}: {}".format(num, menus[num]))
            return
        menu = randchoice(list(menus.keys()))
        await self.bot.say(":fork_knife_plate: ท่านสุ่มได้รายการอาหารลำดับที่ {}: {}".format(menu, menus[menu]))


def setup(bot):
    n = Menus(bot)
    bot.add_cog(n)
