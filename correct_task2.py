# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
import re
from typing import Iterable, Any, Optional

# Basic regex for standard email validation: local@domain.tld
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def is_valid_email(email: str) -> bool:
    """
    Validates an individual email address.

    Checks for:
    1. Correct data type (must be string).
    2. Proper structure (local_part@domain.tld).
    3. Basic length requirements.
    """
    if not isinstance(email, str):
        return False

    # Strip whitespace to be forgiving of minor formatting issues
    email = email.strip()

    # Ensure it's not empty and matches the pattern
    return bool(email and EMAIL_REGEX.match(email))


def count_valid_emails(emails: Optional[Iterable[Any]]) -> int:
    """
    Counts the number of valid email addresses in a collection.

    Safely handles:
    - Non-string elements (None, integers, etc.)
    - Empty inputs or None as input
    - Any iterable type (lists, sets, generators)
    """
    if not emails:
        return 0

    # Declarative approach:
    return sum(1 for entry in emails if is_valid_email(entry))
