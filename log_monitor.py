import pandas as pd
from datetime import datetime, timedelta
from generate_report import generate_html_report  # Import for HTML report generation

# Parses the log file and returns a structured DataFrame
# Each log line is expected to be in the format: "HH:MM:SS,description,START/END,pid"
def parse_log_file(file_path):
    logs = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4:
                timestamp, description, status, pid = parts
                logs.append({
                    "timestamp": datetime.strptime(timestamp.strip(), "%H:%M:%S"),
                    "description": description.strip(),
                    "status": status.strip(),
                    "pid": int(pid.strip())
                })
    return pd.DataFrame(logs)

# Analyzes the logs to calculate job durations and classify severity
# Tricky Part: jobs without a matching START or END will be excluded due to join
# Tricky Part: duration calculation assumes START always comes before END (same day)
def analyze_logs(df):
    # Separate logs into START and END events
    start_logs = df[df["status"] == "START"].set_index("pid")
    end_logs = df[df["status"] == "END"].set_index("pid")

    # Join START and END logs by PID to create one row per job
    # Tricky Part: if END is missing, timestamp_end will be NaT
    merged = start_logs.join(end_logs, lsuffix="_start", rsuffix="_end")

    # Calculate execution duration
    merged["duration"] = merged["timestamp_end"] - merged["timestamp_start"]

    # Define severity based on duration thresholds
    merged["severity"] = merged["duration"].apply(
        lambda d: "ERROR" if d > timedelta(minutes=10)
        else "WARNING" if d > timedelta(minutes=5)
        else "OK"
    )

    # Prepare clean output with renamed PID column
    result = merged[["description_start", "timestamp_start", "timestamp_end", "duration", "severity"]].reset_index()
    result.rename(columns={"pid": "PID"}, inplace=True)
    return result

# Main function for full processing pipeline
# 1. Parse input logs
# 2. Analyze and classify by duration
# 3. Print summary to console
# 4. Generate HTML report (auto-opens in browser)
def main():
    df = parse_log_file("logs.log")
    result = analyze_logs(df)

    for _, row in result.iterrows():
        print(f"PID {row['PID']} ({row['description_start']}): Duration = {row['duration']} [{row['severity']}]")

    generate_html_report(result)  # Tricky Part: generates static HTML and opens it using file:// URI

if __name__ == "__main__":
    main()