#!/usr/local/bin/python3

import sys
from os import system

import argparse

def std_day():
    system("open /Applications/Microsoft\ Teams.app/")
    system("open /System/Applications/Mail.app/")


def engineering():
    system("open /Documents/school/Year 12\_&\_13/Engineering")


def business():
    system("open ~/Documents/school/Year\ 12_\&_13/Business")


def computer_science():
    system("open ~/Documents/school/Year\ 12_\&_13/Computer\ science/")


def python():
    system("open /Applications/PyCharm\ CE.app/")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="This allows quick opening of applications used within the school day")
    subparsers = parser.add_subparsers()

    #main commands
    parser.add_argument("school", choices=['start', 'engine', 'bus', 'cs', 'python'])

    #Sub commands
    parser_engineering = subparsers.add_parser("engine", help="This is used to control all aspects of the engineering command")


    args = parser.parse_args()

    try:
        if args.school:
            if args.school.engine:
                engineering()
            elif args.school == "cs":
                computer_science()
            elif args.school == "python":
                python()
            elif args.school == "bus":
                business()
            elif args.school == "start":
                std_day()
        elif args.engine:
            if args.engine == "engine":
                engineering()
    except Exception as e:
        print("An error has occurred", e)