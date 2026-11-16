---
# qou-slvl
title: slope = q-Gevrey level in general; and the two recursions still defined-to-match
status: in-progress
pr: 8195
type: task
priority: medium
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T08:05:00Z
updated_at: 2026-10-04T15:26:09Z
parent: qou-frzo
---

Two residuals left by `qou-slpd`, both bounded.

## 1. `slope = level` is proved only at `k = 1, 2`

`QGevreyOrder` §MI-3(d) carries `slopeOneCoeff_order_one` (slope 1 → order 1 =
level 1, the degenerate touchstone) and `slopeTwoCoeff_order_half` (slope 2 →
order ½, level 2 — the first case where the readings separate). The script
`c3_w2_newton_slope_is_qgevrey_level.py` checks `k = 1, 2, 3` symbolically.

**Missing**: the general `k`. For `L_k = z^kσ − 1` the solution's nonzero
coefficients are `c_{jk} = q^{k j(j−1)/2}`, so along the subsequence

    2·log_q c_{jk} / (kj)²  =  (j − 1)/(k j)  →  1/k,

i.e. order `1/k`, level `k` = slope. ✅ **DONE 2026-08-08.** `slopeKCoeff` + `slopeKCoeff_order`: for every `k ≥ 1`,
`2·log_q c_{jk}/(kj)² → 1/k`. The two previous instances are now corollaries
(`slopeKCoeff_order_one`, `slopeKCoeff_order_half`) and the duplicated
`slopeOneCoeff`/`slopeTwoCoeff` definitions are gone. Sorry-free,
`[propext, Classical.choice, Quot.sound]`. The `d_j·d_j·q^{kj} = q^{k j²}`
induction avoids ℕ subtraction throughout.

Not in scope here: RSZ's *general* slope↔growth theorem for arbitrary operators
(ch. 5 territory). The `L_k` family is a family of witnesses, not a proof of the
general statement, and the file should keep saying so.

### Why the lacunary structure forces the subsequence

`L_k`'s solution has `c_m = 0` unless `k ∣ m`, and `IsQGevreyOrder` is a **limit**
of `2 log_q‖a_n‖/n²`, which those zeros send to `0` rather than to the order.
RSZ's actual §1.3.2 definition is a **big-O bound**, which handles zeros fine.
So the honest general statement wants the bound form:

    IsQGevreyOrderLE q s a  :=  ∃ C A, ∀ n, ‖a n‖ ≤ C * A^n * q^(s*n^2/2)

`QGevreyOrder`'s own docstring already flags this: *"The limit form above implies
a bound form and is cleaner for the slope algebra; the bound-form equivalence is
an MI-2/MI-3 refinement."* Adding `IsQGevreyOrderLE` and the one-way implication
would let the `L_k` family be stated without the subsequence dodge.

## 2. `infSideCoeff`'s recursion is still defined-to-match

`C1SeriesConvergence.infSideCoeff` — the `h_k` recursion of
`computations/qbeta/c3_w2_c1_pole_divisor.py`, the `∞`-side of the **connection
matrix** construction — is *defined* to match the script, so
`summable_infSideCoeff` certifies convergence of a stated sequence, not that
`Y_∞` is a solution.

✅ **DONE 2026-08-08 — both sides.** `zeroCoeffAt_eq_zero_iff` and
`infCoeffAt_eq_zero_iff` in `C1SeriesConvergence`, plus
`computations/qbeta/c3_w2_c1_side_recursions_derived.py` (4/4) checking that the
collections really are the coefficients and that solving them returns `gc()` and
`hc()` of `c3_w2_c1_pole_divisor.py` **verbatim**.

The interesting part was the prefactors. Neither side is a bare power series, and
the theta factors are exactly what makes the brackets polynomial, via
`θ_p(pw) = w·θ_p(w)`:

* `0`-side `y₀ = e_t(z)G(z)` with `e_t = θ_p(z)/θ_p(z/t)` gives `τe_t = t·e_t` —
  a *constant* multiplier, so the bracket is a plain power series in `z`.
* `∞`-side `y_∞ = H(z)/θ_p(z/T)` gives `τ[1/θ_p(z/T)] = (T/z)/θ_p(z/T)` and
  `τ²[…] = T²/(pz²)·/θ_p(z/T)` — monomial multipliers, and in `u = 1/z` the
  bracket is again polynomial.

So the `l1Obstruction`-style leftover does **not** recur here: it appeared for
`c1InfCoeff` precisely because that ansatz had *no* prefactor, and a pure power
series cannot annihilate an operator of nonzero slope. With the theta prefactors
in place the ansatz is the right shape and there is no leftover.

**Still open** (this is row 4, not this bean): that these series times their
prefactors are the *canonical* solutions — normalisation and uniqueness.

Relates: `qou-slpd`, `qou-c1ln` (row 3).

## Progress (PR #8195)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/C1SingularLocusAndSlopeLevelBridge.lean` (`0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 advisory` across all 7 static vacuity/borrowed-name audits) and wired into `QOU.lean`.
- [x] Verified exact rational witness in `computations/probes/c1-singular-locus-and-slope-level-bridge.witness.json` (`scriptHash: fc315c730706`, `scriptCommitSha: 17c1b41227b6c499979110fb6c31637514935ccf`, `allPassed: true`, `0` raw `float64` fields).
- [ ] Awaiting Merge Manager merge of PR #8195 (`4d59250dbada4070a6545f88b8d6f14fb94d89f6`).
