lst = [1,5,6,4,2,3,]
print("Before Updated: ",lst)
print("Before Updated",lst[0])
print("Before Updated",lst[1])
print("Before Updated",lst[2])
print("Before Updated",lst[3])
print("Before Updated",lst[4])
print("Before Updated",lst[5])

lst[5] = 7
print("\nAfter Updated",lst)
print("After Updated",lst[0])
print("After Updated",lst[1])
print("After Updated",lst[2])
print("After Updated",lst[3])
print("After Updated",lst[4])
print("After Updated",lst[5])

print("\nSlicing:",lst[0:1])
print("Slicing:",lst[0:2])
print("Slicing:",lst[0:3])
print("Slicing:",lst[0:4])
print("Slicing:",lst[0:5])
print("Slicing:",lst[0:])
print("Slicing:",lst[:5])

print("\nMethods")

print("\nSorted list")
lst.sort()
print(lst)

print("\nReversed list")
lst.reverse()
print(lst)

print("\Appended list")
lst.append(45)
print(lst)

print("\nInserted List")
lst.insert(5,36)
print(lst)

print("\nPoped list")
lst.pop(-3)
print(lst)

print("\nRemoved list")
lst.remove(45)
print(lst)

