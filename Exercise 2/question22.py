# original nested list
nested_list =[1,[2,3],[4,5,6],7,[8,8]]
 
 # printing a flatened list using loop
flattened_list=[item for sublist in nested_list
                         for item in (sublist if isinstance(sublist, list) else[sublist])]
print("flatted list: ", flattened_list)