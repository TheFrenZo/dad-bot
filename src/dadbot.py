import discord

from discord.ext import commands
from firebase_admin import credentials, firestore

class DadBot(commands.Cog):
    CMD_PREFIX = '--'

    @commands.Command()
    async def enable(self, ctx):
        pass

    @commands.Command()
    async def add(self, ctx):
        pass

    @commands.Command()
    async def joke(self, ctx):
        pass