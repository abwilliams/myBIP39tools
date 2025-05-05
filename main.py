# main.py
"""
This module serves as the entry point for the project, the main purpose of which is to learn how to code in VCS.
It contains the main function that orcestrates the execution of the project i.e. - main; module1; module2
"""
import logging
# from modules.module1 import function_from_module1
# from modules.module2 import class_from_module2
from modules.seedwords import SeedWordClass

# initialise logging - INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s -%(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main():
    """
    This is the program entry point which calls all other functions.
    Returns : none
    """

    logging.info("Program started.")

    # result = function_from_module1()
    # logging.info(f"Result from module1: {result}")

    # instance = class_from_module2()
    # logging.info(f"Result from module2: {instance.message}")

    # ... rest of your code
    seed_words = SeedWordClass()
    logging.info(f"Result from seedwords module: {seed_words.message}") 

    seed_words.show_language()

    logging.info("Program terminated successfully.")

if __name__ == "__main__":
    main()


