def calculate_average(marks):
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)

marks = []

n = int(input("How many subjects do you have? "))

for i in range(n):
    m = int(input(f"Enter mark {i+1}: "))
    marks.append(m)

avg = calculate_average(marks)

print("average marks:", avg)

if avg >= 60:
    print("YOu passed")
else:
    print("You failed")