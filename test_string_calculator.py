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

class TestInputValidation:
    def test_it_must_prohibit_negative_numbers(self, calculator):
        """Rule 6: Negative numbers are invalid and must trigger an exception."""
        with pytest.raises(ValueError, match="negatives not allowed: \\[-2\\]"):
            calculator.add("1,-2")

    def test_it_must_list_all_negatives_in_the_error_message(self, calculator):
        """Rule 7: Error messages must be helpful by showing all offending numbers."""
        with pytest.raises(ValueError, match="negatives not allowed: \\[-2, -5\\]"):
            calculator.add("1,-2,3,-5")

    def test_it_should_ignore_numbers_greater_than_one_thousand(self, calculator):
        """Rule 8: Numbers > 1000 are considered out of bounds and ignored in sums."""
        assert calculator.add("2,1001") == 2
