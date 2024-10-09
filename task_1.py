from datetime import datetime


def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        dif = today - date
        print(dif.days)
    except Exception as e:
        print(e)


get_days_from_today("2025-10-09")
