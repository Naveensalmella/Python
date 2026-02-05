#conditional statements in Python

age = int(input("Enter your age : "))
if age >= 18:
    print("You are a major")
else:
    print("You are a minor")


name = input("Enter your name : ")
if name == "Naveen":
    print("You born on 1st")
elif name == "Srivally":
    print("You are born on 26th")
elif name == "Ramana Chary":
    print("Tou born on 2nd")
elif name == "Aruna":
    print("You born on 30th")
else:
    print("You are not a family member")
    

num = int(input("Enter a number : "))
if num > 0:
    print("The number is POsitive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")