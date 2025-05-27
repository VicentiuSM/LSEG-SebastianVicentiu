import pandas as pd
import webbrowser
import pathlib

# Generates an HTML report from the analyzed DataFrame
# Tricky Part: this function writes raw HTML, handles missing END values, and opens the file in the browser safely

def generate_html_report(dataframe, output_file="report.html"):
    html = """
    <html>
    <head>
        <title>Log Monitoring Report</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            tr.ok { background-color: #e8f5e9; }        /* Green for OK */
            tr.warning { background-color: #fffde7; }   /* Yellow for WARNING */
            tr.error { background-color: #ffebee; }     /* Red for ERROR */
        </style>
    </head>
    <body>
        <h2>Log Monitoring Report</h2>
        <table>
            <tr>
                <th>PID</th>
                <th>Description</th>
                <th>Start Time</th>
                <th>End Time</th>
                <th>Duration</th>
                <th>Severity</th>
            </tr>
    """

    for _, row in dataframe.iterrows():
        severity = row["severity"].lower()
        # Tricky Part: some entries may have missing END values → show "N/A" instead of breaking the page
        html += f"""
        <tr class="{severity}">
            <td>{row['PID']}</td>
            <td>{row['description_start']}</td>
            <td>{row['timestamp_start'].time()}</td>
            <td>{row['timestamp_end'].time() if pd.notnull(row['timestamp_end']) else 'N/A'}</td>
            <td>{row['duration']}</td>
            <td>{row['severity']}</td>
        </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """

    # Write HTML to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Report generated: {output_file}")

    # Tricky Part: convert file path to URI (file:///...) to ensure browser compatibility on Windows
    file_url = pathlib.Path(output_file).absolute().as_uri()
    webbrowser.open(file_url)