import pytest

from string_calculator import StringCalculator

# Test specifications for the StringCalculator class based on the 
# kata link - https://osherove.com/tdd-kata-1.

@pytest.fixture
def calculator():
    return StringCalculator()

class TestStringCalculatorBasicOperations:
    def test_it_should_return_zero_when_input_is_empty(self, calculator):
        """Rule 1: Empty strings are identity values (0)."""
        assert calculator.add("") == 0
   

    def test_it_should_return_the_number_itself_for_single_inputs(self, calculator):
        """Rule 2: A single number requires no calculation."""
        assert calculator.add("1") == 1