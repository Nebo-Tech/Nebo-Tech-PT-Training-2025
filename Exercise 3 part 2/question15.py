# program to print numbers based on conditions
def filter_numbers(numbers):
    result =[]
    for num in numbers:
        if num > 500:
            break
        if num >150:
            continue
        if num % 5 ==0:
            result.append(num)
    return result

numbers=[12, 75, 150, 180, 145, 525, 50]

filtered_numbers = filter_numbers(numbers)
print('numbers satisfying conditions are:',filtered_numbers)