from datetime import datetime, timedelta


DATE_FORMAT = "%Y.%m.%d"
WEEK = 7
FRIDAY = 5

def get_upcoming_birthdays(users):
    congratulation_list = []
    today = datetime.today().date()
    for user in users:
        birthday_date = datetime.strptime(user["birthday"], DATE_FORMAT).date()
        congratulation_date = datetime(
            year=today.year, month=birthday_date.month, day=birthday_date.day
        ).date()
        dif = (congratulation_date - today).days

        if 0 <= dif and dif < WEEK:
            weekday = congratulation_date.isoweekday()
            if FRIDAY < weekday:
                days_to_monday = timedelta(days=(WEEK - weekday + 1))
                congratulation_date += days_to_monday

            congratulation_list.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime(DATE_FORMAT),
                }
            )

    return congratulation_list


users = [
    {"name": "John Doe", "birthday": "1985.10.11"},
    {"name": "Jane Smith", "birthday": "1990.10.12"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:")
for user in upcoming_birthdays:
    print(f"{user["name"]:<15} {user["congratulation_date"]}")
