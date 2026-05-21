# Rocket League Performance Estimator

A machine learning project that predicts what rank a player performed like based on their Rocket League replay stats.

Paste a Ballchasing replay URL, pick your player, and the app tells you what broad rank your gameplay looked like in that game.

**[Live App](https://rrlperformanceestimator.streamlit.app/)**

---

## The Question

MMR tells you what rank you are. Replay stats tell you how you actually played. This project asks:

> What stats actually separate Rocket League ranks?

The answer based on the data: aerial time, speed, boost efficiency, and positioning matter far more than goals, assists, or score.

---

## How It Works

Replay data was collected from the Ballchasing API across 1,500 ranked standard 3v3 matches, producing 9,000 player rows balanced evenly across Gold through Grand Champion. Each replay was validated to filter out forfeits, blowouts, missing rank data, and uneven lobbies before extracting player stats.

Two models were trained and compared:

| Model | Task | Accuracy |
|---|---|---|
| Random Forest | 15 exact tiers | 22.1% exact / 50.0% within 1 tier |
| Logistic Regression | 5 broad rank groups | 58.3% |

The Logistic Regression broad rank model was chosen for the app. Predicting exact sub-ranks like Diamond 2 vs Diamond 3 is genuinely hard because adjacent tiers are statistically very similar. The broad rank groups have real mechanical differences that the model can pick up on.

### Top Rank-Separating Stats

Based on correlation with rank tier across the full dataset:

- Time spent high in the air
- Average movement speed
- Percentage of time at supersonic speed
- Boost collected per minute
- Powerslide count and duration
- Time spent as the most forward player
- Average distance to teammates

Basic scoreboard stats like goals, score, and assists are far weaker predictors than movement and boost activity.

---

## Dataset

Replay data comes from the [Ballchasing API](https://ballchasing.com).

- Playlist: Ranked Standard (3v3)
- Ranks collected: Gold through Grand Champion
- Replays per tier: 100
- Player rows: 9,000
- Features: 83 gameplay stats across core, boost, movement, positioning, and demos
- Storage: SQLite

---

## Project Structure

```
RLPerformanceEstimator/
├── app/
│   ├── Home.py
│   └── pages/
│       ├── 1_Predictor.py
│       └── 2_Explorer.py
├── data/
│   └── raw/
├── model/
├── notebooks/
│   └── eda.ipynb
├── src/
│   ├── collect.py
│   └── model.py
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Run Locally

```bash
git clone https://github.com/codingdadir/RLPerformanceEstimator.git
cd RLPerformanceEstimator
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
BALLCHASING_TOKEN=your_token_here
```

Run the app:

```bash
streamlit run app/Home.py
```

To collect your own data:

```bash
python src/collect.py
```

---

## Tech Stack

Python, Pandas, scikit-learn, SQLite, Jupyter Notebook, Streamlit, Ballchasing API

---

## About

Built by Abdul as part of a data science portfolio. Mathematics student at the University of Minnesota with a data science specialization.

[GitHub](https://github.com/codingdadir) · [Live App](https://rrlperformanceestimator.streamlit.app/)