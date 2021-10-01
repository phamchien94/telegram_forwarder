import os

TG_API_ID = int(os.environ.get("TG_API_ID"))
TG_API_HASH = os.environ.get("TG_API_HASH")
TG_SESSION = os.environ.get("TG_SESSION")
FORWARD_CHAT_IDS = [int(os.environ.get("FORWARD_CHAT_IDS"))]
TARGET_CHAT_ID = int(os.environ.get("TARGET_CHAT_ID"))
