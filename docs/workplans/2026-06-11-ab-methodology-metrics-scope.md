# A/B methodology metrics — scope

**Date:** 2026-06-11 · **Goal:** measure first-draft proof quality before
vs after the AlphaProof-Nexus methodology adoption, from the repo's own
append-only QA history — the empirical artifact for the
symbiotic-authoring / DeepMind conversation
([`docs/outreach/symbiotic-proof-authoring-note.md`](../outreach/symbiotic-proof-authoring-note.md)).

## Why this is non-fakeable

Every `.qa.json` criterion entry is append-only and carries `result`,
optional `score`, `reviewer` (script/agent id), `reviewed_at` (ISO
timestamp), `reviewed_sha`, and `field_hash` (content hash judged). A
verdict cannot be retro-edited without breaking its hash chain. Session
attribution exists independently via commit trailers (and the #2115
session archiver links full transcripts). Neither side of an A/B claim
has to be taken on faith — the table is recomputable by anyone.

## Cohort and adoption-date definition

- **Unit:** content block with a Lean obligation (theorem / lemma /
  proposition / corollary / definition).
- **Cohort key:** first-commit date of the block's `.lean` sibling
  (`git log --diff-filter=A`), bucketed by week.
- **Adoption events** (each its own A/B cut, detected from data, not
  memory): first corpus-wide appearance of (a) `proof-statement-integrity`
  verdicts (SafeVerify-style gate), (b) `proof-rater-*` scored verdicts
  (good-gap/bad-gap rater). Detection rule: min(`reviewed_at`) per
  criterion across all sidecars. No hand-picked dates.

## Metrics (first-verdict = the entry with minimal `reviewed_at` per criterion per block)

| id | metric | reads |
|----|--------|-------|
| M1 | first-verdict pass rate of `proof-statement-integrity` per cohort | sidecars |
| M2 | first-verdict score distributions of `proof-rater-{strategy-clarity, goal-plausibility}` | sidecars |
| M3 | sorry-citation compliance at block's first commit (`-- Ref:` present) | git + lean |
| M4 | revisions-to-green: entries appended per criterion until first `pass` | sidecars |
| M5 | axiom/`sorry` growth per cohort (from `proof-no-bare-sorries`, `proof-no-axiom-growth`) | sidecars |

## Confounds (stated up front; the writeup must carry all of these)

1. **Model-version drift** — agent capability improved over the same
   period. Mitigation: stratify by model where attributable (session
   trailers → #2115 archive metadata), and report the adoption effect
   *within* model strata where sample permits.
2. **Block-difficulty drift** — later blocks may be harder (Phase 5
   material) or easier (glossary). Mitigation: stratify by chapter and
   block kind; report per-stratum deltas.
3. **Checker-version drift** — criteria themselves evolved. Mitigation:
   first-verdict-only (never re-runs), and report checker id per entry.
4. **Survivorship** — deleted blocks leave the corpus. Mitigation: walk
   git history for sidecars deleted before HEAD, include their first
   verdicts.

## Deliverable + effort

`computations/ab_methodology_metrics.py` → witness with
per-cohort tables + adoption-cut deltas + stratified views; one audit doc
interpreting it. Effort: ~1 session once this scope is approved (the
heavy part is the git-history walk for M3/M4/survivorship). Output feeds
both the methodology paper and the DeepMind thread.

## Open scope decisions (owner)

1. Include voice/canonical axes in a secondary table, or proofs only?
2. Publish raw per-block tables, or cohort aggregates only (privacy of
   failure attribution is not a concern in a single-author repo, but
   table size is)?
