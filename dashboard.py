import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

st.set_page_config(page_title="Warm Lead Dashboard", layout="centered")

st.title("Warm Lead Dashboard")
st.write("Showing the latest 10 qualified leads from Google Sheets")

# Connect to Google Sheets
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
creds = Credentials.from_service_account_file("credentials.json", scopes=scope)
client = gspread.authorize(creds)
sheet = client.open("Warm Leads").sheet1

# Load data
data = sheet.get_all_records()
df = pd.DataFrame(data)

if len(df) > 0:
    df = df.sort_values(by="Timestamp", ascending=False).head(10)
    st.dataframe(df, use_container_width=True)
else:
    st.warning("No leads found yet!")

st.markdown("---")
st.caption("Built by Mohamed Taha ")