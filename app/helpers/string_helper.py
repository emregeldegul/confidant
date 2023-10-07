from datetime import date


def get_day_of_week(date_object: date):
    day_of_week = date_object.weekday()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[day_of_week]
