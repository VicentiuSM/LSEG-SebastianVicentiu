# 📊 LSEG Log Monitoring Application

A Python application that parses log files, calculates job execution durations, and detects long-running jobs.  
This solution demonstrates structured problem-solving, clean and modular code, time-based analysis, and automatic reporting via a generated HTML dashboard.

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
- Generates a standalone HTML report (`report.html`)
- Opens the report automatically in your default web browser

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-user/LSEG.git
   cd LSEG
