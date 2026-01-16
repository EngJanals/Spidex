import streamlit as st
import pandas as pd
import numpy as np

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Crisis Spiders | Digital Twin",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# FUTURISTIC UI STYLE
# --------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b0f1a, #12182b);
    color: #ffffff;
}
.card {
    background: rgba(255,255,255,0.05);
    border: 1px solid #00ffd5;
    border-radius: 16px;
    padding: 20px;
}
h1, h2, h3 {
    color: #00ffd5;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:
    st.markdown("## 🕷️ CRISIS SPIDERS")
    st.markdown("### Digital Twin Control Room")
    st.markdown("---")

    page = st.radio(
        "Navigation",
        ["📊 Dashboard", "👥 Team"]
    )

    st.markdown("---")
    st.markdown("System Status: **ONLINE**")

# --------------------------------------------------
# DIGITAL TWIN STATE (SIMULATED)
# --------------------------------------------------
digital_twin = {
    "Spidex": {"battery": 0.84, "signal": 120, "health": 0.95},
    "Geopider": {"battery": 0.92, "signal": 45, "health": 0.98},
    "Neopider": {"battery": 0.78, "signal": 80, "health": 0.91},
}

# ==================================================
# DASHBOARD PAGE
# ==================================================
if page == "📊 Dashboard":

    selected_robot = st.selectbox(
        "Select Spider",
        ["Spidex", "Geopider", "Neopider"]
    )

    twin = digital_twin[selected_robot]

    st.title("🧠 Digital Twin & AI Monitoring Dashboard")
    st.markdown(f"### Active Twin: **{selected_robot}**")

    # ---------------- TOP METRICS ----------------
    m1, m2, m3, m4 = st.columns(4)

    m1.metric("Battery", f"{int(twin['battery']*100)}%")
    m2.metric("Signal Latency", f"{twin['signal']} ms")
    m3.metric("System Health", f"{int(twin['health']*100)}%")
    m4.metric("AI Status", "Stable")

    # ---------------- MAIN GRID ----------------
    left, center, right = st.columns([1.2, 2.6, 1.2])

    # AI ANALYTICS
    with left:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🤖 AI Analytics")
        st.metric("Inference Rate", "42 FPS")
        st.metric("Anomaly Score", "0.03")
        st.metric("Prediction Confidence", "97%")
        st.markdown("</div>", unsafe_allow_html=True)

    # DIGITAL TWIN
    with center:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🌐 Digital Twin Core")

        st.image(
            "https://via.placeholder.com/900x450/0b0f1a/00ffd5?text=Digital+Twin+Simulation",
            use_container_width=True
        )

        st.markdown("""
        **Simulation Engine:** Unity / Gazebo  
        **Control Layer:** ROS  
        **Visualization:** Streamlit  
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # ROBOT TELEMETRY
    with right:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 📡 Robot Telemetry")
        st.write("Battery Level")
        st.progress(twin["battery"])
        st.write("System Health")
        st.progress(twin["health"])
        st.write(f"Signal Latency: {twin['signal']} ms")
        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- AI CHARTS ----------------
    st.markdown("## 📊 AI & Sensor Trends")

    df = pd.DataFrame({
        "AI Confidence": np.random.normal(0.6, 0.05, 50),
        "Sensor Fusion Score": np.random.normal(0.4, 0.04, 50)
    })

    st.line_chart(df)

# ==================================================
# TEAM PAGE
# ==================================================
else:
    st.title("👥 Crisis Spiders Team")
    st.markdown("### Development & Engineering Unit")

    team_list = [
        ("Manar Mohammed Al-Tuwairqi", "s44208057@students.tu.edu.sa"),
        ("Jana Mohammed Al-Sufyani", "s44251378@students.tu.edu.sa"),
        ("Abrar Mohammed Al-Buqami", "s44204498@students.tu.edu.sa"),
        ("Shehana Sulaiman Al-Juaid", "s44201849@students.tu.edu.sa"),
        ("Sumayah Abdullah Al-Malki", "s44201735@students.tu.edu.sa"),
        ("Huda Mohammed Al-Buqami", "s44200812@students.tu.edu.sa"),
        ("Dareen Aali Al-Ghamdi", "s44204996@students.tu.edu.sa"),
        ("Wasan Fayez Al-Thubaiti", "s44201077@students.tu.edu.sa"),
    ]

    col1, col2 = st.columns(2)

    for i, (name, email) in enumerate(team_list):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class='card'>
                <h4 style='margin:0;'>{name}</h4>
                <p style='margin:0; color:#bbb; font-size:0.85em;'>{email}</p>
            </div>
            """, unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.markdown("**Crisis Spiders | Digital Twin Research Platform**")
