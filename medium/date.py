""" write a function that takes a year in the Gregorian calendar as an integer and returns the day of October on 
which Ada Lovelace day falls, also as an integer.

>>> lovelace_day(2015)
6
>>> lovelace_day(2020)
6
>>> lovelace_day(2019)
8
"""
import calendar

def lovelace_day(year):
    c = calendar.TextCalendar(calendar.SUNDAY)
    days = [i for i in c.itermonthdays(year, 10)]
    print(days[9])








if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HAPPY LOVELACE DAY!!\n")