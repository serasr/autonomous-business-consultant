from crewai import Task
from textwrap import dedent

def task_analyze_kpis(agent, kpi_summary, anomalies):
    return Task(
        description=dedent(f'''
        Analyze the following computed KPIs and anomalies and draft a crisp analytical narrative.
        KPIs: {kpi_summary}
        Anomalies (IsolationForest): {anomalies}
        Deliver 6-10 sentences highlighting: growth, margin movement, CAC dynamics, churn risk, and any suspicious spikes.
        '''),
        agent=agent,
        expected_output="Concise analytical narrative (<= 180 words)"
    )

def task_generate_insights(agent, analysis_text):
    return Task(
        description=dedent(f'''
        Turn this analysis into 3-5 **business insights** with impact, risk, and rationale. 
        Analysis: {analysis_text}
        Use bullet points with **bold** headers and keep it under 160 words.
        '''),
        agent=agent,
        expected_output="3-5 bullet insights, <160 words"
    )

def task_exec_report(agent, insights_text, kpi_summary):
    return Task(
        description=dedent(f'''
        Draft the final **Executive Summary** and **Top 5 Recommendations**.
        Provide:
        1) Executive Summary (<=150 words) focused on what happened and why.
        2) Recommendations (5 bullets): owner, action, expected impact, and a simple KPI to track.
        Context KPIs: {kpi_summary}
        Keep language board-ready and precise.
        '''),
        agent=agent,
        expected_output="Executive summary + 5 recommendations"
    )
