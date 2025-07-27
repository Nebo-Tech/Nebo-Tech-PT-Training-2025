# a pgrogram to count the number of digits in a number


def number_counter(number):
    return len(str(abs(number)))
    
number = input('Enter the number:')

try:
    num= int(number)
    number_counter = number_counter(num)
    print(f"Total number of digits in {num}: {number_counter}")
except ValueError:
    print('Invalid input! please enter a valid integer')    
