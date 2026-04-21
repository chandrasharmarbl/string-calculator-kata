import re

class StringCalculator:

    def __init__(self):
        self.base_delimiter = ','
        self.max_allowed_number = 1000
        self.call_count = 0

    def get_call_count(self):
        return self.call_count

    def _parse(self, numbers: str) -> str:
        parsed = []
        negatives = []

        for n in numbers.split(self.base_delimiter):
            val = int(n)
            if val < 0:
                negatives.append(val)
            elif val <= self.max_allowed_number:
                parsed.append(val)

        return parsed, negatives

    def _normalize(self, numbers: str) -> str:

        if numbers.startswith("//"):
            header, numbers = numbers.split('\n')
            delimiters = re.findall(r"\[(.*?)\]", header)

            if delimiters:
                for d in delimiters:
                    numbers = numbers.replace(d, self.base_delimiter)
            else:
                delimiter = header[2:]
                numbers = numbers.replace(delimiter, self.base_delimiter)

        numbers = numbers.replace('\n', self.base_delimiter)
        return numbers

    def add(self, input_string: str) -> int:
        self.call_count += 1
        if not input_string:
            return 0
        
        normalized_string = self._normalize(input_string)
        parsed, negatives = self._parse(normalized_string)
        if negatives:
            raise ValueError(f"negatives not allowed: {negatives}")
        return sum(parsed)