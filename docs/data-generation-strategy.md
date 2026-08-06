# Data Generation Strategy

## Objective

The Campus Placement Intelligence Platform uses synthetic data to simulate a realistic placement environment while preserving consistent business relationships.

The datasets are generated programmatically to ensure repeatability, maintainability, and realistic analytical behavior.

---

# Generation Principles

## 1. Deterministic Generation

A fixed random seed is used so that datasets can be regenerated consistently during development and testing.

---

## 2. Business-Driven Data

Synthetic data follows realistic placement office scenarios rather than purely random values.

Examples include:

- Branch-specific skill distributions
- Realistic CGPA ranges
- Limited active backlogs
- Valid company-role relationships

---

## 3. Normalized Relationships

Reference entities are generated before transactional entities.

Generation order:

1. Branches
2. Skills
3. Roles
4. Companies
5. Students
6. Student Skills
7. Placement Drives
8. Registrations
9. Interviews
10. Offers

---

## 4. Referential Integrity

Foreign key relationships are preserved throughout generation.

Examples:

- Every Student references a valid Branch.
- Every Registration references an existing Student and Placement Drive.
- Every Interview references an existing Registration.

---

## 5. Reproducibility

Running the generators multiple times produces identical datasets when using the same configuration and random seed.