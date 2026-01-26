question1 = {
    "question": "what color is the sky?",
    "options": ["blue", "red",  "purple",  "gold"],
    "answer": 0
}
question2 = {
    "question": "what color is the blood?",
    "options": ["blue", "red",  "purple",  "gold"],
    "answer": 1
}
question3 = {
    "question": "what color is the hulk?",
    "options": ["blue", "green",  "purple",  "gold"],
    "answer": 1
}
question4 = {
    "question": "what color is mustard?",
    "options": ["yellow", "red",  "purple",  "gold"],
    "answer": 0
}
question5 = {
    "question": "what color is the ketchup?",
    "options": ["blue", "red",  "purple",  "gold"],
    "answer": 1
}
score = 0

def display_question(question):
    print(question.get("question"))
def display_options(question):
    for option_number, option in enumerate(question["options"]):
        print(option_number, option)
def input_answer(question):
    score = 0
    guess_answer = int(input())
    if guess_answer == (question["answer"]):
        score == score  + 1
    else:
        score == score + 0

def final_score():
    print("congratulations you scored", score, "out of 5")



display_question(question1)
display_options(question1)
input_answer(question1)



display_question(question2)
display_options(question2)
input_answer(question2)


display_question(question3)
display_options(question3)
input_answer(question3)


display_question(question4)
display_options(question4)
input_answer(question4)


display_question(question5)
display_options(question5)
input_answer(question5)
final_score()


# print(question1.get("question"))
#
# for ordered_number,options in enumerate(question1["options"])  :
#     print(ordered_number, options)
# guess_answer = int(input())
# if guess_answer == (question1["answer"]):
#    score = score + 1
# else:
#     score = score + 0
#
#
#
# print(question3.get("question"))
# for ordered_number,options in enumerate(question3["options"])  :
#     print(ordered_number, options)
# guess_answer3 = int(input())
# if guess_answer3 == (question3["answer"]):
#    score = score + 1
# else:
#     score = score + 0
#
# print(question4.get("question"))
# for ordered_number,options in enumerate(question4["options"])  :
#     print(ordered_number, options)
# guess_answer4 = int(input())
# if guess_answer4 == (question4["answer"]):
#    score = score + 1
# else:
#     score = score + 0
#
# print(question5.get("question"))
# for ordered_number,options in enumerate(question5["options"])  :
#     print(ordered_number, options)
# guess_answer5 = int(input())
# if guess_answer5 == (question5["answer"]):
#    score = score + 1
# else:
#     score = score + 0
# print("your final score is", score, "out of 5")








