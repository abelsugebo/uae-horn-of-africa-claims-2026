"""Reproduce the X (Twitter) figures reported in the accompanying article.

Usage: python scripts/summarize_x.py
"""
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data" / "x"
UAE_SIDE = ["@Abdulkhaleq_UAE", "@mofauae", "@AfraMalHameli", "@Lana_Nusseibeh"]


def post_level_evidence(codes: pd.Series) -> str:
    """A post counts as citing evidence if any of its claim codes does."""
    if (codes == "Yes").any():
        return "Yes"
    if (codes == "Partial").any():
        return "Partial"
    return "No"


def main() -> None:
    posts = pd.read_csv(DATA / "posts.csv", dtype={"post_id": str})
    claims = pd.read_csv(DATA / "post_claims.csv", dtype={"post_id": str, "claim_code": str})
    views = posts.set_index("post_id").views
    total = posts.views.sum()

    print(f"Posts: {len(posts)}   views: {total:,}")
    print(posts.groupby("language").agg(posts=("post_id", "size"), views=("views", "sum"))
          .sort_values("views", ascending=False).to_string(), "\n")

    uae = posts[posts.account.isin(UAE_SIDE)].views.sum()
    aa = posts[posts.account == "@Abdulkhaleq_UAE"].views.sum()
    print(f"UAE officials and Abdulkhaleq Abdulla: {uae / total:.1%} of views; Abdulla alone: {aa / total:.1%}")

    r1 = claims.merge(posts[["post_id", "collection_round", "account"]], on="post_id")
    r1 = r1[(r1.collection_round == 1) & (r1.claim_code == "1")]
    denial = r1[(r1.stance == "Disputes") & (r1.account == "@Abdulkhaleq_UAE")].post_id.unique()
    support = r1[r1.stance.isin(["Asserts", "Reports"])].post_id.unique()
    print(f"Round 1, claim 1: denial {views[denial].sum():,} views vs {len(support)} asserting or reporting posts "
          f"{views[support].sum():,} views\n")

    register = claims[claims.claim_code.str.fullmatch(r"\d+")]
    ev = register.groupby("post_id").evidence.agg(post_level_evidence).rename("evidence")
    ev = posts.set_index("post_id").join(ev, how="inner")
    share = ev.pivot_table(index="language", columns="evidence", values="views", aggfunc="sum", fill_value=0)
    print("Share of views by evidence, posts coded on claims 1 to 17:")
    print((share.div(share.sum(axis=1), axis=0) * 100).round(1).to_string(), "\n")

    eth = claims[claims.claim_code.isin(["11", "14", "16"]) & (claims.stance == "Asserts")].post_id.unique()
    eth_ev = ev.loc[eth, "evidence"].value_counts().to_dict()
    print(f"Posts asserting claims 11, 14 or 16: {len(eth)}, views {views[eth].sum():,}, evidence {eth_ev}")

    for code in ["E24", "E72"]:
        ids = claims[claims.claim_code == code].post_id.unique()
        print(f"{code}: {len(ids)} posts, {views[ids].sum():,} views")

    codes = claims.groupby("post_id").apply(
        lambda g: "; ".join(f"{c} {s.lower()} ({e.lower()})" for c, s, e in zip(g.claim_code, g.stance, g.evidence)),
        include_groups=False)
    top = posts.sort_values("views", ascending=False).head(10).copy()
    top["codes"] = top.post_id.map(codes).fillna("framing only (see post_frames.csv)")
    print("\nTen most-viewed posts:")
    print(top[["created_at_utc", "account", "language", "views", "codes"]].to_string(index=False))


if __name__ == "__main__":
    main()
