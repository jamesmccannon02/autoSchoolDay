import sys
from os import system
import logging


def std_day():
    logging.info("Opening applications")
    system("open /Applications/Microsoft\ Teams.app/")
    system("open /System/Applications/Mail.app/")


def engine():
    logging.info("Engineering folders opened")
    system("open /Documents/school/Year 12_&_13/Engineering")


def bus():
    logging.info("Business folders opened")
    system("open ~/Documents/school/Year\ 12_\&_13/Business")


def cs():
    logging.info("Business folders opened")
    system("open ~/Documents/school/Year\ 12_\&_13/Computer\ science/")


def python():
    system("open /Applications/PyCharm\ CE.app/")


if __name__ == '__main__':
    logging.basicConfig(filename="/autoProjects/autoSchoolDay/autoSchoolDay.log")
    try:
        if len(sys.argv) > 1:
            if sys.argv[1] == "engine":
                engine()
            elif sys.argv[1] == "cs":
                cs()
            elif sys.argv[1] == "python":
                python()
            elif sys.argv[1] == "bus":
                bus()
        else:
            std_day()
    except:
        logging.error("Operation did not work")
        print("An error has occurred")
