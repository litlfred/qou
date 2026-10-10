---
# qou-4lx3
title: '[LEANNODES L0] Lean parity baseline'
status: completed
type: feature
priority: normal
tags:
    - migration
    - leannodes
created_at: 2026-10-04T16:35:46Z
updated_at: 2026-10-04T17:44:24Z
parent: qou-ahxm
---

From the LEANNODES migration analysis (2026-10-04), story L0. Full report: docs/audits/2026-10-04-workplan-and-migration/LEANNODES_report.md.

| L0 | Lean parity baseline | Static census witness on `qa-reports`; a re-run is byte-identical | S | – |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


## Done 2026-10-04 (session_01NdDGeP1SyShmoUssLuRZ91, branch claude/migration-wave6-2026-10-04)
- Tool: scripts/lean-static-census.py (P-Lean checks 1-3; --rev <commit> reads git blobs; --check <commit>).
- Baseline = the census AT main 41f7d91d052a5ccdbd337c0fda18868a96da62fe, sha256 76548b0562c155ab1d623ee1e51fa2f40579ea6d51198b6cc7fcd5666f1682e8. Re-derive with `--rev 41f7d91d052 --digest`; two runs byte-identical.
- Deviation from done-when, deliberate: NOT published to qa-reports. A lone-file `main/<sha>` entry would become the standing (first-write) entry for that commit and shadow a later complete qa:refresh (cat-harness qa-reports skill, bean 3hk4). A deterministic census needs no stored copy. Publish with the C4 qa:refresh when that lands.
- Correction: library lexical sorry/axiom is 0/12, not 1/24; the analysis counted tokens quoted inside docstrings (B1HyperbolicRowsTheorem, LpDualityHypothesisClass history blocks). Decls 44,908 lib / 7,856 siblings (different heuristic from the analysis's 45,889/6,031; compare like with like).


**Digest correction (same session):** the census JSON records producerSha256, so the digest depends on the script version. The figure 8175b24e… in commit 659995e91 and the 76548b05… above were for earlier revisions of the script. Against the script as merged (sha256 prefix 1dde686b0da1): `--rev 41f7d91d052 --digest` = 9753fa6304f067753932b66d2e33705b57e031ee83e753cd97ed7150d31d5cb8. Totals unchanged.
