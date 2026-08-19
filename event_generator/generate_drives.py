"""
Generate synthetic campus placement drive datasets.
"""

from pathlib import Path
import random
from datetime import date, timedelta

import pandas as pd

from event_generator.config import RANDOM_SEED
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


if __name__ == "__main__":
    print(f"Companies loaded: {len(companies_df)}")
    print(f"Roles loaded: {len(roles_df)}")
    print(f"Branches loaded: {len(branches_df)}")
    print(f"Skills loaded: {len(skills_df)}")