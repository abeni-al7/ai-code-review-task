# AI Code Review Assignment (Python)

## Candidate
- Name: Abenezer Alebachew Endalew
- Approximate time spent: 70 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The function would crash if we provide an empty list as a result of ZeroDivisionError.
- The average considers the total count of orders instead of the non cancelled ones. This means it adds the orders which are not cancelled together, but to find the average it divides that with the number of items in the list which produces an incorrect average.

### Edge cases & risks
- If the orders variable is None or if it is not a list, calling len() on it would produce a TypeError.
- If the order status is not formatted exactly as "cancelled" in lowercase, the function would not be able to filter it out. The external system accessing this function might send "Cancelled" or "CANCELLED".
- The order amount might not be a numeric value like int or float. This is because real world systems usually prefer sending monetary values as a string in order to avoid floating-point errors in transit.
- If the order does not have the status and amount keys or if the amount can not be converted to a numeric value, the function would just crash the system silently.

### Code quality / design issues
- It is better to use the decimal module for monetary calculations since float can accumulate small floating point errors and that is undesireable for calculations that concern money.
- It uses a hard-coded value to check order status. It is better to use enums and constants which would not require our code to change if the value is later renamed to something else.
- The code lacks type hints. This would reduce maintainability as a new programmer in the team would not know if orders is supposed to be an integer, a list or a dictionary at first glance.
- Python favors list comprehensions over imperatively going through each value in a for-loop. It is good for efficiency as well as readability.
- The function also lacks a docstring which is a best practice for readability and easier common understanding.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Used type hinting and function docstring for documentation
- Used Decimal for performing calculations on monetary values
- Used try/catch to handle invalid inputs
- Corrected the average calculation to use the count of the valid orders in the denominator
- Handled the possibility of ZeroDivision error by returning 0 for cases that crashed the program
- Used a constant to store the order status instead of hard-coding it in the function.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

I would focus on testing the function with invalid inputs, missing keys and unexpected values since these tend to be the ones that usually crash programs. I would also test it with different kinds of valid inputs to ensure that the function works as expected.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- The explanation misses the fact that dividing the sum by the number of orders produces a wrong average.

### Rewritten explanation
- This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of non-cancelled orders. It correctly excludes cancelled orders and it uses the decimal module to produce accurate calculations.

## 4) Final Judgment
- Decision: Request Changes
- Justification: It definitely needs change since it has a critical bug and it must handle edge cases if it is going to run in a production server since we don't want to crash the server just because invalid inputs are provided.
- Confidence & unknowns: We might not need to use decimals if the function is just going to be used for statistics and if it does not require the exact precision decimal provides since float provides faster calculations.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- The function only checks for the presence of a single character, instead of actually validating the input for the rules of being an email. An email must have 3 parts, namely the local, the domain name and the tld. The local and the domain name are separated by a singe "@" symbol. The domain name is separated from the tld by a single "." symbol and the local and the tld part can have multiple "." symbols in them. All these validations are not taken into account.
- Even though the description states that it "safely ignores invalid entries", it actually would produce a TypeError if non string data types are provided in the input. This is because the code checks for the presence of "@" before checking if the email is a string. This could have been an edge case, but since the description promises safe handling of invalid entries, it can be considered a critical bug.

### Edge cases & risks
- It does not safely handle cases where the given input list contains other data types other than a string.
- Emails that only contain "@", emails that contain multiple "@" symbols, emails that only contain the domain name and the tld like "@gmail.com", emails that contain spaces, even telegram / x handles like "@abeni" are all accepted as valid emails.
- It could lead to data corruption if the data is stored in a database resulting in incorrect data.

### Code quality / design issues
- The code violates the single responsibility principle by handling both email validation and counting. We might need to validate email for other cases without the need to count them.
- The code lacks type hinting and docstrings which makes it hard for collaboration and common understanding.
- Instead of using a for loop to go through each email, using a simple generator expression is declarative and easier to understand in addition to being more Pythonic.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Separated the logic for validation and counting.
- Handled cases where non string values are in the list and invalid data types as input to the functions are properly and safely handled.
- Used a declarative approach instead of a for loop.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

I would test the function with valid looking but invalid email addresses to better prevent data corruption and I would try a vast variations of correct emails to check for false negatives.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- The description has no issues. The only problem was the code did not live up to the promises of the description.

### Rewritten explanation
- This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

## 4) Final Judgment
- Decision: Request Change
- Justification: The function fails at the most basic promise of actually counting valid email addresses and it has edge cases which are unacceptable in a production server.
- Confidence & unknowns: If new rules for email formats emerge in the future, the email validation function might need updates but the separate implementation would make that future update easier.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The function produces false averages since it considers all the elements in the list by using len(values) in the denominator.
- Eventhough the description states that it handles mixed input types safely, it would produce a type error if a string is present in a list since strings can't be converted to float by float(v).

### Edge cases & risks
- If an empty list is provided, the function would raise a ZeroDivision error and crash the system.
- If "NaN" or "inf" appear in the list, direct conversion to float would consider those and would produce "NaN" or "inf" instead of a correct average.
- If booleans are present in the list float conversion would provide 1.0 for True and 0.0 for False which is misleading.
- If a non-list input is provided or if the argument is None, the function would raise a TypeError and crash while checking the length with len() or while iterating.

### Code quality / design issues
- Validity checks and calculation are implemented in the same function violating the single responsibility principle.
- It is better to use the standard library function math.fsum for more accurate floating point sum.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Separated validity and type casting from the average calculation.
- Used math.fsum for a more accurate sum.
- Handled booleans, non-finite numbers like NaN/inf and non numeric values.
- Used the count of valid measurements instead of the size of the entire list for average calculation.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

I would test the function with a variety of invalid inputs, booleans, non-finite numbers and strings to test for resilience. I would also check the happy path by providing valid numbers to see if the average is correctly calculated.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- The description does not consider the above mentioned edge cases and it promises safe handling of mixed input types while not handling it in the implementation.

### Rewritten explanation
- This function calculates the average of valid measurements by ignoring missing values (None), booleans, non-finite numebrs(NaN/inf) and invalid strings. It then averages the remaining values using a high precision sum function from the standard library. It safely handles mixed input types and ensures an accurate average.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The code needed change as it produces false averages and crashes for a wide variety of invalid inputs.
- Confidence & unknowns: 
