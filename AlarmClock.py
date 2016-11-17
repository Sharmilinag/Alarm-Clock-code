import random
import time
import webbrowser
from datetime import datetime,timedelta
import subprocess
lines = open("C:\Python_code\Links.txt").read().splitlines()
mylines = random.choice(lines)
print "Alarm tone: " , mylines
time_input = str(raw_input("Please enter the time in HH:MM:SS format: "))
current_date = str(raw_input("Please enter the date in YYYY/MM/DD format: "))
selected_time = datetime.strptime('%s %s'%(current_date, time_input),"%Y/%m/%d  %H:%M:%S")
print "Time selected: ",selected_time
t= selected_time - datetime.fromtimestamp(time.mktime(time.localtime()))	
a = datetime.fromtimestamp(time.mktime(time.localtime()))
time.sleep(t.total_seconds())
webbrowser.open(mylines)
