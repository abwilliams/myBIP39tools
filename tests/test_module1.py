# tests/module1.py 

import unittest
from modules.module1 import function_from_module1

class TestModule1(unittest.TestCase):
    """
    Unit tests for funtions in module1.
    """
    def test_function_from_module1(self):
        """
        Test function_from_module1.
        This test ensures that function_from_module1 returns the message.
        Returns: none
        """
        result = function_from_module1()
        self.assertEqual(result, "Hello from inside module1")

if __name__ == "__main__":
    unittest.main()


