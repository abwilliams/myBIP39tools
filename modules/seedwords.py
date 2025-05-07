# mmodules/seed-words.py 

import logging
import os
import binascii
import random

class SeedWordClass():
    """
    This class will handle access to the BIP39 seed words
        set_language();     passed the two letter language code en, de, fr, es... etc.
        get_language();     returns the two letter language code.
        get_word_list();    returns a cleaned array of BIP39 words.
    Attributes : (str): message
    """
    def __init__(self):
        self.message = "Inside SeedWordClass()"
        self.language = "XX"
        self.list_size = 2048
        logging.info("Instance of SeedWordClass() created.")

    def set_language(self, language):
        """Sets (and checks) the BIP39 language to en, fr, de, es, cn... etc"""
        self.language = language
        logging.info(f"The BIP39 seed word language has been set to : - {self.language}")
        return

    def get_language(self):
        """ Returns the currently set BIP39 seed word language."""
        # print(f"The Seed Word Language is : - {self.language}")
        return self.language
    
    def get_word_list(self):
        """
        Returns the text contents of filename as an array.
        Assumes a text file input with one word per line.
        Strips whitespace and one word per element.
        Returns : list
        """
        # logging.info("Executing function get_word_list().")
        filename = "bip39-" + self.language + ".txt"
        logging.info(f"The seed word language file has been set to : '{filename}' .")

        word_list = []
        with open(filename, "rt", encoding="utf-8") as file:
            for line in file.readlines():
                word_list.append(line.strip())
        
        if len(word_list) != self.list_size:
            logging.critical(f"BIP39 Word List - incorrect length.")
        
        return word_list


