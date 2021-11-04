import discord

from discord.ext import commands
from firebase_admin import credentials, firestore

class DadBot(commands.Cog):
    CMD_PREFIX = '--'

    @commands.Command()
    async def enable(ctx):
        

def main():
