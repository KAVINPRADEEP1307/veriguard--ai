import streamlit as st
import pandas as pd
import random
from sklearn.tree import DecisionTreeClassifier

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="VeriGuard AI 🚨", layout="wide")

# ------------------ CUSTOM DARK UI ------------------
st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: white;
}
h1, h2, h3 {
    color: #00FFCC;
}
</style>
""", unsafe_allow_html=True)

st.title("🚨 VeriGuard AI - Emergency Response System")

# ------------------ SIDEBAR INPUT ------------------
st.sidebar.header("📥 Enter Emergency Details")

name = st.sidebar.text_input("Name")
location = st.sidebar.text_input("Location")

symptom = st.sidebar.selectbox(
    "Select Symptom",
    ["Chest Pain", "Accident", "Fever", "Headache", "Minor Injury"]
)

# ------------------ TRAIN SIMPLE ML MODEL ------------------
# Sample dataset
X = [
    [1,0,0],  # Chest Pain
    [1,1,0],  # Accident
    [0,1,0],  # Fever
    [0,0,1],  # Headache
    [0,0,1]   # Minor
]

y = ["Critical", "Critical", "Moderate", "Low", "Low"]

model = DecisionTreeClassifier()
model.fit(X, y)

def encode(symptom):
    if symptom == "Chest Pain":
        return [1,0,0]
    elif symptom == "Accident":
        return [1,1,0]
    elif symptom == "Fever":
        return [0,1,0]
    else:
        return [0,0,1]

# ------------------ MAIN BUTTON ------------------
if st.sidebar.button("🚀 Analyze"):

    input_data = [encode(symptom)]
    severity = model.predict(input_data)[0]

    st.subheader(f"🧠 AI Predicted Severity: {severity}")

    # ------------------ SMART RESPONSE ------------------
    if severity == "Critical":
        st.error("🚑 Ambulance Dispatched Immediately!")
        hospital = "Apollo Hospital"
    elif severity == "Moderate":
        st.warning("🏥 Visit Nearby Hospital")
        hospital = "Government Hospital"
    else:
        st.success("🙂 Low Risk - Home Care Suggested")
        hospital = "Home Care"

    st.write(f"📍 Assigned Resource: {hospital}")

    # ------------------ MAP ------------------
    st.subheader("📍 Live Location Tracking")

    lat = 13.0827 + random.uniform(-0.01, 0.01)
    lon = 80.2707 + random.uniform(-0.01, 0.01)

    df = pd.DataFrame({"lat":[lat], "lon":[lon]})
    st.map(df)

    # ------------------ VOLUNTEER MATCHING ------------------
    st.subheader("🧑‍🤝‍🧑 Volunteer Matching")

    volunteers = ["Ravi", "Priya", "Arun", "Divya"]
    st.info(f"👤 Assigned Volunteer: {random.choice(volunteers)}")

    # ------------------ DASHBOARD ------------------
    st.subheader("📊 Live Dashboard")

    chart_data = pd.DataFrame({
        "Severity": ["Critical", "Moderate", "Low"],
        "Cases": [random.randint(5,15), random.randint(10,20), random.randint(15,30)]
    })

    st.bar_chart(chart_data.set_index("Severity"))

    st.success("✅ Emergency handled successfully!")