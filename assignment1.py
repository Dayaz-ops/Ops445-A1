#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Winter 2025
Program: assignment1.py 
Author: "Daniyal Ayaz"
The python code in this file (a1_111408167.py) is original work written by
"Daniyal Ayaz". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

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
    str_year, str_month, str_day = date.split('-')  # Split date into parts
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    tmp_day = day + 1  # Increment day by 1

    # Check if day exceeds the month's maximum days
    if tmp_day > mon_max(month, year):
        to_day = 1
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month

    # If month exceeds 12, move to next year
    if tmp_month > 12:
        to_month = 1
        year += 1
    else:
        to_month = tmp_month

    # Format new date
    next_date = f"{year}-{to_month:02}-{to_day:02}"
    return next_date

if __name__ == "__main__":
    print(after('2023-01-25'))  # Example test line for now
