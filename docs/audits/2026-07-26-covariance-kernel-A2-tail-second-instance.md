# Covariance-kernel epic (`qou-x631`) — second (TAIL) instance: `ν_{n−1}` carrier reduction + the sign ONSET `n₁ = 8`

**Date:** 2026-07-26 · **Branch:** `claude/covariance-tail-second-instance-2026-07-26` · **Tier:**
derived carrier reduction + honest refinement of (TAIL) (exact `Fraction` verification `n ≤ 25`) ·
**Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged (2/7). **Epic:**
`qou-x631`, attack `qou-ogrk` (A2), (TAIL) sub-target — follow-up to
[`…-tail-first-instance.md`](2026-07-26-covariance-kernel-A2-tail-first-instance.md).

## Derived carrier classification for `v = n−1`

A cell's hook has length `n−1` iff it excludes exactly one cell. Exhaustive classification
(verified `n ≤ 25`):

| shape | carrier cell | data |
|---|---|---|
| two-corner `(a, 2, 1^c)`, `a ≥ 2`, `a+c = n−2` | `(0,0)` | `f = n!/((n−1)·a·(c+2)·(a−2)!·c!)`, `ω₃ = Q(a−1)+Q(c+1)−C(n,2)` |
| row `(n)` | `(0,1)` | `f = 1`, `ω₃ = Q(n−1)−C(n,2)` |
| column `(1^n)` | `(1,0)` | `f = 1`, same `ω₃` (transpose) |

No other carriers (any other cell's hook excludes ≥ 2 cells — e.g. `(0,2)` already excludes
`(0,0),(0,1)`). The resulting finite-sum **reduction formula for `ν_{n−1}` matches the full
`p(n)`-partition enumeration exactly** (Fraction equality, every `n ≤ 25`)
([probe](../../computations/deltalambda/wlambda_covariance_epic_A2_tail_second_instance_probe.py),
[witness](../../computations/deltalambda/wlambda-covariance-epic-A2-tail-second-instance.witness.json)).

## The sign ONSET — the honest refinement of (TAIL)

> `ν_{n−1} = 0` at `n = 4`; **negative for `n = 5, 6, 7`**; positive for all `8 ≤ n ≤ 25`.

So per-depth tail positivity `ν_{n−j} > 0` holds only **past an onset `n_j`**: `n₀ = 4` (from
the `ν_n` closed form's `(n−3)` factor), `n₁ = 8` (here). Consequences for the (TAIL) statement:

- The (TAIL) constant is genuinely `> 2`: at `n = 5..7` the value `v = n−1` lies deep in the
  naive "tail" (`v > n/2`) yet `ν_v < 0`. The conjecture must be carried with per-`n` thresholds
  `T(n)` (as the [sign-structure witness](2026-07-26-covariance-kernel-A2-nu-sign-structure.md)
  already records: `T(n)/n ≤ 0.72` observed) — **not** with a universal `n/2 + 2`-type constant.
- Nothing here contradicts recorded data (the per-`n` patterns already showed these signs); the
  onset makes explicit what a proof must target: **asymptotic per-depth positivity with
  computable onsets**, exactly the shape the carrier method delivers (each `ν_{n−j}` is a finite
  `j`-indexed family sum whose large-`n` positivity is a finite check of leading terms).

## Where the (TAIL) program stands

- `ν_n`: closed form, `≥ 0` all `n`, onset `n₀ = 4` — **derived** (first instance).
- `ν_{n−1}`: exact finite reduction, onset `n₁ = 8` — **derived** (this audit).
- General pattern to prove: for each `j`, `ν_{n−j} > 0` for `n ≥ n_j`, with `n_j` computable
  from the `j`-fold carrier families; then (TAIL) with explicit thresholds + the bulk bound ⇒
  FMP ⇒ A2 (last step machine-checked, `covLnF_nonpos_of_FMP`).

## Honest scope

The carrier classification and reduction are derived and exactly verified (`n ≤ 25`); the
general-`n` carrier proof is elementary (hook-exclusion counting), not yet Lean. The onset
finding is a *refinement* of the (TAIL) conjecture's statement, not a refutation of any recorded
claim. (TAIL)/FMP/A2/kernel remain open; nothing wired.
