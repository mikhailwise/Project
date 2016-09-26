import numpy as np
import time

# current time and tz difference from gmt
limit = time.time()
tz = -4

#basic calculations
yearLength = 365*24*60*60
dayLength = 24*60*60
hourLength = 60*60
minuteLength = 60

#dictionary for month to day of the year
def months(x):
    return{
        31 : 'January',
        59 : 'February',
        90 : 'March',
        120 : 'April',
        151 : 'May',
        181 : 'June',
        212 : 'July',
        243 : 'August',
        273 : 'September',
        304 : 'October',
        335 : 'November',
        365 : 'December'
    }[x]

#indexes for ly and not ly
dayToMonth = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335, 365]
dayToMonthLeap = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 336, 366]

for current in range(0,int(limit),1000000):
    #so these calcs are the unix timestamp/length of things
    #should yield total number since the beginning
    days = current/dayLength
    #for today and the first day of 1970 ^ ?
    #this is odd, I did the math manually and I always am 2 days off
    hours = current/hourLength
    minutes = current/minuteLength

    #initializing list of leap years
    ly = []

    #acquire for leapyears between then and now
    for y in range(1970,2030):
        if (np.mod(y,4)==0):
            ly.append(y)

    #guess the year
    yearApprox = 1970 + int(days/365)

    #count leapyears
    leaps = 0
    for leap in ly:
        if leap <= yearApprox:
            leaps += 1
    #if the ly days offset is more than the day of the year we need to
    #roll back a year and subtract the remaining days
    if np.mod(current, yearLength)/dayLength < leaps:
        year = yearApprox - 1
        day = 365 - (leaps - mod(days, 365))
    else:
        year = yearApprox
        day = int(np.mod(days, 365)) - 12

    #check if we are in a leapyear
    for y in ly:
        if year == y:
            leapCheck = True
            break
        else:
            leapCheck = False

    #this indexes what month we are in depending on if it is a leapyer
    if leapCheck == False:
        for d in dayToMonth:
            if day <= d:
                month = months(d)
                before = dayToMonth[dayToMonth.index(d)-1]
                date = np.mod(day, before)
                break
    else:
        for d in dayToMonthLeap:
            if d >= day:
                if day < 31:
                    month = months(d)
                    date = day
                    break
                elif day < 59 and day > 31:
                    month = months(d)
                    before = dayToMonthLeap[dayToMonthLeap.index(d)-1]
                    date = np.mod(day, before)
                    break
                else:
                    month = months(d-1)
                    before = dayToMonthLeap[dayToMonthLeap.index(d)-1]
                    date = np.mod(day, before)
                    break

    #this is really ghetto but it decides the hour and whether is am or pm
    hour = int(np.mod(hours + tz, 24))
    if hour >= 12:
        split = 'PM'
    else:
        split = 'AM'

    #show the hour properly
    hourNormal = np.mod(hour, 12)

    #this is just ghetto formatting so we always have a leading 0 if it is a one digit number
    if hourNormal == 0:
        hourNormal = 12
    if hourNormal < 10:
        hourNormal = '0' + str(hourNormal)
    minute = int(np.mod(minutes, 60))
    if minute < 10:
        minute = '0' + str(minute)
    second = int(np.mod(current, 60))
    if second < 10:
        second = '0' + str(second)

    #prints is all out
    print month, str(date) +', ', str(year), ' ', str(hourNormal) + ':' + str(minute) + ':' + str(second) + ' ' + split
