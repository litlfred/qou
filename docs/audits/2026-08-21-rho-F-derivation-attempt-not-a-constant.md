# ρ_F(⁴He) derivation attempt — ρ_F is not a categorical constant; "2" is the rounded ⁴He value

**Date:** 2026-08-21 · **Arc:** bk-crossing-coordination, item 2 (surviving route) · **Bean:** `qou-2row` · **PR:** #5389
**Probe:** [`computations/he4_rho_F_two_row_stratum_search.py`](../../computations/he4_rho_F_two_row_stratum_search.py)
**Witness:** [`computations/he4-rho-F-two-row-stratum-search.witness.json`](../../computations/he4-rho-F-two-row-stratum-search.witness.json) (allPassed)
**Follows:** [`2026-08-21-he4-rho-F-cpt-mechanism-refuted.md`](2026-08-21-he4-rho-F-cpt-mechanism-refuted.md)
**Discipline:** scope-(a); genuine derivation attempt, honest wall; no fit; no wiring; q₀ proton-anchored.

After refuting the CPT alt-block mechanism (which showed any ρ_F derivation must live in the two-row
stratum), this is the honest attempt to *derive* ρ_F — and it reaches a structural wall.

## Attempt 1 — a fit-free two-row-stratum ratio

None of the natural ratios of the canonical two-row Frobenius weights reproduces the target
`ρ_F(⁴He) = B_AME/(m_e·A·8G) = 1.889`: `Σy/y[12]=3.35`, `Σ_2row y/y[12]=2.35`,
`(y[12]+y[11,1])/y[12]=1.78`, `Σ(yχ)/(yχ)[12]=16.8`, `tr_M/y[12]=40.6`. The closest (1.78) is −5.7%
off and cherry-picks 2 of 7 blocks — a selection, i.e. a fit.

## Attempt 2 (decisive) — ρ_F is not a constant

`ρ_F = B_AME/(m_e·A·8G)` across the doubly-magic light nuclei (the formula's stated domain):

| nucleus | (Z,N) | ρ_F (obs) | ρ_F (strong, +Coulomb) |
|---|---|--:|--:|
| ⁴He | (2,2) | **1.889** | 1.948 |
| ¹⁶O | (8,8) | **2.130** | 2.390 |
| ⁴⁰Ca | (20,20) | **2.284** | 2.803 |

**ρ_F drifts monotonically upward with A (1.89 → 2.28, a 21% spread), and adding back the Coulomb
energy makes the drift worse (1.95 → 2.80)** — because Coulomb grows ~Z² faster than the binding. So
the integer "2" is the *rounded ⁴He value*, not a universal categorical prefactor; `B = ρ_F·m_e·A·8G`
with a fixed ρ_F=2 is a light-nucleus approximation that degrades as A grows.

## Verdict — the derivation target is ill-posed, and that is why nothing closes

`ρ_F` is a per-nucleus, A-dependent effective prefactor. There is no single categorical constant to
derive:

1. the CPT alt-block route is refuted (empty block);
2. no fit-free two-row-stratum ratio reproduces 1.889;
3. the value itself is not "2" away from ⁴He — it grows with A.

A genuine derivation would have to reproduce the **A-dependence** `ρ_F(A)` (1.89 → 2.28), a strictly
harder target than "which integer," and no categorical quantity in the corpus supplies it. Honest
wall: ρ_F stays an empirical, A-dependent magic-shell prefactor; `ρ_F(⁴He)=2` is a ⁴He-specific
rounding. This does not close `conj:kashaev-density-equals-sdp-multiplicity`; it removes the
"which integer" framing and re-poses the open problem as deriving `ρ_F(A)`.
