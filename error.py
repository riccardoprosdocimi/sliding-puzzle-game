"""
    Riccardo Prosdocimi
    CS 5001, Fall 2021
    Final Project -- The Game: Puzzle Slider

    This is an Error class.
    This makes logging error messages to a file possible.
"""

import datetime
from constants import MONTHS, DAYS


class Error:
    def __init__(self, file, location):
        """
        This is the constructor of the Error class.

        :param file: the file that can't be opened/found/accessed (str)
        :param location: the method in which the error occurs (str)
        """

        self.now = datetime.datetime.today()  # current day and time
        # converts int returned by weekday to a 3-letter str by accessing the
        # DAYS list (0 = Monday)
        self.day = DAYS[self.now.weekday()]
        # converts int returned by month to a 3-letter str by accessing the
        # MONTHS list (1 = January)
        self.month = MONTHS[self.now.month - 1]
        self.date = self.now.day
        self.hour = self.now.hour
        self.minute = self.now.minute
        self.second = self.now.second
        self.year = self.now.year
        self.file = file
        self.location = location

    def write_file_error(self):
        """
        This method writes the error message for a file that can't be opened or
        accessed to a file named '5001_puzzle.err'.
        """

        try:
            with open("5001_puzzle.err", "a") as error_file:
                error_file.write(str(self.day) + " " + str(self.month) + " " +
                                 str(self.date) + " " + str(self.hour) + ":" +
                                 str(self.minute) + ":" + str(self.second) +
                                 " " + str(self.year) + ":" +
                                 "Error: Could not open " + self.file + ". " +
                                 "LOCATION: " + self.location + "\n")
        except FileNotFoundError:
            print("Could not open/access/find 5001_puzzle.err")
        except OSError:
            print("Some unknown error occurred")

    def write_puz_error(self):
        """
        This method writes the error message for a file that can't be found to
        a file named '5001_puzzle.err'.
        """

        try:
            with open("5001_puzzle.err", "a") as error_file:
                error_file.write(str(self.day) + " " + str(self.month) + " " +
                                 str(self.date) + " " + str(self.hour) + ":" +
                                 str(self.minute) + ":" + str(self.second) +
                                 " " + str(self.year) + ":" + "Error: File " +
                                 self.file + " does not exist. LOCATION: " +
                                 self.location + "\n")
        except FileNotFoundError:
            print("Could not open/access/find 5001_puzzle.err")
        except OSError:
            print("Some unknown error occurred")
