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
