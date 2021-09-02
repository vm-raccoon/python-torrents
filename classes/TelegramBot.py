import telebot
from time import sleep


class TelegramBot:

    def __init__(self, token):
        self.bot = telebot.TeleBot(token, parse_mode="HTML")
        # self.countMessages = 0
        # self.maxCountMessages = 10
        self.timeout = 2

    def sendMessage(self, chatID, uriObject):
        # if self.countMessages > self.maxCountMessages:
        #     self.countMessages = 0
        #     sleep(self.timeout)
        try:
            self.bot.send_message(chatID, "\n".join([
                "<a href='{}'>\U0001F517 <b>{}</b></a>\n".format(uriObject.uri, uriObject.name),
                "{}".format(uriObject.value),
            ]))
            # self.countMessages = self.countMessages + 1
            sleep(self.timeout)
            return True
        except Exception as e:
            print(e)
            return False
