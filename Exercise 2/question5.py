# a pgrogram to count the number of digits in a number

number = int(input('Enter the number:'))
count =0
temp = abs(number)
while temp>0:
    temp //=10
    count +=1

print(f'total number of digits is:{count}')