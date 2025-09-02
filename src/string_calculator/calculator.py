
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
    if not numbers:
        return 0

    pattern = r",|\n"
    # Custom delimiter header
    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        custom = header[2:]
        pattern = re.escape(custom)  

    tokens = re.split(pattern, numbers)
    vals: List[int] = []
    negatives: List[int] = []

    for t in tokens:
        if t == "":
            # ignore blank tokens if any
            continue
        n = int(t)
        if n < 0:
            negatives.append(n)
        vals.append(n)

    if negatives:
        raise ValueError("negative numbers not allowed " + ",".join(map(str, negatives)))

    return sum(vals)
