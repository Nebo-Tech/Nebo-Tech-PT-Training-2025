#a program to present the multiplication table

for i in range(1, 11):   #loop for 1 to 10 for the base of the table
    print(f"multiplication table of: {i}")
    
    for j in range(1,11):  #loop to generate each row from 1 to 10
        print( i*j, end=' ')
    print()
    print()