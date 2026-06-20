# `docs/audits/` — Index + staleness assessment

**Generated 2026-05-24** during `/integration-watch all` session,
canonical-iw audit-currency follow-on.

## Scope

`docs/audits/` contains **353 markdown files** + **37 `.witness.json`
sidecars** (390 total as of 2026-05-24, plus the new `_deprecated/`
folder added by this commit).

This index serves three purposes:

1. **Catalogue** the audit corpus by date cluster, with file counts
   and sample titles.
2. **Assess staleness risk** per cluster (high / medium / low).
3. **Recommend next actions** for future deprecation tranches.

This commit creates only the index + the `_deprecated/` folder
infrastructure. It does **NOT** move files — per-file deprecation
review is a phased follow-up tranche to avoid mass-archiving
historically-valuable content without per-doc judgment.

## Date histogram

| Date cluster | `.md` count | Sample title | Staleness risk |
|--------------|------------:|--------------|----------------|
| 2026-05-01 | 17 | `2026-05-01-base-cases-audit` | **HIGH** — early phase 5 churn; many concrete actions integrated since |
| 2026-05-02 | 40 | `2026-05-02-4-parallel-followup-synthesis` | **HIGH** — largest single-day cluster; synthesis docs likely superseded |
| 2026-05-03 | 15 | `2026-05-03-T2T3-derivation-chain-analysis` | **HIGH** — derivation-chain analyses largely refactored into the chain audit |
| 2026-05-04 | 14 | `2026-05-04-alpha-shift-torus-multiplicative-chain` | **HIGH** — α-shift work has multiple subsequent iterations |
| 2026-05-05 | 13 | `2026-05-05-categorical-chain-gamma-to-six-term` | **HIGH** — six-term formula is now a `thm:` block |
| 2026-05-06 | 10 | `2026-05-06-close-321-weinberg-gap` | **HIGH** — Weinberg gap was a focus area, now mostly closed |
| 2026-05-07 | 3 | `2026-05-07-borromean-axial-coupling-fix` | **MEDIUM** — Borromean is current research; check each |
| 2026-05-08 | 15 | `2026-05-08-compute-audit` | **MEDIUM-HIGH** — compute-audit has live `compute-audit-scan.witness.json`, but the doc may be a snapshot |
| 2026-05-09 | 21 | `2026-05-09-A-operator-rank-structure` | **MEDIUM** — May 9 closure wave (Path A pipeline) — some docs may be canonical statements of the closures, others working notes |
| 2026-05-10 | 4 | `2026-05-10-1ppb-workplan-update` | **MEDIUM** — 1ppb workplans have v6+ iterations |
| 2026-05-11 | 11 | `2026-05-11-1ppb-gap-narrowing-plan` | **MEDIUM** — same 1ppb workplan chain |
| 2026-05-12 | 8 | `2026-05-12-1ppb-implementation-plan` | **MEDIUM** — same |
| 2026-05-15 | 5 | `2026-05-15-a-minus-2-q-substrate-derivation` | **MEDIUM** — substrate-derivation still relevant; check each |
| 2026-05-16 | 17 | `2026-05-16-compound-shift-nf-impl` | **MEDIUM** — compound-shift work continues |
| 2026-05-17 | 30 | `2026-05-17-1ppb-workplan-v1-refined` | **MEDIUM-LOW** — explicit `-v1-refined` suggests later vN exists |
| 2026-05-18 | 37 | `2026-05-18-1ppb-workplan-v6-compute-precision` | **LOW** — recent, mostly current |
| 2026-05-19 | 28 | `2026-05-19-c-k-comprehensive-reference` | **LOW** |
| 2026-05-20 | 9 | `2026-05-20-compute-optimization-roadmap` | **LOW** |
| 2026-05-22 | 15 | `2026-05-22-1ppb-compute-precision-speed-tranche` | **LOW** |
| 2026-05-23 | 12 | `2026-05-23-1ppb-gap-closure-analysis` | **LOW** — current week |
| 2026-05-24 | 3 | `2026-05-24-65-isotope-mass-table-audit` | **LOW** — today's work |
| (undated) | 26 | `2h-3a-vs-sdp-tr-m-discrepancy` | **MIXED** — pre-convention docs; each needs individual judgement |

**Total .md**: 353. **Total witness sidecars**: 37.

## Files with explicit deprecation markers (sweep-detected)

Bulk-grep for `^DEPRECATED|^SUPERSEDED|^RETRACTED|deprecated by PR` in
body content found only 3 files:

- [`2026-05-19-delta-lambda-phase5-alpha-derivation-progress.md`](2026-05-19-delta-lambda-phase5-alpha-derivation-progress.md)
- [`2026-05-19-delta-lambda-phase4-z4N-closure.md`](2026-05-19-delta-lambda-phase4-z4N-closure.md)
- [`2026-05-19-stale-witness-survey-results.md`](2026-05-19-stale-witness-survey-results.md)

These three are immediate candidates for `_deprecated/` (verify per-file
that the explicit marker is genuine deprecation, not a phrase inside a
broader discussion).

## Recommended phased deprecation tranches

| Tranche | Scope | Effort | Risk |
|---------|-------|-------:|------|
| **T1** | 2026-05-01 + 2026-05-02 clusters (57 files) — early phase-5 churn; sample-review each, deprecate the obviously-stale | ~2-3 hrs | Medium (per-file judgement needed) — **PARTIAL 2026-05-24** (13 of 57 clearly-stale workplan/status/comparison/handoff/sweep-finding/shell-aware-pair moved; ~44 remaining for follow-up) |
| **T2** | 2026-05-03 .. 2026-05-06 clusters (52 files) — derivation-chain + α-shift + Weinberg work, much integrated since | ~1.5-2 hrs | Medium — **PARTIAL 2026-05-24** (17 of 52 clearly-stale sublemma-iterations + dead-ends + workplans + n-sym/tower-mev/z-eq-n findings + kashaev-limit/r-and-kite-tails/three-pieces investigations moved; ~35 remaining) |
| **T3** | 2026-05-07 .. 2026-05-09 clusters (39 files) — Borromean / compute-audit / May-9 closure-wave docs; selectively deprecate | ~1.5 hrs | Medium-Low — **PARTIAL 2026-05-24** (11 of 39 clearly-stale workplan/batch-status snapshots + pentagon-uv-commutation closure-attempt moved; ~28 remaining; `per-irrep-pole-18-21-research-note` retained per active GAP-B-1 Lean citation) |
| **T4** | 1ppb-workplan chain (2026-05-10..12, 2026-05-16..18) — keep only the latest version per workplan family, deprecate earlier vN iterations | ~1 hr | Low (mechanical: keep latest `vN`) — **DONE 2026-05-24** (10 files moved to `_deprecated/`; v7 retained) |
| **T5** | UNDATED cluster (26 files) — pre-date-prefix convention; needs the most individual judgement | ~1.5 hrs | High (no date signal) — **PARTIAL 2026-05-24** (11 of 26 clearly-stale workplan / status snapshot / migration handoff / investigation snapshots moved; foundational analyses + the live `onepb-status-dashboard.md` retained; ~15 remaining for follow-up review) |

Tranches **T1-T4** total ~7 hours and cover most of the high-staleness
content. T5 is harder (no chronological signal) and could be deferred.

## Cross-references

- [`docs/audits/_deprecated/README.md`](_deprecated/README.md) — the
  deprecation convention itself.
- [`content/quantum-observable-universe/braids-and-knots/derivation-audit-report.md`](../../content/quantum-observable-universe/braids-and-knots/derivation-audit-report.md)
  — the *content-level* GAP-A/B/C/D audit (separate concern; refreshed
  in PRs #1075 + #1082 during the same session that produced this
  index).
- AGENTS.md §"Branch + PR workflow" §"Exception: batch audit-job runs"
  — bulk-move commits are acceptable for mechanical sweeps.

## Why phased + not bulk-move

The 353 audit files are not uniformly stale. Bulk-moving the entire
pre-2026-05-10 cluster (148 files) would archive historically valuable
content without per-file review. Per AGENTS.md "Don't add features…
beyond what the task requires" and the user directive *"once reviewed,
deprecate as needed into folder"* — the **review** step is the
discipline, not the move. This index makes the review tractable for
future tranches.

## Sibling work

- [`derivation-audit-report.md`](../../content/quantum-observable-universe/braids-and-knots/derivation-audit-report.md) (in `content/.../braids-and-knots/`):
  refreshed in PR #1075 (GAP-B-1 + GAP-B-2 closed) and PR #1082
  (GAP-A-2 refined, GAP-B-3 closed, GAP-C-1 detailed). Different
  concern from `docs/audits/`: that doc tracks the **physics** gaps
  (categorical-derivation discipline). This index covers the
  **workplan/audit** docs (sessions' working notes).
