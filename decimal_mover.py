#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: June 2022
# The code will move decimal spaces by user input


def decimals(integer, decimal_movement):
    # this code will make the decimal command
    
    # input
    
    integer = int(input("Enter in a integer with a decimal: "))
    
    decimal_movement = int(input("How many decimals do you want to remove?: "))

    rounding = integer * 10 ** (decimal_movement) + 0.5 * 10 ** (-decimal_movement)
    
    return rounding



def main():
    
    import math
    
    
    
    