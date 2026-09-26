"""
Generate synthetic placement events from the existing
placement source datasets.

Events represent changes/actions that occur throughout
the placement lifecycle.
"""

from pathlib import Path

import json
import random
from datetime import datetime, timedelta

import pandas as pd

from event_generator.config import RANDOM_SEED


# -----------------------------
# Configuration
# -----------------------------

random.seed(RANDOM_SEED)


# -----------------------------
# Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
REFERENCE_DATA = BASE_DIR / "data" / "reference_data"
SYNTHETIC_EVENTS = BASE_DIR / "data" / "synthetic_events"


# -----------------------------
# Load Reference Data
# -----------------------------

placement_drives_df = pd.read_csv(
    REFERENCE_DATA / "placement_drives.csv"
)

registrations_df = pd.read_csv(
    REFERENCE_DATA / "registrations.csv"
)

interviews_df = pd.read_csv(
    REFERENCE_DATA / "interviews.csv"
)

offers_df = pd.read_csv(
    REFERENCE_DATA / "offers.csv"
)


# -----------------------------
# Event Helpers
# -----------------------------

def generate_event_timestamp(base_date):
    """
    Generate a synthetic timestamp for an event.
    """

    hour = random.randint(8, 18)
    minute = random.randint(0, 59)

    timestamp = datetime.combine(
        base_date,
        datetime.min.time()
    ) + timedelta(
        hours=hour,
        minutes=minute
    )

    return timestamp.isoformat()


def create_event(
    event_id,
    event_type,
    event_timestamp,
    student_id=None,
    drive_id=None,
    interview_id=None,
    offer_id=None,
):
    """
    Create a standardized event dictionary.
    """

    return {
        "Event_ID": event_id,
        "Event_Type": event_type,
        "Event_Timestamp": event_timestamp,
        "Student_ID": student_id,
        "Drive_ID": drive_id,
        "Interview_ID": interview_id,
        "Offer_ID": offer_id,
    }


# -----------------------------
# Generate Events
# -----------------------------

def generate_events():

    events = []
    event_number = 1

    # --------------------------------
    # Drive Published events
    # --------------------------------

    for _, drive in placement_drives_df.iterrows():

        registration_start = pd.to_datetime(
            drive["Registration_Start"]
        ).date()

        events.append(
            create_event(
                event_id=f"EVT{event_number:06d}",
                event_type="DrivePublished",
                event_timestamp=generate_event_timestamp(
                    registration_start
                ),
                drive_id=drive["Drive_ID"],
            )
        )

        event_number += 1

    # --------------------------------
    # Student Registered events
    # --------------------------------

    for _, registration in registrations_df.iterrows():

        registration_date = pd.to_datetime(
            registration["Registration_Date"]
        ).date()

        events.append(
            create_event(
                event_id=f"EVT{event_number:06d}",
                event_type="StudentRegistered",
                event_timestamp=generate_event_timestamp(
                    registration_date
                ),
                student_id=registration["Student_ID"],
                drive_id=registration["Drive_ID"],
            )
        )

        event_number += 1

    # --------------------------------
    # Interview events
    # --------------------------------

    for _, interview in interviews_df.iterrows():

        interview_date = pd.to_datetime(
            interview["Interview_Date"]
        ).date()

        # Interview scheduled
        events.append(
            create_event(
                event_id=f"EVT{event_number:06d}",
                event_type="InterviewScheduled",
                event_timestamp=generate_event_timestamp(
                    interview_date
                ),
                student_id=interview["Student_ID"],
                drive_id=interview["Drive_ID"],
                interview_id=interview["Interview_ID"],
            )
        )

        event_number += 1

        # Some interviews are rescheduled
        if random.random() < 0.10:

            rescheduled_date = (
                interview_date
                + timedelta(days=1)
            )

            events.append(
                create_event(
                    event_id=f"EVT{event_number:06d}",
                    event_type="InterviewRescheduled",
                    event_timestamp=generate_event_timestamp(
                        rescheduled_date
                    ),
                    student_id=interview["Student_ID"],
                    drive_id=interview["Drive_ID"],
                    interview_id=interview["Interview_ID"],
                )
            )

            event_number += 1

        # Interview completed
        events.append(
            create_event(
                event_id=f"EVT{event_number:06d}",
                event_type="InterviewCompleted",
                event_timestamp=generate_event_timestamp(
                    interview_date
                ),
                student_id=interview["Student_ID"],
                drive_id=interview["Drive_ID"],
                interview_id=interview["Interview_ID"],
            )
        )

        event_number += 1

    # --------------------------------
    # Offer events
    # --------------------------------

    for _, offer in offers_df.iterrows():

        # Find the corresponding interview.
        matching_interviews = interviews_df[
            (interviews_df["Student_ID"] == offer["Student_ID"])
            & (interviews_df["Drive_ID"] == offer["Drive_ID"])
        ]

        if matching_interviews.empty:
            continue

        interview = matching_interviews.iloc[0]

        interview_date = pd.to_datetime(
            interview["Interview_Date"]
        ).date()

        # Offer released after interview
        offer_date = (
            interview_date
            + timedelta(days=random.randint(1, 5))
        )

        events.append(
            create_event(
                event_id=f"EVT{event_number:06d}",
                event_type="OfferReleased",
                event_timestamp=generate_event_timestamp(
                    offer_date
                ),
                student_id=offer["Student_ID"],
                drive_id=offer["Drive_ID"],
                offer_id=offer["Offer_ID"],
            )
        )

        event_number += 1

        # Accepted offers generate an acceptance event.
        if offer["Offer_Status"] == "Accepted":

            accepted_date = (
                offer_date
                + timedelta(days=random.randint(1, 3))
            )

            events.append(
                create_event(
                    event_id=f"EVT{event_number:06d}",
                    event_type="OfferAccepted",
                    event_timestamp=generate_event_timestamp(
                        accepted_date
                    ),
                    student_id=offer["Student_ID"],
                    drive_id=offer["Drive_ID"],
                    offer_id=offer["Offer_ID"],
                )
            )

            event_number += 1

    return events


# -----------------------------
# Main
# -----------------------------

if __name__ == "__main__":

    SYNTHETIC_EVENTS.mkdir(
        parents=True,
        exist_ok=True
    )

    events = generate_events()

    output_path = (
        SYNTHETIC_EVENTS
        / "placement_events.json"
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            events,
            file,
            indent=2
        )

    events_df = pd.DataFrame(events)

    print()
    print("Event generation completed.")
    print(
        f"Total events generated: "
        f"{len(events_df)}"
    )
    print()
    print(
        events_df["Event_Type"]
        .value_counts()
        .to_string()
    )