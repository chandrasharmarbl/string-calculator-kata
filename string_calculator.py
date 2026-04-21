class StringCalculator:

    def _parse(self, numbers: str) -> str:
        delimiter = ','
        if numbers.startswith("//"):
            delimiter, numbers = numbers[2:].split('\n')
            
        numbers = numbers.replace('\n', delimiter)
        return [int(num) for num in numbers.split(delimiter)]

    def add(self, input_string: str) -> int:
        if not input_string:
            return 0
        
        return sum(self._parse(input_string))