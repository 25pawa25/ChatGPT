import os
import openai
import telebot
from dotenv import load_dotenv
from openai.lib._old_api import APIRemovedInV1


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))


OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY", "key")
BOT_API_KEY=os.environ.get("BOT_API_KEY", "key")
CHANNEL_ID=os.environ.get("CHANNEL_ID", "key")


openai.api_key = OPENAI_API_KEY
bot = telebot.TeleBot(BOT_API_KEY)


@bot.message_handler(func=lambda _: True)
def handle_message(message):
    channel_id = "CHANNEL_ID"
    if message.text:
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=message.text,
                temperature=0.5,
                max_tokens=1000,
                top_p=1.0,
                frequency_penalty=0.5,
                presence_penalty=0.0,
            )
            message = response['choices'][0]['text']
        except APIRemovedInV1:
            message = "Прошу прощения, сейчас я не могу ответить на этот вопрос."
    bot.send_message(channel_id, text=message)


bot.polling()