# a program to print the series of numbers
def print_sum_series(num,terms):
     total= 0
     current_term = 0
 
     for i in range(1, terms + 1):
       current_term =current_term*10+num
       total+=current_term
     return total
num =2
terms= 5

result =print_sum_series(num, terms)
print(f"Sum of the series:",result)
