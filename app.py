#!/usr/bin/env python3

"""
Task 4 - DevOps Internship Project
----------------------------------
This script simulates a simple application file added in a feature branch.
It is used to demonstrate Git branching, pull requests, and version tagging.
"""

import datetime

def main():
    print("="*50)
    print(" Welcome to Task 4 - DevOps Git Workflow Demo ")
    print("="*50)
    print(f"Script executed at: {datetime.datetime.now()}")
    print("\nThis file was created in the 'feature-readme' branch.")
    print("It will be merged into 'dev', then into 'main' via Pull Requests.")
    print("\nGit concepts demonstrated:")
    print("- Branching (main, dev, feature branches)")
    print("- Pull Requests and Merges")
    print("- Tags for versioning")
    print("- Using .gitignore")
    print("="*50)

if __name__ == "__main__":
    main()
