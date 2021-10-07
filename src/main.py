import toml
from frontend.config import Config
from frontend.countingbot import CountingBot

g_CONFIG_FILE = "./config.toml"

# loads the config file into a json object and returns it
# throws FileNotFound error if g_CONFIG_FILE doesn't exist
def load_config():
    with open(g_CONFIG_FILE) as f:
        return Config(toml.loads(f.read()))

if __name__ == "__main__":
    config = load_config()

    counting_bot = CountingBot(config)
    counting_bot.run()