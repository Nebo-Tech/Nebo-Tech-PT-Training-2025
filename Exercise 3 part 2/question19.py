# program to print the pattern
def print_pattern():
    rows=5 
    for i in range(1, rows +1): # loop for the ascending loop
     print("*"*i)

    for i in range(rows-1, 0,-1): # loop for the descending loop
     print("*"*i)

print_pattern()