
score = int(input("Enter score: "))

 if score >= 70:
     print("distinction")
 elif score <= 40:
     print("fail")

if score >=40:
    if score >=70:
        print("pass with merit")
    elif print("pass")
        else
        print("fail")


        #practice1
print("hello what is your age")
age=int(input())
if age < 18:
    if age < 5:
        print("free entry")
    else:
        print("child ticket")
elif age > 65:
    print("senior ticket")
elif age <= 64:
    print("adult ticket")

     #practice 2
 print("how many days late were you?")
 days_late = int(input())
 if days_late < 10:
     if days_late <= 5:
         print("fine is £1")
     elif days_late > 5:
         print("fine is £5")
 else:
     print("fine £10 and membership review")

#     #activity3
 print("what is your score?")
 score = int(input())
 if score >= 38:
     if 42 >= score >=38:
         print("borderline pass, consider review")
     else: print("pass")
 elif score < 38:print("fail")
from random import choice

# #activity4
 print("are you a student?")
 student = input()
 print("how old are you?")
 age  = int(input())
 if student == "no":
     if age > 18:
         print("discount not applied")
     else:
         print("discount applied")
 else:
     print("discount applied")

    #activity5
 print("please submit a color")
 choice = input()
 match choice:
     case "red":
         print("stop")
     case "green":
         print("go")
     case "amber":
         print("get ready")


 print("Enter choice: \n1. Start Quiz\n2. View scored")

 choice = int(input())

 match choice:
     case 1:
         print("You have started the quiz")
     case 2:
         print("Your total score is 10")
     case _:
        print("Invalid choice")


#activity6
number = int(input("please submit a number\n"))
if number % 3==0 and number % 5==0 and number != 0:
    print("FizzBuzz")
elif number % 3==0:
    print("fizz")
elif number % 5==0:
    print("buzz")
else:
    print("invalid")








