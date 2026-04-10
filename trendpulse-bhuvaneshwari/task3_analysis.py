import pandas as pd
import numpy as np
import os

def analysis(df):

    # -------------------------------
    # EXPLORE THE DATA
    # -------------------------------

    print(f"Loaded data: {df.shape}")

    print("\nFirst 5 rows:")
    print(df.head())

    # Averages
    avg_score = df["score"].mean()
    avg_comments = df["num_comments"].mean()

    print(f"\nAverage score   : {avg_score:.2f}")
    print(f"Average comments: {avg_comments:.2f}")

    # -------------------------------
    # NUMPY ANALYSIS
    # -------------------------------
    print("\n--- NumPy Stats ---")

    scores = df["score"].to_numpy()
    comments = df["num_comments"].to_numpy()

    # Score statistics
    print(f"Mean score   : {np.mean(scores):.2f}")
    print(f"Median score : {np.median(scores):.2f}")
    print(f"Std deviation: {np.std(scores):.2f}")
    print(f"Max score    : {np.max(scores)}")
    print(f"Min score    : {np.min(scores)}")

    # Category with most stories
    category_counts = df["category"].value_counts()
    top_category = category_counts.idxmax()
    top_count = category_counts.max()

    print(f"\nMost stories in: {top_category} ({top_count} stories)")

    # Most commented story
    max_comments_index = np.argmax(comments)
    top_story = df.iloc[max_comments_index]

    print(f'\nMost commented story: "{top_story["title"]}" — {top_story["num_comments"]} comments')

    # -------------------------------
    # ADD NEW COLUMNS
    # -------------------------------

    # Engagement = comments per upvote
    df["engagement"] = df["num_comments"] / (df["score"] + 1)

    # Popular flag
    df["is_popular"] = df["score"] > avg_score

    # -------------------------------
    # SAVE RESULT
    # -------------------------------
    os.makedirs("data", exist_ok=True)

    output_file = "data/trends_analysed.csv"
    df.to_csv(output_file, index=False)

    print(f"\nSaved to {output_file}")


file_path = "data/trends_clean.csv"

# -------------------------------
#LOAD CSV INTO PANDA DATAFRAME
# -------------------------------
try:
    df = pd.read_csv(file_path)
    analysis(df)
except Exception as e:
    print(f"Error loading file: {e}")
