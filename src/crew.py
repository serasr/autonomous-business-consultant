import os
from crewai import Crew, Process
from agents import build_data_analyst, build_business_strategist, build_executive_consultant
from tasks import task_analyze_kpis, task_generate_insights, task_exec_report

def build_crew(kpi_summary, anomalies):
    analyst = build_data_analyst()
    strategist = build_business_strategist()
    executive = build_executive_consultant()

    t1 = task_analyze_kpis(analyst, kpi_summary, anomalies)
    t2 = task_generate_insights(strategist, analysis_text="{{t1.output}}")
    t3 = task_exec_report(executive, insights_text="{{t2.output}}", kpi_summary=kpi_summary)

    crew = Crew(
        agents=[analyst, strategist, executive],
        tasks=[t1, t2, t3],
        process=Process.sequential,
        verbose=True
    )
    return crew
