def generate_list_and_turple():
    sampledata= input("Enter comma separated numbers:")
    num_list_str=sampledata.split(',')
    num_list= [int((x.strip())) for x in num_list_str]
    num_tuple =tuple(sorted(int(num.strip()) for num in sampledata.split(',')))
    print('list;',num_list)
    print('turple:',num_tuple)

generate_list_and_turple()