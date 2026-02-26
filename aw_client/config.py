from aw_core.config import load_config_toml

default_config = """
[server]
hostname = "aw.stoep.co.uk"
port = 443
protocol = "https"
api_key = ""

[client]
commit_interval = 10

[server-testing]
hostname = "127.0.0.1"
port = "5666"
protocol = "http"
api_key = ""

[client-testing]
commit_interval = 5
""".strip()


def load_config():
    return load_config_toml("aw-client", default_config)
