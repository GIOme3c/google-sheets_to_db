import telegram
import asyncio

from config import BOT_TOKEN

def simple_run(func):
    def wrapper(message):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(func(message))
    return wrapper

@simple_run
async def send_message_to_all_users(message):
    bot = telegram.Bot(token=BOT_TOKEN)
    updates = await bot.getUpdates()
    sended_ids = {}

    for update in updates:
        if update.message is not None:
            chat_id = update.message.chat_id
            if not sended_ids.get(chat_id, 0):
                await bot.sendMessage(chat_id=chat_id, text=message)
                sended_ids[chat_id] = 1 


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(send_message_to_all_users("I`M WORKING!"))
    send_message_to_all_users("I`M WORKING!")