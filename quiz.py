#!/usr/bin/env python3
#-*- coding:utf-8 -*-

NUM_GUESS = 3
QA_FILE = 'solar_system.txt'
score = 0
total = 0

# Function to let user guess 3 times
def check_guess(guess, answer):
    global score
    still_guessing =  True
    attempt = 0
    while still_guessing and attempt < NUM_GUESS:
        if guess.lower() == answer.lower():
            print('Correct answer!')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry, wrong answer. Try again: ')
            attempt = attempt + 1
    if attempt == NUM_GUESS:
        print(f'No more guesses. The correct answer is {answer}')


# Read a question and answer from file, line by line
# Start by listing the topic from the top of the file
with open(QA_FILE, 'r') as file:
    print(file.readline())
    for line in file.readlines():
        total = total + 1
        q, a= [x for x in line.strip().split(';')]
        guess = input(f'{q} ')
        check_guess(guess, a)
        print(f'Your score is {str(score)}\n')

# Once done, rate the score
if score == total:
    print(f'Awesome, you got full score, {score} out of {total}')
elif score > total / 2:
    print(f'Not bad, you got {score} out of {total} correct')
elif score == 0:
    print('Oh no! Someone needs to read more.')
else:
    print(f'You got only {score} out of {total} correct')
