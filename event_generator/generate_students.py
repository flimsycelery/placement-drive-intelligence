"""
Generate synthetic student data.
"""

from pathlib import Path
import random

import pandas as pd
from faker import Faker

from event_generator.config import RANDOM_SEED
from event_generator.utils.id_generator import generate_id

# ------------------------------------
# Configuration
# ------------------------------------

random.seed(RANDOM_SEED)

fake = Faker()

Faker.seed(RANDOM_SEED)

# ------------------------------------
# Paths
# ------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

REFERENCE_DATA = BASE_DIR / "data" / "reference_data"

# ------------------------------------
# Load Reference Data
# ------------------------------------

branches_df = pd.read_csv(
    REFERENCE_DATA / "branches.csv"
)

skills_df = pd.read_csv(
    REFERENCE_DATA / "skills.csv"
)

def generate_student(student_number: int):
    """
    Generate one synthetic student.
    """

    first_name = fake.first_name()

    last_name = fake.last_name()

    branch = branches_df.sample(
        n=1,
        random_state=random.randint(1, 100000)
    ).iloc[0]

    cgpa = round(
        random.uniform(6.0, 9.95),
        2
    )

    active_backlogs = random.choices(
        [0, 1, 2],
        weights=[80, 15, 5]
    )[0]

    student = {
        "Student_ID": generate_id(
            "STU",
            student_number
        ),
        "First_Name": first_name,
        "Last_Name": last_name,
        "College_Email": f"stu{student_number:04}@nhce.edu",
        "Branch_ID": branch["Branch_ID"],
        "CGPA": cgpa,
        "Active_Backlogs": active_backlogs,
        "Graduation_Year": 2027,
        "Resume_Score": None,
        "Profile_Created_Date": "2026-08-01",
        "Is_Active": True
    }

    return student

student = generate_student(1)

print(student)