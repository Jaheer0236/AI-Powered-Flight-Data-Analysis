# ✈️ AI-Powered Flight Data Analysis & Automation

## 📌 Overview
Automated flight operations reporting using Python, 
Groq AI, Excel, and Power BI — reducing manual 
reporting time by 60%.

## Overview of Dashboard
https://app.powerbi.com/view?r=eyJrIjoiZTNiYTRmN2ItOGVmMi00ZTZhLWE4MjAtYTk1MjllOWQ0NTUyIiwidCI6IjEyYzk2ZjBkLTQzZmUtNDM0Mi1iZGIxLTk3M2QyZTRjOWI0YiJ9

## 🚀 Features
- 📊 Analyzes 173 flights across 4 airlines
- 🔍 Auto detects anomalies (delays > 2 hours)
- 🤖 AI generates professional operations report
- 📈 Interactive Power BI dashboard

## 🛠️ Tech Stack
- Python (Pandas, OpenPyXL)
- Groq AI API (LLaMA 3.3)
- Microsoft Excel (Data Cleaning)
- Power BI (Dashboard)
- SQL (Data Storage)

## 📊 Key Results
- ✅ 173 flights analyzed
- 🚨 33 anomalies detected
- 📉 80.9% on-time performance
- ✈️ DEL-HYD worst route (7 delays)
- 🏆 Air India worst airline (14 delays)

## 📁 Project Structure
flight-data-automation/
├── data/
│   ├── raw/          ← original data
│   └── processed/    ← cleaned data
├── src/
│   ├── data_loader.py
│   ├── anomaly_detection.py
│   ├── report_generator.py
│   └── export_powerbi.py
├── reports/          ← AI generated reports
├── dashboards/       ← Power BI file
└── .env.example      ← API key template

## ⚙️ Setup
pip install pandas openpyxl groq python-dotenv

## 👤 Author
Pinjari Jaheer Khan
jaheerkhanpinjari@gmail.com
