#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: June 2022
# The code will move decimal spaces by user input


def decimals(integer, movement):
    # this code will make the decimal command

    # process

    rounding = integer * (10 ** (movement)) + 0.5
    rounding = int(rounding)
    rounding = rounding / (10 ** (movement))

    return rounding


def main():

    # call functions

    # input & output

    try:
        integer = float(input("Enter in your decimal number: "))
        movement = int(input("How many decimal spaces do you want it rounded to: "))
        print("")

        print(decimals(integer, movement))
    except Exception:
        print("\nPlease follow the instructions listed above.")


if __name__ == "__main__":
    main()
