n = int(input("Enter the Number: "))
prime = True

for i in range(2,n):
    if(n%i==0):
        prime = False
        break
    
if prime:
    print("The Number is prime number")

else:
    print("The Number is not a prime number")

