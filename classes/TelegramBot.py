import telebot


class TelegramBot:

    def __init__(self, token):
        self.bot = telebot.TeleBot(token, parse_mode="HTML")

    def sendMessage(self, chatID, uriObject):
        try:
            self.bot.send_message(chatID, "\n".join([
                "<a href='{}'>\U0001F517 <b>{}</b></a>\n".format(uriObject.uri, uriObject.name),
                "{}".format(uriObject.value),
            ]))
            return True
        except Exception as e:
            print(e)
            return False
