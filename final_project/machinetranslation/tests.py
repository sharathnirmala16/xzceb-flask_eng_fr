import unittest
from translator import english_to_french, french_to_english

class TestMyModule(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french("Hi"), "Salut")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_f2e(self):
        self.assertEqual(french_to_english("Salut"), "Hi")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()