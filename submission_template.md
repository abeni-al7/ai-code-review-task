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
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
