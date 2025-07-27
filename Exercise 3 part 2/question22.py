# a program to flaten the nested list 
def flatten_nested_list():
    # original nested list
    nested_list =[1,[2,3],[4,5,6],7,[8,8]]
 
 # block of code to convert the nested list into a flattened list
    flattened_list=[item for sublist in nested_list
                         for item in (sublist if isinstance(sublist, list) else[sublist])]
    print("flatted list: ", flattened_list)

flatten_nested_list()