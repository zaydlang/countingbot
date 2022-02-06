import toml

class Config:
    def __init__(self, config_toml):
        self.token     = config_toml['bot']['token']
        self.prefix    = config_toml['bot']['prefix']
        self.wa_app_id = config_toml['wa'] ['appid']