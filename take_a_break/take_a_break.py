#import lib files

import webbrowser
import time

#take number of break from user 
total_break =int(input("Enter the Numbers of break you wish to take in a day: "))
break_count = 0;

#print current time

print("The program started on "+time.ctime())
while (break_count < total_break):
    time.sleep(1220);
    webbrowser.open("https://www.youtube.com/watch?v=aTvJWKu9bMs&start_radio=1&list=RDaTvJWKu9bMs");
    break_count=break_count+1

print("You completed all your breaks and current time is "+time.ctime())

