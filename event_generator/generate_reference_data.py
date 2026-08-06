"""
Generate reference datasets for the
Campus Placement Intelligence Platform.
"""

from pathlib import Path
import pandas as pd

from config import BRANCHES, SKILLS, ROLES, COMPANIES

BASE_DIR = Path(__file__).resolve().parent.parent
REFERENCE_DATA = BASE_DIR / "data" / "reference_data"

REFERENCE_DATA.mkdir(parents=True, exist_ok=True)


def save_reference_data(data, id_prefix, id_column, value_column, filename):
    """
    Generates a reference dataset with IDs
    and saves it as a CSV.
    """

    df = pd.DataFrame({
        id_column: [f"{id_prefix}{i+1:03}" for i in range(len(data))],
        value_column: data
    })

    output_file = REFERENCE_DATA / filename
    df.to_csv(output_file, index=False)

    print(f"Created {filename}")


save_reference_data(
    BRANCHES,
    "B",
    "Branch_ID",
    "Branch_Name",
    "branches.csv"
)

save_reference_data(
    SKILLS,
    "SK",
    "Skill_ID",
    "Skill_Name",
    "skills.csv"
)

save_reference_data(
    ROLES,
    "R",
    "Role_ID",
    "Role_Name",
    "roles.csv"
)

save_reference_data(
    COMPANIES,
    "C",
    "Company_ID",
    "Company_Name",
    "companies.csv"
)

print("\nReference datasets generated successfully.")