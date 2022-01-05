from datetime import datetime
from pyrogram import Client, filters, idle

from settings import (
    TG_API_HASH, TG_API_ID, TG_SESSION, FORWARD_CHAT_IDS, TARGET_CHAT_ID, 
    TIME_TO_CHECK_DUPLICATED
)

app = Client(TG_SESSION, TG_API_ID, TG_API_HASH)


@app.on_message(filters.chat(FORWARD_CHAT_IDS))
def handler(client, message):
    is_duplicated = False
    if message.edit_date:
        d = datetime.datetime.strptime(message.date, '%Y-%m-%d %H:%M:%S')
        e = datetime.datetime.strptime(message.edit_date, '%Y-%m-%d %H:%M:%S')
        delta = (e - d).total_seconds()
        if delta < TIME_TO_CHECK_DUPLICATED:
            is_duplicated = True
    if not is_duplicated:
        for target in TARGET_CHAT_ID:
            client.forward_messages(
                chat_id=target,
                from_chat_id=message.chat.id,
                message_ids=message.message_id
            )
        is_duplicated = False


app.start()
idle()
app.stop()