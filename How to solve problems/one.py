# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 


months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if ((year % 100 != 0) or (year % 400 == 0)) and (year % 4 == 0):
        return True
    return False

def daysInMonth(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month == 2:
        if not isLeapYear(year, month):
            return 28 
        return 29
    else:
        return 30

    return months[month - 1]


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""

    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    assert not isDateBefore(year2, month2, day2, year1, month1, day1)
    
        
    days = 0
    
    while isDateBefore(year1, month1, day1, year2, month2, day2):
        year1, month1 , day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def isDateBefore(year1, month1, day1, year2, month2, day2):
    if year2 > year1:
        return True
    elif year2 == year1:
        if month2 > month1:
            return True
        elif month2 == month1:
            if day2 > day1:
                return True
    return False

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2112,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        print(result)

test()
    