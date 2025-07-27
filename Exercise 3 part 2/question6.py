# a program to print number pattern in reverse order

def print_pattern():
   rows = 5

   for i in range(rows,0, -1):  #loop for rows
    
      for j in range(i, 0, -1): #loop for columns
        print(j, end=(" ") )
      print() 
   

print_pattern()