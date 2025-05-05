# mmodules/seed-words.py 

import logging
import os
import binascii

class SeedWordClass():
    """
    This class will handle access to the BIP39 seed words
    The single parameter that will be passed is the language.
    Attributes : (str): message
    """
    def __init__(self):

        self.message = "Inside a class in seedwords module"
        self.language = "XX"
        logging.info("Instance of the SeedWords() class created.")

    def set_language(self, language):
        self.language = language
        print(f"The Seed Word Language has been set to : - {self.language}")


    def show_language(self):
        print(f"The Seed Word Language is : - {self.language}")
    

    def get_word_list(self):
        """
        Returns the text contents of filename as a list.
        Assumes a text file input with one word per line.
        Strips whitespace on output.
        Returns : list
        """
        logging.info("Executing function get_word_list().")
        filename = "bip39-" + self.language + ".txt"
        logging.info("The seed word language file has been set to : " + filename)

        word_list = []
        with open(filename, "rt", encoding="utf-8") as file:
            for line in file.readlines():
                word_list.append(line.strip())
        return word_list

''' Select language function required '''
