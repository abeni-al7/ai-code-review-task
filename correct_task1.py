# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    total = 0
    count = len(orders)

    for order in orders:
        if order["status"] != "cancelled":
            total += order["amount"]

    return total / count
