# program to calculate the factorial of a number
def calculate_facorial():
  
    num = 5  # sample input
    factorial = 1
    for i in range(1, num + 1):# loop to iterate factorial
     factorial *= i
    print(f"Factorial of {num} is {factorial}")

calculate_facorial()
