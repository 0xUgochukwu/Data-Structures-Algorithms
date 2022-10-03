def checkPrime(num):
    isPrime = False
    
    if num == 2 or num == 1:
        isPrime = True
        return isPrime

    for x in range(2, num):
        if num % x == 0:
            return isPrime
    return not isPrime

print(checkPrime(67))