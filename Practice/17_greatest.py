num1 = int(input("Enter Your Number 1: "))
num2 = int(input("Enter Your Number 2: "))
num3 = int(input("Enter Your Number 3: "))
num4 = int(input("Enter Your Number 4: "))

if num1>num2 and num1>num3 and num1>num4:
    print("num1 is Greatest")

elif num2>num3 and num2>num4:
    print("num2 is Greatest")

elif num3>num4:
    print("num3 is Greatest")

else:
    print("num4 is Greatest")