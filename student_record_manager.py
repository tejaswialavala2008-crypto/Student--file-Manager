import re

# Student Record Manager

FILE_NAME = "students.txt"


def validate_email(email):
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    return re.match(pattern, email) is not None


def add_student():
    try:
        name = input("Enter student name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        roll_no = input("Enter roll number: ").strip()
        if not roll_no:
            raise ValueError("Roll number cannot be empty.")

        email = input("Enter email: ").strip()

        if not validate_email(email):
            raise ValueError("Invalid email format.")

        with open(FILE_NAME, "a") as file:
            file.write(f"{roll_no},{name},{email}\n")

        print("Student added successfully!")

    except ValueError as e:
        print("Invalid input:", e)
    except Exception as e:
        print("Error:", e)


def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

        if not data:
            print("No student records found.")
            return

        print("\nStudent Records")
        print("----------------")

        for line in data:
            roll_no, name, email = line.strip().split(",")
            print("Roll No:", roll_no)
            print("Name:", name)
            print("Email:", email)
            print("----------------")

    except FileNotFoundError:
        print("No student records found. File does not exist.")
    except Exception as e:
        print("Error:", e)


def main():
    while True:
        print("\nStudent Record Manager")
        print("1. Add Student")
        print("2. Read Student Data")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                add_student()
            elif choice == "2":
                read_students()
            elif choice == "3":
                print("Thank you!")
                break
            else:
                raise ValueError("Please enter a valid choice (1, 2, or 3).")

        except ValueError as e:
            print("Invalid input:", e)


if __name__ == "__main__":
    main()
