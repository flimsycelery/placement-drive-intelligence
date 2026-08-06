# Business Rules

This document defines the assumptions used while generating synthetic placement data.

## Student Rules

- Every student belongs to exactly one academic branch.
- Every student has one or more technical skills.
- Every student has a CGPA between 6.00 and 9.95.
- Active backlogs range from 0 to 2.
- Every student belongs to the 2027 graduating batch.
- Student email addresses use the college domain (`@nhce.edu`).
- Students may become inactive after graduation but are never deleted from the dataset.

## Placement Drive Rules

- Every placement drive belongs to exactly one company.
- Every drive recruits for one job role.
- A company may conduct multiple placement drives.
- A placement drive can allow multiple academic branches.
- Every drive defines a minimum CGPA and maximum allowed active backlogs.

## Registration Rules

- A student can register for multiple placement drives.
- A student cannot register for the same drive more than once.
- Students who do not meet eligibility criteria cannot register.

## Interview Rules

- Interviews are scheduled only for registered students.
- A student may have multiple interview rounds.
- Interview timings may change through rescheduling events.

## Offer Rules

- Offers are generated only after interviews are completed.
- A student can receive multiple offers.
- Offer acceptance is tracked separately from offer generation.