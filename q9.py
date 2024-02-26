from datetime import datetime


def days_since_birthday(birthday_str):
    # Parse the birthday string into a datetime object
    birthday = datetime.strptime(birthday_str, "%d-%m-%Y")

    # Get the current date
    current_date = datetime.now()

    # Calculate the difference in years
    years_diff = current_date.year - birthday.year - 1  # Subtract 1 to not count the current year

    # Initialize the count of days
    days_count = 0

    # Count the days for the whole years
    for year in range(birthday.year + 1, current_date.year):
        # Check if the year is a leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_count += 366  # Leap year
        else:
            days_count += 365  # Non-leap year

    return days_count


# Your birthday in DD-MM-YYYY format
your_birthday = "04-03-2004"

# Calculate the days since your birthday
days_since_your_birthday = days_since_birthday(your_birthday)
days_since_your_birthday



