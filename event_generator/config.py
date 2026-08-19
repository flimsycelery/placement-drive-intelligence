"""
Shared configuration for synthetic reference data generation.
"""

# Random seed for reproducible datasets
RANDOM_SEED = 42

# Academic branches
BRANCHES = [
    "Computer Science Engineering",
    "Information Science Engineering",
    "Artificial Intelligence & Machine Learning",
    "Data Science",
    "Electronics & Communication",
    "Electrical & Electronics",
    "Mechanical Engineering",
    "Civil Engineering"
]

# Technical skills
SKILLS = [
    "Python",
    "SQL",
    "Java",
    "C++",
    "JavaScript",
    "Power BI",
    "Microsoft Fabric",
    "Azure",
    "PySpark",
    "Apache Spark",
    "Pandas",
    "Machine Learning",
    "Data Analysis",
    "Git",
    "Docker",
    "Azure Data Factory",
    "Databricks",
    "Snowflake",
    "Excel",
    "Communication"
]

# Placement roles
ROLES = [
    "Software Engineer",
    "Data Analyst",
    "Data Engineer",
    "Business Analyst",
    "Machine Learning Engineer",
    "Cloud Engineer",
    "Backend Developer",
    "Frontend Developer",
    "Full Stack Developer",
    "DevOps Engineer"
]

# Companies
COMPANIES = [
    "Microsoft",
    "Amazon",
    "Google",
    "Adobe",
    "SAP",
    "Oracle",
    "Intel",
    "NVIDIA",
    "Cisco",
    "IBM",
    "Accenture",
    "Deloitte",
    "TCS",
    "Infosys",
    "Wipro",
    "Capgemini",
    "Cognizant",
    "LTIMindtree",
    "Bosch",
    "Mercedes-Benz R&D",
    "Flipkart",
    "PhonePe",
    "Swiggy",
    "Zomato",
    "Razorpay",
    "TIFIN",
    "Dremio",
    "Kiwi",
    "Freshworks",
    "Zoho"
]

# -----------------------------
# Student Names
# -----------------------------

FIRST_NAMES = [
    "Aarav", "Aditya", "Akhil", "Ananya", "Anika",
    "Arjun", "Aryan", "Ayesha", "Diya", "Harsh",
    "Ishaan", "Karan", "Kavya", "Meera", "Neha",
    "Nikhil", "Pooja", "Pranav", "Priya", "Rahul",
    "Rohan", "Sai", "Sakshi", "Sanjana", "Shreya",
    "Sneha", "Tanmay", "Varun", "Vedant", "Vihaan",
    "Yash", "Aditi", "Ritika", "Simran", "Abhishek",
    "Akash", "Anirudh", "Bhavya", "Charan", "Deepika",
    "Dev", "Gaurav", "Keerthi", "Lakshmi", "Manasa",
    "Nandini", "Naveen", "Nithin", "Ritika", "Suhas"
]

LAST_NAMES = [
    "Sharma", "Verma", "Patel", "Reddy", "Nair",
    "Iyer", "Rao", "Kulkarni", "Shetty", "Naik",
    "Bhat", "Hegde", "Menon", "Pai", "Prabhu",
    "Kamath", "Acharya", "Shenoy", "Kumar", "Gupta",
    "Singh", "Joshi", "Mishra", "Das", "Chowdhury",
    "Jain", "Agarwal", "Malhotra", "Kapoor", "Mehta",
    "Saxena", "Pandey", "Yadav", "Sinha", "Tripathi",
    "Rastogi", "Bhatt", "Desai", "Patil", "Gowda",
    "Pillai", "Fernandes", "D'Souza", "Pereira", "Lobo",
    "Alva", "Poojary", "Suvarna", "Shekar", "Murthy"
]

BRANCH_SKILL_MAPPING = {
    "Computer Science Engineering": {
        "core": [
            "Python",
            "SQL",
            "Java",
            "Git"
        ],
        "optional": [
            "JavaScript",
            "Docker",
            "Azure",
            "Databricks"
        ]
    },

    "Information Science Engineering": {
        "core": [
            "Python",
            "SQL",
            "Java",
            "Git"
        ],
        "optional": [
            "Power BI",
            "Azure",
            "Excel"
        ]
    },

    "Data Science": {
        "core": [
            "Python",
            "SQL",
            "Pandas",
            "Machine Learning"
        ],
        "optional": [
            "Power BI",
            "Microsoft Fabric",
            "Apache Spark",
            "Azure"
        ]
    },

    "Artificial Intelligence & Machine Learning": {
        "core": [
            "Python",
            "Machine Learning",
            "Pandas"
        ],
        "optional": [
            "SQL",
            "Power BI",
            "Azure"
        ]
    },

    "Electronics & Communication": {
        "core": [
            "C++",
            "Python"
        ],
        "optional": [
            "Git",
            "SQL",
            "Excel"
        ]
    },
    "Electrical & Electronics": {
    "core": [
        "Python",
        "Excel"
    ],
    "optional": [
        "SQL",
        "Git",
        "C++"
    ]
    },

    "Mechanical Engineering": {
        "core": [
            "Excel"
        ],
        "optional": [
            "Python",
            "Communication"
        ]
    },

    "Civil Engineering": {
        "core": [
            "Excel"
        ],
        "optional": [
            "Communication",
            "Python"
        ]
    }
}

# -----------------------------
# Placement Role Rules
# -----------------------------

# -----------------------------
# Placement Role Rules
# -----------------------------

ROLE_RULES = {
    "Software Engineer": {
        "required_skills": [
            "Python",
            "SQL",
            "Git",
        ],
        "optional_skills": [
            "Java",
            "JavaScript",
            "Docker",
            "C++",
        ],
        "eligible_branches": [
            "Computer Science Engineering",
            "Information Science Engineering",
            "Data Science",
            "Artificial Intelligence & Machine Learning",
            "Electronics & Communication",
            "Electrical & Electronics",
        ],
        "cgpa_range": (7.0, 9.0),
        "backlog_limit": 1,
        "ctc_range_lpa": (6.0, 18.0),
    },

    "Data Analyst": {
        "required_skills": [
            "SQL",
            "Excel",
            "Power BI",
        ],
        "optional_skills": [
            "Python",
            "Pandas",
            "Data Analysis",
            "Communication",
        ],
        "eligible_branches": [
            "Computer Science Engineering",
            "Information Science Engineering",
            "Data Science",
            "Artificial Intelligence & Machine Learning",
            "Electronics & Communication",
            "Mechanical Engineering",
        ],
        "cgpa_range": (6.5, 8.5),
        "backlog_limit": 1,
        "ctc_range_lpa": (5.0, 12.0),
    },

    "Data Engineer": {
        "required_skills": [
            "Python",
            "SQL",
        ],
        "optional_skills": [
            "Apache Spark",
            "PySpark",
            "Microsoft Fabric",
            "Azure",
            "Azure Data Factory",
            "Databricks",
            "Git",
        ],
        "eligible_branches": [
            "Computer Science Engineering",
            "Information Science Engineering",
            "Data Science",
            "Artificial Intelligence & Machine Learning",
        ],
        "cgpa_range": (7.0, 9.0),
        "backlog_limit": 0,
        "ctc_range_lpa": (7.0, 20.0),
    },

    "Business Analyst": {
        "required_skills": [
            "Excel",
            "Data Analysis",
        ],
        "optional_skills": [
            "SQL",
            "Power BI",
            "Communication",
        ],
        "eligible_branches": [
            "Computer Science Engineering",
            "Information Science Engineering",
            "Data Science",
            "Electronics & Communication",
            "Mechanical Engineering",
            "Civil Engineering",
        ],
        "cgpa_range": (6.5, 8.5),
        "backlog_limit": 1,
        "ctc_range_lpa": (5.0, 12.0),
    },

    "Machine Learning Engineer": {
        "required_skills": [
            "Python",
            "Machine Learning",
            "Pandas",
        ],
        "optional_skills": [
            "SQL",
            "PySpark",
            "Apache Spark",
            "Databricks",
            "Git",
        ],
        "eligible_branches": [
            "Computer Science Engineering",
            "Data Science",
            "Artificial Intelligence & Machine Learning",
            "Information Science Engineering",
        ],
        "cgpa_range": (7.5, 9.5),
        "backlog_limit": 0,
        "ctc_range_lpa": (8.0, 22.0),
    },

    "Cloud Engineer": {
        "required_skills": [
            "Python",
            "Azure",
            "Git",
        ],
        "optional_skills": [
            "Docker",
            "SQL",
            "Azure Data Factory",
            "Databricks",
        ],
        "eligible_branches": [
            "Computer Science Engineering",
            "Information Science Engineering",
            "Data Science",
            "Artificial Intelligence & Machine Learning",
            "Electronics & Communication",
        ],
        "cgpa_range": (7.0, 9.0),
        "backlog_limit": 1,
        "ctc_range_lpa": (6.0, 16.0),
    },

    "Backend Developer": {
        "required_skills": [
            "Python",
            "SQL",
            "Git",
        ],
        "optional_skills": [
            "Java",
            "C++",
            "Docker",
            "Azure",
        ],
        "eligible_branches": [
            "Computer Science Engineering",
            "Information Science Engineering",
            "Data Science",
            "Artificial Intelligence & Machine Learning",
            "Electronics & Communication",
        ],
        "cgpa_range": (7.0, 9.0),
        "backlog_limit": 1,
        "ctc_range_lpa": (6.0, 18.0),
    },

    "Frontend Developer": {
        "required_skills": [
            "JavaScript",
        ],
        "optional_skills": [
            "Git",
            "Python",
            "SQL",
            "Communication",
        ],
        "eligible_branches": [
            "Computer Science Engineering",
            "Information Science Engineering",
            "Artificial Intelligence & Machine Learning",
        ],
        "cgpa_range": (6.5, 8.5),
        "backlog_limit": 1,
        "ctc_range_lpa": (5.0, 15.0),
    },

    "Full Stack Developer": {
        "required_skills": [
            "JavaScript",
            "SQL",
            "Git",
        ],
        "optional_skills": [
            "Python",
            "Java",
            "Docker",
            "Azure",
        ],
        "eligible_branches": [
            "Computer Science Engineering",
            "Information Science Engineering",
            "Data Science",
            "Artificial Intelligence & Machine Learning",
        ],
        "cgpa_range": (7.0, 9.0),
        "backlog_limit": 1,
        "ctc_range_lpa": (6.0, 18.0),
    },

    "DevOps Engineer": {
        "required_skills": [
            "Git",
            "Docker",
        ],
        "optional_skills": [
            "Azure",
            "Python",
            "Azure Data Factory",
            "Databricks",
        ],
        "eligible_branches": [
            "Computer Science Engineering",
            "Information Science Engineering",
            "Artificial Intelligence & Machine Learning",
        ],
        "cgpa_range": (7.0, 9.0),
        "backlog_limit": 0,
        "ctc_range_lpa": (7.0, 18.0),
    },
}