

from os import system

import argparse

def std_day():
    system("open /Applications/Microsoft\ Teams.app/")
    system("open /System/Applications/Mail.app/")


def engineering():
    system("open ~/Documents/school/Year\ 12_\&_13/Engineering")


def business():
    system("open ~/Documents/school/Year\ 12_\&_13/Business")


def computer_science():
    system("open ~/Documents/school/Year\ 12_\&_13/Computer\ science/")


def python():
    system("open /Applications/PyCharm\ CE.app/")


def fusion():
    system("open ~/Applications/Autodesk\ Fusion\ 360.app/")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="This allows quick opening of applications used within the school day"
    )

    parser.add_argument(
        "-s",
        "--start",
        action='store_true',
        help="This will open all the standard applications used within the school day.",
    )

    parser.add_argument(
        "-e",
        "--engineering",
        action='store_true',
        help="This will show the Engineering folder within Documents",
    )
    parser.add_argument(
        "-b",
        "--business",
        action='store_true',
        help="This will show the Business folder within Documents"
    )
    parser.add_argument(
        "-c",
        "--computer",
        action='store_true',
        help="This will show the Computer Science folder within Documents",
    )
    parser.add_argument(
        "--python", action='store_true', help="This will open the PyCharm application"
    )

    parser.add_argument(
        "--fusion", action='store_true', help="This will open the Fusion 365 application"
    )

    args = parser.parse_args()

    try:
        if args.engineering:
            engineering()
        if args.computer:
            computer_science()
        if args.python:
            python()
        if args.business:
            business()
        if args.start:
            std_day()
        if args.fusion:
            fusion()
    except Exception as error:
        print(error)