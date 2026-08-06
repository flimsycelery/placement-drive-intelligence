"""
Generate synthetic student datasets.
"""

from pathlib import Path
import random

import pandas as pd
from faker import Faker

from event_generator.config import RANDOM_SEED
from event_generator.utils.id_generator import generate_id

# -----------------------------
# Configuration
# -----------------------------

random.seed(RANDOM_SEED)

fake = Faker()

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

def generate_student(student_number: int) -> dict:
    """
    Generate one synthetic student.
    """

    branch = branches_df.sample(n=1).iloc[0]

    student = {
        "Student_ID": generate_id("STU", student_number),
        "First_Name": fake.first_name(),
        "Last_Name": fake.last_name(),
        "College_Email": f"stu{student_number:04}@nhce.edu",
        "Branch_ID": branch["Branch_ID"],
        "CGPA": round(random.uniform(6.0, 9.95), 2),
        "Active_Backlogs": random.choices(
            [0, 1, 2],
            weights=[80, 15, 5]
        )[0],
        "Graduation_Year": 2027,
        "Resume_Score": None,
        "Profile_Created_Date": "2026-08-01",
        "Is_Active": True
    }

    return student

v