 #program to display a prime number
def is_prime(n):
   # check if a number is prime
   if n<=1:
      return False
   for i in range(2,int(n **0.5)+1):
      if n % i==0:
         return False
   return True
 #display prime number
primes=[]
for num in range(25, 50):
        if is_prime(num):
            primes.append(num)
        
print(f"prime numbers between 25 and 50 is {primes}")