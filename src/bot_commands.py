from discord.ext import commands

from formatting.markdown import MD
from logger import logging
from sound import play_song, stop_song
from helpers import restart_pulseaudio, load_module_bluetooth, default_to_bluetooth

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

    @commands.command(aliases=["hi", "hey"])
    async def salut(self, ctx):
        await ctx.send(f"Hello {ctx.author}")


class Sounds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.process = None
        logger.debug(f"{self.__class__.__name__} initialized")

    @commands.command(aliases=["sl", "zz"])
    async def sleep(self, ctx):
        await ctx.send("Processing...")
        self.process = play_song(audio_file="sleep")
        await ctx.send("Playing sleeping song")

    @commands.command(aliases=["lbt.sl", "lbt.zz"])
    async def lbt_sleep(self, ctx):
        await ctx.send("Processing...")
        msg = load_module_bluetooth()
        await ctx.send(msg)
        self.process = play_song(audio_file="sleep")
        await ctx.send("Playing sleeping song")

    @commands.command(aliases=["lbt"])
    async def load_bt(self, ctx):
        msg = load_module_bluetooth()
        await ctx.send(msg)

    @commands.command(aliases=["df"])
    async def default_bt(self, ctx):
        msg = default_to_bluetooth()
        await ctx.send(msg)

    @commands.command(aliases=["rpa"])
    async def restart_pa(self, ctx):
        msg = restart_pulseaudio()
        await ctx.send(msg)

    @commands.command()
    async def stop(self, ctx):
        await ctx.send("Processing...")
        stop_song(process=self.process)
        await ctx.send("Song stopped")


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
                    "link": "https://www.google.com",
                }
            )
        )

    @commands.command()
    async def echo(self, ctx, title, body, link=None):
        await ctx.send(
            MD.card({"title": title, "body": body, "link": "" if link is None else link})
        )

    @commands.command(aliases=["em", "emb"])
    async def embed(self, ctx):
        struct = {
            "title": "Terminator",
            "description": "A human soldier is sent from 2029 to 1984 to stop an almost indestructible cyborg killing machine, sent from the same year, which has been programmed to execute a young woman whose unborn son is the key to humanity's future salvation.",
            "url": "https://www.imdb.com/title/tt0088247/",
            "thumbnail": "",
        }

        await ctx.send(embed=MD.embed(**struct))


COGS = [Greetings, CommandErrorHandler, Status, Sounds, Tests]
