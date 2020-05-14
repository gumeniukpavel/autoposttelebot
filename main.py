from telebot import TeleBot
import schedule
import time
from instagram import Account, WebAgent

bot = TeleBot('1228395330:AAEPH5rF1oNLXiuFBSZ26aosz-g_n3AiFfk')

with open("posted_photos.txt") as file:
    data = [row.strip() for row in file]

agent = WebAgent()
account = Account("sexyhotgrl")

agent.update(account)

media = agent.get_media(account, count=9999)[0]


def job(url):
    bot.send_photo(chat_id='@svalka_2', photo=url)


for m in media:
    if m.display_url in data or m.is_video:
        continue

    data.append(m.display_url)
    with open("posted_photos.txt", "a") as a_file:
        a_file.write(m.display_url)
        a_file.write("\n")
    job(m.display_url)


# schedule.every(1).minutes.do(job)
#
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
