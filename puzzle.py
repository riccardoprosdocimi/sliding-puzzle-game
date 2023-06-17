"""
    Riccardo Prosdocimi
    CS 5001, Fall 2021
    Final Project -- The Game: Puzzle Slider

    This is a Puzzle class.
    This makes saving the puzzles info to a data structure possible.
"""

import glob
import os
from screen import Screen
from error import Error


class Puzzle:
    def __init__(self):
        """
        This is the constructor of the Puzzle class.
        """

        self.screen = Screen()
        self.master_dict = {}
        self.puz_list = []

    def open_puz(self):
        """
        This method looks for .puz files in the root folder and saves the info
        to a nested dictionary while handling potential errors that may occur
        when files are missing.
        """

        default_puzzle = "mario.puz"
        puzzle = ''
        try:
            # scans root folder for .puz files and returns a list containing
            # any one that's found
            self.puz_list = glob.glob("*.puz")  # needed for warn_user()
            puz_list = glob.glob("*.puz")  # local list
            # more than 10 .puz files in the root folder?
            if len(puz_list) > 10:
                puz_list = self.puz_list[:10]  # keep just the first 10
                if default_puzzle not in puz_list:  # mario.puz got removed?
                    puz_list = puz_list[:9]  # remove one more .puz file
                    puz_list.append(default_puzzle)  # add mario.puz back
            try:
                for puzzle in puz_list:
                    puz_dict = {}
                    with open(puzzle, "r") as puz_file:
                        for line in puz_file:
                            key, value = line.split(": ")
                            value = value.strip("\n")
                            puz_dict[key] = value
                        puzzle_name = puz_dict["name"]
                    # nested dictionary with puzzle names as keys and puzzle
                    # info as values
                    self.master_dict[puzzle_name] = puz_dict
            except FileNotFoundError:
                # if .puz file not found in  root folder, show error image and
                # log the error
                self.screen.set_pop_up("Resources/file_error.gif")
                error = Error(puzzle, "Puzzle.open_puz()")
                error.write_puz_error()
        except FileNotFoundError:
            # if there's no .puz files in the root folder, show error image,
            # log the error, and quit the game
            self.screen.set_pop_up("Resources/file_error.gif")
            error = Error(".puz", "Puzzle.open_puz()")
            error.write_puz_error()
            os._exit(0)
        except OSError:
            print("Some unknown error occurred")

    def get_puz(self):
        """
        This method returns the nested dictionary.
        """

        self.open_puz()
        return self.master_dict

    def warn_user(self):
        """
        This method informs the player that some puzzles have been removed from
        the available choices because there were too many.
        """

        if len(self.puz_list) > 10:
            self.screen.set_pop_up("Resources/file_warning.gif")
