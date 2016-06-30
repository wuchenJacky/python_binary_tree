#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

strTime = time.localtime(time.time())
print(type(strTime))
print(time.asctime(strTime))
# print(time.strptime('201606028152315', '%H %m %d %H %M %S'))
struct_time = time.strptime("30 Nov 00", "%d %b %y")
print("returned tuple: {test} ".format(test=struct_time))
print(time.strftime("%H-%m-%d %H:%M:%S", strTime))
print(time.strftime("%a", strTime))
print(time.strftime("%A", strTime))
print(time.strftime("%B", strTime))
print(time.strftime("%b", strTime))
print(time.strftime("%c", strTime))
print(time.strftime("%X", strTime))
print(time.strftime("%x", strTime))
print(time.strftime("%Z", strTime))
print(strTime)

import calendar

cal = calendar.month(2016, 6)
print(cal)

from datetime import datetime
print(datetime(2002, 12, 25).isoformat(' '))

import demoPython
demo=demoPython.printDemo()
demo.printDemoPython()

Money=2000
def AddMoney():
    global Money
    print(locals())
    print(globals().get("cal"))
    Money=Money+2

print(Money)
AddMoney()
print(Money)
pass
pass
pass
pass

