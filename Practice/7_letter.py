letter = '''Dear <|NAME|>,
You are Selected!
Date: <|DATE|> '''


Name = input("Enter Your Name: ")
Date = input("Enter the Date: ")

letter = letter.replace("<|NAME|>",Name)
letter = letter.replace("<|DATE|>",Date)
print(letter)

