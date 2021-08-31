from classes.Config import Config
from classes.Database import Database as DB
from classes.TelegramBot import TelegramBot


for item in Config(__file__, "config.json").read():
    db = DB(item["sqlite"])
    uri = db.getListURI()
    exception = db.getListException(as_list=True)

    # print(exception[0])

    # bot = TelegramBot(item["telegram"]["bot-token"])
    # bot.sendMessage(item["telegram"]["chat_id"], overviewCopy)
