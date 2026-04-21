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
    
    def test_it_should_return_the_sum_of_two_numbers_separated_by_commas(self, calculator):
        """Rule 3: For two numbers separated by commas, the result is their sum."""
        assert calculator.add("1,2") == 3
    
    def test_it_should_return_the_sum_of_all_numbers_separated_by_commas(self, calculator):
        """Rule 4: For any number of comma separated numbers, the result is their sum."""
        assert calculator.add("1,2,3,4,5") == 15

class TestDelimiterHandling:
    def test_it_should_allow_newlines_as_valid_delimiters(self, calculator):
        """Rule 4: Newlines should be treated exactly like commas."""
        assert calculator.add("1\n2,3") == 6

    def test_it_should_support_user_defined_custom_delimiters(self, calculator):
        """Rule 5: Users can define a custom delimiter using the // syntax."""
        assert calculator.add("//;\n1;2") == 3