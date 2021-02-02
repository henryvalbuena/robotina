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
