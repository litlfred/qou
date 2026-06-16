# QA backlog axis-1 (canonical) — staleness audit + remaining real fails

> Companion to PR `claude/qa-backlog-canonical-onevoice-2026-06-02`.
> Surveys all **11 open canonical-discipline fails** in the QA
> sidecars as of 2026-06-02. **Headline: 7 of 11 are definitively
> stale** (work fixed since 2026-05-25 audit, sidecar `result: 'fail'`
> entries never refreshed); 4 may be real and surface here for
> owner / dedicated-session triage.

## Method

For each open `result: 'fail'` entry on a `canonical-*` criterion,
the latest historical entry was read from the corresponding `.qa.json`,
then the current file content was checked against the failure
`evidence`. Stale = the issue described in the evidence is no longer
present at the current path / content. Real = still reproducible.

## Per-fail triage

| # | criterion | block (current location) | reviewed | verdict |
|---|----------|-------------------------|----------|---------|
| 1 | canonical-script-not-deprecated | `binding-scale-catalan` (mass-theory) — script `computations/catalan_binding.py` | 2026-05-26 | **stale** — script refactored, no `mass_endomorphism` import |
| 2 | canonical-script-not-deprecated | `schur-weyl-mass-decomposition` (mass-theory) — script `atom_level_wedderburn_tower.py` | 2026-05-26 | **stale** — script refactored |
| 3 | canonical-script-not-deprecated | `mass-volume-factorization` (mass-theory) — script `d_density_derivation.py` | 2026-05-26 | **stale** — script refactored |
| 4 | canonical-script-not-deprecated | `six-term-per-derivation-weights` (mass-theory) — script `sweeps/paper_six_term_isotope_sweep.py` | 2026-05-26 | **stale** — script refactored |
| 5 | canonical-script-not-deprecated | `e-infinity-page-identifications` (mass-theory) — script `atom_level_wedderburn_tower.py` | 2026-05-26 | **stale** — script refactored (same script as #2) |
| 6 | canonical-no-numerology | `kashaev-density-equals-sdp-multiplicity` (mass-theory) — was in braids-and-knots/ | 2026-05-25 | **stale** — `grep "numerical coincidence"` returns 0 matches |
| 7 | canonical-witness-pinned | `weak-symmetric-normalization.md:99` | 2026-05-26 | **stale** — `:val[q_0]` already carries `witness=computations/q-pinning-50-digit.witness.json` |
| 8 | canonical-cal4-acknowledged | `q-zero-complex-extension.ts` (mass-theory; was stochastic-mechanics) | 2026-05-25 | **may be real** — block is `kind: "proposition"`; the CAL-4-equivalent caveat lives in `authorNotes: [{ kind: "status", body: "Research-grade infrastructure (PR #1127)…" }]`; per CLAUDE.md §4d author-notes are render-skipped by default, so the criterion's "acknowledgment banner" requirement may not be satisfied by an authorNote alone |
| 9 | canonical-cal4-acknowledged | `lusztig-vs-hermitian-bar.ts` (mass-theory; was stochastic-mechanics) | 2026-05-25 | **may be real** — same pattern as #8 |
| 10 | canonical-dilogarithm-context | `borromean-bloch-group-element.md` (mass-theory; was braids-and-knots/) — Φ_q at lines 70, 74, 130, 158 | 2026-05-25 | **may be real** — Φ_q occurrences remain; whether each is correct context (free spectrum) vs incorrect (binding) needs per-line audit |
| 11 | canonical-dilogarithm-context | `pachner-pentagon-borromean.md` (mass-theory; was braids-and-knots/) — Φ_q at lines 4, 42, 45, 50, 58, 67, 111, 130 | 2026-05-25 | **may be real** — Φ_q occurrences remain; same per-line audit needed |

## Recommended owner actions

1. **Re-run the canonical-watcher QA sweep** (`/integration-audit canonical` or `bun run pipeline/qa-sweep.ts content/ --only 'canonical-*'`) to refresh entries #1-7 to `result: "pass"`.
2. **Triage #8 + #9** — decide whether `authorNotes`-only CAL-4 acknowledgment counts as an "acknowledgment banner" per the `canonical-cal4-acknowledged` checker, OR add an explicit `.md`-prose banner per §3b-cond pattern. Per CLAUDE.md §4d the latter is the correct route when the conditional is part of the statement (not author tracking).
3. **Triage #10 + #11** — per-line audit of `Φ_q` occurrences in the two `borromean-*` / `pachner-*` blocks against the [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) Φ_q (Faddeev, free spectrum) vs `Li_2^q` (Rogers, binding) context-sorting rule.

## Pattern observation (cross-session)

This is the **third consecutive QA-backlog axis** (Lean discharge queue, integration-watcher Lean / canonical) where ≥ 50 % of "open" entries are stale because content has been fixed since the audit ran but the sweep has not been re-executed. The systemic issue is sidecar refresh cadence, not content debt.

Suggestion (out of scope for this branch): make `/integration-audit <axis>` a CI cron job, e.g. nightly, so sidecars stay closer to live content state.

## Cross-refs

- [PR #1720 Lean discharge audit](https://github.com/litlfred/qou/pull/1720) — same staleness pattern, 5/8 items
- [`docs/audits/2026-06-02-lean-discharge-queue-staleness-audit.md`](../audits/2026-06-02-lean-discharge-queue-staleness-audit.md) — companion audit on the Lean discharge queue
- CLAUDE.md §4d "authorNotes vs scholarly prose" — relevant to #8, #9
- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) — Φ_q vs `Li_2^q` rule for #10, #11
