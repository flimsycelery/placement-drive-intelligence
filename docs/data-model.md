# Data Model

## Overview

The Campus Placement Intelligence Platform processes placement-related events and transforms them into analytical datasets for students and placement officers.

The platform revolves around the following primary business entities:

1. Student
2. Student_Skills
3. Company
4. Placement_Drive
5. Drive_Branches
6. Registration
7. Interview
8. Offer

---

## Student

Represents a student eligible for campus placements.

| Field | Description |
|--------|-------------|
| Student_ID | Unique student identifier |
| First_Name | Student first name |
| Last_Name | Student last name |
| College_Email | College email address |
| Branch_ID | Reference to student's academic branch |
| CGPA | Current CGPA |
| Active_Backlogs | Number of active backlogs |
| Graduation_Year | Expected graduation year |
| Resume_Score | Synthetic resume evaluation score used for analytical insights |
| Profile_Created_Date | Auditing |
| Is_Active | Current student status |

> **Note:** Student skills are maintained in a separate `Student_Skills` entity to support a many-to-many relationship between students and technical skills.

---

## Student_Skills

Represents the many-to-many relationship between students and technical skills.

| Field | Description |
|--------|-------------|
| Student_ID | Reference to the student |
| Skill_ID | Reference to the technical skill |

---

## Company

Represents a recruiting company.

| Field | Description |
|--------|-------------|
| Company_ID | Unique company identifier |
| Company_Name | Company name |
| Industry | Industry sector |
| Headquarters | Company headquarters |
| Hiring_Location | Office location for the role |
| Company_Type | Product / Service / Consulting |
| Is_Active | Whether the company is actively recruiting |

---

## Placement Drive

Represents a hiring drive conducted by a company.

| Field | Description |
|--------|-------------|
| Drive_ID | Unique drive identifier |
| Company_ID | Associated company |
| Role_ID | Job role |
| Registration_Start | Registration opening date |
| Registration_End | Registration closing date |
| Minimum_CGPA | Minimum CGPA required |
| Eligibility_Backlogs | Maximum allowed active backlogs |
| Status | Open / Closed / Completed |

---

## Drive_Branches
| Field | Description |
| -------- |----------- |
| Drive_ID | Placement drive |
| Branch_ID | Eligible branch |

---

## Interview

Represents an interview scheduled for a student.

| Field | Description |
|--------|-------------|
| Interview_ID | Unique interview identifier |
| Drive_ID | Associated placement drive |
| Interview_Mode | Online / Offline |
| Student_ID | Student appearing |
| Round | Interview round |
| Interview_Date | Scheduled date |
| Start_Time | Interview start time |
| End_Time | Interview end time |
| Interview_Status | Scheduled / Completed / Cancelled / Rescheduled |

----

## Registration

Represents a student's registration for a placement drive prior to the recruitment process.

| Field | Description |
|--------|-------------|
| Registration_ID | Unique registration identifier |
| Student_ID | Reference to the student |
| Drive_ID | Reference to the placement drive |
| Registration_Date | Date of registration |
| Registration_Status | Registered / Withdrawn |

---

## Offer

Represents a placement offer.

| Field | Description |
|--------|-------------|
| Offer_ID | Unique offer identifier |
| Student_ID | Selected student |
| Drive_ID | Placement drive |
| CTC | Offered compensation package |
| Offer_Status | Accepted / Rejected / Pending |