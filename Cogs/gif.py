# import
from Utils.data import *

# class
class GIF(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

# possible alternative to target any endpoint but not recommended due to poor control
#    @commands.Cog.listener()
#    async def on_message(self, message):
#        if message.content.startswith(command_prefix()):
#            command = message.content.split()[0].replace(command_prefix(), '')
#            if command in await request('gif', 'endpoints'):
#                embed = discord.Embed(title=str(command).capitalize(),
#                                      color=discord_color())
#                if len(message.content.split()) > 1:
#                    embed = discord.Embed(title=str(command).capitalize(),
#                                          description='> ' + message.content.replace(command_prefix() + command, ''),
#                                          color=discord_color())
#                embed.set_image(url=await request('gif', command))
#                await message.channel.send(embed=embed)

# alarm
    @commands.command()
    async def alarm(self, ctx, *, message=None):
        await send_gif(ctx, message)

# amazing
    @commands.command()
    async def amazing(self, ctx, *, message=None):
        await send_gif(ctx, message)

# ask
    @commands.command()
    async def ask(self, ctx, *, message=None):
        await send_gif(ctx, message)

# baka
    @commands.command()
    async def baka(self, ctx, *, message=None):
        await send_gif(ctx, message)

# blush
    @commands.command()
    async def blush(self, ctx, *, message=None):
        await send_gif(ctx, message)

# blyat
    @commands.command()
    async def blyat(self, ctx, *, message=None):
        await send_gif(ctx, message)

# brr
    @commands.command()
    async def brr(self, ctx, *, message=None):
        await send_gif(ctx, message)

# clap
    @commands.command()
    async def clap(self, ctx, *, message=None):
        await send_gif(ctx, message)

# coffee
    @commands.command()
    async def coffee(self, ctx, *, message=None):
        await send_gif(ctx, message)

# confused
    @commands.command()
    async def confused(self, ctx, *, message=None):
        await send_gif(ctx, message)

# cry
    @commands.command()
    async def cry(self, ctx, *, message=None):
        await send_gif(ctx, message)

# cuddle
    @commands.command()
    async def cuddle(self, ctx, *, message=None):
        await send_gif(ctx, message)

# cute
    @commands.command()
    async def cute(self, ctx, *, message=None):
        await send_gif(ctx, message)

# dance
    @commands.command()
    async def dance(self, ctx, *, message=None):
        await send_gif(ctx, message)

# destroy
    @commands.command()
    async def destroy(self, ctx, *, message=None):
        await send_gif(ctx, message)

# die
    @commands.command()
    async def die(self, ctx, *, message=None):
        await send_gif(ctx, message)

# disappear
    @commands.command()
    async def disappear(self, ctx, *, message=None):
        await send_gif(ctx, message)

# dodge
    @commands.command()
    async def dodge(self, ctx, *, message=None):
        await send_gif(ctx, message)

# error
    @commands.command()
    async def error(self, ctx, *, message=None):
        await send_gif(ctx, message)

# facedesk
    @commands.command()
    async def facedesk(self, ctx, *, message=None):
        await send_gif(ctx, message)

# facepalm
    @commands.command()
    async def facepalm(self, ctx, *, message=None):
        await send_gif(ctx, message)

# fbi
    @commands.command()
    async def fbi(self, ctx, *, message=None):
        await send_gif(ctx, message)

# fight
    @commands.command()
    async def fight(self, ctx, *, message=None):
        await send_gif(ctx, message)

# happy
    @commands.command()
    async def happy(self, ctx, *, message=None):
        await send_gif(ctx, message)

# hide
    @commands.command()
    async def hide(self, ctx, *, message=None):
        await send_gif(ctx, message)

# highfive
    @commands.command()
    async def highfive(self, ctx, *, message=None):
        await send_gif(ctx, message)

# hug
    @commands.command()
    async def hug(self, ctx, *, message=None):
        await send_gif(ctx, message)

# kill
    @commands.command()
    async def kill(self, ctx, *, message=None):
        await send_gif(ctx, message)

# kiss
    @commands.command()
    async def kiss(self, ctx, *, message=None):
        await send_gif(ctx, message)

# laugh
    @commands.command()
    async def laugh(self, ctx, *, message=None):
        await send_gif(ctx, message)

# lick
    @commands.command()
    async def lick(self, ctx, *, message=None):
        await send_gif(ctx, message)

# lonely
    @commands.command()
    async def lonely(self, ctx, *, message=None):
        await send_gif(ctx, message)

# love
    @commands.command()
    async def love(self, ctx, *, message=None):
        await send_gif(ctx, message)

# mad
    @commands.command()
    async def mad(self, ctx, *, message=None):
        await send_gif(ctx, message)

# money
    @commands.command()
    async def money(self, ctx, *, message=None):
        await send_gif(ctx, message)

# nom
    @commands.command()
    async def nom(self, ctx, *, message=None):
        await send_gif(ctx, message)

# nosebleed
    @commands.command()
    async def nosebleed(self, ctx, *, message=None):
        await send_gif(ctx, message)

# ok
    @commands.command()
    async def ok(self, ctx, *, message=None):
        await send_gif(ctx, message)

# party
    @commands.command()
    async def party(self, ctx, *, message=None):
        await send_gif(ctx, message)

# pat
    @commands.command()
    async def pat(self, ctx, *, message=None):
        await send_gif(ctx, message)

# poke
    @commands.command()
    async def poke(self, ctx, *, message=None):
        await send_gif(ctx, message)

# pout
    @commands.command()
    async def pout(self, ctx, *, message=None):
        await send_gif(ctx, message)

# protect
    @commands.command()
    async def protect(self, ctx, *, message=None):
        await send_gif(ctx, message)

# puke
    @commands.command()
    async def puke(self, ctx, *, message=None):
        await send_gif(ctx, message)

# punch
    @commands.command()
    async def punch(self, ctx, *, message=None):
        await send_gif(ctx, message)

# purr
    @commands.command()
    async def purr(self, ctx, *, message=None):
        await send_gif(ctx, message)

# pusheen
    @commands.command()
    async def pusheen(self, ctx, *, message=None):
        await send_gif(ctx, message)

# run
    @commands.command()
    async def run(self, ctx, *, message=None):
        await send_gif(ctx, message)

# scared
    @commands.command()
    async def scared(self, ctx, *, message=None):
        await send_gif(ctx, message)

# scream
    @commands.command()
    async def scream(self, ctx, *, message=None):
        await send_gif(ctx, message)

# shame
    @commands.command()
    async def shame(self, ctx, *, message=None):
        await send_gif(ctx, message)

# shocked
    @commands.command()
    async def shocked(self, ctx, *, message=None):
        await send_gif(ctx, message)

# shoot
    @commands.command()
    async def shoot(self, ctx, *, message=None):
        await send_gif(ctx, message)

# shrug
    @commands.command()
    async def shrug(self, ctx, *, message=None):
        await send_gif(ctx, message)

# slap
    @commands.command()
    async def slap(self, ctx, *, message=None):
        await send_gif(ctx, message)

# sleepy
    @commands.command()
    async def sleepy(self, ctx, *, message=None):
        await send_gif(ctx, message)

# smile
    @commands.command()
    async def smile(self, ctx, *, message=None):
        await send_gif(ctx, message)

# smoke
    @commands.command()
    async def smoke(self, ctx, *, message=None):
        await send_gif(ctx, message)

# smug
    @commands.command()
    async def smug(self, ctx, *, message=None):
        await send_gif(ctx, message)

# spin
    @commands.command()
    async def spin(self, ctx, *, message=None):
        await send_gif(ctx, message)

# stare
    @commands.command()
    async def stare(self, ctx, *, message=None):
        await send_gif(ctx, message)

# stomp
    @commands.command()
    async def stomp(self, ctx, *, message=None):
        await send_gif(ctx, message)

# tickle
    @commands.command()
    async def tickle(self, ctx, *, message=None):
        await send_gif(ctx, message)

# trap
    @commands.command()
    async def trap(self, ctx, *, message=None):
        await send_gif(ctx, message)

# triggered
    @commands.command()
    async def triggered(self, ctx, *, message=None):
        await send_gif(ctx, message)

# uwu
    @commands.command()
    async def uwu(self, ctx, *, message=None):
        await send_gif(ctx, message)

# wasted
    @commands.command()
    async def wasted(self, ctx, *, message=None):
        await send_gif(ctx, message)

# wave
    @commands.command()
    async def wave(self, ctx, *, message=None):
        await send_gif(ctx, message)

# wiggle
    @commands.command()
    async def wiggle(self, ctx, *, message=None):
        await send_gif(ctx, message)

# yeet
    @commands.command()
    async def yeet(self, ctx, *, message=None):
        await send_gif(ctx, message)

# setup
def setup(bot):
    bot.add_cog(GIF(bot))
