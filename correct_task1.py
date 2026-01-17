# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
from typing import Any
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

# Constants for better maintainability
STATUS_CANCELLED = "cancelled"


def calculate_average_order_value(
    orders: list[dict[str, Any]] | None,
) -> Decimal:
    """
    Calculates the exact average value of non-cancelled orders using
    fixed-point decimal arithmetic for financial accuracy.
    """
    # Handle null or empty input
    if not isinstance(orders, list) or not orders:
        return Decimal("0.00")

    valid_amounts: list[Decimal] = []

    for order in orders:
        # Normalize status for case-insensitive comparison
        status = str(order.get("status", "")).strip().lower()
        amount_raw = order.get("amount")

        if status != STATUS_CANCELLED and amount_raw is not None:
            try:
                # Converting from string to Decimal is safer than from float.
                amount_dec = Decimal(str(amount_raw))
                valid_amounts.append(amount_dec)
            except (InvalidOperation, ValueError, TypeError):
                continue

    if not valid_amounts:
        return Decimal("0.00")

    # Perform the calculation
    total_sum = sum(valid_amounts)
    count = len(valid_amounts)

    average = total_sum / Decimal(count)

    # Standard financial rounding: Round to 2 decimal places
    return average.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
