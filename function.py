def even_or_odd(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"

print(even_or_odd(10))
print(even_or_odd(7))

# def printInfo(name, age, cgpa):
#     print(f"Name: {name}, Age: {age}, CGPA: {cgpa}")

# def studentInfo(name, age, cgpa):
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     cgpa = float(input("Enter your CGPA: "))
#     printInfo(name, age, cgpa)
#     res = studentInfo(name, age, cgpa) 
#     print(res)
    

name = input("Student Name: ")
bangla= int(input("Bangla marks: "))
english = int(input("English marks: "))
math = int(input("Math marks: "))

total = (bangla + english + math ) 
average = total / 3

if average >= 80:
    print("Grade: A+")
elif average >= 70:
    print("Grade: A")    
elif average >= 60:
    print("Grade: B")
else:
    print("Grade: C")


def printInfo():
      print("\n------ Result ------")
      print(f"Name: {name}")
      print(f"Total: {total}")
      print(f"Average: {average:.2f}")

printInfo()  


balance = 5000

while True:
    print("\n====== ATM MENU ======")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice==1:
        print(f"Your balance is: {balance}")
    elif choice==2:
        amount = int(input("Enter the amount to deposit: "))
        balance += amount
        print(f"Amount deposited successfully. Your new balance is: {balance}")
    elif choice==3:
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Amount withdrawn successfully. Your new balance is: {balance}")
        else:
            print("Insufficient balance.")
    elif choice==4:
        print("Thank you for using our ATM.")
        break
    else:
        print("Invalid choice. Please try again.")


students = []

while True:
    print("\n====== STUDENT MANAGEMENT ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        department = input("Enter student department: ")
        cgpa = float(input("Enter student CGPA: "))

        student = {
            "name": name,
            "department": department,
            "cgpa": cgpa
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No students found.")

        else:
            print("\n------ Students ------")

            for student in students:
                print(f"Name: {student['name']}")
                print(f"Department: {student['department']}")
                print(f"CGPA: {student['cgpa']}")
                print("----------------------")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
