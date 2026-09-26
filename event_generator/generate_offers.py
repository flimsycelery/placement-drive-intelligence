"""
Generate synthetic placement offer data.

Offer rules:
- A student can receive a maximum of 3 offers.
- A student can receive at most one offer from a drive.
- A student can have at most one accepted offer.
- Remaining offers are marked as Rejected.
"""

from pathlib import Path

import random

import pandas as pd

from event_generator.config import RANDOM_SEED
from event_generator.utils.id_generator import generate_id


# -----------------------------
# Configuration
# -----------------------------

random.seed(RANDOM_SEED)

OFFER_PROBABILITY = 0.20
MAX_OFFERS_PER_STUDENT = 3


# -----------------------------
# Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
REFERENCE_DATA = BASE_DIR / "data" / "reference_data"


# -----------------------------
# Load Reference Data
# -----------------------------

interviews_df = pd.read_csv(
    REFERENCE_DATA / "interviews.csv"
)

placement_drives_df = pd.read_csv(
    REFERENCE_DATA / "placement_drives.csv"
)


# -----------------------------
# Generate Offers
# -----------------------------

def generate_offers():

    offers = []
    offer_number = 1

    # One interview per student-drive pair.
    interviewed_students = (
        interviews_df[
            interviews_df["Interview_Status"] == "Scheduled"
        ]
        .drop_duplicates(
            ["Student_ID", "Drive_ID"]
        )
    )

    # Group interviews by student so that
    # the 3-offer maximum can be enforced.
    student_interviews = (
        interviewed_students
        .groupby("Student_ID")
    )

    for student_id, student_group in student_interviews:

        # Randomly shuffle the available drives for
        # this student so offers aren't biased toward
        # the first drives in the dataset.
        candidate_interviews = list(
            student_group.to_dict("records")
        )

        random.shuffle(candidate_interviews)

        student_offers = []

        # --------------------------------
        # Generate candidate offers
        # --------------------------------

        for interview in candidate_interviews:

            if len(student_offers) >= MAX_OFFERS_PER_STUDENT:
                break

            if random.random() > OFFER_PROBABILITY:
                continue

            drive_id = interview["Drive_ID"]

            drive = placement_drives_df.loc[
                placement_drives_df["Drive_ID"] == drive_id
            ].iloc[0]

            student_offers.append(
                {
                    "Student_ID": student_id,
                    "Drive_ID": drive_id,
                    "CTC_LPA": drive["CTC_LPA"],
                }
            )

        # --------------------------------
        # Assign offer statuses
        # --------------------------------

        if student_offers:

            # At most ONE offer can be accepted.
            accepted_offer_index = random.randrange(
                len(student_offers)
            )

            for index, offer in enumerate(
                student_offers
            ):

                if index == accepted_offer_index:
                    offer_status = "Accepted"
                else:
                    offer_status = "Rejected"

                offers.append(
                    {
                        "Offer_ID": generate_id(
                            "OFF",
                            offer_number
                        ),
                        "Student_ID": offer[
                            "Student_ID"
                        ],
                        "Drive_ID": offer[
                            "Drive_ID"
                        ],
                        "CTC_LPA": offer[
                            "CTC_LPA"
                        ],
                        "Offer_Status": offer_status,
                    }
                )

                offer_number += 1

    return pd.DataFrame(offers)


# -----------------------------
# Main
# -----------------------------

if __name__ == "__main__":

    offers_df = generate_offers()

    offers_df.to_csv(
        REFERENCE_DATA / "offers.csv",
        index=False
    )

    print()
    print("Offer generation completed.")
    print(
        f"Offers generated: "
        f"{len(offers_df)}"
    )
    print(
        f"Unique students receiving offers: "
        f"{offers_df['Student_ID'].nunique()}"
    )
    print(
        f"Accepted offers: "
        f"{(offers_df['Offer_Status'] == 'Accepted').sum()}"
    )
    print(
        f"Rejected offers: "
        f"{(offers_df['Offer_Status'] == 'Rejected').sum()}"
    )
    print()

    print(
        offers_df.head(10).to_string(
            index=False
        )
    )