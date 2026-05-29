import streamlit as st
import requests
import pandas as pd
import time

st.set_page_config(
    page_title="Store Intelligence Dashboard",
    layout="wide"
)

st.title("🏬 Store Intelligence Dashboard")

# Auto refresh
refresh_button = st.button("Refresh Metrics")

try:

    # Get metrics from API
    response = requests.get("http://127.0.0.1:8000/metrics")

    metrics = response.json()

    # Top metrics
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Events",
        metrics["total_events"]
    )

    col2.metric(
        "Total Entries",
        metrics["total_entries"]
    )

    col3.metric(
        "Unique Visitors",
        metrics["unique_visitors"]
    )

    st.subheader("Zone Analytics")

    zone_counts = metrics["zone_counts"]

    if zone_counts:

        df = pd.DataFrame(
            list(zone_counts.items()),
            columns=["Zone", "Count"]
        )

        st.bar_chart(
            df.set_index("Zone")
        )

        st.dataframe(df)

    else:
        st.warning("No zone data available")

except Exception as e:

    st.error(f"Error connecting to backend: {e}")