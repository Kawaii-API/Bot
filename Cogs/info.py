# import
from Utils.data import *

# cache
gif_commands = 'Retrieves commands...'
stats_commands = 'Retrieves commands...'

# class
class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.update_endpoints.start()

# updating the endpoint list every 12h hours (so that we do not spam the api)
    @tasks.loop(hours=12)
    async def update_endpoints(self):
        global gif_commands, stats_commands
        gif_commands = await request('gif', 'endpoints')
        stats_commands = await request('stats', 'endpoints')

# help
    @commands.command()
    async def help(self, ctx):
        info_commands = []
        for command in self.bot.get_cog('Info').get_commands():
            info_commands.append(str(command))
        info = ', '.join(sorted(info_commands))
        gif = ', '.join(gif_commands)
        stats = ', '.join(stats_commands)
        embed = discord.Embed(title='Bot help',
                              description='[Website](https://kawaii.red/) - [Invite](https://kawaii.red/invite/) - [GitHub](https://kawaii.red/github/)',
                              color=discord_color())
        embed.add_field(name='> Info commands:',
                        value=info,
                        inline=False)
        embed.add_field(name='> Stats commands:',
                        value=stats,
                        inline=False)
        embed.add_field(name='> GIF commands:',
                        value=gif,
                        inline=False)
        embed.add_field(name='> Image commands:',
                        value='currently not ready',
                        inline=False)
        embed.add_field(name='> Text commands:',
                        value='currently not ready',
                        inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

# info
    @commands.command(aliases=['botinfo', 'bot'])
    async def info(self, ctx):
        embed = discord.Embed(title='Bot info',
                              color=discord_color())
        embed.add_field(name='> ID:',
                        value=self.bot.user.id,
                        inline=True)
        embed.add_field(name='> Links:',
                        value="[Website](https://kawaii.red/) - [Invite](https://kawaii.red/invite/) - [GitHub](https://kawaii.red/github/)",
                        inline=False)
        embed.add_field(name='> Developer:',
                        value=str(await self.bot.fetch_user(owner_id())),
                        inline=True)
        embed.add_field(name='> Platform:',
                        value=platform.system(),
                        inline=True)
        embed.add_field(name='> Library:',
                        value='discord.py ' + str(discord.__version__),
                        inline=True)
        embed.add_field(name='> Prefix:',
                        value=command_prefix(),
                        inline=True)
        embed.add_field(name='> Version:',
                        value=version(),
                        inline=True)
        embed.add_field(name="> Shards:",
                        value=self.bot.shard_count,
                        inline=True)
        embed.add_field(name="> CPU:",
                        value=str(psutil.cpu_percent()) + '%',
                        inline=True)
        embed.add_field(name="> RAM:",
                        value=str(psutil.virtual_memory().percent) + '%',
                        inline=True)
        embed.add_field(name="> DISK:",
                        value=str(psutil.disk_usage('/').percent) + '%',
                        inline=True)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

# ping
    @commands.command(aliases=['pong'])
    async def ping(self, ctx):
        start = perf_counter()
        await request('gif', 'kiss')
        end = perf_counter()
        embed = discord.Embed(title='Bot ping',
                              color=discord_color())
        embed.add_field(name="> Discord:",
                        value=str(round(self.bot.latency * 1000, 1)) + 'ms',
                        inline=False)
        embed.add_field(name="> API:",
                        value=str(round((end - start) * 1000, 1)) + 'ms',
                        inline=False)
        await ctx.send(embed=embed)

# links
    @commands.command(aliases=['support'])
    async def links(self, ctx):
        embed = discord.Embed(title='Bot links',
                              description='- [Website](https://kawaii.red/) \n- [Invite](https://kawaii.red/invite/) \n- [Status](https://kawaii.red/status/) \n- [GitHub](https://kawaii.red/github/) \n- [Support](https://kawaii.red/support/)',
                              color=discord_color())
        await ctx.send(embed=embed)

# setup
def setup(bot):
    bot.add_cog(Info(bot))