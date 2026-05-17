import os
from pathlib import Path
from pprint import pprint
import requests
from dotenv import load_dotenv

RANK_TIERS = {
    "bronze-1": 1,
    "bronze-2": 2,
    "bronze-3": 3,

    "silver-1": 4,
    "silver-2": 5,
    "silver-3": 6,

    "gold-1": 7,
    "gold-2": 8,
    "gold-3": 9,

    "platinum-1": 10,
    "platinum-2": 11,
    "platinum-3": 12,

    "diamond-1": 13,
    "diamond-2": 14,
    "diamond-3": 15,

    "champion-1": 16,
    "champion-2": 17,
    "champion-3": 18,

    "grand-champion-1": 19,
    "grand-champion-2": 20,
    "grand-champion-3": 21,

    "supersonic-legend": 22,
}

def is_replay_valid(replay, rank_label):
    if replay["status"] != "ok":
        return False
    
    if replay["playlist_id"] != "ranked-standard":
        return False
    
    if replay["duration"] < 300:
        return False
    
    if abs(replay["blue"]["stats"]["core"]["goals"] - replay["orange"]["stats"]["core"]["goals"]) > 2:
        return False
    
    rank_tiers = []

    for team in ["blue", "orange"]:
        for player in replay[team]["players"]:
            if player.get("stats", None) is None:
                return False
            
            rank_tier = player.get("rank", {}).get("tier")

            if rank_tier is None:
                print(replay["id"], "Rejected: missing player rank")
                return False
            
            rank_tiers.append(rank_tier)
    
    MAX_RANK_SPREAD_BY_LABEL = {
    "bronze": 3,
    "silver": 3,
    "gold": 3,
    "platinum": 3,
    "diamond": 2,
    "champion": 2,
    "grand-champion": 1,
    "supersonic-legend": 0,
}
    rank_spread = max(rank_tiers) - min(rank_tiers)
    max_allowed_spread = MAX_RANK_SPREAD_BY_LABEL[rank_label]
    
    if rank_spread > max_allowed_spread:
        return False
            
    return True
            

def extract_player_stats(detailed_response):
    rows = []
    
    for team in ["blue", "orange"]:
        for player in detailed_response[team]["players"]:
                player_dict = {}
                player_dict["replay_id"] = detailed_response["id"]
                player_dict["rank"] = player.get("rank", None)
                player_dict["rank_tier"] = player.get("rank", {}).get("tier")
                player_dict["team"] = team
                player_dict["duration"] = detailed_response.get("duration", None)
                for category, stat_group in player.get("stats", {}).items():
                    for stat_name, value in stat_group.items():
                        player_dict[f"{category}_{stat_name}"] = value

                rows.append(player_dict)

    return rows


def collect_rows_from_replays(data, rank_label):
    all_rows = []
    for replay in data:
        replay_id = replay["id"]
        detailed_data = requests.get(f"https://ballchasing.com/api/replays/{replay_id}", headers=headers).json()

        if is_replay_valid(detailed_data, rank_label):
            all_rows.extend(extract_player_stats(detailed_data))
    
    return all_rows


load_dotenv(Path(__file__).resolve().parent.parent / ".env")

TOKEN = os.getenv("BALLCHASING_TOKEN")

headers = {
    "Authorization": TOKEN
}
params = {
    "min-rank": "gold-1",
    "max-rank": "gold-2",
    "playlist": "ranked-standard",
    "count": 10
}
response = requests.get("https://ballchasing.com/api/replays", headers=headers, params=params)


data = response.json()

print(len(data["list"]))
all_rows = collect_rows_from_replays(data["list"], "gold")
print(len(all_rows))
