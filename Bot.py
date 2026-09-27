from telebot import*
import subprocess



API_TOKEN = 'YOUR_BOT_API'
ADMIN_ID = YOUR_TELEGRAM_ID







bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    user = message.from_user
    user_id = user.id
    name = user.first_name
    if user_id == ADMIN_ID:
        bot.reply_to(message, f'Привет Admin-{user_id}')
    else:
        bot.reply_to(message, f'Привет {name}, ты не можешь использовать этого бота')


@bot.message_handler(commands=['help'])
def send_help(message):
    user = message.from_user
    user_id = user.id
    if user_id == ADMIN_ID:

        bot.send_message(message.chat.id, 'Используй /rcon')

    else:
        bot.send_message(message.chat.id, 'Ты не можешь использовать этого бота')
    




@bot.message_handler(commands=['rcon'])
def rcon(message):
    user = message.from_user
    chat_id = user.id
    if chat_id == ADMIN_ID:
        sent_message = bot.send_message(message.chat.id, 'Напиши сообщение')
        bot.register_next_step_handler(sent_message, rco)
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование команды')

def rco(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, 'Ты отменил')
        return

    c = message.text

    res = subprocess.run(['python3', 'rcon.py', f'{c}'], capture_output=True,text=True)

    otputput_res = res.stdout.strip()
    try:

        bot.send_message(message.chat.id, f'{otputput_res}')

    except Exception:
        bot.send_message(message.chat.id, 'Всё ок!')
   



        
@bot.message_handler(func=lambda message: not message.text.startswith("/"))
def s(message):
    user = message.from_user
    username = user.username
    user_id = user.id
    if user_id == ADMIN_ID:

        bot.send_message(message.chat.id, f'Буть добр использовать комнады @{username}')

    else:
        bot.send_message(message.chat.id, 'Ты не можешь использовать этого бота')


if user_id in ADMIN_ID:
    print('ok')



bot.infinity_polling()
