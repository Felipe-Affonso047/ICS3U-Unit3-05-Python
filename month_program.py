#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program gets a number and show which month relates to it

def main():
    # this function relates the number with the month
    month_number = int(input("Insert a month number from 1 to 12:"))

    if month_number == 1:
        print("\nThe {} month is January!".format(month_number))
    elif month_number == 2:
        print("\nThe {} month is February!".format(month_number))
    elif month_number == 3:
        print("\nThe {} month is March!".format(month_number))
    elif month_number == 4:
        print("\nThe {} month is April!".format(month_number))
    elif month_number == 5:
        print("\nThe {} month is May!".format(month_number))
    elif month_number == 6:
        print("\nThe {} month is June!".format(month_number))
    elif month_number == 7:
        print("\nThe {} month is July!".format(month_number))
    elif month_number == 8:
        print("\nThe {} month is August!".format(month_number))
    elif month_number == 9:
        print("\nThe {} month is September!".format(month_number))
    elif month_number == 10:
        print("\nThe {} month is October!".format(month_number))
    elif month_number == 11:
        print("\nThe {} month is November!".format(month_number))
    elif month_number == 12:
        print("\nThe {} month is December!".format(month_number))
    else:
        print("\nThis number is invalid.")

    print("\nDone.")


if __name__ == "__main__":
    main()
