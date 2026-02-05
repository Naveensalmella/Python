print("Day 3 is started")

#for loop in Python

for i in range(1, 7):
    print(i)


#while loop in Python
count = 1
while count <= 9:
    print(count)
    count += 3

#Task-1

num = int(input("Enter a number : "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

#Task-2

password = input("Enter your password : ")
if password == "Naveen46":
    print("You are logged in successfully")
else:
    print("Invalid password, failed to login")

#Task-3

n = int(input("Enter a number : "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#function 

def greet():
    print("Hello, Welcome")
greet()

#function with parameters

def greet_user(name):
    print("Hello", name)
greet_user("Naveen Salmella")

#function with return value
#addition

def add(a, b):
    return a + b
result = add(3, 5)
print(result)

#subtraction

def sub(a, b):
    return a - b
result = sub(2, 5)
print(result)

#multiplication

def mult(a, b):
    return a * b
result = mult(2, 7)
print(result)

#division

def div(a, b):
    return a / b
result = div(10, 5)
print(result)

#create and access list

fruits = ["Banana", "Apple", "Pomegranate"]
print(fruits[0])
print(len(fruits)) 

#loop through list

for fruit in fruits:
    print(fruit)


print("Day 3 is successfully completed")