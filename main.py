from telebot import TeleBot
import schedule, time, datetime
from instagram import Account, WebAgent

bot = TeleBot('1228395330:AAEPH5rF1oNLXiuFBSZ26aosz-g_n3AiFfk')

with open("posted_photos.txt") as file:
    data = [row.strip() for row in file]

agent = WebAgent()
account = Account("erotic_model_girls")

agent.update(account)

media = agent.get_media(account, count=9999)[0]
count = 1

now = datetime.datetime.now()


def job():
    global count
    global media
    while True:
        m = media[-count]
        count += 1
        if m.id in data or m.is_video:
            continue
        else:
            data.append(m.display_url)
            with open("posted_photos.txt", "a") as a_file:
                a_file.write(m.id)
                a_file.write("\n")
            try:
                bot.send_photo(chat_id='@n_a_g_r_a_n_i', photo=m.display_url)
            except:
                print('except')
                print(datetime.datetime.now())
                bot.send_photo(chat_id='@n_a_g_r_a_n_i', photo=m.display_url)
            break


# for m in media:
#     if m.id in data or m.is_video:
#         continue
#
#     data.append(m.display_url)
#     with open("posted_photos.txt", "a") as a_file:
#         a_file.write(m.id)
#         a_file.write("\n")
#     bot.send_photo(chat_id='@svalka_2', photo=m.display_url)


schedule.every().day.at("08:45").do(job)
schedule.every().day.at("11:00").do(job)
schedule.every().day.at("13:30").do(job)
schedule.every().day.at("15:00").do(job)
schedule.every().day.at("17:20").do(job)
schedule.every().day.at("19:30").do(job)
schedule.every().day.at("21:25").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
