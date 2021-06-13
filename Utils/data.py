# imports (don't remove)
from discord.ext.commands import CommandNotFound
from discord.ext import commands, tasks
from datetime import datetime
from time import perf_counter
import platform
import requests
import discord
import aiohttp
import asyncio
import psutil
import json
import os
import re

# config imports
def dc_token():
    return json.load(open(r'Data/config.json', 'r'))["DC-Token"]
def api_token():
    return json.load(open(r'Data/config.json', 'r'))["API-Token"]
def description():
    return json.load(open(r'Data/config.json', 'r'))["Description"]
def owner_id():
    return json.load(open(r'Data/config.json', 'r'))["Owner-ID"]
def time_syntax():
    return json.load(open(r'Data/config.json', 'r'))["Time-Syntax"]
def color():
    return json.load(open(r'Data/config.json', 'r'))["Color"]
def cooldown():
    return json.load(open(r'Data/config.json', 'r'))["Cooldown"]
def command_prefix():
    return json.load(open(r'Data/config.json', 'r'))["Prefix"]
def version():
    return json.load(open(r'Data/config.json', 'r'))["Version"]
def shard_count():
    return json.load(open(r'Data/config.json', 'r'))["Shard-Count"]

# color for discord
def discord_color():
    return discord.Color.from_rgb(color()[0], color()[1], color()[2])

# request
async def request(main_endpoint: str, sub_endpoint: str, response_type: str = 'json'):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://kawaii.red/api/{main_endpoint}/{sub_endpoint}/token={api_token()}&type={response_type}/') as r:
            js = await r.json()
            return js["response"]

# send gif
async def send_gif(ctx, message):
    embed = discord.Embed(title=str(ctx.command).capitalize(),
                          color=discord_color())
    if message:
        embed = discord.Embed(title=str(ctx.command).capitalize(),
                              description='> ' + message,
                              color=discord_color())
    embed.set_image(url=await request('gif', ctx.command))
    await ctx.send(embed=embed)
