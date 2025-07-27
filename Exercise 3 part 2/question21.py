# program to print the loop

def print_loop():
    num =1 

    for row in range(1,6):
      for col in range(row):
        print(num, end=" ")
        num +=1
      print()

print_loop()