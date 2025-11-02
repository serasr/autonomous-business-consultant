from crewai import Agent
import os

DEFAULT_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

def build_data_analyst():
    return Agent(
        role="Data Analyst",
        goal=(
            "Transform raw company metrics into clear KPI trends and risks. "
            "Be precise, conservative, and business-friendly."
        ),
        backstory=(
            "You are a senior analytics consultant who blends deterministic analysis with interpretability. "
            "You focus on clarity and executive usefulness."
        ),
        model=DEFAULT_MODEL,
        verbose=True
    )

def build_business_strategist():
    return Agent(
        role="Business Strategist",
        goal=(
            "Synthesize analytics into 3-5 actionable insights with impact, owners, and measurable outcomes."
        ),
        backstory=(
            "Ex-EY/Deloitte strategist with a knack for crisp narratives and practical next steps."
        ),
        model=DEFAULT_MODEL,
        verbose=True
    )

def build_executive_consultant():
    return Agent(
        role="Executive Consultant",
        goal="Produce an executive-ready report that a CFO/COO can act on immediately.",
        backstory=(
            "You write concise, board-facing summaries and prioritize impact and feasibility."
        ),
        model=DEFAULT_MODEL,
        verbose=True
    )
