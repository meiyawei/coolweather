import datetime


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(hours=120)
    yesterday = today - oneday
    return yesterday


print(getYesterday())
