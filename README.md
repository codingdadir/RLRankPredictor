# Rocket League Performance Estimator

A data science and machine learning project that estimates what Rocket League rank a player performed like based on their replay statistics.

The app uses Ballchasing replay data to extract player-level gameplay stats and predict a broad performance rank — Gold, Platinum, Diamond, Champion, or Grand Champion — based on how the player actually played, not just their current MMR.

> **Live Demo:** _coming soon_

---

## The Idea

A player might be ranked Diamond, but their replay stats could tell a different story — playing like a Champion in some games, or Platinum in others. This project separates performance from rank label, asking:

> **What stats actually separate Rocket League ranks?**

The answer, based on feature importance from a trained Random Forest model: aerial ability, speed consistency, boost efficiency, powerslide usage, and spacing from teammates — not just goals or saves.

---

## Models

Two models were trained on player-level stats extracted from ranked 3v3 replays:

| Model | Task | Exact Accuracy | Within 1 Rank |
|---|---|---|---|
| Random Forest | 15-tier prediction | 21.7% | 46.1% |
| Logistic Regression | 5-class broad rank | Higher | — |

The Random Forest predicts across 15 fine-grained tiers (Gold 1 through Grand Champion 3). The Logistic Regression predicts the broader 5-class rank group and achieves higher accuracy due to the simpler classification boundary.

Top predictive features (from Random Forest importance):
- `movement_time_high_air` — aerial play time
- `movement_percent_high_air` — proportion of time in the air
- `positioning_avg_distance_to_mates` — spacing and rotations
- `movement_count_powerslide` — mechanical awareness
- `boost_bcpm` — boost collection efficiency

---

## Dataset

Replay data is collected from the [Ballchasing.com API](https://ballchasing.com).

- **Playlist:** Ranked Standard (3v3)
- **Ranks collected:** Gold through Grand Champion
- **Stat categories:** Core, Boost, Movement, Positioning, Demos
- **Storage:** SQLite (`data/raw/database_v2.db`)

Replays are filtered before extraction to remove forfeits, blowouts, missing rank data, and lobbies with large rank disparities.

---

## Project Status

- [x] Ballchasing API integration
- [x] Replay validation and filtering
- [x] Player-level stat extraction
- [x] SQLite database storage
- [x] Exploratory data analysis
- [x] Random Forest model trained and evaluated
- [x] Logistic Regression model trained and evaluated
- [x] Feature importance analysis
- [x] Streamlit app structure
- [x] Replay URL input
- [x] Player selection from replay
- [x] Prediction output with rank icon
- [ ] Full dashboard deployment

---

## Project Structure

```
RLPerformanceEstimator/
├── app/
│   ├── main.py
│   ├── home.py
│   ├── predictor.py
│   └── explorer.py
├── data/
│   └── raw/
├── model/
├── notebooks/
│   └── eda.ipynb
├── src/
│   ├── collect.py
│   ├── model.py
│   └── utils.py
├── Rank Icons/
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Tech Stack

- Python, Pandas, scikit-learn
- SQLite
- Jupyter Notebook
- Streamlit
- Ballchasing.com API
- Git / GitHub

---

## Run Locally

```bash
git clone https://github.com/codingdadir/RLPerformanceEstimator.git
cd RLPerformanceEstimator
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows PowerShell
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
BALLCHASING_TOKEN=your_token_here
```

Run data collection:

```bash
python src/collect.py
```

---

## About

Built by [codingdadir](https://github.com/codingdadir) - mathematics student at the University of Minnesota.