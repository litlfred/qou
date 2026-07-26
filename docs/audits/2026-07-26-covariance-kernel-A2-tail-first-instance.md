# Covariance-kernel epic (`qou-x631`) — first (TAIL) instance in closed form: `ν_n = n(n−2)(n−3)·C(2n−4, n−2)/(3·n!)`

**Date:** 2026-07-26 · **Branch:** `claude/covariance-tail-first-instance-2026-07-26` · **Tier:**
derived closed form (carrier lemma + binomial-square sums; exact `Fraction` verification
`n ≤ 25`) · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged (2/7).
**Epic:** `qou-x631`, attack `qou-ogrk` (A2), (TAIL) sub-target of
[`2026-07-26-covariance-kernel-A2-nu-sign-structure.md`](2026-07-26-covariance-kernel-A2-nu-sign-structure.md).

## Result

The extreme member of the (TAIL) conjecture (`ν_v ≥ 0` for `v` past `~n/2`) is **derived in
closed form**:

> `ν_n = Cov₂(N_n, ω₃) = n(n−2)(n−3)·C(2n−4, n−2) / (3·n!)`

— manifestly `≥ 0` for all `n ≥ 3`, strictly positive for `n ≥ 4`, and **exactly zero at
`n = 3`**, reproducing the observed `ν`-pattern `-+0` at `n = 3` from the sign-structure witness.
Exact-`Fraction` verification of carriers, formula, and nonnegativity for all `n ≤ 25`
([probe](../../computations/deltalambda/wlambda_covariance_epic_A2_tail_first_instance_probe.py),
[witness](../../computations/deltalambda/wlambda-covariance-epic-A2-tail-first-instance.witness.json)).

## Derivation (referee-checkable; each step elementary)

1. **Carrier lemma.** A diagram of `n` cells has a hook of length `n` iff it is a **hook shape**
   `λ = (a, 1^{n−a})`, and the carrier is the corner `(0,0)` with multiplicity 1. (The
   `(0,0)`-hook is row 0 ∪ column 0; length `n` forces it to exhaust the diagram.) Verified
   exhaustively `n ≤ 25`.
2. **Hook-shape data.** `f^{(a,1^{n−a})} = C(n−1, a−1)`; contents are `{0,…,a−1}` and
   `{−1,…,−(n−a)}`, so `ω₃ = Q(a−1) + Q(n−a) − C(n,2)` with `Q(m) = m(m+1)(2m+1)/6`.
3. **Mean-zero reduction.** `E₂[ω₃] = 0` (proved in Lean at the scaffold), so
   `ν_n = E₂[N_n·ω₃] = (1/n!)·Σ_{k=0}^{m} C(m,k)²·[Q(k) + Q(m−k) − C(n,2)]`, `m = n−1`.
4. **Binomial-square sums** (via `k·C(m,k) = m·C(m−1,k−1)`, applied twice):
   `ΣC² = C(2m,m)`, `ΣkC² = (m/2)C(2m,m)`, `Σk²C² = m²C(2m−2,m−1)`,
   `Σk³C² = m²(m+1)/2·C(2m−2,m−1)`.
5. **Algebra.** The bracket collapses to
   `(m³ − 2m² − m + 2)/3 · C(2m−2,m−1) = (m−2)(m−1)(m+1)/3 · C(2m−2,m−1)`, i.e. the boxed
   formula. The factor `(m−2) = (n−3)` is the exact source of the `n = 3` zero.

## Why this matters

- **First proved-shaped (TAIL) instance**: the long-hook tail positivity now has an exactly
  derived anchor at `v = n`, complementing the proved even moments as the second *derived*
  ingredient of the FMP mechanism (`(TAIL) + bulk bound ⇒ FMP ⇒ A2`, the last implication
  machine-checked in `covLnF_nonpos_of_FMP`).
- **The locality mechanism works as predicted**: long hooks confine the carriers to few explicit
  families (here: exactly the `n` hook shapes), making the covariance a finite classical sum.
  The same method applies at `v = n−1` (carriers: `(a,2,1^c)` two-corner shapes + the row/column
  at cells `(0,1)`/`(1,0)`) and downward — each `v = n−j` a finite-family computation.
- **Lean route (queued)**: the carrier lemma is list-level combinatorics on the existing
  `cells`/`hookLen` machinery (`hookLen p = l.sum` forces the hook shape); the closed form is a
  finite binomial identity. Both are within the scaffold's established patterns.

## Honest scope

The closed form is **derived and exactly verified** (`n ≤ 25`); its general-`n` proof is the
5-step derivation above (elementary, not yet Lean). (TAIL) as a whole, FMP, A2, and the kernel
remain open; nothing wired.
