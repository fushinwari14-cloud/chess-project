import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("shanks-sama12_chess_games.csv")

print("CLEANED DATA")
print(df.head())

train_data, temp_data = train_test_split(
    df,
    test_size=0.30,
    random_state=42
)

validation_data, test_data = train_test_split(
    temp_data,
    test_size=0.50,
    random_state=42
)

print("\nTRAIN DATA")
print(train_data.shape)

print("\nVALIDATION DATA")
print(validation_data.shape)

print("\nTEST DATA")
print(test_data.shape)

train_data.to_csv("train_data.csv", index=False)
validation_data.to_csv("validation_data.csv", index=False)
test_data.to_csv("test_data.csv", index=False)

print("\nDataset split successfully!")
print("Train, Validation and Test files saved.")