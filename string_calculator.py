class StringCalculator:

    def __init__(self):
        self.base_delimiter = ','

    def _parse(self, numbers: str) -> str:
        return [int(num) for num in numbers.split(self.base_delimiter)]

    def _normalize(self, numbers: str) -> str:

        if numbers.startswith("//"):
            delimiter, numbers = numbers[2:].split('\n')
            numbers = numbers.replace(delimiter, self.base_delimiter)

        numbers = numbers.replace('\n', self.base_delimiter)
        return numbers

    def add(self, input_string: str) -> int:
        if not input_string:
            return 0
        
        normalized_string = self._normalize(input_string)
    
        return sum(self._parse(normalized_string))