from discord.ext import commands

from frontend.config import Config

class CountingBot(commands.Bot):
    def __init__(self, config: Config):
        self.config = config

        super().__init__(command_prefix = self.config.prefix)
        self.register_events()

    def run(self):
        super().run(self.config.token)

    def register_events(self):
        @self.event
        async def on_ready():
            print('logged in')

        @self.command(pass_context=True)
        async def hi(message):
            await message.channel.send("hi")