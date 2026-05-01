"""enter a number and tell it is prime or not"""
n = int(input("Enter the number :"))
if n <= 1 :
     print("not prime ")
else :
    for i in range ( 2 , n ) :
        if ( n % i == 0 ) :
            print( "not prime ")
            break
    else :
        print( "prime ")

"""Enter a number which number up to you want to find the prime numbers"""
for num in range(2, n + 1):
    is_prime = True
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")