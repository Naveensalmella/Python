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

print("Day 3 is successfully completed")