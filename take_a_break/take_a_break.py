#import lib files

import webbrowser
import time

#take number of break from user 
total_break =int(input("Enter the Numbers of break you wish to take in a day: "))

#take the input from user about the time interval
no_of_hours=int(input("Enter the time interval in which you wish to take break: "))

time_in_sec=no_of_hours*60*60

break_count = 0;

#print current time


print("The program started on "+time.ctime())
while (break_count < total_break):
    time.sleep(time_in_sec);
    url="https://www.youtube.com/watch?v=aTvJWKu9bMs&start_radio=1&list=RDaTvJWKu9bMs"
    webbrowser.open(url);
    break_count=break_count+1

print("You completed all your breaks and current time is "+time.ctime())

