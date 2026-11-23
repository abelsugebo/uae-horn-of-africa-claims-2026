# The UAE's Role in the Horn of Africa: Claims, Evidence and Circulation

Data and code behind the Inform Africa/HaqCheck report *The UAE's Role in the Horn of Africa: What Is Documented and What Is Not* (November 2026) by Abel W. Sugebo. Read the **current report (version 1.1, November 23, 2026)**: [PDF in this repository](report/UAE_Role_Horn_of_Africa_Abel_W_Sugebo_Nov2026_v1-1.pdf), the identical [PDF on Inform Africa](https://informafrica.net/wp-content/uploads/2026/11/UAE_Role_Horn_of_Africa_Abel_W_Sugebo_Nov2026_v1-1.pdf) or the [report landing page](https://informafrica.net/2026/11/23/the-uaes-role-in-the-horn-of-africa/). A shorter article on the findings: [The UAE in the Horn of Africa: What the Evidence Shows](https://informafrica.net/2026/11/23/uae-horn-of-africa-evidence/).

The report separates what is documented about the United Arab Emirates' role in the conflicts and crises of Sudan, Somalia and Somaliland, Ethiopia and Eritrea from what is asserted without evidence, and measures how each claim circulates in news coverage and on X. This repository holds three datasets:

1. **Claims register.** 17 claims, each rated on a five-level evidence scale with the sources behind the rating, plus claims that surfaced during monitoring.
2. **News coverage.** Monthly counts from the Media Cloud online news archive for six topics, in English and Arabic, January 1, 2025 to November 19, 2026. Headlines are deduplicated within each topic/language search, not across all searches.
3. **X posts.** 89 posts in English, Arabic, Somali, Amharic and Tigrinya, coded by claim, stance and evidence.

## Repository structure

```
report/
  UAE_Role_Horn_of_Africa_Abel_W_Sugebo_Nov2026_v1-1.pdf  The full report, version 1.1
  cover.jpg, social-card.png, web-hero.jpg, figure1-claims-by-verdict.png,
  web-headlines-by-topic.png                     Report and article images
data/
  claims/
    claims_register.csv               17 claims, verdicts, evidence and source links
    verdict_scale.csv                 Definitions of the five verdicts
    additional_claims.csv             Claims that surfaced during monitoring, with status
    influence_operations_findings.csv Public findings on coordinated or inauthentic activity
    other_external_actors.csv         Documented or reported roles of other outside states
  news/
    queries.csv                       Exact Media Cloud queries, dates and exclusions
    collections.csv                   Media Cloud collections in each language group
    monthly_counts.csv                Stories, distinct headlines and UAE headlines per month
    corpus_monthly_totals.csv         Size of each archive group per month
    excluded_domains.csv              Outlets removed for false matches, and why
    headline_patterns.csv             Patterns used for the headline measure and checks
  x/
    posts.csv                         One row per post: account, language, engagement
    post_claims.csv                   One row per post and claim: stance and evidence
    post_frames.csv                   Framing codes for UAE-side posts on Somalia
scripts/
  verify_post_ids.py                  Checks each post ID against its recorded time
  summarize_x.py                      Reproduces the X figures in the report
  summarize_news.py                   Reproduces the news figures in the report
CODEBOOK.md                           Every variable and code value
METHODOLOGY.md                        How the data were collected, cleaned and coded
```

## What the data show

- Of the 17 claims, 8 are established, 1 is credibly reported, 7 are unproven and 1 is misleading. The established claims of military support for a warring party all concern the Rapid Support Forces (RSF) in Sudan.
- In the news archive, 595 distinct headlines named the UAE together with Sudan or the RSF, against 204 for Somalia and Somaliland, 118 for the ICJ case, 32 for Ethiopia and Eritrea, 26 for the Colombian contractors and 5 for UAE-linked influence operations.
- UAE headlines peaked around legal and diplomatic events: 99 in May 2025 (the ICJ dismissal, Sudan's break with the UAE and an Amnesty International arms report) and 65 in January 2026 (Somalia's annulment of its UAE agreements).
- **Count definition:** Across the 12 topic/language searches, `distinct_headlines` sums to **12,281**, after deduplication within each search. This is **not** a count of globally unique headlines because the topic searches overlap. The six `uae_headlines` topic counts sum to **980**, again with possible overlaps. The 16,811 story matches are summed across searches in the same way. None of these sums should be presented as a globally deduplicated count.
- On X, posts by UAE officials and the Emirati political scientist Abdulkhaleq Abdulla account for 52 percent of the views in the collection. Among Arabic posts on the claims, 41 percent of views went to posts citing a document or investigation, against 19 percent in English.

The scripts recompute these figures from the processed files in `data/`. The collection of X posts is a purposive sample, so its shares describe the posts collected, not X as a whole. See `METHODOLOGY.md` for limitations.

## What can be reproduced

- **X posts:** every post is listed by ID and link, so the collection and its codes can be checked against the posts themselves.
- **News coverage:** the scripts recompute the report's news figures from processed monthly counts. Story-level records (Media Cloud story IDs, URLs, outlets and headlines) are not included in this version, so the outlet exclusions and headline deduplication cannot be rerun or audited from this repository alone. The queries (`data/news/queries.csv`, UTF-8; use this file rather than the report's Annex A for exact strings), collections, excluded outlets and headline patterns are published, but rerunning the queries in Media Cloud will not return identical counts because its archive keeps changing. See section 4 of `METHODOLOGY.md`.

## Using the data

```
pip install -r requirements.txt
python scripts/verify_post_ids.py
python scripts/summarize_x.py
python scripts/summarize_news.py
```

All files are UTF-8 CSV. Arabic, Amharic and Tigrinya query strings and patterns are stored as written. `post_claims.csv` joins to `posts.csv` on `post_id`; claim codes 1 to 17 join to `claims_register.csv` on `claim_id`, and other codes to `additional_claims.csv` on `claim_code`.

## Privacy and platform terms

Government bodies, officials, news outlets, organizations and public figures appear under their own handles. Private individuals appear under pseudonyms (`private_001` and so on), and their post links use the handle-free form `https://x.com/i/status/<id>`. The repository shares post IDs, engagement counts and derived codes, not post text, in line with X's terms for sharing data; the posts themselves can be viewed through the links. Anyone who wants a post or account removed from the dataset can contact Inform Africa.

## Citation

Sugebo, Abel W. (2026). *The UAE's Role in the Horn of Africa: Claims, Evidence and Circulation* (Version 1.1) [Data set]. Inform Africa/HaqCheck.

Machine-readable citation details are in `CITATION.cff`. News counts come from Media Cloud; please also cite Media Cloud when reusing them: https://doi.org/10.1609/icwsm.v20i1.42778

## License

Data in `data/` are released under the Creative Commons Attribution 4.0 International License (see `LICENSE-DATA.md`). Code in `scripts/` is released under the MIT License (see `LICENSE`). Linked sources and X posts remain subject to their owners' terms.

## Author

Abel W. Sugebo is Executive Director and Founder of Inform Africa/HaqCheck, a research organization focused on disinformation, digital rights and information integrity in Sub-Saharan Africa. Contact: [informafrica.net](https://informafrica.net)

## Version

1.1, November 23, 2026. No data values changed. Clarifies that the story, headline and UAE-headline totals are sums across overlapping searches, describes what can and cannot be reproduced, and replaces the report PDF with version 1.1 (count wording, key figures and a legible Annex A). The PDF's file name carries its version, and the file is identical to the copy on informafrica.net (SHA-256 `70fb50cb030968a1d7624b0b2c466c036222ada2e1b9d2541131fc3814d45f12`). The version 1.0 PDF remains in the repository history, for example at commit `5288d46`.

1.0, November 2026. First release.

Dates for both versions: claim verdicts reflect public evidence as of November 19, 2026; news data run to November 19, 2026; X posts were collected November 19 to 21, 2026, to measure circulation; they are not part of the evidence behind the verdicts.
