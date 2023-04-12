from nextcord.ext import commands 

#initialize the cog class
class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #we can now create commands here
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.guild)
    async def hello(self, ctx):
        await ctx.send("Hi!")

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.guild)
    async def ping(self, ctx):
        await ctx.send("Pong!")

#this will take the bot Class and add it to the cog
def setup(bot):
    bot.add_cog(BasicCommands(bot))