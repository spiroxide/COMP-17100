# Erich Ostendarp
# 10/24/17
# Prints the user's age in days, hours, minutes and seconds


def yearsToDays(years):
    """
    Converts years to days
    :param years: number of years
    :return: number of days in those years
    """
    return years * 365


def daysToHours(days):
    """
    Converts days to hours
    :param days: number of days
    :return: number of hours in those days
    """
    return days * 24


def hoursToMinutes(hours):
    """
    Converts hours to minutes
    :param hours: number of hours
    :return: number of minutes in those hours
    """
    return hours * 60


def minutesToSeconds(minutes):
    """
    Converts minutes to seconds
    :param minutes: number of minutes
    :return: number of seconds in those minutes
    """
    return minutes * 60


def main():
    age = int(input("Enter your age: "))
    dayAge = yearsToDays(age)
    hourAge = daysToHours(dayAge)
    minuteAge = hoursToMinutes(hourAge)
    secondAge = minutesToSeconds(minuteAge)
    print("days: ", dayAge, " hours: ", hourAge, " minutes: ", minuteAge, " seconds: ", secondAge)


main()
