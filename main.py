# NAME OF AUTHOR:  Lucas Galan
# NAME OF THE PROGRAM: Amougs SUSSY QUIZ 
# DATE OF CREATION:  febuary 1st 2022
# PURPOSE OF PROGRAM:  to test user in critical thinking skills

from questions import quiz


def check_ans(question, ans, attempts, score):
    #Amogs checks for question answer and failure
    
    
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!ඞඞඞ")
        return True
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} left cause ur garbageඞඞඞ! \nTry again idiotඞඞඞ")
        return False


def print_dictionary():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])

#the intro message
def intro_message():
    
    
    
    print("Amogus quiz for non sussy people!")
    print("You get 6 questions. You can type skip cause ur bad")
    input("Press any key to start the sussy quiz ඞ ")
    return True


# Shows the messages and the scoring system
intro = intro_message()
while True:
    score = 0
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])
            answer = input("Enter Answer (To skip type skip. when you run out of attempts just skip to next question. If you run out of attempts ur badඞඞඞඞඞඞඞඞඞ) ")
            if answer == "skip":
                break
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1

    break
#the end game
print(f"Your final score is {score}!\n\n you sussy bakaඞ")
print("Want to know the correct answers? Please see them below! ;)\n")
print_dictionary()
print("Thanks for playing you sussy baka.")