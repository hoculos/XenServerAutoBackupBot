from RocketChatBot import RocketChatBot
import datetime
import os

botname = os.environ['BOTNAME'] = 'login' # Login bot in chat
botpassword = os.environ['BOTPASSWORD'] = 'password' #Pass bot in chat
server_url = os.environ['BOT_URL'] = '' # Url rocket chat

bot = RocketChatBot(botname, botpassword, server_url)


def SendLogToChat(path):
    with open(path, 'r') as file:
        data = file.read().rstrip()
        bot.send_message(data, channel_id='VmBacups')
        file.close()


def main():
    host1 = 'YOUR_HOST1' #Hostname xen server
    host2 = 'YOUR_HOST2' #Hostname xen server

    date = datetime.datetime.today()
    date.strftime("%d-%m-%Y")

    path1 = '/var/backup/' + host1 +'/' + date.strftime("%d-%m-%Y") + '/backup.log'
    path2 = '/var/backup/' + host2 +'/'+ date.strftime("%d-%m-%Y") + '/backup.log'

    try:
        SendLogToChat(path1)
    except FileNotFoundError:
        bot.send_message(date.strftime("%d-%m-%Y") + ' ' + host1 + ' log not found...', channel_id='VmBacups')

    try:
        SendLogToChat(path2)
    except FileNotFoundError:
        bot.send_message(date.strftime("%d-%m-%Y") + ' ' + host2 + ' log not found...', channel_id='VmBacups')


main()
