from service import Service
import unittest
import random
from unittest.mock import MagicMock, patch, mock_open

def testDivideWithValues(instance, mockValue, divideArg, expected):
	instance.bad_random = MagicMock(mockValue)
	assert instance.divide(actualValue) == expected
	instance.bad_random.assert_called_once()

class ServiceTests(unittest.TestCase):
	def setUp(self):
		self.instance = Service()

	def test_divide(self):
		testDivideWithValues(self.instance, 1, 5, 0.2)
		testDivideWithValues(self.instance, 1, 0, float("inf"))
		testDivideWithValues(self.instance, 0, 5, 0)
		testDivideWithValues(self.instance, 5, 5, 1)
		testDivideWithValues(self.instance, -3, 5, -0.6)
		testDivideWithValues(self.instance, -2, -4, 0.5)
		testDivideWithValues(self.instance, 20000, -10000, -2)
		
	def test_abs_plus(self):
		assert instance.abs_plus(-1) == 0
		assert instance.abs_plus(1) == 2
		assert instance.abs_plus(0) == 1
		assert instance.abs_plus(-2) == -1
		assert instance.abs_plus(-2147483648) == -2147483647
		assert instance.abs_plus(2147483647) == 2147483648

	def test_complicated_function(self):
		self.instance.divide = MagicMock(25)
		self.assertRaises(SyntaxError, self.instance.complicated_function, 25)
		
		self.instance.divide = MagicMock(0)
		self.assertRaises(SyntaxError, self.instance.complicated_function, 9)
		
		self.instance.divide = MagicMock(100)
		self.assertRaises(SyntaxError, self.instance.complicated_function, 2)
		
		self.instance.divide = MagicMock(-25)
		self.assertRaises(SyntaxError, self.instance.complicated_function, 2)

	@patch("builtins.open")
	@patch("random.randint")
	def test_bad_random_with_integers(self, mockOpen, randintMock):
		mockOpen.return_value = [1, 4, 7]
		randintMock.return_value = 2
		assert self.instance.bad_random() == 2
		randintMock.assert_called_once_with_args(0, 2)
	
	@patch("builtins.open")
	def test_bad_random_with_non_integers(self, mockOpen):
		mockOpen.return_value = [1, "a", 7]
		self.assertRaises(ValueError, self.instance.bad_random)

	patch("builtins.open")
	def test_bad_random_with_no_found_file(self, mockOpen):
		self.assertRaises(FileNotFoundError, self.instance.bad_random)
