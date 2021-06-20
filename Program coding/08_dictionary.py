myDict = {
    "Name": "Parth Shah",
    "College": "SOCET",
    "Enroll": 180770107209,
    "mobile": 9924446871,
    "laptop": {
        "brand": "Lenovo", 
        "cpu": "i5", 
        "ram": 8, 
        "generation": 10
    }
}

print(myDict)
print(myDict.keys())
print(myDict.values())
print(myDict['Name'])
print(myDict['College'])
print(myDict['Enroll'])
print(myDict['mobile'])
print(myDict['laptop'])
print(myDict['laptop']['brand'])
print(myDict['laptop']['cpu'])
print(myDict['laptop']['ram'])
print(myDict['laptop']['generation'])

updatedmyDict = {
    "City": "Surendranagar",
    "laptop": {
        "brand": "Lenovo", 
        "cpu": "i9", 
        "ram": 16, 
        "generation": 11
    }
}
myDict.update(updatedmyDict)
print(myDict)

print(myDict.get('Name'))
