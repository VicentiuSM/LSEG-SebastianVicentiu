# Ensure the root project folder is visible to the test runner
# Tricky Part: pytest may not find modules in parent folder without manually setting sys.path
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the functions to be tested from the main script
from log_monitor import parse_log_file, analyze_logs

def test_log_parsing_and_analysis():
    # Parse the log file and load it into a DataFrame
    df = parse_log_file("logs.log")

    # Ensure the log file was correctly parsed into rows
    assert not df.empty, "Parsed DataFrame is empty"

    # Check for presence of expected columns in raw log data
    expected_columns = {"timestamp", "description", "status", "pid"}
    assert expected_columns.issubset(df.columns), "Missing expected columns in parsed DataFrame"

    # Run the main analysis logic to pair START/END and compute durations
    result = analyze_logs(df)

    # Ensure output is not empty and structure is preserved
    assert not result.empty, "Analyzed result is empty"

    # Validate that analysis produced the required output columns
    assert "duration" in result.columns, "Missing 'duration' column in result"
    assert "severity" in result.columns, "Missing 'severity' column in result"

    # Tricky Part: Ensure that all severity values are among accepted constants
    valid_severities = {"OK", "WARNING", "ERROR"}
    assert result["severity"].isin(valid_severities).all(), "Invalid severity levels detected"
