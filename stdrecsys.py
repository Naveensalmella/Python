def save_student(student):
    with open("students.txt", "a") as file:
        file.write(f"{student['name']}, {student['marks']}\n")

def show_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No students saved yet.")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))

        student = {
            "name": name,
            "marks": marks
        }

        save_student(student)
        print("Student saved")
    
    elif choice == "2":
        show_students()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")