<img src="https://j.gifs.com/P7DOB4.gif" width="250" height="444,6" />


Умный сервис прогноза погоды

Базовый уровень сложности

Был выбран язык программирования python, пользовательским интерфейсом будет чат-бот в telegram, данные, получаемые с
API подставляются в текстовый шаблон: 

Погода в Москве на сегодня: ___
Температура воздуха: ___
Минимальная температура воздуха: ___
Максимальная температура воздуха: ___
Скорость ветра: ___
Влажность воздуха: ___


Сервис - чат-бот, принимает ограниченный набор команд:

start - запуск бота, информация о доступной команде /info

help - информация о доступной команде /info

info - основная команда этого бота, данные получаемые с API подставляются в шаблон,
и ответ с данными отправляется пользователю в виде сообщения

Чтобы запустить бота необходимо запустить программу bot.py (проще всего в PyCharm), при этом установив последние версии библиотек:
pyTelegramBotAPI (version 3.7.2), requests (version 2.7.0), также скопировав значения token и appid из файла .gitignore и вставив их в соответсвующие позиции в коде.

Воспользоваться ботом можно перейдя по ссылке: t.me/weatherinmoscowwwbot




