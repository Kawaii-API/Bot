# import
from Utils.data import *

# class
class Stats(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

# all
    @commands.command()
    async def all(self, ctx):
        embed = discord.Embed(title='All my API requests',
                              description=await request('stats', ctx.command),
                              color=discord_color())
        await ctx.send(embed=embed)

# failed
    @commands.command()
    async def failed(self, ctx):
        embed = discord.Embed(title='My failed API requests',
                              description=await request('stats', ctx.command),
                              color=discord_color())
        await ctx.send(embed=embed)

# history
    @commands.command()
    async def history(self, ctx):
        requested_list = await request('stats', ctx.command)
        embed = discord.Embed(title='My API request history',
                              color=discord_color())
        for requested_item in requested_list:
            embed.add_field(name=requested_item["name"], value=requested_item["value"])
        await ctx.send(embed=embed)

# most_endpoint
    @commands.command()
    async def most_endpoint(self, ctx):
        requested_data = await request('stats', ctx.command)
        embed = discord.Embed(title='My most used API endpoint',
                              description=f'{requested_data["name"]} with {requested_data["value"]} requests',
                              color=discord_color())
        await ctx.send(embed=embed)

# most_endpoints
    @commands.command()
    async def most_endpoints(self, ctx):
        requested_list = await request('stats', ctx.command)
        embed = discord.Embed(title='My most used API endpoints',
                              color=discord_color())
        limiter = 0
        for requested_item in requested_list:
            if not limiter > 14:
                embed.add_field(name=requested_item["name"], value=requested_item["value"])
                limiter += 1
        await ctx.send(embed=embed)

# most_type
    @commands.command()
    async def most_type(self, ctx):
        requested_data = await request('stats', ctx.command)
        embed = discord.Embed(title='My most used API respond type',
                              description=f'{requested_data["name"]} with {requested_data["value"]} requests',
                              color=discord_color())
        await ctx.send(embed=embed)

# most_types
    @commands.command()
    async def most_types(self, ctx):
        requested_list = await request('stats', ctx.command)
        embed = discord.Embed(title='My most used API respond types',
                              color=discord_color())
        for requested_item in requested_list:
            embed.add_field(name=requested_item["name"], value=requested_item["value"])
        await ctx.send(embed=embed)

# setup
def setup(bot):
    bot.add_cog(Stats(bot))