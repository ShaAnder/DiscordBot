from nextcord.ext import commands 

#initialize the cog class
class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #admin commands can go here
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.guild)
    @commands.has_any_role("Spooky Man", "Pillar Mods")
    async def Say_Pong(self, ctx):
        await ctx.send("Pong!")

#this will take the bot Class and add it to the cog
def setup(bot):
    bot.add_cog(Admin(bot))