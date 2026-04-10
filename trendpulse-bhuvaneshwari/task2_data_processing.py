import pandas as pd
import glob
import os

def get_latest_file():
    files = glob.glob("data/trends_*.json")

    if not files:
        print("No files found.")
        return None

    # Sort filenames (YYYYMMDD format works perfectly)
    files.sort()

    return files[-1]  # latest

def clean_data(df): 
    # -------------------------------
    # CLEAN THE DATA
    # -------------------------------
    # Remove duplicates based on post_id
    df = df.drop_duplicates(subset="post_id")
    print(f"After removing duplicates: {len(df)}")

    # Remove rows with missing important fields
    df = df.dropna(subset=["post_id", "title", "score"])
    print(f"After removing nulls: {len(df)}")

    # Convert data types
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].fillna(0).astype(int)

    # Remove low-quality stories (score < 5)
    df = df[df["score"] >= 5]
    print(f"After removing low scores: {len(df)}")

    # Clean whitespace in titles
    df["title"] = df["title"].str.strip()
    #print(f"No: of Rows remaining after cleaning: {len(df)}")

    # -------------------------------
    # SAVE AS CSV
    # -------------------------------

    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)

    output_file = "data/trends_clean.csv"
    df.to_csv(output_file, index=False)

    print(f"\nSaved {len(df)} rows to {output_file}")

    # -------------------------------
    # SUMMARY: stories per category
    # -------------------------------
    print("\nStories per category:")
    print(df["category"].value_counts())

# -------------------------------
# LOAD JSON FILE
# -------------------------------
# Latest File path
file_path = get_latest_file()

try:
     df = pd.read_json(file_path)
     print(f"Loaded {len(df)} stories from {file_path}")
     clean_data(df)
except Exception as e:
     print(f"Error loading file: {e}")

