# mmodules/odule2.py 

import logging

class class_from_module2():
    """
    This is a sample class from module2.
    This class represents XYZ and provides a message attribute.
    Attributes : (str): message
    """
    def __init__(self):
        self.message = "Hello from inside a class in module2"
        logging.info("This is an instance of a class created in module2.")

