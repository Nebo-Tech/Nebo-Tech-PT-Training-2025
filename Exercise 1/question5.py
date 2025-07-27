# a program to convert the user data into list and turple

data =input("Enter the list of numbers separated by commas:")

num_list =data.split(',')
num_tuple =tuple(sorted(int(num.strip()) for num in data.split(',')))
print('list:', num_list)
print('tuple:', num_tuple)