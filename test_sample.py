import unittest
from unittest.mock import patch
import sample # Import the module we want to test

class TestSample(unittest.TestCase):

    def test_generate_random_number_range(self):
        """Test that the generated number is within the default range."""
        for _ in range(100): # Run multiple times due to randomness
            num = sample.generate_random_number()
            self.assertTrue(1 <= num <= 100)

    def test_generate_random_number_custom_range(self):
        """Test that the generated number is within a custom range."""
        lower, upper = 10, 20
        for _ in range(50): # Run multiple times
            num = sample.generate_random_number(lower, upper)
            self.assertTrue(lower <= num <= upper)

    def test_generate_random_number_invalid_bounds_type(self):
        """Test that non-integer bounds raise TypeError."""
        with self.assertRaises(TypeError):
            sample.generate_random_number(1.5, 10)
        with self.assertRaises(TypeError):
            sample.generate_random_number(1, 10.5)
        with self.assertRaises(TypeError):
            sample.generate_random_number("a", 10)

    def test_generate_random_number_invalid_bounds_order(self):
        """Test that lower bound > upper bound raises ValueError."""
        with self.assertRaises(ValueError):
            sample.generate_random_number(100, 1)

    @patch('random.randint') # Mock the random.randint function
    def test_generate_random_number_mocked(self, mock_randint):
        """Test the function behavior by mocking random.randint."""
        expected_value = 42
        mock_randint.return_value = expected_value # Configure the mock

        # Call the function with default bounds
        result = sample.generate_random_number()

        # Assert that random.randint was called correctly
        mock_randint.assert_called_once_with(1, 100)
        # Assert that the function returned the mocked value
        self.assertEqual(result, expected_value)

        # Reset mock for next call
        mock_randint.reset_mock()

        # Call with custom bounds
        lower, upper = 5, 15
        expected_value_custom = 10
        mock_randint.return_value = expected_value_custom
        result_custom = sample.generate_random_number(lower, upper)

        # Assert that random.randint was called correctly with custom bounds
        mock_randint.assert_called_once_with(lower, upper)
        # Assert that the function returned the new mocked value
        self.assertEqual(result_custom, expected_value_custom)


if __name__ == '__main__':
    unittest.main()