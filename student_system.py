students = []

while True:
    print("\n=== STUDENT RECORD SYSTEM ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        course = input("Enter course: ")

        student = {
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)
        print("Student added successfully")

    elif choice == "2":
        if len(students) == 0:
            print("No students recorded")

        else:
            for s in students:
                print("\nName:", s["name"])
                print("Age:", s["age"])
                print("Course:", s["course"])

    elif choice == "3":
        search_name = input("Enter name to search: ")

        found = False
        for s in students:
            if s["name"].lower() == search_name.lower():
                print("\nStudent Found!")
                print("Name:", s["name"])
                print("Age:", s["age"])
                print("Course:", s["course"])
                found = True
                break

        if not found:
            print("Student not found")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid option")