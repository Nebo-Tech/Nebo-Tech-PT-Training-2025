# printing the reverse of a number
def reverse_number(num):
   reversed_num =0 
   while num > 0:
      digit =num % 10
      reversed_num =(reversed_num * 10) + digit
      num = num // 10
   return reversed_num

reversed_num =reverse_number(765432)
print(f"Reversed number:{reversed_num}")
