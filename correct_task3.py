# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
import math
from typing import Iterable, Any, Optional


def try_to_float(value: Any) -> Optional[float]:
    """
    Validates and converts a single input into a float.
    Returns the float if valid, otherwise returns None.
    """
    # 1. Eliminate None and Booleans
    if value is None:
        return None
    if isinstance(value, bool):
        return None

    try:
        num = float(value)

        # 2. Handle non-finite numbers (NaN/Inf)
        if not math.isfinite(num):
            return None

        return num
    except (ValueError, TypeError):
        # 3. Handle incompatible types (strings like "missing", etc.)
        return None


def calculate_average(values: Iterable[Any]) -> Optional[float]:
    """
    Calculates the average of numeric values in an iterable,
    properly ignoring invalid entries.
    """
    # Create a list of only validated float values
    valid_numbers = [
        transformed
        for item in values
        if (transformed := try_to_float(item)) is not None
    ]

    # Handle empty lists/no valid data to avoid ZeroDivisionError
    if not valid_numbers:
        return None

    # Use high-precision sum for the final calculation
    return math.fsum(valid_numbers) / len(valid_numbers)
