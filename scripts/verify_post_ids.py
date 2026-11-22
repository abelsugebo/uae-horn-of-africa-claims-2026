"""Check every X post in data/x/posts.csv against the creation time encoded in its post ID.

X post IDs are "snowflake" IDs: the first 41 bits hold the creation time in milliseconds
since 2010-11-04 01:42:54.657 UTC. A fabricated or mistyped ID will not decode to the
time recorded at collection. The script also checks that each URL ends in its post ID.

Usage: python scripts/verify_post_ids.py
"""
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data" / "x"
X_EPOCH_MS = 1288834974657


def decode_time(post_id: str) -> datetime:
    return datetime.fromtimestamp(((int(post_id) >> 22) + X_EPOCH_MS) / 1000, timezone.utc)


def main() -> None:
    posts = pd.read_csv(DATA / "posts.csv", dtype={"post_id": str, "recorded_at": str})
    problems = []
    for row in posts.itertuples(index=False):
        decoded = decode_time(row.post_id)
        if decoded.strftime("%Y-%m-%dT%H:%M:%SZ") != row.created_at_utc:
            problems.append((row.post_id, "created_at_utc does not match the ID"))
        if len(row.recorded_at) == 10:  # recorded with a date only; allow for time zones
            recorded_day = datetime.strptime(row.recorded_at, "%Y-%m-%d").date()
            if abs((decoded.date() - recorded_day).days) > 1:
                problems.append((row.post_id, f"recorded date {row.recorded_at} vs ID {decoded:%Y-%m-%d}"))
        else:
            recorded = datetime.strptime(row.recorded_at, "%Y-%m-%dT%H:%MZ").replace(tzinfo=timezone.utc)
            if abs(decoded - recorded) > timedelta(minutes=2):
                problems.append((row.post_id, f"recorded {row.recorded_at} vs ID {decoded:%Y-%m-%dT%H:%M}Z"))
        if row.post_url.rstrip("/").split("/")[-1] != row.post_id:
            problems.append((row.post_id, "URL does not end in the post ID"))

    print(f"{len(posts)} posts checked, {len(problems)} problems")
    for post_id, issue in problems:
        print(f"  {post_id}: {issue}")


if __name__ == "__main__":
    main()
