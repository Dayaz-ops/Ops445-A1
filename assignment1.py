#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Winter 2025
Program: assignment1.py 
Author: Dayaz
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def usage():
    "Print a usage message to the user"
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    exit()

def leap_year(year: int) -> bool:
    "Return True if the year is a leap year"
    if year % 4 != 0:
        return False
    if year % 100 == 0 and year % 400 != 0:
        return False
    return True

def mon_max(month: int, year: int) -> int:
    "Returns the maximum day for a given month. Includes leap year check"
    if month == 2:
        return 29 if leap_year(year) else 28
    mon_days = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return mon_days.get(month, 0)

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format
    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This function has been tested to work for years after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    tmp_day = day + 1

    if tmp_day > mon_max(month, year):
        to_day = 1
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month

    if tmp_month > 12:
        to_month = 1
        year += 1
    else:
        to_month = tmp_month

    next_date = f"{year}-{to_month:02}-{to_day:02}"
    return next_date

def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    try:
        parts = date.split('-')
        if len(parts) != 3:
            return False
        year, month, day = map(int, parts)
        if year < 1500 or month < 1 or month > 12:
            return False
        if day < 1 or day > mon_max(month, year):
            return False
        return True
    except:
        return False

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {1: 0, 2: 3, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    weekend_count = 0
    current = min(start_date, stop_date)
    end = max(start_date, stop_date)

    while True:
        y, m, d = map(int, current.split('-'))
        dow = day_of_week(y, m, d)
        if dow in ['sat', 'sun']:
            weekend_count += 1
        if current == end:
            break
        current = after(current)
    return weekend_count

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    d1 = sys.argv[1]
    d2 = sys.argv[2]

    if not valid_date(d1) or not valid_date(d2):
        usage()

    start = min(d1, d2)
    end = max(d1, d2)

    count = day_count(start, end)
    print(f"The period between {start} and {end} includes {count} weekend days.")

