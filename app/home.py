import streamlit as st

st.set_page_config(page_title="RL Rank Perfomance Estimator", page_icon="🏎️", layout="wide")

st.markdown("<h1 style='text-align: center;'>RL Rank Perfomance Estimator</h1>", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center; font-size: 18px;'>
A machine learning project that predicts what rank a player performs like based on their Rocket League replay stats.
</p>
""", unsafe_allow_html=True)

st.divider()

st.markdown("""
<div style='text-align: center; max-width: 700px; margin: 0 auto;'>

<h3>The Research Question</h3>

<p>What stats actually separate Rocket League ranks? Instead of looking at wins or MMR,
this project uses player-level replay data — boost usage, movement, aerial play, positioning,
and more — to predict what broad rank a player performed like in a given game.</p>

<h3>How It Works</h3>

<p>Replay data was collected from the Ballchasing API across 1,500 ranked standard 3v3 matches,
producing 9,000 player rows balanced across Gold through Grand Champion. A Logistic Regression
model trained on 83 gameplay features predicts one of five broad rank groups with 58.3% accuracy.
Nearly 90% of predictions land within one rank group of the correct answer.</p>

<h3>Pages</h3>

</div>
""", unsafe_allow_html=True)

_, c1, c2, _ = st.columns([3, 1, 1, 3])
with c1:
    st.page_link("pages/1_Predictor.py", label="Rank Predictor", icon="🔮", use_container_width=True)
with c2:
    st.page_link("pages/2_Explorer.py", label="Rank Explorer", icon="📊", use_container_width=True)

st.markdown("""
<div style='text-align: center; max-width: 700px; margin: 0 auto;'>

<h3>Model Results</h3>

</div>
""", unsafe_allow_html=True)

_, m1, m2, m3, _ = st.columns([2, 1, 1, 1, 2])
m1.metric("Broad Rank Accuracy", "58.3%", help="Logistic Regression on 5 rank groups")
m2.metric("Within 1 Tier (Exact)", "50.0%", help="Random Forest exact-tier model")
m3.metric("Player Rows", "9,000", help="Balanced across 15 rank tiers")

st.markdown("""
<div style='text-align: center; max-width: 700px; margin: 0 auto;'>

<h3>Data</h3>

<p>All replay data is sourced from the <a href="https://ballchasing.com" target="_blank">Ballchasing API</a>,
covering Gold through Grand Champion in ranked standard 3v3.</p>

<hr>

<p>Built by Abdul · <a href="https://github.com/codingdadir/RLRankPredictor" target="_blank">GitHub</a></p>

</div>
""", unsafe_allow_html=True)