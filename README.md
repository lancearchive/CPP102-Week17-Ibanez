# Simulated Device Monitoring and Alert System

**Student Name:** Lance A. Ibañez
**Student Number:** 2600690
**Section:** 1CPE - A

## Project Description
This program monitors simulated device temperature readings. It classifies each reading as NORMAL, WARNING, or CRITICAL and prints a summary with the overall status. Users can view, add, analyze readings through a simple menu interface.

## Features
- View all stored temperature readings
- Add a new reading (ehole numbers from 0 to 100 only)
- Classify every reading
- Generate a numerical summary anf overall status
- Reject invalid menu choices and invalid readings

## Requirements
- Python 3 (no external packages)

## How to Run
1. Open the terminal inside the week17 folder
2. Type: python device_monitor.py

## Sample Output
---
def classify_reading(reading, warning_limit, critical_limit):
    """Return classification: NORMAL, WARNING, or CRITICAL."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"
---

## Test Cases
I performed 10 tests. 10 passed and 0 failed.
Full details are in test_cases.md

## Known Limitations
- Readings are lost when the program closes
- Data cannot be saved between sessions
- Only integer temperature values are accepted

## Reflection
The hardest part was organizing the program into separate functions that each did one specific job. I learned how to pass data into functions using parameters instead of relying on global variables. In future projects, I want to get even better at planning my code before I start writing it.