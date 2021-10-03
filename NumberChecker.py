n = int(input('Enter a number'))
if n%2 == 0:
  print('The number is even')
else:
  print('The number is odd')

  

  
def isPrime(n):
    if n <= 1 :
        return False
 
    for i in range(2, n):
        if n % i == 0:
            return False
 
    return True

if isPrime(n):
  print('The number is prime')
else:
  print('The number is compsite')
