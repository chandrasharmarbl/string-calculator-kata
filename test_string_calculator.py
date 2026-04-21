import pytest

from string_calculator import StringCalculator

# Test specifications for the StringCalculator class based on the 
# kata link - https://osherove.com/tdd-kata-1.

@pytest.fixture
def calculator():
    return StringCalculator()

class TestStringCalculatorBasicOperations:
    def test_it_should_return_zero_when_input_is_empty(self, calculator):
        assert calculator.add("") == 0

    def test_it_should_return_the_number_itself_for_single_inputs(self, calculator):
        assert calculator.add("1") == 1
    
    def test_it_should_return_the_sum_of_two_numbers_separated_by_commas(self, calculator):
        assert calculator.add("1,2") == 3
    
    def test_it_should_return_the_sum_of_all_numbers_separated_by_commas(self, calculator):
        assert calculator.add("1,2,3,4,5") == 15

class TestDelimiterHandling:
    def test_it_should_allow_newlines_as_valid_delimiters(self, calculator):
        assert calculator.add("1\n2,3") == 6

    def test_it_should_support_user_defined_custom_delimiters(self, calculator):
        assert calculator.add("//;\n1;2") == 3

class TestInputValidation:
    def test_it_must_prohibit_negative_numbers(self, calculator):
        with pytest.raises(ValueError, match="negatives not allowed: \\[-2\\]"):
            calculator.add("1,-2")

    def test_it_must_list_all_negatives_in_the_error_message(self, calculator):
        with pytest.raises(ValueError, match="negatives not allowed: \\[-2, -5\\]"):
            calculator.add("1,-2,3,-5")

    def test_it_should_ignore_numbers_greater_than_one_thousand(self, calculator):
        assert calculator.add("2,1001") == 2

class TestCalculatorUsage:
    def test_it_should_report_the_total_number_of_times_add_was_called(self, calculator):
        calculator.add("1")
        calculator.add("2")
        assert calculator.get_call_count() == 2

class TestAdvancedDelimiters:
    def test_it_should_handle_long_delimiters(self, calculator):
        assert calculator.add("//[***]\n1***2***3") == 6

    def test_it_should_handle_multiple_delimiters(self, calculator):
        assert calculator.add("//[*][%]\n1*2%3") == 6

    def test_it_should_handle_multiple_long_delimiters(self, calculator):
        assert calculator.add("//[***][%%]\n1***2%%3") == 6

class TestEdgeCases:
    def test_it_should_handle_numbers_with_leading_or_trailing_spaces(self, calculator):
        assert calculator.add(" 1 , 2 , 3 ") == 6