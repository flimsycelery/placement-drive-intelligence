"""
Generate synthetic student datasets.
"""

from pathlib import Path
import random

import pandas as pd
from faker import Faker

from event_generator.config import (
    RANDOM_SEED,
    FIRST_NAMES,
    LAST_NAMES,
)
from event_generator.utils.id_generator import generate_id

# -----------------------------
# Configuration
# -----------------------------

random.seed(RANDOM_SEED)

fake = Faker("en_IN")

Faker.seed(RANDOM_SEED)

# -----------------------------
# Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

REFERENCE_DATA = BASE_DIR / "data" / "reference_data"

# -----------------------------
# Load Reference Data
# -----------------------------

branches_df = pd.read_csv(
    REFERENCE_DATA / "branches.csv"
)

skills_df = pd.read_csv(
    REFERENCE_DATA / "skills.csv"
)

def calculate_resume_score(cgpa: float, active_backlogs: int) -> int:
    """
    Calculate a synthetic resume score based on
    academic performance.
    """

    score = cgpa * 10

    if active_backlogs == 1:
        score -= 10
    elif active_backlogs >= 2:
        score -= 20

    score = max(0, min(100, score))

    return round(score)

def generate_student(student_number: int) -> dict:
    """
    Generate one synthetic student.
    """

    branch = branches_df.sample(n=1).iloc[0]

    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)

    email = (
    f"{first_name.lower()}."
    f"{last_name.lower()}"
    f"{student_number:04}@nhce.edu"
    )

    cgpa = round(random.uniform(6.0, 9.95), 2)

    active_backlogs = random.choices(
        [0, 1, 2],
        weights=[80, 15, 5]
    )[0]

    resume_score = calculate_resume_score(
        cgpa,
        active_backlogs
    )

    resume_score = calculate_resume_score(
        cgpa,
        active_backlogs
    )

    student = {
        "Student_ID": generate_id("STU", student_number),
        "First_Name": first_name,
        "Last_Name": last_name,
        "College_Email": email,
        "Branch_ID": branch["Branch_ID"],
        "CGPA": round(random.uniform(6.0, 9.95), 2),
        "Active_Backlogs": random.choices(
            [0, 1, 2],
            weights=[80, 15, 5]
        )[0],
        "Graduation_Year": 2027,
        "Resume_Score": resume_score,
        "Profile_Created_Date": "2026-08-01",
        "Is_Active": True
    }

    return student

def generate_students(count: int = 600) -> pd.DataFrame:
    """
    Generate a DataFrame containing synthetic student records.
    """

    students = [
        generate_student(i)
        for i in range(1, count + 1)
    ]

    return pd.DataFrame(students)

def save_students(df: pd.DataFrame):
    """
    Save generated students to CSV.
    """

    output_file = (
        REFERENCE_DATA /
        "students.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    print(
        f"Generated {len(df)} students."
    )

    print(
        f"Saved to {output_file}"
    )

if __name__ == "__main__":

    students_df = generate_students()

    save_students(students_df)

    print()

    print(students_df.head())