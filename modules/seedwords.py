# mmodules/seed-words.py 

import logging
import os
import binascii
import random

class SeedWordClass():
    """
    This class will handle access to the BIP39 seed words
        set_language();     passed the lowercase two letter language code en, de, fr, es... etc.
        get_language();     returns the two letter language code.
        set_bip39_array();  sets a cleaned ordered array[2048] of BIP39 words.
        get_bip39_array();  returns the BIP39 ordered array[2048] of words.
        set_bip39_file();   sets the BIP39 word list filename.
        set_bip39_file();   returns the BIP39 word list filename.
        set_seed_words():   creates an array of 12 or 24 BIP39 words.
        get_seed_words():   returns the length [12|24] of the BIP39 word list.
        set_random_numbers(): returns a 12 or 24 BIP39 word list as an array
    Attributes : (str): message
    """
    def __init__(self):
        self.message = "Inside SeedWordClass() - setting defaults - 12 English words."   
        self.language = "en"
        self.list_size = 2048
        self.bip39_array = []
        self.sp_length = 12
        self.bip39_file = "bip39-en.txt"
        # logging.info("Instance of SeedWordClass() with default values created.")

    def set_language(self, BIP39lang):
        """Sets (and checks) the BIP39 language to en, fr, de, es, cn... etc"""
        logging.info(f"LAnguage = {BIP39lang}")
        match BIP39lang:
            case "en":
                self.language = BIP39lang
                return
            case "es":
                self.language = BIP39lang
                return
            case "de":
                self.language = BIP39lang
                return
            case "fr":
                self.language = BIP39lang
                return
            case "cn":
                self.language = BIP39lang
                return
            case "xx":
                self.language = BIP39lang
                return
            case "":
                self.language = "ERROR - Selected Nothing."
                return
            case _:
                self.language = "ERROR - UNKNOWN Error."
                return
        return

    def get_language(self):
        """ Returns the currently set BIP39 seed word language."""
        # print(f"The Seed Word Language is : - {self.language}")
        return self.language
    
    def set_bip39_file(self):
        self.bip39_file = "bip39-" + self.get_language() + ".txt"
        return
    
    def get_bip39_file(self):
        return self.bip39_file

    def set_bip39_array(self):
        """
        Returns the text contents of filename as an array.
        Assumes a text file with one word per line.
        Strips whitespace and one word per element.
        Returns : array[2048]
        """
        logging.info(f"Loading word_list array with the contents of '{self.bip39_file}'.")

        with open(self.bip39_file, "rt", encoding="utf-8") as file:
            for line in file.readlines():
                self.bip39_array.append(line.strip())
        
        logging.info(f"Array Length = {len(self.bip39_array)}")
        
        if len(self.bip39_array) != self.list_size:
            logging.critical(f"ERROR - BIP39 Word List - incorrect length.")

        return

    def get_bip39_array(self):
        return self.bip39_array
    
    def set_seed_words(self, number_of_words):
        if number_of_words == 12:
            self.sp_length = 12
        elif number_of_words == 24:
            self.sp_length = 24
        else:
            self.sp_length = 0
            logging.info(f"ERROR invalid seed phrase: {number_of_words}")
       
        return

    def get_seed_words(self):
        """Returns the length of the BIP39 seed phrase (i.e. 12 or 24."""
        return self.sp_length

    def get_random_numbers(self, n):
        """Returns an array of 12 or 24 random numbers between 0 and 2047."""
        # logging.info(f"Debug: returning array [0,10,20..100,110].")     # Debug print
        # logging.info(f"Debug: n = {n}.")     # Debug print
        return [0,10,20,30,40,50,60,70,80,90,100,110]

