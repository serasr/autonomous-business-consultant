import streamlit as st
import pandas as pd
import base64
import os
from io import BytesIO
from dotenv import load_dotenv

from tools.data_tools import load_company_df, compute_operational_kpis, detect_anomalies
from crew import build_crew
from report.report_generator import render_pdf, create_kpi_charts

load_dotenv()
st.set_page_config(page_title="Autonomous Business Consultant Crew", layout="wide")
st.title("🤖 Autonomous Business Consultant")

# Sidebar Information
st.sidebar.title("Configuration")
st.sidebar.write("Upload a company KPI CSV to generate an executive business report.")
st.sidebar.write("You can preview analytics, insights, and recommendations before downloading the final PDF.")

uploaded = st.sidebar.file_uploader("Upload KPI CSV", type=["csv"])

if uploaded:
    df = load_company_df(uploaded)
    st.subheader("Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

    if st.sidebar.button("Run Autonomous Analysis"):
        with st.spinner("Agents collaborating to prepare your report..."):
            kpi = compute_operational_kpis(df)
            anom = detect_anomalies(df)
            crew = build_crew(kpi['kpi_summary'], anom['anomalies'])
            result = crew.kickoff()
            exec_text = str(result)

            pdf_path = "outputs/report.pdf"
            os.makedirs("outputs", exist_ok=True)
            render_pdf(
                pd.DataFrame(kpi["kpi_table"]),  # <- dataframe for graphs
                kpi["kpi_summary"],              # <- dictionary for KPIs
                exec_text[:600],                 # <- insights / summary
                exec_text,                       # <- recommendations
                pdf_path                         # <- output path
            )


        st.success("Report successfully generated!")

        # ---- Section: Interactive Dashboard ----
        st.header("KPI Dashboard")

        st.markdown("Below are the core metrics computed by the Data Analyst Agent.")
        kpi_df = pd.DataFrame(kpi["kpi_table"])
        st.dataframe(kpi_df, use_container_width=True)

        st.markdown("### Trend Visualizations")
        chart_files = create_kpi_charts(kpi_df)
        cols = st.columns(2)
        for i, ch in enumerate(chart_files):
            with cols[i % 2]:
                st.image(ch, caption=os.path.basename(ch), use_container_width=True)

        # ---- Section: Report Preview ----
        st.header("Executive Report Preview")

        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
            base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")
            pdf_display = (
                f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" '
                f'style="border:none;"></iframe>'
            )
            st.markdown(pdf_display, unsafe_allow_html=True)

            st.download_button(
                label="Download Report (PDF)",
                data=pdf_bytes,
                file_name="Business_Consultant_Report.pdf",
                mime="application/pdf"
            )
