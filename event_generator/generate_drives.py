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


if __name__ == "__main__":
    validate_role_rules()

    print(f"Companies loaded: {len(companies_df)}")
    print(f"Roles loaded: {len(roles_df)}")
    print(f"Branches loaded: {len(branches_df)}")
    print(f"Skills loaded: {len(skills_df)}")