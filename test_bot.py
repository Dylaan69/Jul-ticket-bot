import os
from telegram import Bot

token = os.environ[7572591928:AAHwEM2lT4IUQBRoOH2rQkz4ry0fUzg0Uik]
chat_id = os.environ[247319776]

bot = Bot(token=token)
bot.send_message(chat_id=chat_id, text="✅ Test depuis Render (ça marche bro 🔥)")
