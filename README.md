## Task 4 – DevOps Internship Project
Objective: Implement a Git workflow with branching, pull requests, version tags, and documentation.

## Project Overview
This repository demonstrates Git best practices:

Creating and managing branches (main, dev, feature-readme)

Using Pull Requests (PRs) for merging code

Creating and pushing Git tags for versioning

Using .gitignore to exclude unnecessary files

Documenting the workflow in README.md

##  Branching Strategy

main           → Production-ready code
dev            → Integration branch for testing features
feature-readme → Feature branch for adding specific files (e.g., README.md, app.py)
## Git Workflow
Create repository on GitHub.

Clone locally and initialize Git.

Create branches:

git checkout -b main
git checkout -b dev
git checkout -b feature-readme
Add files in feature-readme (README.md, .gitignore, app.py).

Commit and push to GitHub:
git add .
git commit -m "Added files"
git push -u origin feature-readme
Open PR: feature-readme → dev and merge.

Open PR: dev → main and merge.

Tag versions:
git tag -a v1.0 -m "Initial setup"
git tag -a v1.1 -m "Added app.py"
git push origin v1.0
git push origin v1.1

'''
📂 Repository Structure
Copy
Edit
task4-devops-project/
│── .gitignore
│── README.md
│── app.py
📜 .gitignore Example
'''
gitignore

*.log
__pycache__/
*.tmp
💻 app.py Output Example

==================================================
 Welcome to Task 4 - DevOps Git Workflow Demo 
==================================================
Script executed at: 2025-08-08 12:45:32.123456
This file was created in the 'feature-readme' branch.
It will be merged into 'dev', then into 'main' via Pull Requests.

Git concepts demonstrated:
- Branching (main, dev, feature branches)
- Pull Requests and Merges
- Tags for versioning
- Using .gitignore
==================================================
