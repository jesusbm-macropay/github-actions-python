import unittest
from hello import greetings

class TestGreeting(unittest.TestCase):
    """My first test class"""
    
    def test_greeting(self):
        """My first test case"""
        self.assertEqual(greetings(), "hola mundo")

    def test_greeting2(self):
        """My second test case"""
        self.assertEqual(greetings(), "hola mundo")

if __name__ == "__main__":
    unittest.main()
