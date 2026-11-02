# PyTest API Automation Framework

> A scalable, production-ready REST API Automation Framework built using **Python**, **PyTest**, and **Requests**. This project demonstrates enterprise-level API test automation practices, framework design, and clean coding principles.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![PyTest](https://img.shields.io/badge/PyTest-Latest-green)
![Automation](https://img.shields.io/badge/API-Automation-orange)

---

# Overview

This repository showcases a robust REST API automation framework developed using **Python** and **PyTest**.

The framework is designed using industry best practices to create a scalable, maintainable, and reusable automation solution suitable for enterprise applications.

It demonstrates practical implementation of API automation concepts that are commonly used in cloud, enterprise software, and CI/CD environments.

---

# Key Features

- REST API Automation using Python
- PyTest Framework
- Modular and Scalable Framework Design
- Reusable API Client
- Configuration Management
- Test Data Management
- Centralized Logging
- HTML Test Reporting
- Utility Functions
- Environment-based Execution
- Clean Project Structure
- CI/CD Ready Architecture

---

# Technology Stack

- Python 3
- PyTest
- Requests
- JSON
- Logging
- HTML Reports
- Git
- GitHub

---

# Project Structure

```
PyTest_API_Automation/
│
├── api/                 # API client implementation
├── config/              # Configuration files
├── data/                # Test data
├── logs/                # Execution logs
├── reports/             # HTML reports
├── tests/               # Test cases
├── utils/               # Utility modules
├── conftest.py          # PyTest fixtures
├── pytest.ini           # PyTest configuration
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/susamant/PyTest_API_Automation.git
```

Navigate to the project

```bash
cd PyTest_API_Automation
```

Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running Tests

Run all tests

```bash
pytest
```

Run with verbose output

```bash
pytest -v
```

Run a specific test

```bash
pytest tests/test_login.py
```

Run smoke tests

```bash
pytest -m smoke
```

Generate HTML report

```bash
pytest --html=reports/report.html --self-contained-html
```

---

# Framework Components

## API Client

Reusable methods for

- GET
- POST
- PUT
- PATCH
- DELETE

---

## Configuration Management

Supports multiple environments such as

- Development
- QA
- UAT
- Production

---

## Logging

Centralized logging captures

- Request details
- Response details
- Errors
- Execution information

---

## Test Data Management

Supports separation of test logic and test data for improved maintainability.

---

## Reporting

Generates HTML execution reports including

- Passed Tests
- Failed Tests
- Skipped Tests
- Execution Time
- Failure Details

---

# Design Principles

The framework follows modern automation engineering practices including:

- Modular Architecture
- DRY (Don't Repeat Yourself)
- Reusable Components
- Config-Driven Execution
- Fixture-Based Test Setup
- Maintainable Code Structure
- Easy Scalability

---

# Planned Enhancements

Future improvements may include:

- OAuth Authentication
- JWT Token Management
- Automatic Token Refresh
- Retry Mechanism with Exponential Backoff
- JSON Schema Validation
- Database Validation
- Parallel Test Execution
- Docker Support
- Jenkins Integration
- GitHub Actions CI
- Allure Reporting

---

# Skills Demonstrated

- Python Programming
- REST API Automation
- PyTest
- Requests Library
- Automation Framework Development
- Software Testing
- API Validation
- Logging
- Reporting
- Test Architecture
- Continuous Integration

---

# About the Author

## Suman Samanta

**Lead SDET | QA Automation Engineer**

Experienced QA Automation professional with **13+ years** of expertise in:

- Python Automation
- REST API Testing
- Enterprise Storage
- VMware Technologies
- IBM Cloud
- Automation Framework Development
- CI/CD Automation
- Test Strategy & Quality Engineering

**GitHub:**  
https://github.com/susamant

**LinkedIn:**  
*Add your LinkedIn profile URL here*

---

# Repository Usage

This repository is published for:

- Professional portfolio
- Technical demonstration
- Learning and reference

You are welcome to browse the code and learn from the implementation.

However, this repository is **not an open-source project**.

The source code may **not** be copied, modified, redistributed, republished, or used commercially without prior written permission from the author.

---

# Contributions

This repository is **not accepting**:

- Pull Requests
- Code Contributions
- Feature Requests

If you identify an issue or have a question, you may open a GitHub Issue for discussion.

---

# License

**Copyright © 2026 Suman Samanta. All Rights Reserved.**

This project is provided solely for educational, evaluation, and portfolio purposes.

No permission is granted to copy, modify, distribute, sublicense, publish, or commercially use any part of this repository without explicit written permission from the copyright holder.

---

## Support

If this project helped you understand API Automation concepts, please consider giving the repository a ⭐ on GitHub.

Your support is appreciated.