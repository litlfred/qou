/-!
# QOU.Hecke.staircasePartition — staircase partition `ρ_k = (k, k−1, …, 1)`

**Sibling-resolution stub** for content block
[`def:staircase-partition`](staircase-partition.md).  The buildable
formalisation lives at
[`content/quantum-observable-universe/lean/QOU/Hecke/Staircase.lean`](../lean/QOU/Hecke/Staircase.lean)
and is compiled by `lake build QOU` via the `qou` Lake package.

This file mirrors the public-API surface of the canonical:

  * `QOU.Hecke.staircaseList : ℕ → List ℕ`
        — recursive list `[k, k−1, …, 1]`.
  * `QOU.Hecke.staircaseList_sum`
        — discharges `Partition.sum_eq = k·(k+1)/2`.
  * `QOU.Hecke.staircasePartition (k : ℕ) : Partition (k*(k+1)/2)`
        — the staircase partition `ρ_k`, self-conjugate.
  * `QOU.Hecke.staircaseStrands (k : ℕ) : ℕ := k*(k+1)/2`
        — strand-count `n_k` of the canonical β_EW operator on `ρ_k`.

Per the chapter-dir convention this file is for `.md` / `.ts` sibling
resolution only and is **not** itself part of the Lake build path
(only `content/quantum-observable-universe/lean/` is).  See the
canonical for theorems, sanity examples (`ρ_3 = (3,2,1)`), and the
`betaEWWord` construction consumed by `conj:staircase-ew-residual`.

## References

* Hoefsmit (1974), thesis, §III — staircase Specht modules.
* `computations/staircase_ew_predictions.py`
  — Python reference implementation of `beta_ew_word`.
* `docs/audits/2026-05-06-staircase-ew-residual-conjecture.md`.

-- Ref: [hoefsmit1974] Representations of symmetric groups, §III
-/

namespace QOU.Hecke

/-- Staircase partition $\\rho_k = (k, k-1, \\ldots, 1)$ -/
def staircasePartition   :=
  -- Ref: [manuscript] def:staircase-partition
  trivial

end QOU.Hecke
