import discord


COLORS = {
    "red": discord.Colour.red(),
    "blue": discord.Colour.blue(),
    "orange": discord.Color.orange(),
    "green": discord.Color.green()
}


class MD:
    @staticmethod
    def bold(text):
        return f"**{text}**"

    @staticmethod
    def italics(text):
        return f"*{text}*"

    @staticmethod
    def bold_italics(text):
        return f"***{text}***"

    @staticmethod
    def underline(text):
        return f"__{text}__"

    @staticmethod
    def code_block(text):
        return f"`{text}`"

    @staticmethod
    def code_blocks(text):
        return f"```{text}```"

    @staticmethod
    def quote_block(text):
        return f"> {text}"

    @staticmethod
    def quote_blocks(text):
        return f">>> {text}"

    @staticmethod
    def composition(text):
        return f">>> {MD.bold(text)}"

    @staticmethod
    def card(struct):
        msg = f">>> {MD.bold(struct['title'])} {MD.code_blocks(struct['body'])} {struct['link']}"

        return msg

    @staticmethod
    def embed(**kwargs):
        struct = {
            "title": kwargs.get("title", "Unknown"),
            "description": kwargs.get("description", "Unknown"),
            "color": COLORS.get(kwargs.get("color", "red")),
            "url": kwargs.get("url", "")
        }

        embed = discord.Embed(**struct)
        embed.set_thumbnail(url=kwargs.get("thumbnail", "https://cdn.pixabay.com/photo/2016/10/04/13/52/fail-1714367_1280.jpg"))
        embed.set_image(url=kwargs.get("image", "https://cdn.pixabay.com/photo/2016/10/04/13/52/fail-1714367_1280.jpg"))
        embed.set_footer(text=kwargs.get("footer", ""))

        return embed
