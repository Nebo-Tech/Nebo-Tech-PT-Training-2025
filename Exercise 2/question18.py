# a program to print the series of numbers

number = 2
terms = 5

series = " "
for i in range(1, terms + 1):
    series += str(number * i)
    
print(series)
