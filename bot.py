import telebot
import requests

s_city = "Moscow"
city_id = 524901
appid = "appid"  # appid находится в файле .gitignore, просто скопируйте и вставьте вместо слова appid
bot = telebot.TeleBot('token')  # token находится в файле .gitignore, просто скопируйте и вставьте вместо слова token
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
d1 = data['weather'][0]['description']
d2 = data['main']['temp']
d3 = data['main']['temp_max']
d4 = data['main']['temp_min']
d5 = data['wind']['speed']
d6 = data['main']['humidity']


@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id, "Погода в Москве на сегодня: " + str(d1) + '\n' + "Температура воздуха: "
                     + str(d2) + "°C\n"
                     + "Минимальная температура воздуха: " + str(d4) + "°C\n" +
                     "Максимальная температура воздуха: " + str(d3) + "°C\n" +
                     "Скорость ветра: " + str(d5) + " м/с\n" +
                     "Влажность воздуха: " + str(d6) + "%\n")


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "Чтобы узнать погоду в Москве сегодня введите команду: /info")


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Добро пожаловать в чат с актуальной погодой в Москве\n"
                                      "Чтобы узнать погоду на сегодня введите команду: /info\n")


if __name__ == '__main__':
    bot.polling(none_stop=True)
