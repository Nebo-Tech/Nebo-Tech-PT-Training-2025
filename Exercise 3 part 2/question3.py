# program to print the multiplication table of the number
number=2

def print_multiplication_table():

     print('multiplication table for {number} is:')
     for i in range(1,11):     #loop through the range
      print(number*i)

print_multiplication_table()