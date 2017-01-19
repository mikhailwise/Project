import numpy as np
import time

current = time.time()
tz = -4
yearLength = 365*24*60*60
dayLength = 24*60*60
hourLength = 60*60
minuteLength = 60

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

dayToMonth = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335, 365]
dayToMonthLeap = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 336, 366]

days = current/dayLength
hours = current/hourLength
minutes = current/minuteLength

ly = []

for y in range(1970,2030):
    if (np.mod(y,4)==0):
        ly.append(y)

yearApprox = 1970 + int(days/365)

leaps = 0
for leap in ly:
    if leap <= yearApprox:
        leaps += 1

if np.mod(current, yearLength)/dayLength < leaps:
    rollOver = True
    year = yearApprox - 1
    day = 365 - (leaps - mod(days, 365))
    print rollOver
else:
    year = yearApprox
    day = int(np.mod(days, 365) - leaps)

for y in ly:
    if year == y:
        leapCheck = True
        break
    else:
        leapCheck = False

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

hour = int(np.mod(hours + tz, 24))
if hour >= 12:
    split = 'PM'
else:
    split = 'AM'

hourNormal = np.mod(hour, 12)

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


print month, str(date) +', ', str(year), ' ', str(hourNormal) + ':' + str(minute) + ':' + str(second) + ' ' + split
