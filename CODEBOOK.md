# Codebook

All files are UTF-8 CSV with a header row. Empty cells mean the value was not recorded or does not apply.

## data/claims/claims_register.csv

| Variable | Description |
| --- | --- |
| claim_id | Claim number, 1 to 17 |
| theme | Sudan war; Somalia and Somaliland; Ethiopia and Eritrea; Influence operations; Ethiopia and the Sudan war |
| claim | The claim as worded for assessment |
| verdict | Established, Credibly reported, Disputed, Unproven or Misleading (see `verdict_scale.csv`) |
| verdict_qualifier | A limit on the verdict's scope, for example "diplomatic" or "2015–2021" |
| evidence | Summary of the evidence behind the verdict, plain text |
| evidence_markdown | The same summary with inline source links |
| source_urls | URLs cited in the evidence, separated by semicolons |

Verdicts reflect public evidence as of November 19, 2026. A denial by the UAE government is recorded in the evidence but does not change a verdict on its own.

## data/claims/verdict_scale.csv

| Verdict | Meaning |
| --- | --- |
| Established | Supported by multiple independent investigations, official findings or physical evidence |
| Credibly reported | Supported by one detailed investigation, not yet independently corroborated |
| Disputed | Credible sources conflict |
| Unproven | Asserted without public evidence |
| Misleading | A real event presented as proof of something it does not show |

## data/claims/additional_claims.csv

Claims and codes used in `post_claims.csv` that are not among the 17 register claims.

| Variable | Description |
| --- | --- |
| claim_code | 4j, 15R, N1 to N4, E24, E72 or gen |
| claim | The claim as worded |
| first_seen | Month the claim first appeared in the collection or the underlying event |
| posts_in_collection | Number of posts in `posts.csv` carrying the code |
| views_in_collection | Sum of those posts' views |
| languages | Languages of those posts |
| status | Accurate, False, Unproven, Unverified, No corroboration found, Consistent with the ruling, or Not applicable |
| status_basis | Why the status was given |
| source_url | Source for the status, where one applies |

Code meanings: **4j** argues the ICJ lacks jurisdiction (made before the ruling); **15R** says an anti-UAE campaign fabricated the al-Zubaidi story; **N1** to **N4** are new factual claims; **E24** and **E72** give the deadline in Somalia's expulsion order as 24 or 72 hours; **gen** marks general framing with no specific factual claim.

## data/claims/influence_operations_findings.csv

Public findings on coordinated or inauthentic activity around Sudan's war and the UAE's role in the region: `date`, `source`, `finding`, `attribution` (who the source says ran the activity, with its stated confidence) and `source_url`.

## data/claims/other_external_actors.csv

Documented or reported roles of other outside states in the same conflicts: `actor`, `documented_or_reported_role`, `sources` and `source_urls`.

## data/news/queries.csv

| Variable | Description |
| --- | --- |
| set_id | Query set, A to F |
| topic | Short topic name used in the charts |
| query_set_label | Full label of the query set |
| related_claims | Register claims the set covers |
| language | en or ar |
| query | The exact Boolean query run in Media Cloud |
| excluded_domains | Domains excluded in the query, separated by semicolons |
| collection_group | Group of collections searched (see `collections.csv`) |
| platform | Media Cloud platform identifier |
| start_date, end_date | Search window |
| run_date | Date the query was run |

## data/news/collections.csv

`collection_group` (en or ar), `collection_id` (Media Cloud collection ID) and `collection_name`.

## data/news/monthly_counts.csv

One row per query set, language and month, January 2025 to November 2026. November 2026 covers November 1 to 19 only.

| Variable | Description |
| --- | --- |
| set_id, topic, language, month | Keys; month is YYYY-MM |
| stories | Stories matching this search after domain exclusions, before deduplication. A story that matches more than one search appears in each, so the column sum (16,811) is not a count of unique stories |
| distinct_headlines | Distinct normalized headlines, each counted in the month it first appeared |
| uae_headlines | Distinct headlines that match both the UAE pattern and the topic pattern in `headline_patterns.csv` |

Headlines are normalized by lowercasing, replacing every character that is not a letter or digit with a space, and collapsing spaces. Deduplication happens **within each topic/language search**. The sum of `distinct_headlines` (12,281) is therefore a sum of within-search counts, not a globally unique headline total. The sum of `uae_headlines` (980) is also not a globally unique count. Topics overlap: a headline about the ICJ case that names Sudan counts under both topics.

## data/news/corpus_monthly_totals.csv

`collection_group`, `month` and `total_stories`, the number of stories in that group of collections in that month, for normalizing counts.

## data/news/excluded_domains.csv

`set_id`, `language`, `domain`, `matches` (stories matched before exclusion), `headline_hits` (matched stories whose headline was on topic) and `method`.

## data/news/headline_patterns.csv

Regular expressions, applied case-insensitively to headlines: `uae_headline_pattern`, `topic_headline_pattern` and `contamination_check_pattern` (the pattern used to test whether an outlet's matches were on topic).

## data/x/posts.csv

| Variable | Description |
| --- | --- |
| post_id | X post ID |
| post_url | Link to the post; handle-free for pseudonymized accounts |
| created_at_utc | Creation time decoded from the post ID |
| recorded_at | Time recorded at collection, to the minute or the day |
| account | Handle for public accounts; `private_NNN` pseudonym otherwise, stable within this release |
| account_public | True for officials, institutions, outlets and public figures |
| account_name | Name of a public account |
| account_type | Official, News outlet, Journalist, Researcher or advocate, Commentator, or Unclassified |
| language | ISO 639-1 code: ar, en, am, ti, so; am;en for a bilingual post; und if undetermined |
| likes, reposts, replies, views | Counts as displayed at collection; views are X impressions, which include repeat views |
| collection_round | 1 = November 19, 2026; 2 = November 20 to 21, 2026 (AI-assisted multilingual searches) |

Account types: **Official**, a government body or officeholder; **News outlet**, a news organization's account; **Journalist**, an individual reporter; **Researcher or advocate**, an NGO, academic, analyst or lawyer; **Commentator**, an individual posting commentary; **Unclassified**, a private account not classified in round 1.

## data/x/post_claims.csv

One row per post and claim. A post that addresses three claims has three rows.

| Variable | Description |
| --- | --- |
| post_id | Joins to `posts.csv` |
| claim_code | 1 to 17 for register claims; other codes in `additional_claims.csv` |
| stance | Asserts, Reports or Disputes |
| evidence | Yes, Partial or No |
| coding_note | Short note from the coder |

**Stance.** Asserts: presents the claim as true. Reports: attributes the claim to a source without endorsing it. Disputes: denies or rebuts the claim, or leaves out a material fact; omissions are marked "By omission" in `coding_note`.

**Evidence.** Yes: links to or names a document, investigation, official record or imagery. Partial: points to some support, such as photos or an unnamed outlet, without a checkable source. No: no source.

## data/x/post_frames.csv

Framing codes for UAE-side posts on Somalia's expulsion of the UAE ambassador (November 18 to 19, 2026): `post_id`, `event` and `frame`. A post can carry more than one frame.

| Frame | Meaning |
| --- | --- |
| Internal power struggle | Presents Somalia's measures as a product of Mogadishu's internal political crisis |
| Relations with the Somali people | Separates the Somali people from the government and affirms ties with the people |
| Benefactor | Lists UAE support to Somalia |
| Delegitimizing the president | Questions the Somali president's mandate or standing |
