'''
Write a program that lets the user play the game of Rock, Paper, Scissors against
the computer. The program should work as follows:
At each turn the program asks the user to place a bet in the amount of 1 to 10
units. When the user places a bet outside of this range, say 0, the game
terminates.
After the user places the bet, they (singular they) are asked to select one from
among Paper, Scissors, or Rock. The computer selects one of these at random (say
a random number in the range of 1 through 3 is generated. If the number is 1, then
the computer selects rock. If the number is 2, then the computer selects paper. If
the number is 3, then the computer selects scissors)
Having displayed computer’s choice, display the winner.
Keep the running total of the user’s wins/losses.
If a given run produces no winner, it is ignored
At the end of the game display:
1. the number of rounds played,
2. the number of times the user won
3. total number of points (positive or negative) “won” by the user
Everything you might want to know about Rock-Paper-Scissors (and lots of things
you don’t care to know) can be found in wikipiedia
https://en.wikipedia.org/wiki/Rock%E2%80%93paper%E2%80%93scissors
A sample run of this games appears on the next page. Your output need not follow
this style!
'''
import random

import UserInputCopy

ROCK = 3
PAPER = 1
SCISSORS = 2

USER = 'u'
COMPUTER = 'c'

rounds_played = 0
user_won_rounds = 0
user_points = 0

def main():
    while True:
        bet = get_bet()

        if bet < 1 or bet > 10:
            print('you won', user_won_rounds, 'round(s)\n'
            'user has', user_points, 'points\n'
            'there were', rounds_played, 'round(s) played')
            print('you chose to end the game, goodbye')
            break

        user_choice = input('choose rock, paper, scissors ').upper()
        user_move = get_user_move(user_choice)
        while user_move == 0:
            user_choice = input('choose rock, paper, scissors ').upper()
            user_move = get_user_move(user_choice)

        comp_move = get_computer_move()
        get_winner(user_move, comp_move, bet)


def get_bet():
    return UserInputCopy.get_integer('place a bet from 1 to 10 (to end game enter outside range) ')

def get_user_move(user_choice):
    move = 0
    user_choice.upper()
    if user_choice == 'ROCK':
        move = ROCK
    elif user_choice == 'PAPER':
        move = PAPER
    elif user_choice == 'SCISSORS':
        move = SCISSORS
    else:
        move = 0
        print('you entered an invalid move')
    return move

def get_computer_move():
    move = random.randint(1, 3)
    result = num_to_move(move)
    print('computer move is', result)

    return move

def num_to_move(move):
    if move == ROCK:
        result = 'ROCK'
    elif move == PAPER:
        result = 'PAPER'
    else:
        result = 'SCISSORS'

    return result

def get_winner(user_move, comp_move, bet):

    print('your move was', num_to_move(user_move))
    winner = ''
    if user_move == comp_move:
        print('tie game!')
    elif user_move == ROCK and comp_move == SCISSORS:
        winner = USER
    elif user_move == SCISSORS and comp_move == ROCK:
        winner = COMPUTER
    elif user_move == ROCK and comp_move == PAPER:
        winner = COMPUTER
    elif user_move == PAPER and comp_move == ROCK:
        winner = USER
    elif user_move == SCISSORS and comp_move == PAPER:
        winner = USER
    elif user_move == PAPER and comp_move == SCISSORS:
        winner = COMPUTER

    global user_won_rounds
    global user_points
    global rounds_played

    if winner == USER:
        print('you won')
        user_won_rounds += 1
        user_points += bet
    elif winner == COMPUTER:
        print('computer won')
        user_points -= bet

    rounds_played += 1

main()



