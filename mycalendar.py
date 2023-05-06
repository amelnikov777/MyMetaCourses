import sys
locations = sys.path
for i in locations:
    print(i)

import calendar

leapdays = calendar.leapdays(2000,2050)
print(leapdays)
formatyearpage()

