################################################################################################################
#                       Project Euler Problem 19 Solution -- Counting Sundays
#                                           By Mike Kane
#
#  You are given the following information, but you may prefer to do some research for yourself.
#
#  1 Jan 1900 was a Monday.
#  Thirty days has September,
#  April, June and November.
#  All the rest have thirty-one,
#  Saving February alone,
#  Which has twenty-eight, rain or shine.
#  And on leap years, twenty-nine.
#  A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#  How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
################################################################################################################


def getAnswer():
    #Declaring Necessary Variables
    totalDateCounter = 1
    monthValues = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leapYearValues = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = 0
    
    for year in range(1901, 2000):
        if year % 4 == 0:
            for month in leapYearValues:
                if totalDateCounter % 7 == 0:
                    answer += 1
                for day in range(month):
                    totalDateCounter += 1
        else:
            for month in monthValues:
                if totalDateCounter % 7 == 0:
                    answer += 1
                for day in range(month):
                    totalDateCounter += 1
    return answer
                    
    
    
