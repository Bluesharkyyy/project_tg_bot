from telebot import types
from telebot import TeleBot
import sqlite3
import random
TOKEN = '7863824535:AAHv1Xv9Wt30cZRLw96V6j3M_-U-AJj7avw'
bot = TeleBot(TOKEN)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Казино')
btn2 = types.KeyboardButton('💲Баланс💲')
btn3 = types.KeyboardButton('📦Инвентарь📦')
btn4 = types.KeyboardButton('🏬Магазин🏬')
keyboard.add(btn1)
keyboard.add(btn2)
keyboard.add(btn3)
keyboard.add(btn4)

con = sqlite3.connect('inventory.db')

cursor_object = con.execute(
  """
    CREATE TABLE IF NOT EXISTS inv (
        id INTEGER PRIMARY KEY,
        name TEXT,
        kol_vo INT
    )
  """
)
con.execute(
    """
        INSERT INTO inv(name, kol_vo)
        VALUES ('печенька', 0), ('кофе', 0), ('мышь', 0)
    """
)

con.commit()
con.close()

gamble = 0
chance = 0
coins = 500
lives = 7
run = True
num = ''
cookies = 0
coffe = 0
mouses = 0



@bot.message_handler(commands=['start'])
def handle_start(msg: types.Message):
    bot.send_message(msg.chat.id, 'И снова здравствуйте!', reply_markup=keyboard)

    

@bot.message_handler(func=lambda msg: msg.text == "📦Инвентарь📦", content_types=["text"]) # инвентарь
def handle_balance(msg: types.Message):
    bot.send_message(msg.chat.id, (
        'Вот что у вас есть\n'
        f'🍪Печенек - {cookies}\n'
        '---------------------------\n'
        f'☕Кофе - {coffe}\n'
        '---------------------------\n'
        f'🖱Мышек - {mouses}\n'
        '---------------------------\n'
    ))

@bot.message_handler(func=lambda msg: msg.text == "🏬Магазин🏬", content_types=["text"]) #покупка 
def handle_balance(msg: types.Message):
    bot.send_message(msg.chat.id, (
        "1 печенька🍪 - 100 монет №1\n"
        "5 печенек🍪 - 500 монет №2\n"
        '10 печенек🍪 - 1000 монет №3 \n'
        '---------------------------\n'
        "1 кофе☕ - 200 монет №4\n"
        "5 кофе☕ - 1000 монет №5\n"
        '10 кофе☕  - 2000 монет №6 \n'
        '---------------------------\n'
        "1 Мышь🖱 - 500 монет №7\n"
        "5 Мышек🖱 - 2500 монет №8\n"
        '10 Мышек🖱 - 5000 монет №9\n'
        '---------------------------\n'
        'Для приобретения вещи напишите номер товара\n'
        'Если нужно выйти с магазина напишите (Выход)\n'
    ), reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, handle_buy)


def handle_buy(msg: types.Message):
    global cookies, coffe, mouses, coins
    if msg.text.lower() == 'выход':
        bot.send_message(msg.chat.id, 'Пока!')
        bot.register_next_step_handler(msg, handle_start)
    else:
        con = sqlite3.connect('inventory.db')
        if msg.text.isdigit():
            if msg.text == '1':
                if coins >= 100:
                    cookies += 1
                    coins -= 100
                    bot.send_message(msg.chat.id,'Вы преобрели 1 печеньку🍪!', reply_markup=keyboard)
                    con.execute(
                        f"""
                            UPDATE inv
                            SET kol_vo = kol_vo + 1
                            WHERE id = 1
                        """
                    )
                    handle_start(msg)
                else:
                    bot.send_message(msg.chat.id,'Недостаточно средств', reply_markup=keyboard)
                    handle_start(msg)
            elif msg.text == '2':
                if coins >= 500:
                    cookies += 5
                    coins -= 500
                    bot.send_message(msg.chat.id,'Вы преобрели 5 печенек🍪!', reply_markup=keyboard)
                    con.execute(
                        f"""
                            UPDATE inv
                            SET kol_vo = kol_vo + 5
                            WHERE id = 1
                        """
                    )
                    handle_start(msg)
                else:
                    bot.send_message(msg.chat.id,'Недостаточно средств', reply_markup=keyboard)
                    handle_start(msg)
            elif msg.text == '3':
                if coins >= 1000:
                    cookies += 10
                    coins -= 1000
                    bot.send_message(msg.chat.id,'Вы преобрели 10 печенек🍪!', reply_markup=keyboard)
                    con.execute(
                        f"""
                            UPDATE inv
                            SET kol_vo = kol_vo + 10
                            WHERE id = 1
                        """
                    )
                    handle_start(msg)
                else:
                    bot.send_message(msg.chat.id,'Недостаточно средств', reply_markup=keyboard)
                    handle_start(msg)
            elif msg.text == '4':
                if coins >= 200:
                    coffe += 1
                    coins -= 200
                    bot.send_message(msg.chat.id,'Вы преобрели 1 кофе☕!', reply_markup=keyboard)
                    con.execute(
                        f"""
                            UPDATE inv
                            SET kol_vo = kol_vo + 1
                            WHERE id = 2
                        """
                    )
                    handle_start(msg)
                else:
                    bot.send_message(msg.chat.id,'Недостаточно средств', reply_markup=keyboard)
                    handle_start(msg)
            elif msg.text == '5':
                if coins >= 1000:
                    coffe += 5
                    coins -= 1000
                    bot.send_message(msg.chat.id,'Вы преобрели 5 кофе☕!', reply_markup=keyboard)
                    con.execute(
                        f"""
                            UPDATE inv
                            SET kol_vo = kol_vo + 5
                            WHERE id = 2
                        """
                    )
                    handle_start(msg)
                else:
                    bot.send_message(msg.chat.id,'Недостаточно средств', reply_markup=keyboard)
                    handle_start(msg)
            elif msg.text == '6':
                if coins >= 2000:
                    coffe += 10
                    coins -= 2000
                    bot.send_message(msg.chat.id,'Вы преобрели 10 кофе☕!', reply_markup=keyboard)
                    con.execute(
                        f"""
                            UPDATE inv
                            SET kol_vo = kol_vo + 10
                            WHERE id = 2
                        """
                    )
                    handle_start(msg)
                else:
                    bot.send_message(msg.chat.id,'Недостаточно средств', reply_markup=keyboard)
                    handle_start(msg)
            elif msg.text == '7':
                if coins >= 500:
                    mouses += 1
                    coins -= 500
                    bot.send_message(msg.chat.id,'Вы преобрели 1 Мышь🖱!', reply_markup=keyboard)
                    con.execute(
                        f"""
                            UPDATE inv
                            SET kol_vo = kol_vo + 1
                            WHERE id = 3
                        """
                    )
                    handle_start(msg)
                else:
                    bot.send_message(msg.chat.id,'Недостаточно средств', reply_markup=keyboard)
                    handle_start(msg)
            elif msg.text == '8':
                if coins >= 2500:
                    mouses += 5
                    coins -= 2500
                    bot.send_message(msg.chat.id,'Вы преобрели 5 Мышек🖱!', reply_markup=keyboard)
                    con.execute(
                        f"""
                            UPDATE inv
                            SET kol_vo = kol_vo + 5
                            WHERE id = 3
                        """
                    )
                    handle_start(msg)
                else:
                    bot.send_message(msg.chat.id,'Недостаточно средств', reply_markup=keyboard)
                    handle_start(msg)
            elif msg.text == '9':
                if coins >= 5000:
                    mouses += 10
                    coins -= 5000
                    bot.send_message(msg.chat.id,'Вы преобрели 10 Мышек🖱!', reply_markup=keyboard)
                    con.execute(
                        f"""
                            UPDATE inv
                            SET kol_vo = kol_vo + 10
                            WHERE id = 3
                        """
                    )
                    handle_start(msg)
                else:
                    bot.send_message(msg.chat.id,'Недостаточно средств', reply_markup=keyboard)
                    handle_start(msg)
        else:
            bot.send_message(msg.chat.id, 'Пожалуйста напише номер что вы хотите приобрести')
            bot.register_next_step_handler(msg,handle_buy)
        




@bot.message_handler(func=lambda msg: msg.text == "💲Баланс💲", content_types=["text"]) # баланс
def handle_balance(msg: types.Message):
    bot.send_message(msg.chat.id, f'Ваш баланс: {coins}🥇')

@bot.message_handler(func=lambda msg: msg.text == "Казино", content_types=["text"]) # казино
def handle_message_casino(msg: types.Message):
    global gamble
    gamble = random.randint(0,100)

    bot.send_message(msg.chat.id,(
        'Правила:\n'
        'я загадываю число, а твоя задача угадать\n'
        'Когда ты угадаешь ты получешь 500 монет\n'
        'если проиграешь то заберу у тебя 200 монет\n'
        '---------------------------\n'
        'я уже загадал, можешь писать\n'
    ), reply_markup=types.ReplyKeyboardRemove())
  
    bot.register_next_step_handler(msg, handle_message_gambler)


def handle_message_gambler(msg: types.Message):
    global gamble, coins, lives, run
    if lives > 0:
        if msg.text.isdigit():
            num = int(msg.text)
            if num > gamble:
                bot.send_message(msg.chat.id,f'Твое число больше загаданого, жизней {lives}❤')    
                lives -= 1
                bot.register_next_step_handler(msg, handle_message_gambler)
            elif num < gamble:
                bot.send_message(msg.chat.id,f' Твое число меньше загаданого, жизней {lives}❤')
                lives -= 1
                bot.register_next_step_handler(msg, handle_message_gambler)
            elif num == gamble:
                bot.send_message(msg.chat.id,'Угадал, маладец,  +500 монет🥇, чтобы начать игру снова нажмите на кнопку [Казино]',reply_markup=keyboard)
                coins += 500
                lives = 7
        else:
            bot.send_message(msg.chat.id, 'Напишите пожалуйста число')  
            bot.register_next_step_handler(msg, handle_message_gambler)
    else:
        run = False
        coins -= 250
        lives = 7
        bot.send_message(msg.chat.id,'Ты не смог угадать?  -250монет🥇, чтобы начать игру снова нажмите на кнопку [Казино]',reply_markup=keyboard)

con.close()
bot.polling(non_stop=True, interval=1)


