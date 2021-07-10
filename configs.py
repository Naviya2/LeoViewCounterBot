# (c) @Naviya2


import os


class Config(object):
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Rename-Bot-0")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1069002447))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
