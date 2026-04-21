from utils.input_parser import InputParser
from utils.number_validator import NumberValidator
from utils.call_counter import CountCalls

class StringCalculator:
    def __init__(self):
        self.parser = InputParser()
        self.validator = NumberValidator()

    def get_call_count(self) -> int:
        return StringCalculator.add.get_count(self)

    @CountCalls
    def add(self, input_string: str) -> int:
        if not input_string:
            return 0
            
        parsed_numbers = self.parser.parse(input_string)
        valid_numbers = self.validator.validate_and_filter(parsed_numbers)
        
        return sum(valid_numbers)