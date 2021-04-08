import unittest
from random import randrange
from .main import Enigma


class TestEnigma(unittest.TestCase):
    def setUp(self):
        self.enigma = Enigma()
        self.text_before_encode = 'This is testing text, lets check the code'
        self.key = 'keyword'

    def get_random_text(self):
        random_text_before_encode = ''
        for i in range(randrange(10, 200)):
            random_text_before_encode += chr(randrange(32, 126))
        return random_text_before_encode

    def get_random_key(self):
        random_key = ''
        for i in range(randrange(5, 20)):
            random_key += chr(randrange(32, 126))
        return random_key

    def test_text_after_encode_is_different_than_before(self):
        cipher = self.enigma.encode(self.text_before_encode, self.key)
        self.assertNotEqual(cipher, self.text_before_encode)

    def test_text_after_encode_and_decode_is_the_same(self):
        cipher = self.enigma.encode(self.text_before_encode, self.key)
        text_after_decode = self.enigma.decode(cipher, self.key)
        self.assertEqual(self.text_before_encode, text_after_decode)

    def test_random_text_after_encode_and_decode_is_the_same_1(self):
        random_text_before_encode = self.get_random_text()
        random_key = self.get_random_key()

        print(f"text: {random_text_before_encode}")
        print(f"key: {random_key}\n\n")

        cipher = self.enigma.encode(random_text_before_encode, random_key)
        text_after_decode = self.enigma.decode(cipher, random_key)
        self.assertEqual(random_text_before_encode, text_after_decode)

    def test_random_text_after_encode_and_decode_is_the_same_2(self):
        random_text_before_encode = self.get_random_text()
        random_key = self.get_random_key()

        print(f"text: {random_text_before_encode}")
        print(f"key: {random_key}\n\n")

        cipher = self.enigma.encode(random_text_before_encode, random_key)
        text_after_decode = self.enigma.decode(cipher, random_key)
        self.assertEqual(random_text_before_encode, text_after_decode)