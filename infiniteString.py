#!/bin/python
import os


# Complete the repeatedString function below.
def repeated_string(input_str, char_count):
    repeat_count = char_count / len(input_str)
    last_chunk = char_count % len(input_str)
    occurrence_count = input_str.count('a') * repeat_count + input_str[:last_chunk].count('a')
    return occurrence_count


if __name__ == '__main__':
    input_str = raw_input()
    char_count = int(raw_input())
    result = repeated_string(input_str, char_count)
    print(result)

