"""
Generate synthetic student registration data for campus placement drives.

Only students who satisfy the drive's eligibility criteria can register.
"""

from pathlib import Path

import random
from datetime import timedelta

import pandas as pd

from event_generator.config import RANDOM_SEED
from event_generator.utils.id_generator import generate_id


# -----------------------------
# Configuration
# -----------------------------

random.seed(RANDOM_SEED)


# -----------------------------
# Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
REFERENCE_DATA = BASE_DIR / "data" / "reference_data"


# -----------------------------
# Load Reference Data
# -----------------------------

students_df = pd.read_csv(
    REFERENCE_DATA / "students.csv"
)

placement_drives_df = pd.read_csv(
    REFERENCE_DATA / "placement_drives.csv"
)

drive_branches_df = pd.read_csv(
    REFERENCE_DATA / "drive_branches.csv"
)


# -----------------------------
# Eligibility Check
# -----------------------------

def is_student_eligible(student, drive, eligible_branch_ids):
    """
    Check whether a student satisfies a placement drive's
    eligibility criteria.

    Eligibility is based on:
    - Branch
    - CGPA
    - Active backlogs
    """

    branch_eligible = student["Branch_ID"] in eligible_branch_ids

    cgpa_eligible = (
        student["CGPA"] >= drive["Minimum_CGPA"]
    )

    backlog_eligible = (
        student["Active_Backlogs"]
        <= drive["Eligibility_Backlogs"]
    )

    return (
        branch_eligible
        and cgpa_eligible
        and backlog_eligible
    )


# -----------------------------
# Generate Registrations
# -----------------------------

def generate_registrations():
    """
    Generate registrations only for eligible students.

    A student may register for multiple placement drives.
    """

    registrations = []

    registration_number = 1

    for _, drive in placement_drives_df.iterrows():

        drive_id = drive["Drive_ID"]

        # Get branches eligible for this drive
        eligible_branch_ids = set(
            drive_branches_df.loc[
                drive_branches_df["Drive_ID"] == drive_id,
                "Branch_ID"
            ]
        )

        eligible_students = []

        # -----------------------------
        # Find eligible students
        # -----------------------------

        for _, student in students_df.iterrows():

            if is_student_eligible(
                student,
                drive,
                eligible_branch_ids
            ):
                eligible_students.append(student)

        # -----------------------------
        # Select students who register
        # -----------------------------

        if not eligible_students:
            continue

        # Students do not necessarily register for
        # every drive they are eligible for.
        registration_probability = 0.45

        for student in eligible_students:

            if random.random() > registration_probability:
                continue

            registration_start = pd.to_datetime(
                drive["Registration_Start"]
            ).date()

            registration_end = pd.to_datetime(
                drive["Registration_End"]
            ).date()

            registration_date = (
                registration_start
                + timedelta(
                    days=random.randint(
                        0,
                        (
                            registration_end
                            - registration_start
                        ).days
                    )
                )
            )

            registrations.append(
                {
                    "Registration_ID": generate_id(
                        "REG",
                        registration_number
                    ),
                    "Student_ID": student["Student_ID"],
                    "Drive_ID": drive_id,
                    "Registration_Date": registration_date,
                    "Registration_Status": "Registered",
                }
            )

            registration_number += 1

    return pd.DataFrame(registrations)


# -----------------------------
# Main
# -----------------------------

if __name__ == "__main__":

    registrations_df = generate_registrations()

    registrations_df.to_csv(
        REFERENCE_DATA / "registrations.csv",
        index=False
    )

    print()
    print("Registration generation completed.")
    print(
        f"Registrations generated: "
        f"{len(registrations_df)}"
    )
    print(
        f"Unique students registered: "
        f"{registrations_df['Student_ID'].nunique()}"
    )
    print(
        f"Unique drives with registrations: "
        f"{registrations_df['Drive_ID'].nunique()}"
    )
    print()

    print(
        registrations_df.head(10).to_string(
            index=False
        )
    )