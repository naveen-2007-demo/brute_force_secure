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

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "show_404" not in st.session_state:
    st.session_state.show_404 = False

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

    # 🐞 BUG ICON → SHOW 404 WARNING ONLY
    if st.button("🐞"):
        st.session_state.show_404 = True

st.caption("🐞 Click the bug icon to simulate a brute-force attack")

# ---------------- SHOW 404 WARNING (TEMPORARY) ----------------
if st.session_state.show_404:
    st.error(
        "🚫 404 ERROR\n\n"
        "Suspicious automated activity detected.\n"
        "Access to this website has been blocked."
    )
    # Auto-reset after showing warning
    st.session_state.show_404 = False

# ---------------- LOGIN BUTTON (HUMAN LOGIN) ----------------
if st.button("Login"):
    if username in CREDENTIALS and password == CREDENTIALS[username]:
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
