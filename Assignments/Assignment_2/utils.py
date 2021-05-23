import os


RAW = "data/raw/"
PRE = "data/preprocessed/"
AUG = "data/augmented/"
ADD = "data/add/"
LEN = 5


def calculate_return(close_init, close_final):
    return 100 * (close_final - close_init) / close_init


def is_continues(date_0, date_1):
    leap_years = (2020, 2016, 2012, 2008, 2004, 2000, 1996, 1992, 1988, 1984, 1980, 1976, 1972, 1968, 1964, 1960)
    y1, m1, d1 = map(int, date_0.split('-'))
    y2, m2, d2 = map(int, date_1.split('-'))
    if d1 + 1 == d2:
        return True
    if m1 in (1, 3, 5, 7, 8, 10, 12) and d1 == 31 and d2 == 1:
        return True
    if m1 in (4, 6, 9, 10) and d1 == 30 and d2 == 1:
        return True
    if m1 == 2 and y1 in leap_years and d1 == 29 and d2 == 1:
        return True
    if m1 == 2 and y1 not in leap_years and d1 == 28 and d2 == 1:
        return True
    return False
