import streamlit as st
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Secure Login Demo",
    layout="centered"
)

# ---------------- CREDENTIALS ----------------
CREDENTIALS = {
    "naveen": "0067",
    "aadhish": "0069"
}

# ---------------- SESSION STATE (SAFE INIT) ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "blocked" not in st.session_state:
    st.session_state.blocked = False

# ---------------- RESET BLOCK ON FRESH LOAD ----------------
if "fresh_load" not in st.session_state:
    st.session_state.blocked = False
    st.session_state.fresh_load = True

# ---------------- TITLE ----------------
st.markdown("## 🔐 Secure Login Demo")
st.caption(
    "This page demonstrates how brute-force attacks are detected and blocked "
    "using behavior-based security mechanisms."
)

# ---------------- LOGIN FORM ----------------
username = st.text_input("Username")

col1, col2 = st.columns([5, 1])

with col1:
    password = st.text_input("Password (4 digits)", type="password")

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🐞"):
        # Bot detected instantly
        st.session_state.blocked = True

st.caption("🐞 Click the bug icon to simulate a brute-force attack")

# ---------------- LOGIN BUTTON ----------------
if st.button("Login"):

    # If bot detected via bug icon
    if st.session_state.blocked:
        st.error(
            "🚫 404 ERROR\n\n"
            "Suspicious automated activity detected.\n"
            "Access to this website has been blocked."
        )

    # Manual human login (correct credentials)
    elif username in CREDENTIALS and password == CREDENTIALS[username]:
        st.session_state.logged_in = True

    else:
        st.error("❌ Invalid username or password")

# ---------------- ACCESS GRANTED ----------------
if st.session_state.logged_in:
    st.success("✅ Access Granted (Human Verified)")

    st.markdown("### 📄 Brute Force Attack – Awareness Resources")

    # ---- PDF ----
    pdf_path = os.path.join(os.path.dirname(__file__), "brute_force.pdf")

    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            pdf_data = f.read()

        st.download_button(
            label="📥 Download Brute Force Attack PDF",
            data=pdf_data,
            file_name="brute_force_attack_awareness.pdf",
            mime="application/pdf"
        )
    else:
        st.info("PDF will be added later.")

    # ---- ARTICLE ----
    st.markdown(
        "🔗 **Read our article:** "
        "[Brute Force Attack – Explained]"
        "(https://bruteforce-attack-explained.blogspot.com/2026/01/brute-force-attack.html)"
    )

    st.markdown("---")
    st.caption("Team THUNDER (Naveen, Aadhish) • Educational demo only")
