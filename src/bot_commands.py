from discord.ext import commands

from formatting.markdown import MD


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(error)


class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["stat", "st"])
    async def status(self, ctx):
        await ctx.send(f"latency: {self.bot.latency:0.3f}s")


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def salut(self, ctx):
        await ctx.send(f"Hello {ctx.author}")

    @commands.command(aliases=["ft_b"])
    async def format_b(self, ctx):
        await ctx.send(MD.bold(f"Hello {ctx.author}"))

    @commands.command(aliases=["ft_i"])
    async def format_i(self, ctx):
        await ctx.send(MD.italics(f"Hello {ctx.author}"))

    @commands.command(aliases=["ft_u"])
    async def format_u(self, ctx):
        await ctx.send(MD.underline(f"Hello {ctx.author}"))

    @commands.command(aliases=["qt"])
    async def quote(self, ctx):
        await ctx.send(MD.quote_block(f"Hello {ctx.author}"))

    @commands.command(aliases=["qts"])
    async def quotes(self, ctx):
        await ctx.send(MD.quote_blocks(f"Hello {ctx.author}"))

    @commands.command(aliases=["cd"])
    async def code(self, ctx):
        await ctx.send(MD.code_blocks("JavaScript\nhelloWorld"))

    @commands.command(aliases=["cmp"])
    async def comp(self, ctx):
        await ctx.send(MD.quote_blocks(MD.bold("JavaScript") + "\nhelloWorld"))


class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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


COGS = [Math, Greetings, CommandErrorHandler, Status]
