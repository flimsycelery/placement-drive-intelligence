# Data Model

## Overview

The Campus Placement Intelligence Platform processes placement-related events and transforms them into analytical datasets for students and placement officers.

The platform revolves around five primary business entities:

1. Student
2. Company
3. Placement Drive
4. Interview
5. Offer

---

## Student

Represents a student eligible for campus placements.

| Field | Description |
|--------|-------------|
| Student_ID | Unique student identifier |
| Name | Student name |
| Branch | Academic branch |
| CGPA | Current CGPA |
| Backlogs | Number of active backlogs |
| Graduation_Year | Expected graduation year |
| Skills | Technical skills |

---

## Company

Represents a recruiting company.

| Field | Description |
|--------|-------------|
| Company_ID | Unique company identifier |
| Company_Name | Company name |
| Industry | Industry sector |
| Location | Office location |

---

## Placement Drive

Represents a hiring drive conducted by a company.

| Field | Description |
|--------|-------------|
| Drive_ID | Unique drive identifier |
| Company_ID | Associated company |
| Role | Job role |
| Registration_Start | Registration opening date |
| Registration_End | Registration closing date |
| Minimum_CGPA | Minimum CGPA required |
| Allowed_Branches | Eligible branches |

---

## Interview

Represents an interview scheduled for a student.

| Field | Description |
|--------|-------------|
| Interview_ID | Unique interview identifier |
| Drive_ID | Associated placement drive |
| Student_ID | Student appearing |
| Round | Interview round |
| Interview_Date | Scheduled date |
| Start_Time | Interview start time |
| End_Time | Interview end time |

---

## Offer

Represents a placement offer.

| Field | Description |
|--------|-------------|
| Offer_ID | Unique offer identifier |
| Student_ID | Selected student |
| Drive_ID | Placement drive |
| Package | Offered CTC |
| Offer_Status | Accepted / Rejected / Pending |