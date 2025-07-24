# Accepting comma-separated numbers and splitting them into list/tuple
data = input("Enter comma-separated numbers: ")
items_list = data.split(",")
items_tuple = tuple(items_list)
print("List:", items_list)
print("Tuple:", items_tuple)