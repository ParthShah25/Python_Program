def greater(num1,num2,num3):
    if num1>num2 and num1>num3:
        # print("Num1 is Greatest")
        return num1,"is greater" 

    elif num2>num3:
        # print("Num2 is Greatest")
        return num2,"is greater" 

    else:
        # print("Num3 is Greatest")
        return num3,"is greater" 

a = greater(12,56,89)
print(a)

b = greater(12,90,89)
print(b)

c = greater(91,56,89)
print(c)