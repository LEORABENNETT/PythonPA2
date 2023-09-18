''' Write a program that does the following:
1. Asks the user to provide a name of the file to be used
2. Ask the user to input the number of times a dodecahedral die (with faces
numbered 1, 2, 3,...,12) is to be tossed. This number should be no less than 100,
but no more than 12,000. Do use UserInput module.
3. Write the specified number of random integers in the range 1 – 12 to the file
specified in 1. This is to simulate tossing a dodecadral die this many times.
4. (close the file. Then ) Read the integers from the file specified in 1
a. Use a list (of size 12) to keep track how many times each number was read
b. Display the frequency of all numbers
c. Display the number that was tossed the most, and the number that was
tossed the fewest number of times.
d. Display (a perhaps fictitious) average number tossed – this should be a
float.
Make sure that your program protects against invalid input. It should not crash, no
matter what the user types.
'''
import random

import UserInputCopy


def main():
    file_name, number = get_user_parameters()

    success = write_numbers2file(file_name, number)
    if success:
        lines = read_file(file_name)

        frequencies = count_numbers(lines)

        display_results(frequencies)

        average_number_tossed(frequencies)
    else:
        complain(file_name)


def get_user_parameters():
    file_name = input('what would you like to call the file? ')
    number = UserInputCopy.get_integer('how many times should the dodecahedral die be tossed?', 100, 12000)

    return file_name, number


def write_numbers2file(file_name, number):
    aok = True
    try:
        output_file = open(file_name, "w")
        total = 0
        for each in range(number):
            toss = random.randint(1, 12)
            output_file.write(str(toss) + '\n')
            total += toss
        output_file.close()
    except:
        aok = False
    return aok


def complain(file_name):
    print(file_name, "is not a valid name for a file")


def read_file(file_name):
    try:
        input_file = open(file_name, "r")
        text = input_file.readlines()
        input_file.close()
    except:
        text = ''

    return text


def count_numbers(text):
    my_list = [0] * 12
    for line in text:
        number = int(line) - 1
        my_list[number] += 1

    return my_list


def display_results(frequencies):
    print("Face\tNumber of Tosses")
    print("----------------------------")
    count = 1
    new_list = []
    for line in frequencies:
        print(count, "\t\t", line)
        count += 1
        new_list += [line]
    smallest = min(new_list)
    biggest = max(new_list)
    smalls = []
    bigs = []
    for ix in range(len(new_list)):
        if new_list[ix] == smallest:
            smalls.append(ix+1)
        if new_list[ix] == biggest:
            bigs.append(ix+1)
    print('numbers', smalls, 'were the least rolled')
    print('numbers', bigs, 'were the most rolled')


def average_number_tossed(frequencies):
    total = 0
    number = 0
    for ix in range(len(frequencies)):
        product = (ix+1)*frequencies[ix]
        total += product
        number += frequencies[ix]
    average = total / number
    print(f'the average number tossed is {average:.2f}')


main()
