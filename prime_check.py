def isPrime(n):  
    # Checking that given number is more than 1  
    if n > 1:  
        # Iterating over the given number with for loop  
        for j in range(2, int(n/2) + 1):  
            # If the given number is divisible or not  
            if (a % j) == 0:  
                print("Composite number")  
                break  
        # Else it is a prime number  
        else:  
            print("Prime number")  
    # If the given number is 1  
    else:  
        print("Composite number")
 
