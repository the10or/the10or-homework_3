from datetime import date, datetime


def get_birthdays_per_week(users):
    today = date.today()
    birthdays = {}
    for user in users:
        year = today.year + 1 if (today.month == 12 and today.day > 24) and user["birthday"].month == 1 else today.year
        birthday = datetime(year, user["birthday"].month, user["birthday"].day).date()
        if 0 <= (birthday - today).days < 7:

            weekday = birthday.strftime("%A")
            if weekday == 'Saturday' or weekday == 'Sunday':
                weekday = 'Monday'

            name = user["name"].split()[0]
            if weekday in birthdays.keys():
                birthdays[weekday].append(name)
            else:
                birthdays[weekday] = [name]

    return birthdays


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
