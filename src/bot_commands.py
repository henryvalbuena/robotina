from discord.ext import commands


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

    @commands.command(aliases=["ft"])
    async def format(self, ctx):
        await ctx.send(f"```Hello {ctx.author}```")

    @commands.command(aliases=["qt"])
    async def quote(self, ctx):
        await ctx.send(f"> Hello {ctx.author}")

    @commands.command(aliases=["md"])
    async def markdown(self, ctx):
        await ctx.send("```JavaScript\nhelloWorld```")


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
