#!/usr/bin/env python3

# Created by: Cameron Teed
# Created on: Nov 2019
# This program calculates the area of a triangle with 2 funcitons


def area(base, height):
    # calculates the area of a triangle

    # process
    area = (base * height) / 2

    # output
    print("\nThe area is " + str(area) + " cm squared.")


def main():
    # This is asks for the base and hieght, then it  runs area()

    # variables
    base = 0
    height = 0

    while True:
        try:
            base = int(input("What is the base (cm): "))
            height = int(input("What is the height (cm): "))

            # runs area()
            area(base, height)
            break
        except ValueError:
            print("Please put in a integer. ")


if __name__ == "__main__":
    main()
