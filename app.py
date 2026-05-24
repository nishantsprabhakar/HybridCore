import streamlit as st

st.set_page_config(
    page_title="HybridCore — Hybrid Compute Simulator",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; height: 0; }
    .block-container { padding: 0 !important; max-width: 100% !important; margin: 0 !important; }
    [data-testid="stMain"] { padding: 0 !important; overflow: hidden !important; }
    [data-testid="stMainBlockContainer"] { padding: 0 !important; }
    [data-testid="stAppViewContainer"] { overflow: hidden !important; }
    iframe { border: none; width: 100% !important; height: 100vh !important; display: block; }
</style>
""", unsafe_allow_html=True)

with open("hybrid-compute-simulator.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=900, scrolling=True)
