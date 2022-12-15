#!/usr/bin/env.python3

# Created by: Patrice Pat-Odita
# Created on: Dec 10, 2022
# This program calculates the distance between two points
# using user input while accepting decimals.

# calculates the distance of two points

import math


def calc_distance(
    x1,
    y1,
    x2,
    y2,
):

    # initializing points
    # first point
    distance1 = x2 - x1
    # second point
    distance2 = y2 - y1
    # calculating distance
    return math.sqrt((distance1**2) + (distance2**2))

    # get user input and display results


def main():
    # get user inputs
    x1 = input("enter x1 : ")

    x2 = input("enter x2 : ")

    y1 = input("enter y1 : ")

    y2 = input("enter y2 : ")

    try:
        # converts to float
        x1 = float(x1)

        x2 = float(x2)

        y1 = float(y1)

        y2 = float(y2)

        # calls function with the arguments
        distance = calc_distance(x1, y1, x2, y2)
        print(f"distance between ({x1}, {x2})and ({y1}, {y2}) is : {distance}")

    except Exception:
        print("Invalid input")


if __name__ == "__main__":
    main()
