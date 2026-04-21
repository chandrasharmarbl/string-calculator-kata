import re

class InputParser:
    def __init__(self):
        self.base_delimiter = ','

    def parse(self, input_string: str) -> list[int]:
        if not input_string:
            return []
        
        normalized_string = self._normalize(input_string)
        return [int(n) for n in normalized_string.split(self.base_delimiter)]

    def _normalize(self, numbers: str) -> str:
        if numbers.startswith("//"):
            header, numbers = numbers.split('\n', 1)
            delimiters = re.findall(r"\[(.*?)\]", header)

            if delimiters:
                for d in delimiters:
                    numbers = numbers.replace(d, self.base_delimiter)
            else:
                delimiter = header[2:]
                numbers = numbers.replace(delimiter, self.base_delimiter)

        numbers = numbers.replace('\n', self.base_delimiter)
        return numbers

class NumberValidator:
    def __init__(self):
        self.max_allowed_number = 1000

    def validate_and_filter(self, numbers: list[int]) -> list[int]:
        negatives = [n for n in numbers if n < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {negatives}")
        
        return [n for n in numbers if n <= self.max_allowed_number]

class StringCalculator:
    def __init__(self):
        self.call_count = 0
        self.parser = InputParser()
        self.validator = NumberValidator()

    def get_call_count(self) -> int:
        return self.call_count

    def add(self, input_string: str) -> int:
        self.call_count += 1
        if not input_string:
            return 0
            
        parsed_numbers = self.parser.parse(input_string)
        valid_numbers = self.validator.validate_and_filter(parsed_numbers)
        
        return sum(valid_numbers)