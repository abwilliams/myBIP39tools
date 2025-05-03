# main.py
"""
This module serves as the entry point for the project.
It contains the main function that orcestrates the execution of the project.
"""
import logging
from modules.module1 import function_from_module1
from modules.module2 import class_from_module2

# initialise logging - INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s -%(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main():
    """
    This is the main function of the program.
    This program does XYZ and calls other functions
    Returns : none
    """
    logging.info("Program started.")

    result = function_from_module1()
    logging.info(f"Result from module1: {result}")

    instance = class_from_module2()
    logging.info(f"Result from module2: {instance.message}")   

    # ... rest of your code
    
    logging.info("Program terminated successfully.")

if __name__ == "__main__":
    main()


