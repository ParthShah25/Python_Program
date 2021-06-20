def addition(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

num = addition(20)
print("Sum of first n Natural number is: ",num)