# Telegram Forwarder

## Quick Start

This application using docker, docker-compose to run. So I suppose that you can 
install these two things.

### Prepare essential files

- `./session/my_telegram.session.sesion`: This is a database for `pyrogram` - a telegram
client lib
- `./config.env`: Environment variable for this forwarder

```env
TG_API_ID=xxxxxxx
TG_API_HASH=xxxxxxx
TG_SESSION=/telegram_forwarder/session/my_telegram.session
FORWARD_CHAT_IDS=xxxxxxx
TARGET_CHAT_ID=xxxxxxx
```
`TG_API_ID` and `TG_API_HASH`: Telegram api id and hash of your application.
Reference: https://core.telegram.org/api/obtaining_api_id

`FORWARD_CHAT_IDS`: chat ids of channel/group/user you want to forward 
message from

`TARGET_CHAT_ID`: chat ids of channel/group/user you want to forward 
message to

### Start the app

- Build docker images: `docker-compose build`
- Start the app: `docker-compose up -d`