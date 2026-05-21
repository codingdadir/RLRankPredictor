# Rocket League Performance Rank Estimator

A data science and machine learning project that estimates what Rocket League rank a player performed like based on replay stats.

The app uses Ballchasing replay data, extracts player-level gameplay statistics, and predicts a broad performance rank such as Gold, Platinum, Diamond, Champion, or Grand Champion.

## Project Idea

The goal of this project is not just to predict a player's current Rocket League rank. The goal is to estimate what rank their performance looks like based on how they played in a replay.

For example, a player may currently be Diamond, but the model may estimate that their replay performance looked closer to Champion or Platinum.

## Current Status

This project currently has:

- Ballchasing API data collection working
- Replay validation and filtering working
- Player-level stat extraction working
- SQLite database storage working
- A larger v2 dataset collected
- Exploratory data analysis started
- Baseline machine learning models trained
- Streamlit app structure created
- Replay URL input working
- Player selection from replay working
- Saved model loading in Streamlit working
- Prediction output displayed with a rank icon

## Dataset

Replay data comes from the Ballchasing API.

The current larger dataset is stored in:

```text
data/raw/database_v2.db