# Autonomous Business Consultant  

**Autonomous Business Consultant** is an **Agentic AI system** that transforms raw company KPIs into actionable executive intelligence.  
It ingests performance data, computes insights, detects anomalies, and autonomously generates a **professional, visually rich PDF report** - ready for boardroom use.  

This project demonstrates your ability to build **end-to-end agentic AI solutions** combining data analytics, LLM reasoning, and business strategy generation.  

---

## Key Features  
- **Data-Driven Insights** - Computes operational KPIs like Revenue Growth, Gross Margin %, CAC, and Net Contribution.  
- **Autonomous Reasoning** - Uses an AI “crew” (Analyst → Strategist → Publisher) for narrative insight generation.  
- **Anomaly Detection** - Flags abnormal quarters using robust z-score logic.  
- **Executive-Grade PDF Reports** - Automatically generated reports with charts, KPIs, and strategic recommendations.  
- **Interactive Streamlit Dashboard** - Upload CSVs, run analysis, visualize metrics, and download polished reports.  
- **Modular Architecture** - Clean separation of data, logic, and presentation - extensible to real CrewAI agents or OpenAI APIs.  

---

## Architecture Overview  

```text
autonomous-business-consultant/
├── src/
│   ├── streamlit_app.py          # Streamlit web dashboard
│   ├── run.py                    # CLI interface for quick report generation
│   ├── crew.py                   # Agent orchestration layer (stub for CrewAI)
│   ├── tools/
│   │   └── data_tools.py         # Data loading, KPI computation, anomaly detection
│   └── report/
│       └── report_generator.py   # Professional PDF report generator
│
├── data/
│   └── sample_company.csv        # Example KPI dataset
├── assets/
│   └── logo.png (optional)       # Custom logo for report header
├── outputs/                      # Generated charts & reports
├── requirements.txt
├── .env.example
└── README.md
```

---

## Installation  

### Clone the Repository  
```bash
git clone https://github.com/<your-username>/autonomous-business-consultant.git
cd autonomous-business-consultant
```

### Create and Activate a Virtual Environment  
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### Install Dependencies  
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables  
```bash
cp .env.example .env
# Add your OpenAI API key if you plan to use LLMs
OPENAI_API_KEY=sk-...
```

---

## Sample Data Format  

**`data/sample_company.csv`**
```csv
Quarter,Revenue,Gross_Profit,Gross_Margin_%,CAC_approx,Net_Contribution,New_Customers,Churned_Customers
2024-Q1,590000,270000,45.76,261.82,130000,275,38
2024-Q2,610000,285000,46.10,240.20,142000,310,35
2024-Q3,640000,300000,46.50,235.10,150000,325,33
2024-Q4,670000,320000,47.20,230.50,166000,340,31
```

---

## Usage  

### Run the Streamlit App  
```bash
streamlit run src/streamlit_app.py
```
**Features:**  
- Upload any CSV with KPIs following the sample structure.  
- Visualize revenue, margin, and CAC trends.  
- Run autonomous analysis and generate an executive report.  
- Preview and download PDF reports directly in the browser.  

### Generate Report via CLI  
```bash
python src/run.py --file data/sample_company.csv
```
Outputs:  
- `outputs/report.pdf` – detailed executive report  
- `outputs/charts/` – visual KPI trend charts  

---

## Example Output  

**Executive Report (Preview)**  
- Front page with company summary and date  
- KPI table with quarter-over-quarter deltas  
- Visual KPI dashboard (auto-generated charts)  
- Strategic recommendations & insights  

*(Report uses Unicode-safe DejaVu fonts, ensuring smooth rendering on any OS.)*  

---

## How It Works  

| Component | Description |
|------------|-------------|
| **Data Tools** | Loads CSVs, computes KPIs, and detects anomalies |
| **Crew Layer** | A stub multi-agent system producing insights (can be replaced with CrewAI) |
| **Report Generator** | Renders an executive-style PDF with analytics visuals |
| **Streamlit UI** | Provides an intuitive interface for non-technical users |

You can replace the stub crew with actual **CrewAI agents** (Analyst, Strategist, Publisher) to make it fully agentic.  

---

## Deployment  

Deploy on **Streamlit Cloud**, **Heroku**, or **Render**:  
```bash
streamlit run src/streamlit_app.py
```
Then connect your GitHub repository to Streamlit Cloud and deploy in one click.

---

## Tech Stack  
- **Python 3.10+**  
- **Streamlit** - Frontend & interactivity  
- **pandas / NumPy** - Data processing  
- **Matplotlib** - Chart generation  
- **FPDF2** - PDF creation  
- **dotenv** - Environment config  
- **CrewAI** - Agentic orchestration 

---

## Ideal For  
- Showcasing **Agentic AI + Business Analytics** capability.  
- Demonstrating **end-to-end AI system design** (data → insight → report).  

---


