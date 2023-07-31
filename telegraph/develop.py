import telegram 
import asyncio

bot = telegram.Bot(token='6369029803:AAG3zFr6QcJC-XSgOYAPUcdPuVmU3eySC8w')

chat_id = '-1001846671651'

# Create the poll
question = 'Server is to be rebooted?'
options = ['Yes', 'No']

keyboard = [[telegram.InlineKeyboardButton(option, callback_data=option)] for option in options]
reply_markup = telegram.InlineKeyboardMarkup(keyboard)

async def send_poll():
    await bot.send_poll(chat_id=chat_id, question=question, options=options, reply_markup=reply_markup)

asyncio.run(send_poll())