#!/usr/bin/env python3

# main.py
"""
This is the entry point for the project.
The secondary purpose is to learn how to code in VCS.
"""

import logging
import argparse
# import requests     # TESTING ONLY
# import json         # TESTING ONLY
from modules.seedwords import SeedWordClass

# initialise logging - INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s -%(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main():
    """
    main() program entry point.
    Returns : none
    """
    # Consider seperating arg parsing into its own module and ouside SeedWordClass.
    # Parse arguments, unknown language and incorrect number of words ie. != 12 or 24.

    logging.info("Program started.")

    # import argparse to take 
    parser = argparse.ArgumentParser(description="Create a 12 or 24 word BIP39 pass phrase.")
    parser.add_argument('language', help='Two letter code of the language word list to be used.', type=str)
    parser.add_argument('number_of_words', help='The number of seed words. [12|24]', type=int)
    args = parser.parse_args()

    logging.info(f"\n\nargs : {args}, Language : {args.language}, Number of Words : {args.number_of_words}.\n")

    # ... rest of the code

    seed_words = SeedWordClass()
    seed_words.set_language(args.language)
    seed_words.set_seed_words(args.number_of_words)
    # logging.info(f"The seed word language is '{seed_words.get_language()}'." )
    # logging.info(f"The seed phrase length has been set to '{seed_words.get_seed_words()}'." )
    seed_words.set_bip39_array()
    # Get 12 or 24 random numbers between 0 and 2047

    # logging.info(f"Seed words are {seed_words.get_random_numbers(seed_words.get_bip39_file())}.")
    # logging.info(f"Filename = {seed_words.get_bip39_file()}.")

    # word_list = seed_words.get_word_list()
    # print(f"The first word is : '{word_list[0]}'.")     
    # # NOTE blank first word in xx seed word file
    # print(f"The 256th word is : '{word_list[255]}'.")
    # print(f"The last word is  : '{word_list[2047]}'.")

    logging.info("Program terminated successfully.")
    return

if __name__ == "__main__":
    main()

