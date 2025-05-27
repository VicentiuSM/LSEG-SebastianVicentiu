# 📊 LSEG Log Monitoring Application

[![Python CI] (https://github.com/VicentiuSM/LSEG-SebastianVicentiu/actions)

A Python application that parses log files, calculates job execution durations, and detects long-running jobs.  
This solution demonstrates structured problem-solving, modular code, test coverage, and automated reporting via an HTML dashboard.

---

## ✅ Features

- Parses a structured log file (`logs.log`)
- Matches `START` and `END` entries by job PID
- Calculates execution duration per job
- Automatically flags:
    - ✅ `OK` if duration ≤ 5 minutes
    - ⚠️ `WARNING` if duration > 5 minutes
    - ❌ `ERROR` if duration > 10 minutes
- Displays a summary in the console
- Generates an offline HTML report (`report.html`)
- Opens the report automatically in the browser
- Includes unit test coverage with `pytest`
- GitHub Actions CI pipeline for continuous integration

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/VicentiuSM/LSEG-SebastianVicentiu.git
cd LSEG-SebastianVicentiu
```
### 2. Install required dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the application
```bash
python log_monitor.py
```
