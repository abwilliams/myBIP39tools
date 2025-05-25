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
        get_seed_words():   returns a 12 or 24 BIP39 word list as an array.
    Attributes : (str): message
    """
    def __init__(self):
        self.message = "Inside SeedWordClass() - setting defaults - 12 English words."   
        self.language = "en"
        self.list_size = 2048
        self.sp_length = 12
        logging.info("Instance of SeedWordClass() created.")

    def set_language(self, BIP39lang):
        """Sets (and checks) the BIP39 language to en, fr, de, es, cn... etc"""
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
        # self.language = language
        # logging.info(f"The BIP39 seed word language has been set to : - {self.language}")
        return self.language

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
        filename = "bip39-" + self.language + ".txt"
        logging.info(f"Loading word_list array with the contents of '{filename}'.")
        word_list = []
        with open(filename, "rt", encoding="utf-8") as file:
            for line in file.readlines():
                word_list.append(line.strip())
        
        if len(word_list) != self.list_size:
            logging.critical(f"ERROR - BIP39 Word List - incorrect length.")
            
        return word_list
    
    def set_seed_words(self, number_of_words):
        # logging.info(f"Debug: number_of_words = {number_of_words}")  # Debug print
        # logging.info(f"Debug: seed_phrase_length = {self.sp_length}")  # Debug print
        if (number_of_words == 24):
            self.sp_length = 24
            # logging.info(f"BIP39 seed phrase length is {number_of_words} :'{self.sp_length}'")
        else:
            self.sp_length = 12        # NOTE NO CHECKS MADE
        logging.info(f"The length of the BIP39 seed phrase has been set to : - {self.sp_length}")
        return self.sp_length

    def get_seed_words(self):
        """Returns the length of the BIP39 seed phrase (i.e. 12 or 24."""
        return self.sp_length

    def get_random_numbers(self, n):
        """Returns an array of 12 or 24 random numbers between 0 and 2047."""
        # logging.info(f"Debug: returning array [0,10,20..100,110].")     # Debug print
        # logging.info(f"Debug: n = {n}.")     # Debug print
        return [0,10,20,30,40,50,60,70,80,90,100,110]

