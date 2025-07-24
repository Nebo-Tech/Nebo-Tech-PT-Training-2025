# Importing 'datetime' to get current system time
import datetime

now = datetime.datetime.now()
print("Current date and time:")

# Formatting to match sample output
print(now.strftime("%Y-%m-%d %H:%M:%S"))