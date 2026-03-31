import streamlit as st
import pandas as pd
import random
import time
import math
import requests
import sqlite3
from sklearn.tree import DecisionTreeClassifier

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="VeriGuard AI 🚨", layout="centered")

# ------------------ CUSTOM UI ------------------
st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: white;
}
.block-container {
    max-width: 400px;
    margin: auto;
}
.card {
    background-color: #1c1f26;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 15px;
}
.stButton>button {
    width: 100%;
    border-radius: 10px;
    background-color: #00FFCC;
    color: black;
}
</style>
""", unsafe_allow_html=True)

st.markdown("## 🚨 VeriGuard AI")
st.caption("AI Emergency Assistant")
st.success("🟢 System Active")

# ------------------ DATABASE ------------------
conn = sqlite3.connect("emergency.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cases (
    name TEXT,
    location TEXT,
    symptom TEXT,
    severity TEXT,
    hospital TEXT
)
""")
conn.commit()

# ------------------ INPUT ------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

name = st