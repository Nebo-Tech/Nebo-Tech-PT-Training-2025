# program to display a prime number
start= 25
End= 50

print(f"\n Prime numbers between{start} and {End}:")
for num in range(start, End+1):  #loop through the range
    if num>1:
        flag=True
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                flag=False
                break
        if flag:
            print(num)