"""
Generate synthetic student data.
"""

from pathlib import Path
import random

import pandas as pd
from faker import Faker

from event_generator.config import RANDOM_SEED

# -----------------------------
# Configuration
# -----------------------------

random.seed(RANDOM_SEED)
fake = Faker()
Faker.seed(RANDOM_SEED)

# -----------------------------
# Project Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

REFERENCE_DATA = BASE_DIR / "data" / "reference_data"

# -----------------------------
# Load Reference Data
# -----------------------------

branches_df = pd.read_csv(REFERENCE_DATA / "branches.csv")
skills_df = pd.read_csv(REFERENCE_DATA / "skills.csv")

print(branches_df.head())
print(skills_df.head())