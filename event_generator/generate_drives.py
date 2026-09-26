"""
Generate synthetic campus placement drive datasets.
"""

from pathlib import Path
import random
from datetime import date, timedelta

import pandas as pd

from event_generator.config import (
    RANDOM_SEED,
    ROLE_RULES,
)
from event_generator.utils.id_generator import generate_id


# -----------------------------
# Configuration
# -----------------------------

random.seed(RANDOM_SEED)

NUMBER_OF_DRIVES = 40


# -----------------------------
# Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
REFERENCE_DATA = BASE_DIR / "data" / "reference_data"


# -----------------------------
# Load Reference Data
# -----------------------------

companies_df = pd.read_csv(
    REFERENCE_DATA / "companies.csv"
)

roles_df = pd.read_csv(
    REFERENCE_DATA / "roles.csv"
)

branches_df = pd.read_csv(
    REFERENCE_DATA / "branches.csv"
)

skills_df = pd.read_csv(
    REFERENCE_DATA / "skills.csv"
)


def validate_role_rules():
    """Validate role configuration against reference data."""

    valid_roles = set(roles_df["Role_Name"])
    valid_skills = set(skills_df["Skill_Name"])
    valid_branches = set(branches_df["Branch_Name"])

    for role_name, rules in ROLE_RULES.items():

        if role_name not in valid_roles:
            raise ValueError(
                f"Unknown role in ROLE_RULES: {role_name}"
            )

        configured_skills = (
            rules["required_skills"]
            + rules["optional_skills"]
        )

        for skill in configured_skills:
            if skill not in valid_skills:
                raise ValueError(
                    f"Unknown skill '{skill}' "
                    f"configured for role '{role_name}'"
                )

        for branch in rules["eligible_branches"]:
            if branch not in valid_branches:
                raise ValueError(
                    f"Unknown branch '{branch}' "
                    f"configured for role '{role_name}'"
                )

    print("Role configuration validation passed.")


def generate_placement_drives(count: int = 40):
    """
    Generate synthetic placement drives along with
    branch eligibility and required skill mappings.
    """

    drives = []
    drive_branches = []
    drive_skills = []

    for drive_number in range(1, count + 1):

        # -----------------------------
        # Select company and role
        # -----------------------------

        company = companies_df.sample(
            n=1,
            random_state=RANDOM_SEED + drive_number
        ).iloc[0]

        role = roles_df.sample(
            n=1,
            random_state=RANDOM_SEED + drive_number * 10
        ).iloc[0]

        role_name = role["Role_Name"]

        rules = ROLE_RULES[role_name]

        # -----------------------------
        # Generate dates
        # -----------------------------

        registration_start = date(2026, 8, 1) + timedelta(
            days=random.randint(0, 60)
        )

        registration_end = registration_start + timedelta(
            days=random.randint(5, 10)
        )

        # -----------------------------
        # Eligibility
        # -----------------------------

        minimum_cgpa = round(
            random.uniform(
                rules["cgpa_range"][0],
                rules["cgpa_range"][1]
            ),
            2
        )

        backlog_limit = rules["backlog_limit"]

        # -----------------------------
        # Compensation
        # -----------------------------

        ctc = round(
            random.uniform(
                rules["ctc_range_lpa"][0],
                rules["ctc_range_lpa"][1]
            ),
            1
        )

        # -----------------------------
        # Positions
        # -----------------------------

        open_positions = random.randint(2, 20)

        # -----------------------------
        # Drive ID
        # -----------------------------

        drive_id = generate_id(
            "DRV",
            drive_number
        )

        # -----------------------------
        # Drive record
        # -----------------------------

        drives.append(
            {
                "Drive_ID": drive_id,
                "Company_ID": company["Company_ID"],
                "Role_ID": role["Role_ID"],
                "Registration_Start": registration_start,
                "Registration_End": registration_end,
                "Minimum_CGPA": minimum_cgpa,
                "Eligibility_Backlogs": backlog_limit,
                "CTC_LPA": ctc,
                "Open_Positions": open_positions,
                "Status": "Open",
            }
        )

        # -----------------------------
        # Eligible branches
        # -----------------------------

        for branch_name in rules["eligible_branches"]:

            branch_id = branches_df.loc[
                branches_df["Branch_Name"] == branch_name,
                "Branch_ID"
            ].iloc[0]

            drive_branches.append(
                {
                    "Drive_ID": drive_id,
                    "Branch_ID": branch_id,
                }
            )

        # -----------------------------
        # Drive skills
        # -----------------------------

        for skill_name in rules["required_skills"]:

            skill_id = skills_df.loc[
                skills_df["Skill_Name"] == skill_name,
                "Skill_ID"
            ].iloc[0]

            drive_skills.append(
                {
                    "Drive_ID": drive_id,
                    "Skill_ID": skill_id,
                    "Skill_Type": "Required",
                }
            )


        for skill_name in rules["optional_skills"]:

            skill_id = skills_df.loc[
                skills_df["Skill_Name"] == skill_name,
                "Skill_ID"
            ].iloc[0]

            drive_skills.append(
                {
                    "Drive_ID": drive_id,
                    "Skill_ID": skill_id,
                    "Skill_Type": "Recommended",
                }
            )

    return (
        pd.DataFrame(drives),
        pd.DataFrame(drive_branches),
        pd.DataFrame(drive_skills),
    )


if __name__ == "__main__":

    validate_role_rules()

    drives_df, drive_branches_df, drive_skills_df = (
        generate_placement_drives()
    )

    drives_df.to_csv(
        REFERENCE_DATA / "placement_drives.csv",
        index=False
    )

    drive_branches_df.to_csv(
        REFERENCE_DATA / "drive_branches.csv",
        index=False
    )

    drive_skills_df.to_csv(
        REFERENCE_DATA / "drive_skills.csv",
        index=False
    )

    print()
    print("Placement drive generation completed.")
    print(f"Drives generated: {len(drives_df)}")
    print(f"Drive-branch mappings: {len(drive_branches_df)}")
    print(
        f"Drive-skill mappings: "
        f"{len(drive_skills_df)}"
    )

    print()
    print(drives_df.head())