from discord.ext import commands

from formatting.markdown import MD
from logger import logging

logger = logging.getLogger(f"robotina.{__name__}")


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        logger.debug(f"{self.__class__.__name__} initialized")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(error)


class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        logger.debug(f"{self.__class__.__name__} initialized")

    @commands.command(aliases=["stat", "st"])
    async def status(self, ctx):
        await ctx.send(f"latency: {self.bot.latency:0.3f}s")


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        logger.debug(f"{self.__class__.__name__} initialized")

    @commands.command()
    async def salut(self, ctx):
        await ctx.send(f"Hello {ctx.author}")


class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        logger.debug(f"{self.__class__.__name__} initialized")

    @commands.command()
    async def sum(self, ctx, a: int, b: int):
        await ctx.send(f"Sum {a} + {b} = {a + b}")

    @commands.command()
    async def sub(self, ctx, a: int, b: int):
        await ctx.send(f"Sub {a} - {b} = {a - b}")

    @commands.command()
    async def div(self, ctx, a: int, b: int):
        await ctx.send(f"Div {a} / {b} = {a / b}")

    @commands.command()
    async def mul(self, ctx, a: int, b: int):
        await ctx.send(f"Mul {a} * {b} = {a * b}")


class Tests(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        logger.debug(f"{self.__class__.__name__} initialized")

    @commands.command()
    async def notify(self, ctx):
        await ctx.send(
            MD.card(
                {
                    "title": "Server Response",
                    "body": "Press !st\nThen after that, you should be able to\ndepear lorem ipsum",
                    "link": "https://www.google.com"
                }
            )
        )

    @commands.command()
    async def echo(self, ctx, title, body, link=None):
        await ctx.send(
            MD.card(
                {
                    "title": title,
                    "body": body,
                    "link": "" if link is None else link
                }
            )
        )

    @commands.command(aliases=["em", "emb"])
    async def embed(self, ctx):
        struct = {
            "title": "Terminator",
            "description": "A human soldier is sent from 2029 to 1984 to stop an almost indestructible cyborg killing machine, sent from the same year, which has been programmed to execute a young woman whose unborn son is the key to humanity's future salvation.",
            "url": "https://www.imdb.com/title/tt0088247/",
            "thumbnail": ""
        }

        await ctx.send(embed=MD.embed(**struct))


COGS = [Math, Greetings, CommandErrorHandler, Status, Tests]
