import telebot
from env import token 
from main import *


bot = telebot.TeleBot(token)
main()
keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('News')
button2 = telebot.types.KeyboardButton('Description')
button3 = telebot.types.KeyboardButton('Photo')
keyboard.add(button1)
show = keyboard.add(button2,button3)


@bot.message_handler(commands=['start'])
def start_dunction(message):    
    bot.send_message(message.chat.id, 'Здраствуйте',reply_markup=keyboard)
    bot.register_next_step_handler(message,get_news)
    
def get_news(message):
    for i,k in enumerate(zip1):
        bot.send_message(message.chat.id, i+1)
        bot.send_message(message.chat.id, k)
    bot.register_next_step_handler(message,start_game)
    bot.send_message(message.chat.id, 'Нажмите Кнопку Description')
    

def start_game(message):
    if button2:
        msg = bot.send_message(message.chat.id, 'Введите индекс ')
        bot.register_next_step_handler(message,news_open)


def news_open(message):
    bot.send_message(message.chat.id, f'{dict_.get(str(message.text))}', reply_markup=show)
    about_new(message, dict_.get(str(message.text.strip())))
    bot.send_photo(message.chat.id, f'{dict__.get(str(message.text))}')
    # if button3:
    #     bot.send_photo(message.chat.id, f'{dict__.get(str(message.text))}')
    # bot.register_next_step_handler(message, func)

# def check(message):
#     if message.text == 'Description':
#         about_new(message, dict_.get(str(message.text.strip())))
#     elif message.text == 'Photo':
#         bot.send_photo(message.chat.id, f'{dict__.get(str(message.text))}')



def about_new(message,str):
    url=zip1.get(str)
    html =get_html(url)
    soup=get_soup(html)
    get_info(message,soup)
    
def get_info(message,soup):
    aboutt=soup.find_all('div', class_='BbCode')
    for abou in aboutt:
        try:
            abou=abou.text.strip()
        except AttributeError:
            abou=''
        bot.send_message(message.chat.id,f'{abou}')


bot.polling()

