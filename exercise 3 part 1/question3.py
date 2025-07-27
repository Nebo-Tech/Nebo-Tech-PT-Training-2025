# a program to display date and time

import datetime
now =datetime.datetime.now()

def current_date_and_time():
    print('Current date and time:')
    print(now.strftime("%Y-%m-%d, %H:%M:%S"))

current_date_and_time()