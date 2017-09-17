# Hint:  use Google to find python function
import datetime

from time import strftime
import calendar
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

###b)
date_start = '12312013'
date_stop = '05282015'

####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'


def days_between_one(date1, date2):
    #finds the difference for section a
    date1_arr = date1.split("-")
    date2_arr = date2.split("-")
    date1 = datetime.date(int(date1_arr[2]), int(date1_arr[0]), int(date1_arr[1]))
    date2 = datetime.date(int(date2_arr[2]), int(date2_arr[0]), int(date2_arr[1]))
    diff = date2-date1
    return diff.days

def days_between_two(date1, date2):
    date1 = datetime.date(year=int(date1[4:]), month=int(date1[0:2]), day=int(date1[2:4]))
    date2 = datetime.date(year=int(date2[4:]), month=int(date2[0:2]), day=int(date2[2:4]))
    diff = date2 -date1
    return diff.days

def days_between_three(date1, date2):
    date1 = datetime.datetime.strptime(date1,"%d-%b-%Y")
    date2 = datetime.datetime.strptime(date2,"%d-%b-%Y")
    diff = date2-date1
    return diff.days

# print days_between_two(date_start, date_stop)
print date_start, date_stop
print days_between_three(date_start, date_stop)


