
"""
AI & ML Internship - Day 1
Environment Setup Verification Program

Author: Vaishnavi Babanagoud 
"""

import platform
import sys
from datetime import datetime


def print_header():
    print("=" * 65)
    print("       AI & ML INTERNSHIP - DAY 1")
    print("       ENVIRONMENT SETUP VERIFICATION")
    print("=" * 65)


def show_system_information():
    print("\n[ System Information ]")
    print("-" * 65)

    print(f"Operating System : {platform.system()} {platform.release()}")
    print(f"Machine          : {platform.machine()}")
    print(f"Processor        : {platform.processor()}")
    print(f"Python Version   : {platform.python_version()}")
    print(f"Python Path      : {sys.executable}")


def internship_information():
    print("\n[ Internship Information ]")
    print("-" * 65)

    intern_name = "vaishnavi Babanagoud"
    organization = "Codomax Digital Solutions"
    internship_domain = "Artificial Intelligence & Machine Learning"

    print(f"Intern Name      : {intern_name}")
    print(f"Organization     : {organization}")
    print(f"Domain           : {internship_domain}")


def environment_status():
    print("\n[ Development Environment Status ]")
    print("-" * 65)

    software_tools = {
        "Python": "Ready",
        "VS Code": "Ready",
        "Git": "Ready",
        "Jupyter Notebook": "Ready"
    }

    for tool, status in software_tools.items():
        print(f"{tool:<25}: {status}")


def final_message():
    print("\n" + "=" * 65)
    print(" Environment Setup Completed Successfully!")
    print(" AI, ML and Data Science Development Environment is Ready.")
    print(f" Verification Time : {datetime.now()}")
    print("=" * 65)


def main():
    print_header()
    show_system_information()
    internship_information()
    environment_status()
    final_message()


if __name__ == "__main__":
    main()
