# tests/test_module2.py 

import unittest

from modules.module2 import class_from_module2

class TestModule2(unittest.TestCase):
    def test_class_from_seedwords(self):
        instance = class_from_module2()
        self.assertEqual(instance.message, "Hello from inside a class in module2")

if __name__ == "__main__":
    unittest.main()


