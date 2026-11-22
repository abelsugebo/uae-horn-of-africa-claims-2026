"""Reproduce the news-coverage figures reported in the accompanying article.

Usage: python scripts/summarize_news.py
"""
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data" / "news"


def main() -> None:
    m = pd.read_csv(DATA / "monthly_counts.csv")
    print(f"Stories after exclusions: {m.stories.sum():,}   distinct headlines: {m.distinct_headlines.sum():,}\n")

    by_topic = m.pivot_table(index="topic", columns="language", values="uae_headlines", aggfunc="sum")
    by_topic["total"] = by_topic.sum(axis=1)
    print("Distinct headlines naming the UAE with each topic (topics overlap):")
    print(by_topic.sort_values("total", ascending=False)[["en", "ar", "total"]].to_string(), "\n")

    monthly = m.pivot_table(index="month", columns="topic", values="uae_headlines", aggfunc="sum")
    for topic in ["Sudan and the RSF", "Somalia and Somaliland"]:
        top3 = monthly[topic].sort_values(ascending=False).head(3)
        print(f"{topic}, peak months (English and Arabic combined): "
              + ", ".join(f"{month} = {n}" for month, n in top3.items()))
    print("\nNovember 2026 covers November 1 to 19 only.")

    totals = pd.read_csv(DATA / "corpus_monthly_totals.csv")
    print("\nArchive size, stories per month (min to max):")
    print(totals.groupby("collection_group").total_stories.agg(["min", "max"]).to_string())


if __name__ == "__main__":
    main()
