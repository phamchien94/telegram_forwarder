from pyrogram import Client, filters, idle

from settings import (
    TG_API_HASH, TG_API_ID, TG_SESSION, FORWARD_CHAT_IDS, TARGET_CHAT_ID
)

app = Client(TG_SESSION, TG_API_ID, TG_API_HASH)


@app.on_message(filters.chat(FORWARD_CHAT_IDS))
def handler(client, message):
    client.forward_messages(
        chat_id=TARGET_CHAT_ID,
        from_chat_id=message.chat.id,
        message_ids=message.message_id
    )


app.start()
idle()
app.stop()
