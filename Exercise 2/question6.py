# a program to print a program in reverse order

rows = 5

for i in range(rows,0, -1):  #loop for rows
    
    for j in range(i, 0, -1): #loop for columns
        print(j, end=(" ") )
    print()