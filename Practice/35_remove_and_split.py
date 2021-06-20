def remove(string, word):
    new = string.replace(word, " ")
    return new.strip()

str = "      Parth is a Good                 boy"
n = remove(str,"boy")
print(n)