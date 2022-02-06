from discord.ext import commands

from frontend.config import Config
from backend.core import Core

class CountingBot(commands.Bot):
    def __init__(self, config: Config):
        self.config = config
        self.core   = Core(config)

        super().__init__(command_prefix = self.config.prefix)
        self.register_events()

    def run(self):
        super().run(self.config.token)

    def register_events(self):
        @self.event
        async def on_message(message):
            response = self.core.get_response_to_message(message.content)
            
            if message.author.bot:
                return


            if response != None:
                await message.channel.send(response)