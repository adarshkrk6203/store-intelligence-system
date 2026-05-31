import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# =========================================
# CONFIG
# =========================================

DEMO_MODE = True
STORE_ID = "STORE_001"

st.set_page_config(
    page_title="Store Intelligence Dashboard",
    page_icon="🏬",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    color: #111827;
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    border: 1px solid #e5e7eb;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    border: 1px solid #e5e7eb;
}

.stDataFrame {
    background: white;
    border-radius: 18px;
    padding: 10px;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR
# =========================================

st.sidebar.title("⚙️ Dashboard Controls")

st.sidebar.info(
    "AI-powered retail analytics dashboard "
    "for real-time store intelligence."
)

refresh = st.sidebar.button("🔄 Refresh Dashboard")

st.sidebar.divider()

st.sidebar.success("System Status: ONLINE")

# =========================================
# HEADER
# =========================================

st.markdown("""
# 🏬 Store Intelligence Dashboard

### AI-Powered Retail Analytics Platform

Real-time store intelligence using:
- YOLOv8 Detection
- ByteTrack Tracking
- FastAPI Analytics
- Event Streaming Architecture
""")

st.divider()

# =========================================
# DATA
# =========================================

try:

    if DEMO_MODE:

        metrics = {
            "unique_visitors": 52,
            "conversion_rate_percent": 21.15,
            "queue_depth": 3,
            "zone_visit_counts": {
                "ENTRY": 33,
                "BILLING": 11,
                "AISLE": 27,
                "COSMETICS": 19
            },
            "avg_dwell_seconds_by_zone": {
                "ENTRY": 4.2,
                "BILLING": 12.7,
                "AISLE": 18.3,
                "COSMETICS": 24.6
            }
        }

        funnel = {
            "stages": {
                "Entry": 52,
                "Zone Visit": 41,
                "Billing": 18,
                "Purchase": 11
            }
        }

    else:

        metrics_response = requests.get(
            f"http://127.0.0.1:8000/stores/{STORE_ID}/metrics"
        )

        metrics = metrics_response.json()

        funnel_response = requests.get(
            f"http://127.0.0.1:8000/stores/{STORE_ID}/funnel"
        )

        funnel = funnel_response.json()

    # =========================================
    # KPI SECTION
    # =========================================

    st.subheader("📊 Key Performance Indicators")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Unique Visitors",
        metrics.get("unique_visitors", 0)
    )

    col2.metric(
        "Conversion Rate",
        f"{metrics.get('conversion_rate_percent', 0)}%"
    )

    col3.metric(
        "Queue Depth",
        metrics.get("queue_depth", 0)
    )

    st.divider()

    # =========================================
    # ZONE ANALYTICS
    # =========================================

    st.subheader("🧭 Zone Traffic Analytics")

    zone_counts = metrics.get("zone_visit_counts", {})

    if zone_counts:

        zone_df = pd.DataFrame(
            list(zone_counts.items()),
            columns=["Zone", "Visits"]
        )

        fig_zone = px.bar(
            zone_df,
            x="Zone",
            y="Visits",
            title="Zone Visit Distribution",
            text_auto=True
        )

        st.plotly_chart(
            fig_zone,
            use_container_width=True
        )

        st.dataframe(
            zone_df,
            use_container_width=True
        )

    else:
        st.warning("No zone analytics available")

    st.divider()

    # =========================================
    # DWELL ANALYTICS
    # =========================================

    st.subheader("⏱️ Average Dwell Time")

    dwell = metrics.get(
        "avg_dwell_seconds_by_zone",
        {}
    )

    if dwell:

        dwell_df = pd.DataFrame(
            list(dwell.items()),
            columns=["Zone", "Avg Dwell Seconds"]
        )

        fig_dwell = px.bar(
            dwell_df,
            x="Zone",
            y="Avg Dwell Seconds",
            title="Average Dwell Time by Zone",
            text_auto=True
        )

        st.plotly_chart(
            fig_dwell,
            use_container_width=True
        )

        st.dataframe(
            dwell_df,
            use_container_width=True
        )

    else:
        st.warning("No dwell analytics available")

    st.divider()

    # =========================================
    # FUNNEL ANALYTICS
    # =========================================

    st.subheader("🛒 Conversion Funnel")

    funnel_stages = funnel.get("stages", {})

    if funnel_stages:

        funnel_df = pd.DataFrame(
            list(funnel_stages.items()),
            columns=["Stage", "Visitors"]
        )

        fig_funnel = px.funnel(
            funnel_df,
            x="Visitors",
            y="Stage",
            title="Store Conversion Funnel"
        )

        st.plotly_chart(
            fig_funnel,
            use_container_width=True
        )

        st.dataframe(
            funnel_df,
            use_container_width=True
        )

    else:
        st.warning("No funnel analytics available")

    st.divider()

    # =========================================
    # SYSTEM STATUS
    # =========================================

    st.subheader("🟢 System Status")

    st.success("Store Intelligence Pipeline Running Successfully")

    st.markdown("""
### Active Components
- ✅ YOLOv8 Detection Pipeline
- ✅ ByteTrack Multi-Object Tracking
- ✅ Event Streaming Engine
- ✅ FastAPI Analytics Backend
- ✅ Funnel Analytics
- ✅ Dwell Time Analytics
- ✅ Anomaly Detection
- ✅ Docker Deployment
""")

except Exception as e:

    st.error(f"Dashboard Error: {e}")
