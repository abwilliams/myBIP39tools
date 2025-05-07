#!/usr/bin/env python3

# main.py
"""
This is the entry point for the project, the main purpose of which is to learn how to code in VCS.
"""

import logging
# import argparse
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
    logging.info("Program started.")

    # # This example requires 'import argparse'.
    # parser = argparse.ArgumentParser(description="Create a Bitcoin pass phrase.")
    # parser.add_argument('filename', help='Word list file to be used.', type=str)
    # parser.add_argument('second', help='second number', type=str)
    # args = parser.parse_args()
    # print(args)
    # print(args.filename)        print(filename)

    # print(args.second)

    # ... rest of your code
    seed_words = SeedWordClass()
    seed_words.set_language("en")
    print(f"The current seed word language is set to '{seed_words.get_language()}'." )
    word_list = seed_words.get_word_list()

    

    print(word_list[333])

    logging.info("Program terminated successfully.")
    return    

if __name__ == "__main__":
    main()

