import os

TIME_TO_CHECK_DUPLICATED = 5 # seconds

TG_API_ID = int(os.environ.get("TG_API_ID"))
TG_API_HASH = os.environ.get("TG_API_HASH")
TG_SESSION = os.environ.get("TG_SESSION")

FORWARD_CHAT_IDS = []
for id in os.environ.get("FORWARD_CHAT_IDS").split(":"):
	FORWARD_CHAT_IDS.append(int(id))

TARGET_CHAT_ID = []
for id in os.environ.get("TARGET_CHAT_ID").split(":"):
	TARGET_CHAT_ID.append(int(id))
