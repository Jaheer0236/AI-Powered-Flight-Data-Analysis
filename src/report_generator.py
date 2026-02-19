import os
import pandas as pd
from dotenv import load_dotenv
from groq import Groq
from data_loader import load_flight_data
from anomaly_detection import detect_anomalies

# Load API key from .env file
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_report(df, anomalies):
    
    # Prepare summary stats
    total = len(df)
    total_delayed = len(anomalies)
    on_time_pct = round((1 - total_delayed / total) * 100, 1)
    worst_airline = anomalies.groupby('airline').size()\
                              .sort_values(ascending=False).index[0]
    worst_route = anomalies.groupby('route').size()\
                            .sort_values(ascending=False).index[0]
    max_delay = anomalies['delay_hours'].max()
    worst_flight = anomalies.loc[anomalies['delay_hours'].idxmax(), 'flight_id']

    # Build the prompt
    prompt = f"""
You are a senior flight operations analyst. 
Write a professional flight operations summary report based on the data below.

--- FLIGHT DATA SUMMARY ---
Total Flights Analyzed  : {total}
Total Delayed (>2 hrs)  : {total_delayed}
On-Time Performance     : {on_time_pct}%
Worst Performing Airline: {worst_airline}
Most Delayed Route      : {worst_route}
Maximum Delay           : {max_delay} hours
Worst Flight            : {worst_flight}

--- DELAY BREAKDOWN BY AIRLINE ---
{anomalies.groupby('airline').size().sort_values(ascending=False).to_string()}

--- DELAY BREAKDOWN BY ROUTE ---
{anomalies.groupby('route').size().sort_values(ascending=False).to_string()}

Write the report with these sections:
1. Executive Summary
2. Key Findings
3. Airline Performance Analysis
4. Route Analysis
5. Recommendations

Use a professional tone suitable for operations managers.
Keep it clear and concise.
"""

    print("\n🤖 Sending data to Groq AI...")
    print("⏳ Please wait...\n")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert flight operations analyst who writes clear professional reports."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4,
        max_tokens=1000
    )

    report = response.choices[0].message.content

    # Save report to file
    with open("reports/flight_report.txt", "w") as f:
        f.write(report)

    print("=" * 50)
    print("📋 AI GENERATED FLIGHT OPERATIONS REPORT")
    print("=" * 50)
    print(report)
    print("\n💾 Report saved to reports/flight_report.txt")

    return report

if __name__ == "__main__":
    df = load_flight_data("data/processed/flight_data_clean.xlsx")
    df, anomalies = detect_anomalies(df)
    generate_report(df, anomalies)