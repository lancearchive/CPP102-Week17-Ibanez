# Test Cases – Simulated Device Monitoring and Alert System

**Tested by:** Lance A. Ibañez
**Date:** 12/10/2026

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | Shows all 5 readings correctly | Pass |
| TC02 | Choose 2, enter 33 | Reading added successfully | Reading added successfully; list updated | Pass |
| TC03 | Choose 2, enter abc | Rejected; List unchanged | Rejected: "Enter a whole number only." | Pass |
| TC04 | Choose 2, leave empty / press Enter | Rejected; List unchanged | Rejected: "The reading cannot be empty." | Pass |
| TC05 | Choose 2, enter -8 | Rejected; List unchanged | Rejected: "Enter a value from 0 to 100." | Pass |
| TC06 | Choose 2, enter 120 | Rejected; List unchanged | Rejected: "Enter a value from 0 to 100." | Pass |
| TC07 | Choose 3, check 30°C | Classified as WARNING | 30 °C -> WARNING | Pass |
| TC08 | Choose 3, check 35°C | Classified as WARNING | 35 °C -> WARNING | Pass |
| TC09 | Choose 4 | Summary shows Total=160, Avg=32.00, Min=28, Max=37 | All values match exactly | Pass |
| TC10 | Enter menu choice 8 | Invalid choice; Menu shown again | "Invalid choice. Please enter a number from 1 to 5." | Pass |

## Bugs Found and Fixed

- **Bug 1 — Boundary Classification Error:** Initially, `classify_reading()` used `reading < 35` instead of `reading <= 35`. This caused 35°C to be incorrectly classified as CRITICAL instead of WARNING. I fixed it by changing the operator from `< 35` to `<= 35`, then retested both boundary values — 30°C and 35°C now both correctly return WARNING.
 - **Bug 2 — Overall Status Logic Order:** In `determine_overall_status()`, I originally checked for WARNING before CRITICAL. This meant readings with both WARNING and CRITICAL would incorrectly show "MONITOR" instead of "ATTENTION REQUIRED". I fixed it by swapping the order — CRITICAL is now checked first, so it takes priority.
 - **Bug 3 — Minimum Value Started at 0 (Not Fixed):** Early version set `minimum = 0` instead of `minimum = readings[0]`, which made the minimum always show 0 instead of the actual lowest reading. I corrected it to initialize from the first list element so the loop compares correctly against real values.