from typing_extensions import runtime


comment = input("Enter your Comment here: ")

if("make a lot of money" in comment):
    spam = True

elif("click this" in comment):
    spam = True

elif("subscribe this" in comment):
    spam = True

elif("buy now" in comment):
    spam = True

else:
    spam = False

if(spam):
    print("This comment is spam")

else:
    print("This comment is ham")