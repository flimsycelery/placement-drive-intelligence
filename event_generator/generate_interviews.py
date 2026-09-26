"""
Generate synthetic interview schedules from placement registrations.

Interviews are generated only for registered students.
Some schedules intentionally overlap so that the analytics layer
can detect interview conflicts later.
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

INTERVIEW_PROBABILITY = 0.75
CONFLICT_PROBABILITY = 0.15

INTERVIEW_MODES = [
    "Online",
    "Offline",
]

INTERVIEW_ROUNDS = [
    "Technical",
    "HR",
]


# -----------------------------
# Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
REFERENCE_DATA = BASE_DIR / "data" / "reference_data"


# -----------------------------
# Load Reference Data
# -----------------------------

registrations_df = pd.read_csv(
    REFERENCE_DATA / "registrations.csv"
)

placement_drives_df = pd.read_csv(
    REFERENCE_DATA / "placement_drives.csv"
)


# -----------------------------
# Generate Interview Time
# -----------------------------

def generate_interview_time():
    """
    Generate a one-hour interview slot between 9 AM and 5 PM.
    """

    hour = random.randint(9, 16)

    start_time = f"{hour:02d}:00"
    end_time = f"{hour + 1:02d}:00"

    return start_time, end_time


# -----------------------------
# Generate Interviews
# -----------------------------

def generate_interviews():

    interviews = []
    interview_number = 1

    for _, registration in registrations_df.iterrows():

        # Not every registration reaches interview stage.
        if random.random() > INTERVIEW_PROBABILITY:
            continue

        drive_id = registration["Drive_ID"]
        student_id = registration["Student_ID"]

        drive = placement_drives_df.loc[
            placement_drives_df["Drive_ID"] == drive_id
        ].iloc[0]

        registration_start = pd.to_datetime(
            drive["Registration_Start"]
        ).date()

        registration_end = pd.to_datetime(
            drive["Registration_End"]
        ).date()

        # Schedule interview shortly after registration closes.
        interview_date = (
            registration_end
            + timedelta(
                days=random.randint(1, 7)
            )
        )

        start_time, end_time = generate_interview_time()

        interviews.append(
            {
                "Interview_ID": generate_id(
                    "INT",
                    interview_number
                ),
                "Drive_ID": drive_id,
                "Student_ID": student_id,
                "Round": random.choice(
                    INTERVIEW_ROUNDS
                ),
                "Interview_Date": interview_date,
                "Start_Time": start_time,
                "End_Time": end_time,
                "Interview_Mode": random.choice(
                    INTERVIEW_MODES
                ),
                "Interview_Status": "Scheduled",
            }
        )

        interview_number += 1

    interviews_df = pd.DataFrame(interviews)

    # --------------------------------
    # Inject realistic conflicts
    # --------------------------------

    if len(interviews_df) > 1:

        conflict_count = int(
            len(interviews_df)
            * CONFLICT_PROBABILITY
        )

        conflict_count = max(
            conflict_count,
            1
        )

        # Only students with multiple interviews
        # can have scheduling conflicts.
        students_with_multiple_interviews = (
            interviews_df.groupby("Student_ID")
            .filter(lambda group: len(group) >= 2)
            ["Student_ID"]
            .unique()
        )

        if len(students_with_multiple_interviews) > 0:

            selected_students = random.sample(
                list(students_with_multiple_interviews),
                min(
                    conflict_count,
                    len(students_with_multiple_interviews)
                )
            )

            for student_id in selected_students:

                student_interviews = interviews_df[
                    interviews_df["Student_ID"] == student_id
                ]

                # Select two different interviews
                conflict_indexes = random.sample(
                    list(student_interviews.index),
                    2
                )

                first_index = conflict_indexes[0]
                second_index = conflict_indexes[1]

                first_drive_id = interviews_df.loc[
                    first_index,
                    "Drive_ID"
                ]

                second_drive_id = interviews_df.loc[
                    second_index,
                    "Drive_ID"
                ]

                first_drive = placement_drives_df.loc[
                    placement_drives_df["Drive_ID"] == first_drive_id
                ].iloc[0]

                second_drive = placement_drives_df.loc[
                    placement_drives_df["Drive_ID"] == second_drive_id
                ].iloc[0]

                first_registration_end = pd.to_datetime(
                    first_drive["Registration_End"]
                ).date()

                second_registration_end = pd.to_datetime(
                    second_drive["Registration_End"]
                ).date()

                # The conflict date must be after
                # BOTH registration windows.
                latest_registration_end = max(
                    first_registration_end,
                    second_registration_end
                )

                conflict_date = (
                    latest_registration_end
                    + timedelta(
                        days=random.randint(1, 7)
                    )
                )

                start_time, end_time = (
                    generate_interview_time()
                )

                # Give both interviews the same
                # date and time to create a conflict.
                interviews_df.loc[
                    first_index,
                    "Interview_Date"
                ] = conflict_date

                interviews_df.loc[
                    first_index,
                    "Start_Time"
                ] = start_time

                interviews_df.loc[
                    first_index,
                    "End_Time"
                ] = end_time

                interviews_df.loc[
                    second_index,
                    "Interview_Date"
                ] = conflict_date

                interviews_df.loc[
                    second_index,
                    "Start_Time"
                ] = start_time

                interviews_df.loc[
                    second_index,
                    "End_Time"
                ] = end_time

    return interviews_df


# -----------------------------
# Main
# -----------------------------

if __name__ == "__main__":

    interviews_df = generate_interviews()

    interviews_df.to_csv(
        REFERENCE_DATA / "interviews.csv",
        index=False
    )

    print()
    print("Interview generation completed.")
    print(
        f"Interviews generated: "
        f"{len(interviews_df)}"
    )
    print(
        f"Unique students with interviews: "
        f"{interviews_df['Student_ID'].nunique()}"
    )
    print(
        f"Unique drives with interviews: "
        f"{interviews_df['Drive_ID'].nunique()}"
    )
    print()

    print(
        interviews_df.head(10).to_string(
            index=False
        )
    )