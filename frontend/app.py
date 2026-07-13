import requests
import streamlit as st
import time

API_URL = "https://thinkforge-ai.onrender.com//api/research"

st.set_page_config(
    page_title="ThinkForge AI",
    page_icon="🧠",
    layout="wide",
)

# ---------- CSS ----------
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ---------- Sidebar ----------
with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/4712/4712027.png",
        width=90,
    )

    st.title("ThinkForge AI")

    st.success("Backend Online")

    st.markdown("---")

    st.markdown("### Sample Topics")

    if st.button("AI in Healthcare"):
        st.session_state.topic = "Artificial Intelligence in Healthcare"

    if st.button("Quantum Computing"):
        st.session_state.topic = "Quantum Computing"

    if st.button("Climate Change"):
        st.session_state.topic = "Climate Change"

    if st.button("Cyber Security"):
        st.session_state.topic = "Cyber Security"

# ---------- Header ----------

st.markdown(
"""
<h1 style='text-align:center;'>
🧠 ThinkForge AI
</h1>

<p style='text-align:center;font-size:18px'>
Autonomous Research Intelligence System
</p>
""",
unsafe_allow_html=True,
)

query = st.text_area(
    "Research Topic",
    value=st.session_state.get("topic",""),
    height=120,
)

if st.button("🚀 Generate Research", use_container_width=True):

    if query == "":
        st.warning("Enter a topic.")
        st.stop()

    progress = st.progress(0)

    status = st.empty()

    agents = [
        "Planner Agent",
        "Research Agent",
        "Analysis Agent",
        "Writer Agent",
        "Reviewer Agent",
    ]

    for i,agent in enumerate(agents):

        status.info(f"Running {agent}")

        progress.progress((i+1)/len(agents))

        time.sleep(0.5)

    with st.spinner("Generating Report..."):

        response = requests.post(
            API_URL,
            json={"query":query},
            timeout=300
        )

    if response.status_code == 200:

        data = response.json()

        st.success("Research Completed")

        tab1,tab2,tab3,tab4 = st.tabs(
            [
                "📋 Plan",
                "🔍 Research",
                "📊 Analysis",
                "📄 Report",
            ]
        )

        with tab1:
            st.markdown(data["plan"])

        with tab2:
            st.markdown(data["search_results"])

        with tab3:
            st.markdown(data["analysis"])

        with tab4:
            st.markdown(data["report"])

        st.download_button(
            "⬇ Download Report",
            data["report"],
            "report.md",
        )

    else:

        st.error(response.text)