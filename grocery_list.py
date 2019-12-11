#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: December 2019
# This program makes a grocery list


def make_list(fruits, veggies):
    # This function creates a grocery list
    grocery_list = []

    # combines elements alternately in one 'array'
    for loop_counter in range(0, 3):
        grocery_list.append(fruits[loop_counter])
        grocery_list.append(veggies[loop_counter])

    return grocery_list


def main():
    # This asks for grocery items

    fruits = []
    veggies = []

    # output
    print("Welcome to the useless all-vegan grocery list maker!")
    print("")

    # input for fruits
    for loop_counter in range(0, 3):
        while True:
            fruit = input("What fruits will you buy: ")
            if fruit.isalpha():
                fruits.append(fruit)
                break
            else:
                print("Letters only please.")

    # input for veggies
    for loop_counter in range(0, 3):
        while True:
            veggie = input("What veggies will you buy: ")
            if veggie.isalpha():
                veggies.append(veggie)
                break
            else:
                print("Letters only please.")
    print("")

    # call function
    grocery_list = make_list(fruits, veggies)

    # output
    print("This is your grocery list:")
    for loop_counter in range(0, 6):
        print("☐", grocery_list[loop_counter])


if __name__ == "__main__":
    main()
