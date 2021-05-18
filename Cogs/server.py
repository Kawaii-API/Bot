# import
from Utils.data import *

# roles
api_user = 843252523733090384
user = 843252810178101258

# class
class Server(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

# on server join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            user_data = db.find_one({"_id": str(member.id)})
            if user_data:
                await member.add_roles(member.guild.get_role(role_id=api_user))
            else:
                await member.add_roles(member.guild.get_role(role_id=user))
        except Exception:
            await member.add_roles(member.guild.get_role(role_id=user))

# on website join
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 844247139412606996:
            embed_content = message.embeds[0]
            if embed_content.title == 'Joined':
                match = re.match(r'<@!?([0-9]+)>$', embed_content.description)
                member = await message.guild.fetch_member(int(match.group(1)))
                await member.add_roles(message.guild.get_role(role_id=api_user))

# setup
def setup(bot):
    bot.add_cog(Server(bot))