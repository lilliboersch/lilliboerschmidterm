def days_since_birthday(birthday):
    birth_day, birth_month, birth_year = map(int, birthday.split('-'))
    current_day, current_month, current_year = 26, 2, 2024

    days = 0
    for year in range(birth_year + 1, current_year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days += 366
        else:
            days += 365

    return days


birthday = "04-03-2004"
days = days_since_birthday(birthday)
print(days)
