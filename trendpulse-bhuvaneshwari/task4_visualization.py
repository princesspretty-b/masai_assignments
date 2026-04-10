import pandas as pd
import matplotlib.pyplot as plt
import os

def shorten_title(title, max_len=50):
    """Shorten long titles for better display"""
    return title if len(title) <= max_len else title[:max_len] + "..."

def visualize(df):
    # Create outputs folder
    os.makedirs("outputs", exist_ok=True)

    # -------------------------------
    # CHART 1: TOP 10 STORIES
    # -------------------------------
    top10 = df.sort_values(by="score", ascending=False).head(10)

    titles = top10["title"].apply(shorten_title)
    scores = top10["score"]

    plt.figure(figsize=(10, 6))
    plt.barh(titles, scores)
    plt.xlabel("Score")
    plt.ylabel("Story Title")
    plt.title("Top 10 Stories by Score")
    plt.gca().invert_yaxis()  # highest score on top

    plt.savefig("outputs/chart1_top_stories.png")
    plt.show()
    plt.close()

    # -------------------------------
    # CHART 2: STORIES PER CATEGORY
    # -------------------------------
    category_counts = df["category"].value_counts()

    plt.figure(figsize=(8, 5))
    plt.bar(category_counts.index, category_counts.values,
            color=["red", "blue", "green", "purple", "orange"])

    plt.xlabel("Category")
    plt.ylabel("Number of Stories")
    plt.title("Stories per Category")

    plt.savefig("outputs/chart2_categories.png")
    plt.show()
    plt.close()

    # -------------------------------
    # CHART 3: SCATTER PLOT
    # -------------------------------
    popular = df[df["is_popular"] == True]
    not_popular = df[df["is_popular"] == False]

    plt.figure(figsize=(8, 5))
    plt.scatter(popular["score"], popular["num_comments"],
                color="green", label="Popular", alpha=0.7)

    plt.scatter(not_popular["score"], not_popular["num_comments"],
                color="red", label="Not Popular", alpha=0.7)

    plt.xlabel("Score")
    plt.ylabel("Number of Comments")
    plt.title("Score vs Comments")
    plt.legend()

    plt.savefig("outputs/chart3_scatter.png")
    plt.show()
    plt.close()

    # -------------------------------
    # BONUS: DASHBOARD
    # -------------------------------
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Chart 1 (inside dashboard)
    axes[0].barh(titles, scores)
    axes[0].set_title("Top Stories")
    axes[0].invert_yaxis()

    # Chart 2
    axes[1].bar(category_counts.index, category_counts.values,
                color=["red", "blue", "green", "purple", "orange"])
    axes[1].set_title("Categories")

    # Chart 3
    axes[2].scatter(popular["score"], popular["num_comments"],
                    color="green", label="Popular", alpha=0.7)
    axes[2].scatter(not_popular["score"], not_popular["num_comments"],
                    color="red", label="Not Popular", alpha=0.7)
    axes[2].set_title("Score vs Comments")
    axes[2].legend()

    fig.suptitle("TrendPulse Dashboard")

    plt.savefig("outputs/dashboard.png")
    plt.close()

    print("All charts saved in outputs/ folder")

file_path = "data/trends_analysed.csv"

# -------------------------------
# READ CSV FILE
# -------------------------------
try:
    df = pd.read_csv(file_path)
    visualize(df)
except Exception as e:
    print(f"Error loading file: {e}")
