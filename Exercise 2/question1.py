# a program to display a pattern of numbers

rows = 5

for i in range(1, rows + 1):    #loop through rows
    for j in range(1, i + 1):
        print(j, end=(" ") )
    print()
  