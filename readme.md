!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## Перед первым запуском запуском:
# Установка ПО
1) Установить PostgreSQL
2) Установить Python
3) Установить Node.js

# Настройка PostgreSQL
2) Создать новую БД в PostgreSQL и восстановить из дампа "start.sql"
3) В файле ./back-end/config.py заполнить поля dbname, user, password, host, port данными, соответствующими вашей БД

# Настройка Python
1) Открыть консоль в папке ./back-end и последовательно ввести команды
2) python -m venv venv (для Windows)
   python3 -m venv venv (для Linux)
3) venv\Scripts\activate (для Windows) 
   venv/bin/activate (для Linux)
4) python -m pip install --upgrade pip
5) pip install -r requirements.txt

# Настройка React
1) Открыть консоль в папке ./front-end и ввести команду npm i

# Подключение бота для уведомлений
1) Перейдите по ссылке https://t.me/test_task_qaz123wsxedc234_bot 
2) Напишите боту /start
(Бот будет присылать уведомления об устаревших поставках каждый день в 8 утра)

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## Для запуска (первого и последующих):
# Python
1) Открыть консоль в папке ./back-end и последовательно ввести команды
2) venv\Scripts\activate (для Windows) 
   venv/bin/activate (для Linux)
3.1) python app.py 
     для запуска в режиме, когда база обновляется только от запросов с клиента
3.2) python app.py --schedule
     для запуска в режиме, когда база обновляется каждые 10 секунд, пока работает приложение

# React
1) Открыть консоль в папке ./front-end и ввести команду npm start