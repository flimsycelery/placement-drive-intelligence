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

student_skills = []

for _, student in students_df.iterrows():

    student_id = student["Student_ID"]

    branch_name = branch_lookup[student["Branch_ID"]]

    mapping = BRANCH_SKILL_MAPPING[branch_name]

    core_skills = mapping["core"]

    optional_skills = mapping["optional"]

    selected_optional = random.sample(
    optional_skills,
    k=random.randint(
        1,
        min(3, len(optional_skills))
    )
    )

    assigned_skills = (
        core_skills +
        selected_optional
    )

    for skill in assigned_skills:

        student_skills.append(
        {
            "Student_ID": student_id,
            "Skill_ID": skill_lookup[skill]
        }
    )

if branch_name not in BRANCH_SKILL_MAPPING:
    raise ValueError(
        f"No skill mapping found for branch: {branch_name}"
    )

mapping = BRANCH_SKILL_MAPPING[branch_name]

student_skills_df = pd.DataFrame(
    student_skills
)

student_skills_df.to_csv(
    REFERENCE_DATA / "student_skills.csv",
    index=False
)


print(student_skills_df.head())

print()

print(
    f"Generated {len(student_skills_df)} student skills."
)

print(f"Students processed: {students_df['Student_ID'].nunique()}")
print(f"Unique skills assigned: {student_skills_df['Skill_ID'].nunique()}")
print(f"Average skills per student: {len(student_skills_df) / len(students_df):.2f}")