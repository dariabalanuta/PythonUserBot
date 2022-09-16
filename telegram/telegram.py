from pyrogram import Client
from time import time, sleep

app = Client("my_account")
users = []

with open('users.txt', 'r') as file:
        users = file.readlines()
        users = [x.strip() for x in users]

        def sent_message():
            for user in users:
                sleep(20 - time() % 20)
                with app:
                    app.send_message(user, "Привет! Предлагаю разместится у меня на канале\n"
                                        "Цена 400(под закуп)\n"
                                        "https://t.me/GEONewsss\n")
                    app.send_photo(user, "stata.jpg")

sent_message()