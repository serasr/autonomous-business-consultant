import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def load_company_df(path_or_buffer) -> pd.DataFrame:
    df = pd.read_csv(path_or_buffer)
    # Basic cleaning
    for col in df.columns:
        if df[col].dtype == object and df[col].str.replace('-', '').str.replace('Q','').str.isnumeric().all():
            # leave quarter-like strings as-is
            pass
    return df

def compute_operational_kpis(df: pd.DataFrame) -> dict:
    df = df.copy()
    df['Gross_Profit'] = df['Revenue'] - df['COGS']
    df['Gross_Margin_%'] = (df['Gross_Profit'] / df['Revenue']).round(4) * 100
    df['CAC_approx'] = (df['Marketing_Spend'] / df['New_Customers']).replace([np.inf, -np.inf], np.nan).fillna(0).round(2)
    df['Net_Contribution'] = df['Gross_Profit'] - df['Operating_Expense']
    kpis = {
        'Revenue_last': float(df['Revenue'].iloc[-1]),
        'Gross_Margin_%_last': float(df['Gross_Margin_%'].iloc[-1]),
        'CAC_approx_last': float(df['CAC_approx'].iloc[-1]),
        'Net_Contribution_last': float(df['Net_Contribution'].iloc[-1]),
        'New_Customers_last': int(df['New_Customers'].iloc[-1]),
        'Churned_Customers_last': int(df['Churned_Customers'].iloc[-1]),
    }
    # Growth rates
    def growth(series):
        if len(series) < 2 or series.iloc[-2] == 0: 
            return 0.0
        return float((series.iloc[-1] - series.iloc[-2]) / abs(series.iloc[-2]) * 100.0)
    kpis.update({
        'Revenue_qoq_%': round(growth(df['Revenue']), 2),
        'Gross_Margin_qoq_pts': round(df['Gross_Margin_%'].iloc[-1] - df['Gross_Margin_%'].iloc[-2], 2) if len(df) > 1 else 0.0,
        'CAC_qoq_%': round(growth(df['CAC_approx']), 2),
        'Net_Contribution_qoq_%': round(growth(df['Net_Contribution']), 2),
        'New_Cust_qoq_%': round(growth(df['New_Customers']), 2),
        'Churn_qoq_%': round(growth(df['Churned_Customers']), 2),
    })
    return {'kpi_table': df.to_dict(orient='records'), 'kpi_summary': kpis}

def detect_anomalies(df: pd.DataFrame, cols=('Revenue','COGS','Operating_Expense','Marketing_Spend')) -> dict:
    df = df.copy()
    X = df[list(cols)].astype(float).values
    if len(df) < 4:
        return {'anomalies': []}
    iso = IsolationForest(n_estimators=200, contamination='auto', random_state=42)
    preds = iso.fit_predict(X)  # -1 = anomaly
    anomalies = []
    for i, p in enumerate(preds):
        if p == -1:
            anomalies.append({'index': int(i), 'Quarter': str(df['Quarter'].iloc[i])})
    return {'anomalies': anomalies}

def kpi_markdown(kpi_summary: dict) -> str:
    lines = [f"- **{k}**: {v}" for k,v in kpi_summary.items()]
    return "\n".join(lines)
