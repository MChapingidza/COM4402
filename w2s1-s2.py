# activity 1

print("enter your name")
name = input()

print("enter your age")
age = int(input())
print(type(age))




print("hello, " + name + " you are" + str(age) + " years old")

#activity 2

print("enter the first number please")
num1 = int(input())

print("please enter your second number")
num2 = int(input())
num3 = num1 * num2

print( "your final number is" , num3)

#activity 6
print("please enter the product name")
product_name = input()
print("enter price")
price = float(input())
print("enter quantity")
quantity = int(input())

total_price = price * quantity
print("you have purchased " , quantity , "of" , product_name , "so your total price is" , total_price )

#problem 8
print("hi,what is your name?")
name = input()
print("what is your age")
age = int(input())
print("what is your height?")
height = float(input())
age_plus_one = age + 1
print("hello" , name , "next year you will be " , age_plus_one, "and your height is " , height )

#activity 10
# in first line a "print" isn't being used
#name was not declared as an input
#age isnt declared or entered with a print

print("enter your name")
name = input()
print("enter your age")
age = int(input())
age_next_year = age + 1
print("hello" , name, "next year you will be" , age_next_year)

#problem 7 total marks for two tests

test_1 = 50
test_2 = 60
test_total = a + b
print(test_total)

#problem 6
#when i run it i will run into an error as i havent decalred age as an int.
#there was a concatenation error as i predicted
print("enter age")
age = int(input())
age_next_year = age + 1
print("next year you will be" , age_next_year)

#problem4
print("please enter your first number")
num1 = float(input())
print("please enter your second number")
num2 = float(input())
num3 = num1 + num2
print(num3)

#multi line activity
name="matthew"
age = 20
course ="COM4402"

print(f"I'm {name} \n I am {age} \n and i study {course}.")

# exercise 5 replace
template = "Hello NAME, welcome to COURSE."

name = input("Please enter your name: ")
course = input ("Please enter the course: ")

# stripping content
name = name.strip()
course = course.strip()

template = template.replace("NAME", name)
template = template.replace("COURSE", course)

#problem 3

