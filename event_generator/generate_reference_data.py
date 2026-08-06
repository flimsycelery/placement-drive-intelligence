"""
Generate reference datasets for the
Campus Placement Intelligence Platform.
"""

from pathlib import Path
import pandas as pd

from config import BRANCHES, SKILLS, ROLES, COMPANIES

# -----------------------------
# Project Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

REFERENCE_DATA = BASE_DIR / "data" / "reference_data"

REFERENCE_DATA.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Generate DataFrames
# -----------------------------

branches_df = pd.DataFrame({
    "Branch_ID": [f"B{i+1:03}" for i in range(len(BRANCHES))],
    "Branch_Name": BRANCHES
})

skills_df = pd.DataFrame({
    "Skill_ID": [f"S{i+1:03}" for i in range(len(SKILLS))],
    "Skill_Name": SKILLS
})

roles_df = pd.DataFrame({
    "Role_ID": [f"R{i+1:03}" for i in range(len(ROLES))],
    "Role_Name": ROLES
})

companies_df = pd.DataFrame({
    "Company_ID": [f"C{i+1:03}" for i in range(len(COMPANIES))],
    "Company_Name": COMPANIES
})

# -----------------------------
# Save CSV files
# -----------------------------

branches_df.to_csv(
    REFERENCE_DATA / "branches.csv",
    index=False
)

skills_df.to_csv(
    REFERENCE_DATA / "skills.csv",
    index=False
)

roles_df.to_csv(
    REFERENCE_DATA / "roles.csv",
    index=False
)

companies_df.to_csv(
    REFERENCE_DATA / "companies.csv",
    index=False
)

print("Reference datasets generated successfully!")
print(f"Location: {REFERENCE_DATA}")