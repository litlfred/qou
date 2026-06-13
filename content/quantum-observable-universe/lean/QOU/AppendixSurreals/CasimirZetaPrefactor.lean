import Mathlib.NumberTheory.LSeries.HurwitzZetaValues
import Mathlib.Tactic

/-!
# QOU.AppendixSurreals.CasimirZetaPrefactor — the π²/720 prefactor's arithmetic core

Stage B of the `N_⊙`-construction workplan
(`docs/workplans/2026-06-12-n-odot-construction-scoping.md`) for
[`conj:casimir-epsilon-vacuum`](../../../quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md).

The leading parallel-plate Casimir energy per unit area is
`−(π²ℏc/720)·d⁻³`. Under the free-field ↔ disjoint-unknot
identification (audit `2026-06-01-casimir-free-field-disjoint-grounding.md`),
the mode-count functional is the bare disjoint-unknot count (the unique
`n`-stable functional, `CasimirNStability.lean`), carrying no `y_λ`
Hecke weighting, so the prefactor is `q`-free and reduces to

  `(π²/6) · |ζ(−3)|  =  (π²/6) · (1/120)  =  π²/720`,

where `π²/6` is the transverse (`k_⊥`) geometric factor and
`ζ(−3) = 1/120` is the regularised cubic mode-sum.

This file formalises the **number-theoretic core** of that prefactor:

* `riemannZeta_neg_three : riemannZeta (−3) = 1/120`, from Mathlib's
  `riemannZeta_neg_nat_eq_bernoulli'` together with
  `bernoulli' 4 = −1/30`. Previously the value entered the witness only
  as a 40-digit numerical `mp.zeta(-3)` check; it is now a Mathlib
  theorem.
* `casimir_prefactor_factorization : (π²/6)·(1/120) = π²/720`.

**Honest scope.** What is machine-checked here is (i) the exact value
`ζ(−3) = 1/120` and (ii) its combination with the geometric factor into
`π²/720`. What is **not** formalised — and is not elementary — is the
ζ-regularisation step itself (the identification of the divergent
cubic mode-sum `Σ n³` with `ζ(−3)`); the regulator-independence of that
identification is checked numerically in
`folio-assistant/computations/casimir_n_unknot_construction.py` (the
exponential-cutoff route gives the same `1/120` via the same
`B₄ = −1/30`). And the categorical mode-count object `N_⊙(A, d)` — the
genuine blocker of the conjecture (Stage C) — is not constructed here.
This file pins one input; it does not close the conjecture.

Ref: [casimir1948] https://dwc.knaw.nl/DL/publications/PU00018547.pdf
-/

namespace QOU.AppendixSurreals

open scoped Real

/-- **`ζ(−3) = 1/120`.** The Riemann zeta value at `−3`, from Mathlib's
negative-integer Bernoulli formula `riemannZeta (−k) = −B'_{k+1}/(k+1)`
with `B'_4 = −1/30`. This is the regularised value of the cubic mode
tower `Σ_{n≥1} n³` that sets the Casimir prefactor. -/
theorem riemannZeta_neg_three : riemannZeta (-3 : ℂ) = 1 / 120 := by
  have h := riemannZeta_neg_nat_eq_bernoulli' 3
  have h3 : ((3 : ℕ) : ℂ) = 3 := by norm_num
  rw [h3] at h
  rw [h]
  norm_num [bernoulli'_four]

/-- The real part of `ζ(−3)` is the rational `1/120` used downstream in
the (real-valued) energy prefactor. -/
theorem riemannZeta_neg_three_re : (riemannZeta (-3 : ℂ)).re = 1 / 120 := by
  rw [riemannZeta_neg_three]
  norm_num

/-- **Prefactor factorisation.** `(π²/6) · |ζ(−3)| = π²/720`: the
transverse geometric factor `π²/6` times the regularised cubic
mode-sum `|ζ(−3)| = 1/120` is the textbook Casimir energy prefactor.
The right-hand side is `q`-free — no Hecke `y_λ` enters, because the
leading-order modes are disjoint unknots. -/
theorem casimir_prefactor_factorization :
    (π ^ 2 / 6) * (1 / 120) = π ^ 2 / 720 := by ring

/-- The prefactor is strictly positive (its sign as a *force* is fixed
separately by the `∂_d` of the energy; here we record the magnitude is
nonzero, so the leading Casimir term does not vanish). -/
theorem casimir_prefactor_pos : 0 < π ^ 2 / 720 := by positivity

end QOU.AppendixSurreals
