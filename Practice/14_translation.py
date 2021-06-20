translate = {
    "istemal": "Uses",
    "Vishvas": "trust",
    "rakhdo": "Put Down"
}

print("The Options are: ",translate.keys())
a = input("Enter the Hindi words: ")
print("The meaning of your word is: ",translate.get(a))