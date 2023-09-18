'''
An attached text file WorldSeriesWinners.txt.txt contains a chronological list of the World
Series winning teams from 1903 through 2022. (The first line in the file is the name of the
team that won in 1903, and the last line is the name of the team that won in 2022. Note
the World Series was not played in 1904 or 1994.)
Write a program that lets the user repeatedly enter the name of a team, then displays
the number of times that team has won the World Series since 1903. If the team has not
won a single World Series title, the program should display a message to that effect.
'''
import sys

def main():
    try:
        file_name = sys.argv[1]

        teams = make_list(file_name)

        while True:
            choice = input("choose a team (start with city): ")
            if len(choice) < 2:
                break
            counter = count_winner(teams, choice.upper())
            print('the', choice, 'won the World Series', counter, 'times')

    except Exception as exc:
        print(exc)


def make_list(file_name):
    file = open(file_name, 'r')
    teams = file.readlines()
    my_list = []
    for team in teams:
        upper_team = team.upper()
        new_list = my_list.append(upper_team.replace('\n', ''))
    #print(my_list)
    return my_list


def count_winner(teams, choice):
    counter = teams.count(choice)
    return counter


main()
