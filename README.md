# String Calculator Kata

This repository contains the implementation of the String Calculator kata in Python.

## Behaviors Implemented

The following test suite output demonstrates all the supported features and behaviors of the String Calculator.

```text
command: pytest --spec
test_string_calculator.py:

Advanced Delimiters:
  ✓ It should handle long delimiters
  ✓ It should handle multiple delimiters
  ✓ It should handle multiple long delimiters

Calculator Usage:
  ✓ It should report the total number of times add was called

Delimiter Handling:
  ✓ It should allow newlines as valid delimiters
  ✓ It should support user defined custom delimiters

Input Validation:
  ✓ It must prohibit negative numbers
  ✓ It must list all negatives in the error message
  ✓ It should ignore numbers greater than one thousand

String Calculator Basic Operations:
  ✓ It should return zero when input is empty
  ✓ It should return the number itself for single inputs
  ✓ It should return the sum of two numbers separated by commas
  ✓ It should return the sum of all numbers separated by commas

================================================== 13 passed in 0.01s ===================================================
```
