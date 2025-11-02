import argparse, os, json
from dotenv import load_dotenv
from tools.data_tools import load_company_df, compute_operational_kpis, detect_anomalies
from crew import build_crew
from report.report_generator import render_pdf, render_email_md

def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, help='Path to CSV file with company KPIs')
    parser.add_argument('--outdir', default='outputs', help='Where to save outputs')
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    df = load_company_df(args.file)
    kpi = compute_operational_kpis(df)
    anom = detect_anomalies(df)
    kpi_summary = kpi['kpi_summary']

    crew = build_crew(kpi_summary, anom['anomalies'])
    result = crew.kickoff()

    # result holds last task output; we also want step outputs
    # If your CrewAI version supports, result.raw or similar; fall back to strings
    exec_text = str(result)

    # Split executive text into summary and recommendations heuristically
    if "Recommendations" in exec_text:
        parts = exec_text.split("Recommendations", 1)
        exec_summary = parts[0].strip()
        recommendations = "Recommendations" + parts[1]
    else:
        exec_summary = exec_text
        recommendations = "1) Prioritize revenue and margin. 2) Reduce CAC. 3) Address churn."

    pdf_path = os.path.join(args.outdir, 'report.pdf')
    render_pdf(kpi_summary, exec_summary, recommendations, pdf_path)

    email_md = render_email_md(kpi_summary, exec_summary, recommendations)
    with open(os.path.join(args.outdir, 'summary_email.md'), 'w') as f:
        f.write(email_md)

    print(f"✅ Done. Wrote:\n- {pdf_path}\n- {os.path.join(args.outdir,'summary_email.md')}")

if __name__ == '__main__':
    main()
