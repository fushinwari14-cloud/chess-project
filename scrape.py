import requests
import pandas as pd
from datetime import datetime

username = "Shanks_sama12"

headers = {
    "User-Agent": "Mozilla/5.0"
}

archives_url = f"https://api.chess.com/pub/player/{username}/games/archives"
response = requests.get(archives_url, headers=headers)

if response.status_code != 200:
    print("Failed to fetch archives")
    exit()

archives = response.json()["archives"]

games_list = []

for archive in archives:
    archive_response = requests.get(archive, headers=headers)

    if archive_response.status_code != 200:
        continue

    games = archive_response.json()["games"]

    for game in games:
        white = game["white"]["username"]
        black = game["black"]["username"]

        if white.lower() == username.lower():
            opponent = black
            result = game["white"]["result"]
        else:
            opponent = white
            result = game["black"]["result"]

        if result == "win":
            outcome = "Win"
        elif result == "agreed":
            outcome = "Draw"
        else:
            outcome = "Loss"

        games_list.append({
            "player": username,
            "opponent": opponent,
            "game_type": game.get("time_class"),
            "result": outcome,
            "url": game.get("url"),
            "date": datetime.fromtimestamp(
                game["end_time"]
            ).strftime("%Y-%m-%d %H:%M:%S")
        })

df = pd.DataFrame(games_list)

df.to_csv(f"{username}_chess_games.csv", index=False)

print(f"Saved {len(df)} games")
print(df.head())