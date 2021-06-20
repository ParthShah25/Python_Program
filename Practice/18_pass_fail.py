marks1 = int(input("Enter Your Marks of Subject-1: "))
marks2 = int(input("Enter Your Marks of Subject-2: "))
marks3 = int(input("Enter Your Marks of Subject-3: "))

avg = (marks1 + marks2 + marks3)/3
print(avg)

if marks1<33 or marks2<33 or marks3<33 or avg<40:
    print("You are Fail")

else:
    print("You are Passs")