from collections import defaultdict
from datetime import datetime


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 3, 3)},
    {"name": "Jan Khoum", "birthday": datetime(2003, 3, 5)},
    {"name": "Jill Valentine", "birthday": datetime(1981, 3, 4)},
    {"name": "Kim Kardashian", "birthday": datetime(2014, 3, 8)},
    {"name": "Tomas Addison", "birthday": datetime(2003, 3, 5)},
    {"name": "John Doe", "birthday": datetime(1995, 3, 8)},
    ]

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year = today.year)
        is_monday = today.weekday() == 0
        is_birthday_next_year = (not is_monday and birthday_this_year < today) or (is_monday and birthday_this_year < today.replace(day = today.day - 2))
        if is_birthday_next_year:
            birthday_this_year = birthday.replace(year = today.year + 1)
        
        delta_start = 0
        delta_end = 7
        if is_monday:
            delta_start = -2
            delta_end = 5
        delta_days = (birthday_this_year - today).days
        if delta_days > delta_start and delta_days < delta_end:
            str_day_of_week = birthday_this_year.strftime('%A')
            if str_day_of_week in ['Saturday', 'Sunday']:
                str_day_of_week = 'Monday'
            birthdays_per_week[str_day_of_week].append(name)
    for day, users in birthdays_per_week.items():
        print(f"{day}: {', '.join(users)}")
            


get_birthdays_per_week(users)