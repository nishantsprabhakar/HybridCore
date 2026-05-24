import streamlit as st

st.set_page_config(
    page_title="HybridCore — Hybrid Compute Simulator",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove default Streamlit chrome
st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    iframe { border: none; }
</style>
""", unsafe_allow_html=True)

with open("hybrid-compute-simulator.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=900, scrolling=True)
