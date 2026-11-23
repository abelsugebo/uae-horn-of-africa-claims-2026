# Methodology

## 1. Claims register

The register covers claims about the UAE's role in Sudan, Somalia and Somaliland, Ethiopia and Eritrea that appear in news coverage, official statements and social media. Claims 1 to 15 were set before monitoring began; claims 16 and 17 were added when monitoring showed they circulated widely. Each claim was assessed against public evidence and given one of five verdicts (see `data/claims/verdict_scale.csv`). Investigations, official findings, court records, sanctions designations and physical or satellite evidence carry the most weight. A denial by the UAE government is recorded but does not change a verdict on its own; neither does an accusation by another government. Verdicts reflect public evidence as of November 19, 2026 and will be revised if new evidence emerges.

Claims that surfaced during monitoring but fall outside the register are listed in `data/claims/additional_claims.csv` with a status and its basis.

## 2. News coverage

**Source.** Media Cloud's online news archive (search.mediacloud.org), searched for January 1, 2025 to November 19, 2026. Queries were run on November 19, 2026; November figures are partial.

**Outlets.** The English group combined Media Cloud's Global English Language Sources collection (1,602 outlets) with its national collections for Sudan, Somalia, Ethiopia, Eritrea, Kenya, the UAE, Saudi Arabia, Qatar and Egypt. The Arabic group used the national collections for Sudan, the UAE, Saudi Arabia, Qatar, Egypt, Jordan, Yemen and Somalia. Collection IDs are in `data/news/collections.csv`.

**Queries.** Six query sets (A to F), one per topic, each in English and Arabic. The exact strings are in `data/news/queries.csv`. They tie ambiguous terms to context, for example "RSF" only with "Sudan", so that Reporters Without Borders is not counted, and Ethiopia and Eritrea only with military terms.

**Cleaning.** Three steps:

1. Outlets whose page templates produced false matches were excluded. The rule: 30 or more matches with fewer than 5 percent of headlines on topic. Two further outlets were excluded after a sample of their matches showed page-template text rather than relevant coverage. All exclusions are in `data/news/excluded_domains.csv`.
2. Stories were deduplicated by normalized headline **within each topic/language search**, because a network of sites republishing wire copy under country names inflated some monthly counts nearly sevenfold. Each normalized headline is counted once per search, in the month it first appeared in that search. Searches were not deduplicated against one another.
3. The headline measure counts only distinct headlines that name the UAE together with the topic, using the patterns in `data/news/headline_patterns.csv`.

After exclusions, the searches matched 16,811 stories. The sum of within-search distinct headline counts is 12,281. Because topics can overlap, **12,281 must not be described as 12,281 globally unique news headlines**. Across topics, `uae_headlines` sums to 980; these topical counts can likewise overlap.

**Checks.** Story-level totals matched Media Cloud's aggregate counts for every query. A random check of 24 headlines counted by the headline measure found all of them were about the UAE's role or relations in the country concerned.

**Limitations.** Media Cloud holds few Horn of Africa outlets (34 for Sudan, 49 for Somalia, 88 for Ethiopia and 18 for Eritrea). Arabic searches miss words carrying attached prefixes. The English archive grew by about 15 percent from March 2026; `corpus_monthly_totals.csv` allows counts to be normalized. The Somalia set also captures UAE-related Somalia news unrelated to the register, such as a May 2026 piracy incident.

## 3. X posts

**Collection.** Posts were collected in two rounds. Round 1 (November 19, 2026) covered mainly English posts on the register claims and UAE-side messaging on Somalia's expulsion of the UAE ambassador, collected by the author through X searches. Round 2 (November 20 to 21, 2026) used AI-assisted X searches in Arabic, Somali, Amharic and Tigrinya, with search terms based on the query sets, to add high-view posts and voices not already in the collection. Searches that returned no relevant posts were recorded; for example, Amharic searches on claim 17 found none.

**Coding.** Each post was coded by claim, with one row per claim, by stance and by evidence (definitions in `CODEBOOK.md`). Posts that frame the Somalia rupture without a factual claim were coded for framing in `post_frames.csv`. AI-assisted codes were reviewed and corrected before analysis, and native-language readings of the Amharic posts were confirmed by the author.

**Verification.** Every post ID was checked against the creation time encoded in it and against its URL (`scripts/verify_post_ids.py`); all 89 matched.

**Limitations.** The collection is a purposive sample of 89 posts, not a census, so shares describe the posts collected. Round 2 deliberately sought voices outside the UAE side, which affects comparisons between languages. View counts are X impressions captured at collection time and include repeat views. X search does not return every relevant post, and major outlets' accounts were under-represented in round 2. No test for coordinated or inauthentic behavior was run on this sample, so none is claimed.

## 4. Ethics

Government bodies, officials, news outlets, organizations and public figures are named. Private individuals are pseudonymized, and their post links omit the handle. The repository shares post IDs, counts and derived codes rather than post text. Requests to remove a post or account can be sent to Inform Africa.
