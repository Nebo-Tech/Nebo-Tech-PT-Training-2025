def find_largest_and_smallest():
    #a program to display the largest and smallest nember

     num1= 987654321
     num2= -5082

     digits1= str(abs(num1))           # remove negative sign and convert to string
     digits1= [int(d) for d in digits1]

     largest1= max(digits1)
     smallest1= min(digits1)
     print(f"largest digit in a {num1}; {largest1}")
     print(f"smallest digit in a {num1}: {smallest1}")

     digits2= str(abs(num2))                # the same for the second digit
     digits2= [int(d) for d in digits2]

     largest2= max(digits2)
     smallest2= min(digits2)
     print(f"largest digit in a {num2}; {largest2}")
     print(f"smallest digit in a {num2}: {smallest2}")

find_largest_and_smallest()