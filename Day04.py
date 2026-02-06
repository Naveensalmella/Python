#Dictionaries in Python

student = {
    "name": "Naveen Salmella",
    "age": 21,
    "course": "Python Programming"
}

print(student)

print(student["name"])
print(student["age"])
print(student["course"])

#modification

student["age"] = 22
student["marks"] = 90

print(student)

#loop through dictionary

for key, value in student.items():
    print(key, ":", value)

#write to a file

file = open("data.txt", "w")
file.write("Hello Python\n")
file.write("Learning file handling")
file.close()

#read from a file

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

#append to a file

file = open("data.txt", "a")
file.write("\nNew line added")
file.close()

print("Day 04 completed successfully")
