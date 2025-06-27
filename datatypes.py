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