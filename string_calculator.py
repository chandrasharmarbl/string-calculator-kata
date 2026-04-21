class StringCalculator:
    def add(self, input_string: str) -> int:
        if not input_string:
            return 0
        
        input_string = input_string.replace('\n', ',')
        return sum(int(num) for num in input_string.split(','))