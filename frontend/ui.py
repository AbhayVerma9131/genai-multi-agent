import streamlit as st
import requests

API_URL = "YOUR_CLOUD_RUN_URL"

st.set_page_config(page_title="AI Assistant", layout="wide")

st.title("🤖 Multi-Agent Productivity Assistant")

query = st.text_area("Enter your task")

if st.button("Run"):
    res = requests.post(f"{API_URL}/chat", params={"query": query})
    data = res.json()

    st.subheader("🧠 Plan")
    st.write(data["plan"])

    st.subheader("⚡ Result")
    st.write(data["result"])
