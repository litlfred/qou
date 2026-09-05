# The complete n=9 census: the envelope is monotone, and the pointwise obstruction is *the hooks*

**Date:** 2026-09-05 · **Bean:** `qou-o6ov` · **Scope:** (a) scope-limited — n = 9 (with n = 6 as a gate). Nothing wired, no witness, no fit.

## Three results

1. **n=9 is complete at 30/30**, and the envelope `max_{b(λ)=b} tr_λ(X*X)/dim_λ` is **strictly
   decreasing across all seven interior levels** — the first time that claim rests on complete
   levels rather than dim-capped subsets.
2. **Pointwise monotonicity is refuted with exactly 6 violations, and every one of them is a hook
   sitting anomalously low in its level.** Excluding hooks, pointwise monotonicity **holds**. The
   obstruction is one family — and it is the family that already has a closed form.
3. **The `dim ≤ 50` cap that shaped this whole arc was an artifact of dense matrix products**, not a
   property of the seminormal construction.

## 3 first, because it changes how to read 1 and 2

My first straggler probe called `build`, which forms `ρ` by **dense** `dim×dim` products; one shape
at dim 189 had not finished after a long run. That is not an intrinsic cost. The Young seminormal
generators are **at most 2-sparse per row** — `sigma_csr` emits one entry for a `diag` block and two
per row for a 2×2 block — so #6710's column-wise kernel applies directly to the seminormal
representation. Measured: dim 216 goes from not-finishing to **8.6 s**.

So a good part of the tensor scaffolding built over the preceding PRs was **not strictly necessary
at n=9**. Recorded plainly because it is convenient to leave unsaid. What the scaffolding still
buys, and it is not nothing: at larger `n` the weight sectors stay bounded by multinomials while
`dim_λ` explodes, and — used here — the closed forms are **independent** cross-checks of the sparse
kernel, which is exactly what makes the gate below meaningful.

## The census

Probe: [`magnus_n9_complete_census_probe.py`](../../computations/deltalambda/magnus_n9_complete_census_probe.py).
All 30 shapes recomputed from **one** kernel rather than transcribed between runs — a census
assembled by quoting printed tables is only as good as its transcription, and this arc has already
been bitten by a figure correct where computed and stale where quoted.

**Gate:** sparse seminormal vs the reduced-Burau closed form on **all 9 hooks**, worst
`|Δ_rel| = 1.38e-64`. The straggler probe adds a second gate against `sl₃`+Kostka at dim 105–168 —
the regime the largest shapes actually live in, not only small ones.

### Envelope — every level complete

| b | envelope max per-dim | attained by |
|---|---|---|
| 1 | 4718.6197 | `(8,1)` |
| 2 | 3478.2851 | `(7,1,1)` |
| 3 | 1671.2349 | `(6,1,1,1)` |
| 4 | 981.20482 | `(5,4)` |
| 5 | 605.58457 | `(4,4,1)` |
| 6 | 211.56463 | `(3,3,3)` |
| 7 | 31.556344 | `(2,2,2,2,1)` |

**Strictly decreasing.** Both pre-registered ways the four stragglers could have broken it came back
null: `(5,2,1,1)` measured 699.33 against the 1671.23 it needed to break `b=3 > b=4`, and no `b=5`
straggler approached 981.20.

## The pointwise obstruction is entirely the hooks

| low side | b | per-dim | high side | b | per-dim |
|---|---|---|---|---|---|
| `(5,1,1,1,1)` | 4 | 581.1633 | `(4,4,1)` | 5 | 605.5846 |
| `(4,1,1,1,1,1)` | 5 | 134.6275 | `(3,3,3)` | 6 | 211.5646 |
| `(4,1,1,1,1,1)` | 5 | 134.6275 | `(3,3,2,1)` | 6 | 170.6339 |
| `(4,1,1,1,1,1)` | 5 | 134.6275 | `(3,3,1,1,1)` | 6 | 154.2493 |
| `(3,1,1,1,1,1,1)` | 6 | 14.31901 | `(2,2,2,2,1)` | 7 | 31.55634 |
| `(3,1,1,1,1,1,1)` | 6 | 14.31901 | `(2,2,2,1,1,1)` | 7 | 24.97006 |

**6 of 6 have a hook on the low side; 0 on the high side; 0 violations involve no hook at all.**
The probe *counts* this rather than leaving it to be read off the list — reading a pattern off a
printed table is how a coincidence becomes a claim.

**Why this is actionable rather than descriptive.** The obstruction to a pointwise ordering is a
single family, and it is precisely the family with a derived closed form (the reduced Burau,
#6556). A bound can therefore treat hooks separately and make a uniform statement about everything
else, instead of needing one statistic that works across all shapes — which #6669 showed no
candidate does, and #6677 showed would have to reproduce a sign-changing hook/two-row relation.

This also explains, in retrospect, the earlier observations that looked unrelated: the hook is near
the *minimum* of its level at large `b` (15× and 72× below the level max at `b=6,7`), and the
hook/two-row ratio crosses 1 — both are the same fact about hooks decaying faster than everything
else.

## What is NOT established

- **n = 9 only** (gated at n = 6). Nothing here is proved for general `n`.
- **The four stragglers rest on one kernel.** `(5,2,1,1)`, `(4,3,1,1)`, `(4,2,2,1)`, `(4,2,1,1,1)`
  have no independent second route *by construction* — that is what made them stragglers — so
  unlike every other shape in this arc they are gated but not cross-derived. Positivity holds on
  all four, which it must for a positive element.
- **Nothing here bounds anything.** These are traces of the positive element `X*X`.
- "Pointwise holds off hooks" is a statement about **this census**, not a theorem, and one size
  cannot distinguish it from an n=9 coincidence.
