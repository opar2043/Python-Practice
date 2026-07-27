from itertools import count


# print("Rijoan Rashid Opar")

# #? variable name
# name = "opar"
# age = 25
# cgpa=3.80
# isStudent = True
# parents = {"father" : "Motalab" , "mother" : "Lucky"}

# print(f"Name: {name} son of {parents['father']} and {parents['mother']},  Age: {age}, CGPA: {cgpa}")

# marks = [85, 90, 78, 92, 88]  # List type
# course = ("Math", "Physics", "Chemistry")  # Tuple type
#? type 
# print("type name: " , type(name) )
# print("type age: " , type(age) )
# print("type cgpa: " , type(cgpa) )
# print("type marks: " , type(marks) )
# print("type course: " , type(course) )
# print("type is he Student: " , type(isStudent) )
# print("type parents: " , type(parents) )


# your_name = input("Enter your name: ")
# num1 = int(input("Enter the first number: "))     #type casting 
# num2 = int(input("Enter the second number: "))
# sum = num1 + num2
# min = num1 - num2
# multi = num1 * num2
# divide = num1/num2
# mod = num1%num2
# power= num2**num1 

# print(f"name: {your_name} sum: {sum}, min: {min}, multiply: {multi}, divide: {divide}, modulus: {mod}, power: {power} ")

#? if else 
# if num1 > num2 :
#     print("num1 is greater") 
# else:
#     print("num2 is greater")



#? COMPARISON

# a=15 
# b= 10

# if a>b  and a!=b:
#     print("A is greater" , a>b)
# elif a<b and a!=b:
#     print("b is greater than a")
# elif a==b :
#     print("A is equal to B")
# else :
#     print("None of the above")


#?   marks condition 
marks = 82
age = 2 
isTrue = age >18 or age ==25     #reverse

# if marks >= 80:
#     print("Grade A")
# elif marks >= 70:
#     print("Grade B")
# elif marks >= 60:
#     print("Grade C")
# else:
#     print("Fail")


# if age > 18 :
#     if marks > 75 :
#         print("he is eligible to go aborad")
#     else:
#         print("he is not eligible to go aborad")
# else : 
#     print("Not mature enough! STILL CHILD")





#? Input from user 

# Student Information Program

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# cgpa = float(input("Enter your CGPA: "))

# print("\nStudent Information")
# print("--------------------")
# print(f"Name : {name}")
# print(f"Age  : {age}")
# print(f"CGPA : {cgpa}")

# print("\nEligible:", age >= 18)

#? LIST [] IN PYTHON 

fruits = ["apple", "banana", "orange"]
print(fruits[0])

fruits.append("grape")     # Add in LIST
# print(fruits)
fruits.remove(fruits[0])   # Remove in LIST
fruits[2] = "mango"        # Update in LIST
print(fruits , "Length: " + str(len(fruits)))

for fruit in fruits:
    print(fruit)

# ?  Tuple() - A tuple cannot be changed after creation.
numbers = (1, 2, 3, 4, 5)
print(numbers , numbers[2] , "Length: " + str(len(numbers)))

# ? Dictionary {key : Value} - Stores data as key : value.

students = {
    "name" : "Rijoan Rashid Opar",
    "Age" : 18,
    "Adress" : "Dhaka,Narayanganj",
    "CGPA" : 3.80,
    "Profession" : "Full Stack Developer",
    "isStudent" : True,
    "Skills" : ["react", "next js" ,"Python"]
}

if students["isStudent"] and students["CGPA"] > 3.75 :
    print(students["name"] + ", He is eligible for the scholarship." ,)

students["Adress"] = "Bandar, Narayanganj"    
print(students["Adress"])



#? loop 
for i in range(1,5):
  print(i)


# increment everytime 2
for i in range(2,20,2):
   if i == 8:
      continue
   if i == 16:
      break
   print(i)  

#?    function 

def hello():
   print("Hello, World!")   
   hello()


   def stdInfo(name, age, cgpa):
      print(f"Name: {name}, Age: {age}, CGPA: {cgpa}")
   stdInfo("Rijoan Rashid Opar", 18, 3.80)
