from classes.Config import Config
from classes.Database import Database as DB
from classes.TelegramBot import TelegramBot


for item in Config(__file__, "config.json").read():
    db = DB(item["sqlite"])
    uriList = db.getListURI()
    exceptionList = db.getListException()

    for u in uriList:
        update = u.getUpdate()

        if update in exceptionList or u.value == update:
            continue

        u.value = update
        db.setUpdate(u.id, update)

        bot = TelegramBot(item["telegram"]["bot_token"])
        bot.sendMessage(item["telegram"]["chat_id"], u)

