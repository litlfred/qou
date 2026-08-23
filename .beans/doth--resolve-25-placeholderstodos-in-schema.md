---
# doth
title: Resolve 25 placeholders/TODOs in schema
status: completed
type: task
priority: normal
created_at: 2026-06-22T02:25:52Z
updated_at: 2026-07-05T05:05:00Z
---

resweep 2026-06-22: honest counter = 22 actionable (claimed 25) via scripts/count-actionable-placeholders.ts.

resweep 2026-06-23 (#2637): honest actionable = 22 (claimed 25) — roughly ACCURATE; the one genuinely large backlog item. See docs/audits/2026-06-23-placeholder-bean-resweep.md.

finding 2026-06-24: the ~7 actionable items are all bib-metadata verification TODOs in content/schema/references.ts (verify exact title/authors/pages/DOI for: kashiwara Duke 1990 + CMP refs, Carter arxiv math/0008040, Pawlowski-Leitner 2009, Chlouveraki HDR 2016). These need DOI/arxiv/source lookup — BLOCKED in this sandbox (agent proxy denies doi.org/api.crossref.org/export.arxiv.org with 403; only package registries are allowlisted). Anti-fabrication bib discipline forbids guessing the metadata, so these are bib-human-review items (route via local/bib-human-review, assign @litlfred), NOT a mechanical drain. Not drainable without web access. (The '22' counts placeholder doc-tokens; real TODO refs ≈ 5-7.)

resweep 2026-06-24 (honest counter, PR hygiene): **uncited-sorry = 0 corpus-wide**; this title count is a raw grep and is badly inflated. Honest actionable count for this scope + the full per-bean table in docs/audits/2026-06-24-placeholder-bean-count-resweep.md. Remaining TODO/FIXME are intentional markers (-- TODO upstream: on proved lemmas, witness-deps, research notes), NOT actionable placeholders — do not "drain a count" by removing them. Re-title/close is owner-only.

> **Resolved 2026-07-05 (swarm 1).** Triaged: no agent-tractable prose/metadata placeholders remain (already drained by prior sessions #2649/#2654/#2637/#2796); residual = author DOI/edition decisions, documented as deferred. Audit merged in PR #3339.

<!-- recovered 2026-08-23 from orphaned file `doth--resolve-25-placeholders-todos-in-schema.md` (no front-matter; invisible to the tracker) -->

## Result (2026-06-23, session nifty-cerf, PR #2649)

Actionable 22 → **12** via two background bib-verification agents over
references.ts. Full sourced findings: docs/audits/2026-06-23-bibliography-doi-verification-doth.md.

**Resolved (10):** chlouveraki2016-hdr (title + HAL URL tel-01411063);
faddeev1995 (title finding — entry data was already correct);
halverson_ram_1998 (year 1998→1996); bertsimas1997/majid1995/murasugi1996
(ISBN confirmed); abel1826/frobenius1898/rogers1907/klein1884 (pre-DOI
archival — PLACEHOLDER was mislabeled, reworded to settled).

**HIGH-VALUE BUGS FOUND (await author decision, 12 remaining markers):**
- kashiwara1990-cmp2 DOI BF02100009 → resolves to a **WITTEN** paper; correct
  is Kashiwara DMJ 73(2) 1994, DOI 10.1215/S0012-7094-94-07317-1.
- kashiwara1990-duke DOI is a spurious 1990 vol-61 slot; correct is Kashiwara
  DMJ 71 (1993) 839–858, DOI 10.1215/S0012-7094-93-07131-1.
  (Both also appear inline in 3 .lean files — needs coordinated sync.)
- wenzl1988b DOI BF01393839 → a number-theory regulator paper (not Wenzl);
  correct Wenzl DOI not found. wenzl1988c BF01388470 → unresolved.
- carter-leal-saliola-2000 is actually single-author R. J. Marsh (id is a
  misidentification; used as a cite key in 2 files).
- pawlowski-leitner-rep UNVERIFIED (no citable id); sibling leitnerpawloski2004
  also mis-recorded (math/0409565 = Unital Grobner Bases, Leitner & R. Pawloski).
- drinfeld1985/habiro2000/james1984 — not re-verified this session / edition
  ambiguity (kept flagged honestly).

CAVEAT: sandbox 403-blocked all DOI landing pages; confirmations are
link-title-level. Resolve DOIs directly before any swap lands. Pending human close.

## Update (2026-06-24) — author-authorized A+B+C applied; 12 → 9

Author OK'd Groups A (Kashiwara DOI fixes + .lean sync), B (carter→marsh2000),
and supplied arXiv math/0409565 for C. Kashiwara cmp2's DOI was resolving to a
Witten paper; both corrected. carter-leal-saliola renamed to marsh2000 (single
author R. J. Marsh). leitnerpawloski2004's fabricated title fixed to "Unital
Gröbner Bases…" (corpus + local PDF verified); pawlowski-leitner-rep kept flagged
(PDF-verified NOT math/0409565). 9 markers remain (off-sandbox DOI resolution /
author input). See docs/audits/2026-06-23-bibliography-doi-verification-doth.md.

## Update (2026-06-24) — pawlowski-leitner-rep agent-mistake corrected; 9 → 7

Author clarified there is one Pawloski-Leitner paper (the uploads arXiv =
math/0409565 = leitnerpawloski2004); pawlowski-leitner-rep was a fabricated
split. Rewired its citations to leitnerpawloski2004, fixed 6 wrong-title inline
.lean comments, deprecated the stub entry + ledger. wenzl1988b/c kept (real,
widely-cited; only DOIs wrong). schema actionable 7 remain (off-sandbox DOI /
author input).

resweep 2026-06-24 (honest counter, PR hygiene): **uncited-sorry = 0 corpus-wide**; this title count is a raw grep and is badly inflated. Honest actionable count for this scope + the full per-bean table in docs/audits/2026-06-24-placeholder-bean-count-resweep.md. Remaining TODO/FIXME are intentional markers (-- TODO upstream: on proved lemmas, witness-deps, research notes), NOT actionable placeholders — do not "drain a count" by removing them. Re-title/close is owner-only.

> **Resolved 2026-07-05 (swarm 1).** Triaged: no agent-tractable prose/metadata placeholders remain (already drained by prior sessions #2649/#2654/#2637/#2796); residual = author DOI/edition decisions, documented as deferred. Audit merged in PR #3339.
