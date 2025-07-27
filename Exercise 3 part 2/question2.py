 #program to print the sum of numbers

 
def print_sum_of_numbers():
     number = int(input("enter the number:"))
     total = 0
     for i in range(1, number + 1): # loop through the range
      total += i
     print("Sum is:", total)
     return total

print_sum_of_numbers()