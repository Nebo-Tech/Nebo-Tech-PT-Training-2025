# a program to display the fibonacci sequence

def display_fibonacci_sequence():
    a,b = 0, 1
    count =10

    print("fibonacci sequence:")
    for i in range(count):
     print(a, end=" ")
     a, b = b, a + b

display_fibonacci_sequence()