from service import Service
import unittest
import random
from unittest.mock import MagicMock, patch, mock_open

class MockFile:
	def __init__(self, returnValue):
		self.returnValue = returnValue
	
	def readlines(self):
		return self.returnValue

class ServiceTests(unittest.TestCase):
	def setUp(self):
		self.instance = Service()
		
	def _testDivideWithValues(self, mockValue, divideArg, expected, badRandomMock):
		badRandomMock.return_value = mockValue
		assert self.instance.divide(divideArg) == expected
	
	@patch("service.Service.bad_random")
	def test_divide(self, badRandomMock):
		self._testDivideWithValues(1, 5, 0.2, badRandomMock)
		self._testDivideWithValues(0, 5, 0, badRandomMock)
		self._testDivideWithValues(5, 5, 1, badRandomMock)
		self._testDivideWithValues(-3, 5, -0.6, badRandomMock)
		self._testDivideWithValues(-2, -4, 0.5, badRandomMock)
		self._testDivideWithValues(20000, -10000, -2, badRandomMock)
		
		badRandomMock.return_value = 1
		self.assertRaises(ZeroDivisionError, self.instance.divide, 0)
		
	def test_abs_plus(self):
		assert self.instance.abs_plus(-1) == 2
		assert self.instance.abs_plus(1) == 2
		assert self.instance.abs_plus(0) == 1
		assert self.instance.abs_plus(-2) == 3
		assert self.instance.abs_plus(-2147483648) == 2147483649
		assert self.instance.abs_plus(2147483647) == 2147483648
		assert self.instance.abs_plus(0.55555) == 1.55555
		assert self.instance.abs_plus(-0.55555) == 1.55555
		self.assertRaises(TypeError, self.instance.abs_plus, "a")

	def test_complicated_function(self):
		self.instance.divide = MagicMock(25)
		self.assertRaises(TypeError, self.instance.complicated_function, 25)
		
		self.instance.divide = MagicMock(0)
		self.assertRaises(TypeError, self.instance.complicated_function, 9)
		
		self.instance.divide = MagicMock(100)
		self.assertRaises(TypeError, self.instance.complicated_function, 2)
		
		self.instance.divide = MagicMock(-25)
		self.assertRaises(TypeError, self.instance.complicated_function, 2)

	@patch("builtins.open")
	@patch("random.randint")
	def test_bad_random(self, randintMock, mockOpen):
		# integers
		mockOpen.return_value = MockFile([1, 4, 7])
		randintMock.return_value = 2
		assert Service.bad_random() == 2
		randintMock.assert_called_once_with(0, 2)
		randintMock.reset_mock()
		
		# empty
		mockOpen.return_value = MockFile([])
		randintMock.return_value = -1
		assert Service.bad_random() == -1
		randintMock.assert_called_once_with(0, -1)
		randintMock.reset_mock()
		
		# float
		mockOpen.return_value = MockFile([5.2])
		randintMock.return_value = 0
		assert Service.bad_random() == 0
		randintMock.assert_called_once_with(0, 0)
		randintMock.reset_mock()
		
		# non-numeric values
		mockOpen.return_value = MockFile([1, "a", 7])
		self.assertRaises(ValueError, Service.bad_random)
		mockOpen.reset_mock()
		
	def test_bad_random_file_error(self):
		self.assertRaises(FileNotFoundError, Service.bad_random)
