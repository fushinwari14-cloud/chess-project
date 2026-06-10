import pandas as pd

df = pd.read_csv("Shanks_sama12_chess_games.csv")

df = df.drop_duplicates()

df["player"] = df["player"].str.strip()
df["opponent"] = df["opponent"].str.strip()
df["game_type"] = df["game_type"].str.strip().str.lower()
df["result"] = df["result"].str.strip().str.title()

df["date"] = pd.to_datetime(df["date"], errors="coerce")

df = df.dropna(subset=["date"])

df = df.dropna(
    subset=[
        "player",
        "opponent",
        "game_type",
        "result"
    ]
)

df = df.reset_index(drop=True)

df.to_csv("shanks-sama12_chess_games.csv", index=False)
