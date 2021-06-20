names = ['Parth', 'Shruti', 'Neeta', 'Rupesh']
name = input("Enter the name: ")

if name in names:
    result = True

else:
    result = False

if(result):
    print("The name is present in the list")

else:
    print("The name is not present in the list")