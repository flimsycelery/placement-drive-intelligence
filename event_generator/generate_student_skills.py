from pathlib import Path
import random

import pandas as pd

from event_generator.config import (
    RANDOM_SEED,
    BRANCH_SKILL_MAPPING
)

random.seed(RANDOM_SEED)

BASE_DIR = Path(__file__).resolve().parent.parent

REFERENCE_DATA = BASE_DIR / "data" / "reference_data"

students_df = pd.read_csv(
    REFERENCE_DATA / "students.csv"
)

branches_df = pd.read_csv(
    REFERENCE_DATA / "branches.csv"
)

skills_df = pd.read_csv(
    REFERENCE_DATA / "skills.csv"
)

branch_lookup = dict(
    zip(
        branches_df["Branch_ID"],
        branches_df["Branch_Name"]
    )
)

skill_lookup = dict(
    zip(
        skills_df["Skill_Name"],
        skills_df["Skill_ID"]
    )
)