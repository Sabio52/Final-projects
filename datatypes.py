
# Data types
# string, integer, float, boolean
name = 'Sabit'
age = 14
weight = 50.0
is_student = True  

print("hello everyone, my name is", name)
print("the data type of name is", type(name))
print("I am", age, "years old")
print("the data type of age is", type(age))
print("I weigh", weight, "kilograms")
print("the data type of weight is", type(weight))
print("Am I a student?", is_student)
print("the data type of is_student is", type(is_student))

# after type casting 
name = str(name)
age = str(age)
weight = str(weight)
is_student = str(is_student)
print("After type casting:")
print("data type of name is", type(name))
print("data type of age is", type(age))
print("data type of weight is", type(weight))
# operators
# arithmetic operators
num1 = 10
num2 = 20

print("num1 + num2 =", num1 + num2)
print("num1 - num2 =", num1 - num2)
print("num1 * num2 =", num1 * num2)
print("num1 / num2 =", num1 / num2)

print("are they equal?", num1 == num2)
print("are they not equal?", num1 != num2)
print("is num1 greater than num2?", num1 > num2)
print("is num1 less than num2?", num1 < num2)
print("is num1 greater than or equal to num2?", num1 > num2)
print("square of num1 is", num1 ** 2)
# string operations
first_name = "Sabit"
last_name = "Hossain"
full_name = first_name + " " + last_name
multiple_words = "ha"

print("My first name is", first_name)
print("My last name is", last_name)
print("My full name is", full_name)
print("multiplication of strings:", multiple_words * 3)
print("lenght of full name is", len(full_name))
print("first character of full name is", full_name[0])
print("last character of full name is", full_name[-1])
print("string slicing:", full_name[0:3])

# string swapping 
x = input("Enter first string: ")
y = input("Enter second string: ")
z = input("Enter third string: ")

z ,x, y = y, x, z
print("After swapping:") 
print("First string:", y)
print("Second string:", z)
print("Third string:", x)