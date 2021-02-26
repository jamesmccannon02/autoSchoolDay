import sys
from os import system
import logging

def std_day():
    logging.info("Opening applications")
    system("open /Applications/Microsoft\ Teams.app/")
    system("open /System/Applications/Mail.app/")




if __name__ == '__main__':
    logging.basicConfig(filename="autoSchoolDay.log")
    try:
        if len(sys.argv) > 1:
            print("Operation not available")
        else:
            std_day()
    except:
        logging.error("Operation did not work")
        print("An error has occurred")

