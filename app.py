import streamlit as st
from snowflake.snowpark import Session
import pandas as pd

st.set_page_config(page_title="Snowflake Streamlit App", layout="centered")
st.title("📊 Project 7: Snowflake + Streamlit App")
st.markdown("This app connects to Snowflake using **Snowpark for Python** and displays session details for the user `RASHMI`.")

# Define Snowflake connection configuration
connection_parameters = {
    "account": "lha05326.east-us-2.azure",  # ✅ Replace only if your account locator changes
    "user": "RASHMI",
    "password": "rashmi",  # ⚠️ For demo purposes only; don't hardcode in production
    "role": "ACCOUNTADMIN",
    "warehouse": "PROJECT7_WH",
    "database": "PROJECT7_DB",
    "schema": "PUBLIC"
}

try:
    # Create session
    session = Session.builder.configs(connection_parameters).create()

    # Execute a test query
    df = session.sql("SELECT CURRENT_DATE(), CURRENT_USER(), CURRENT_ROLE()").to_pandas()

    st.success("✅ Connected to Snowflake successfully!")
    st.subheader("🔍 Session Info")
    st.dataframe(df)

except Exception as e:
    st.error("❌ Failed to connect to Snowflake:")
    st.exception(e)
