import telebot
from telebot import types
import COVID19Py
from covid import Covid
covid = Covid(source="worldometers")
covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1110568887:AAGUY6hAiNqGHUno5FS6kjnyHY3s3UD9kBg')


# Функция, что сработает при отправке команды Старт
# Здесь мы создаем быстрые кнопки, а также сообщение с привествием
@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('Total')
	btn2 = types.KeyboardButton('Uzbekistan')
	btn3 = types.KeyboardButton('Turkey')
	btn4 = types.KeyboardButton('Russia')
	btn5 = types.KeyboardButton('US')
	btn6 = types.KeyboardButton('Italy')
	markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

	send_message = f"Hi {message.from_user.first_name}!Welcom to COVID-19 BOT " \
		f"made by http://kholmirzaev.ru/"
	bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
	final_message = ""
	get_message_bot = message.text.strip().lower()
	if get_message_bot == "uzbekistan":
		location = covid.get_status_by_country_name("uzbekistan")
	elif get_message_bot == "turkey":
		location = covid.get_status_by_country_name("turkey")
	elif get_message_bot == "russia":
		location = covid.get_status_by_country_name("russia")
	elif get_message_bot == "us":
		location = covid.get_status_by_country_name("usa")
	elif get_message_bot == "italy":
		location = covid.get_status_by_country_name("italy")
	else: location = covid19.getLatest()

	final_message = f"Active Cases: {location['confirmed']:,} Death: {location['deaths']:,}"
	if final_message == "": final_message ="dsfdsf"
	bot.send_message(message.chat.id, final_message, parse_mode='html')
# Это нужно чтобы бот работал всё время
bot.polling(none_stop=True)
