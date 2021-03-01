import sys
from os import system


def std_day():
    system("open /Applications/Microsoft\ Teams.app/")
    system("open /System/Applications/Mail.app/")


def engine():
    system("open /Documents/school/Year 12_&_13/Engineering")


def bus():
    system("open ~/Documents/school/Year\ 12_\&_13/Business")


def cs():
    system("open ~/Documents/school/Year\ 12_\&_13/Computer\ science/")


def python():
    system("open /Applications/PyCharm\ CE.app/")


if __name__ == '__main__':
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
        print("An error has occurred")