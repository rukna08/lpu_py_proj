import random

answer = random.randrange(1, 10)

user_given_answer = 0

limit = 4
tries = 0
while(user_given_answer != answer and tries <= limit):
    user_given_answer = int(input("Guess: "))

    if user_given_answer > answer:
        print("Answer is lower than your guess")
    elif user_given_answer < answer:
        print("Answer is greater than your guess")
    else:
        print("{} is the answer!".format(user_given_answer))

    tries += 1

print("No. of tries: {}".format(tries))