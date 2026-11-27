import Mathlib.Tactic

/-!
# The n − p electromagnetic term with its own length: the two-scale class

Bean `qou-mbfv` (the energy-to-length gap of the nucleon split). Context:
`NucleonSplitScaleRatio` (#9654) proves that if the flavour term and the electromagnetic term of
`m_n − m_p` are the *same* energy map `E` times two numbers, their ratio is `−2L/(a·Q)` for every
`E`. Its scope note leaves open the class in which the electromagnetic term is a Coulomb energy
`f · a · Q · ℏc / r` with a length `r` that is not `ℏc/E`. This file states that class and proves
the three facts it needs.

All quantities are elements of an arbitrary field. No logarithm, no square root, no numerical value
and no measured constant enters.

## Notation

* `f` — the Coulomb shape factor of the 0s state (`E_C · r / Q²`; the q-Hankel value is #9699).
* `a` — the coupling (`α_em`), `Q` — the n − p charge-pair factor (`1/3`, probe of #9654).
* `hc` — the product `ℏ_q c_q`, `M` — the model nucleon rest energy, `D` — the radius factor
  `r = D · ℏ_q c_q / M` of `EnergyLengthMap` (#9697).
* `E₁` — a model gap energy, `ε = E₁ / M`; the SU_q(2) route sets `D² = q / (2ε)`.

## What is proved

* `coulomb_hc_cancels`: with `r = D · hc / M`, the Coulomb term is `f·a·Q·M / D`. The action–speed
  product cancels, so the electromagnetic term needs only the dimensionless `D` and the rest energy.
* `coulomb_sq_of_casimir`: on the SU_q(2) route the square of the Coulomb term is
  `2·f²·a²·Q²·M·E₁ / q`. The electromagnetic scale is the **geometric mean** of the rest energy and
  the gap, not either one alone.
* `ratio_sq_two_scale`: with flavour term `2L·E₀` and gap `E₁ = c·E₀`, the squared ratio of the two
  terms is `2·q·L²·E₀ / (f²·a²·Q²·M·c)`. It depends on `E₀ / M`, so this class is **outside** the
  one-scale class of `NucleonSplitScaleRatio`; the 27–44× verdict of #9654 does not apply to it.

## What is NOT claimed

* Any value of `D`, `E₁`, `c`, `M` or `E₀`. The gap `E₁` is the open input (§9 of
  `docs/audits/2026-11-27-energy-length-radius-routes.md`).
* That the SU_q(2) relation `D² = q/(2ε)` holds for the nucleon; it is a hypothesis here.
* Anything about the magnetic channel, whose `r⁻³` coefficient needs a strand mass not on record.
-/

namespace QOU.Nuclear.NucleonSplitTwoScale

variable {R : Type*} [Field R]

/-- Coulomb term `f · a · Q · hc / r` of a charge structure `Q` in a state of radius `r`. -/
def coulombTerm (f a Q hc r : R) : R := f * a * Q * hc / r

/-- The radius on the energy-to-length map: `r = D · hc / M`. -/
def radius (D hc M : R) : R := D * hc / M

/-- **The action–speed product cancels.** -/
theorem coulomb_hc_cancels (f a Q hc D M : R) (hhc : hc ≠ 0) (hD : D ≠ 0) (hM : M ≠ 0) :
    coulombTerm f a Q hc (radius D hc M) = f * a * Q * M / D := by
  unfold coulombTerm radius
  field_simp

/-- **SU_q(2) route: the electromagnetic scale is the geometric mean of `M` and `E₁`.**
Hypothesis `hD : D² · 2 · E₁ = q · M` is `D² = q / (2ε)` with `ε = E₁ / M`, cleared of
denominators. -/
theorem coulomb_sq_of_casimir (f a Q D M E₁ q : R) (hD0 : D ≠ 0) (hq : q ≠ 0)
    (hD : D ^ 2 * (2 * E₁) = q * M) :
    (f * a * Q * M / D) ^ 2 = 2 * f ^ 2 * a ^ 2 * Q ^ 2 * M * E₁ / q := by
  rw [div_pow, div_eq_div_iff (pow_ne_zero 2 hD0) hq]
  linear_combination (-(f ^ 2 * a ^ 2 * Q ^ 2 * M)) * hD

/-- **The two-scale ratio depends on `E₀ / M`.** Flavour term `2L·E₀`, electromagnetic term
`C` with `C² = 2 f² a² Q² M E₁ / q` and gap `E₁ = c · E₀`. -/
theorem ratio_sq_two_scale (f a Q M E₀ c q L C : R) (hf : f ≠ 0) (ha : a ≠ 0) (hQ : Q ≠ 0)
    (hM : M ≠ 0) (hE : E₀ ≠ 0) (hc : c ≠ 0) (hq : q ≠ 0)
    (hC : C ^ 2 = 2 * f ^ 2 * a ^ 2 * Q ^ 2 * M * (c * E₀) / q) :
    (2 * L * E₀ / C) ^ 2 = 2 * q * L ^ 2 * E₀ / (f ^ 2 * a ^ 2 * Q ^ 2 * M * c) := by
  rw [div_pow, hC]
  field_simp

end QOU.Nuclear.NucleonSplitTwoScale
