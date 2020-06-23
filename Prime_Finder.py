n = int(input("Enter a number equal to or greater than 2: "))
factors = 0
for i in range(1, n+1):
    if n % i == 0:
        factors += 1
if factors == 2:
    print("This number is a prime number")
else:
    print("This number is not prime")
