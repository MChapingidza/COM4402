from ctypes import HRESULT
from random import choice


# def subtraction (a,b):
#
#     result = a - b
#     print(result)
#
# subtraction(10,2)

# activity 1

# message = "Hello from the function"
# def greet():
#  message = "Hello from the function"
# greet()
# print(message)

# activity 2
# count =0
# def add_one(count):
#  count = count + 1
#  print("Inside:", count)
#  return count
# count = add_one(count)
# print("Outside:", count)

# # activity 3
# def area_of_rectangle(width, height):
#     x = width * height
#     print("area is", x)
#     return  x
#
#
# area_of_rectangle(10.2, 10.2)

# activity 4

# Version 1
# additional_years = 5
# def age_in_5_years(age):
#  return age + additional_years

# version2
# def age_in_5_years(age):
#     additional_years = 5
#     return
#     age + additional_years

# advantage - the additional age can be changed

# # activity 5
#
# def apply_discount(price):
#  if price > 100:
#     discount = 10
#  elif price <= 100:
#      discount = 0
#  final_price = price - discount
#  return final_price
# p = float(input("Enter price: "))
# result = apply_discount(p)
# print("Final price:", result)

# activity 6
account_balance = 1000

def show_menu():
 print("1. Deposit")
 print("2. Withdraw")
 print("0. Exit")
 print(f"Current Balance: {account_balance}\n-----")
 choice = input("Enter choice: ")
 return choice


def deposit(balance):
 amount = float(input("Amount to deposit: "))
 if amount > 0:
      balance = balance + amount
      return balance
 else:
     print("error")

def withdraw(balance):
 amount = float(input("Amount to withdraw: "))
 if amount > 0:
      balance = balance - amount
      return balance
 else:
     print("error")

while True:
    print(f"STARTING Balance: {account_balance}")
    choice = show_menu()
    if choice == "1":
        account_balance = deposit(account_balance)
    elif choice == "2":
        account_balance = withdraw(account_balance)
    elif choice == "0":
        break
print("exit succsefful")


























