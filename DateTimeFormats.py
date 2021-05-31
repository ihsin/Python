"""
#https://www.programiz.com/python-programming/datetime/strftime
Write a Python script to display the various Date Time formats.

a) Current date and time
  - current time
  - current date
b) Current year (Y)
c) Month of year
"""

from datetime import datetime
import time

print("Current date and time: {}".format(datetime.now()))
#Current date and time: 2021-05-30 00:51:39.057707
print("Current time: {}".format(datetime.now().time()))
#Current time: 00:51:39.057807
print("Current date: {}".format(datetime.now().date()))
#Current date: 2021-05-30
print("Current year: {}".format(datetime.now().strftime("%Y")))
#Current year: 2021
print("Current year(short): {}".format(datetime.now().strftime("%y")))
#Current year(short): 21
print("Month of the year: {}".format(datetime.now().strftime("%B")))
#Month of the year: May

