from telebot import TeleBot
import schedule, time, datetime
from instagram import Account, WebAgent

bot = TeleBot('1228395330:AAEPH5rF1oNLXiuFBSZ26aosz-g_n3AiFfk')


with open("posted_photos.txt") as file:
    data = [row.strip() for row in file]

agent = WebAgent()
account = Account("sexyhotgrl")

agent.update(account)

media = agent.get_media(account, count=9999)[0]
count = 1


def job():
    global count
    global media
    while True:
        m = media[-count]
        count += 1
        if m.display_url in data or m.is_video:
            continue
        else:
            data.append(m.display_url)
            with open("posted_photos.txt", "a") as a_file:
                a_file.write(m.display_url)
                a_file.write("\n")
            bot.send_photo(chat_id='@n_a_g_r_a_n_i', photo=m.display_url)
            break


# for m in media:
#     if m.display_url in data or m.is_video:
#         continue
#
#     data.append(m.display_url)
#     with open("posted_photos.txt", "a") as a_file:
#         a_file.write(m.display_url)
#         a_file.write("\n")
#     job(m.display_url)


schedule.every().day.at("17:04").do(job)
schedule.every().day.at("17:40").do(job)
schedule.every().day.at("18:55").do(job)
schedule.every().day.at("19:30").do(job)
schedule.every().day.at("20:35").do(job)
schedule.every().day.at("21:20").do(job)

now = datetime.datetime.now()

while True:
    if now.hour == 22:
        break

    schedule.run_pending()
    time.sleep(55)
