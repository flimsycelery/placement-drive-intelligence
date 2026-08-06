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