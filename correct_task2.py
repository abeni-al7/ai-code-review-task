# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
def count_valid_emails(emails):
    count = 0

    for email in emails:
        if "@" in email:
            count += 1

    return count
