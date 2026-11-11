# Mini SOC Monitoring and Threat Detection System

## Project Overview
A beginner cybersecurity project developed using Python and Streamlit to monitor authentication logs, identify failed login attempts, and detect suspicious login activity.

## Features
- Reads authentication log files.
- Counts successful and failed login attempts.
- Tracks failed login attempts by IP address.
- Detects suspicious activity using a configurable threshold.
- Displays login statistics in a Streamlit dashboard.
- Shows security events in a table.

## Technologies Used
- Python
- Streamlit
- VS Code
- Authentication Log Analysis

## How to Run

1. Clone this repository.
2. Open the project folder in VS Code.
3. Install dependencies:

   `pip install streamlit`

4. Start the dashboard:

   `python -m streamlit run dashboard.py`

## Project Structure

```text
Mini-SOC-Monitoring-System/
├── main.py
├── dashboard.py
├── logs/
│   └── auth.log
└── .gitignore
```

## Detection Logic
The project uses a simple threshold-based rule to flag IP addresses with three or more failed login attempts.

This is a learning project using fictional authentication logs. Alerts indicate possible suspicious activity, not confirmed attacks.

## Learning Outcomes
- Python file handling
- Authentication log analysis
- Basic security event monitoring
- Threshold-based threat detection
- Building dashboards with Streamlit

**Project Status:** Completed beginner portfolio project.