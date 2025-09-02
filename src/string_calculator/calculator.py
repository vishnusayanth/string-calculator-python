
import re
from typing import List

def add(numbers: str) -> int:
    """Return the sum of numbers in a string with comma/newline/custom delimiters.

    Rules:
    - Empty string -> 0
    - Comma or newline delimited numbers
    - Custom delimiter header: "//<delimiter>\n<numbers>" (single delimiter string)
    - Negative numbers raise ValueError with message:
      "negative numbers not allowed <comma_separated_negatives>"
    """
    pass