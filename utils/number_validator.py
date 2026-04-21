class NumberValidator:
    def __init__(self):
        self.max_allowed_number = 1000

    def validate_and_filter(self, numbers: list[int]) -> list[int]:
        negatives = [n for n in numbers if n < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {negatives}")
        
        return [n for n in numbers if n <= self.max_allowed_number]
