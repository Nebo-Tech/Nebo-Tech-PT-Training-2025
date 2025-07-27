# a program to display number pattern using function
rows=5

def display_number_pattern():
    for i in range(1, rows+1):
       for j in range(1,i+1):
           print(j, end=(" "))
       print()

display_number_pattern()