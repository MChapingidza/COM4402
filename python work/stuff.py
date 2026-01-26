# for i in range(5):
#     number = int(input("enter a number"))
#     print("you entered", number)

# rep_number = int(input("how many times should i say hello"))
# for i in range(rep_number):
#         print("hello")
#
# for i in range(1,6):
#     print(i)

# x = 0
#
# while x <= 3:
#     print("x is", x)
#     x = x + 1

# choice = ""

# while choice != "0":
#     print("1. Say hello")
#     print("2. Say goodbye")
#     print("0. Exit")
#
#     choice = input("Enter choice: ")
#
#     if choice == "1":
#         print("Hello!")
#     elif choice == "2":
#         print("Goodbye!")
#     elif choice == "0":
#         print("Exiting...")
#     else:
#         print("Invalid choice")

# while True:
#     number = int(input("Enter a positive number: "))
#     if number > 0:
#         break
#     print("That is not positive, try again.")
#
# print("You entered:", number)

# correct = "python123"
#
# while True :
#     entered_char = input("please enter your password")
#     if entered_char == correct:
#         break
#     print("incorrect password")
# print("access granted")

# total = 0
#
# while True:
#     num = int(input("Enter a number (0 to stop): "))
#     if num == 0:
#         break
#     total = total + num
#     print(total)
#
# print("Total is:", total)

name_counter = 0

while True:
    name = input("name")
    print(f"nice to meet you {name}")
    name_counter = name_counter + 1
    if name_counter == 3:
        break










