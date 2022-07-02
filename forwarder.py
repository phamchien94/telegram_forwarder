from datetime import datetime
from pyrogram import Client, filters, idle

from settings import (
    TG_API_HASH, TG_API_ID, TG_SESSION, FORWARD_CHAT_IDS, TARGET_CHAT_ID
)

app = Client(TG_SESSION, TG_API_ID, TG_API_HASH)

chat_ids = FORWARD_CHAT_IDS
dest_chat_ids = TARGET_CHAT_ID

@app.on_message(filters.chat(chat_ids))
def handler(client, message):
    is_duplicated = False
    if message.edit_date:
        d = datetime.datetime.strptime(message.date, '%Y-%m-%d %H:%M:%S')
        e = datetime.datetime.strptime(message.edit_date, '%Y-%m-%d %H:%M:%S')
        delta = (e - d).total_seconds()
        if delta < 5:
            is_duplicated = True
    if not is_duplicated:
        for target in dest_chat_ids:
            client.forward_messages(
                chat_id=target,
                from_chat_id=message.chat.id,
                message_ids=message.message_id
            )
        is_duplicated = False


app.start()
idle()
app.stop()
