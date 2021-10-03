from prime_check.py  import isPrime()

n = int input('Enter a number')
if n%2 == 0:
  print('The number is even')
else:
  print('The number is odd')
  
if isPrime(n):
  print('The number is prime')
else:
  print('The number is compsite')
