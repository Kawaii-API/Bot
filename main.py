# Kawaii API Bot created by Error44 free to use for everyone

# imports
from Utils.data import *

# bot
bot = commands.AutoShardedBot(
    help_command=None,
    case_insensitive=True,
    owner_id=owner_id(),
    description=description(),
    shard_count=shard_count(),
    command_prefix=command_prefix(),
    intents=discord.Intents.default(),
    activity=discord.Game(name='kawaii.red | k.help'))

# start print
print(f'[{datetime.now().strftime(time_syntax())}][INFO] Connecting...')

# ready
@bot.event
async def on_ready():
    print('\nBot information:')
    print(f'-Name: {bot.user.name}')
    print(f'-ID: {bot.user.id}')
    print(f'-Version: {version()}')
    print(f'-Prefix: {command_prefix()}')
    print(f'\n[{datetime.now().strftime(time_syntax())}][INFO] Loading Cogs...\n')
    for filename in os.listdir('Cogs'):
        if filename.endswith('.py'):
            try:
                bot.load_extension(f'Cogs.{filename[:-3]}')
                print(f"[{datetime.now().strftime(time_syntax())}][INFO] The file {filename[:-3]} was loaded")
            except Exception:
                print(f"[{datetime.now().strftime(time_syntax())}][INFO] The file {filename[:-3]} was not loaded")
    print(f'\n[{datetime.now().strftime(time_syntax())}][INFO] The Bot is online')

# error handler
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return

# run
bot.run(dc_token())