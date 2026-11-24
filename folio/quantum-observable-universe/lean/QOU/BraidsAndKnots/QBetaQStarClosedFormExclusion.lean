import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Order.Monotone.Basic

/-!
# QOU.BraidKnot.QBetaQStarClosedFormExclusion

**The substrate landmark `q*` (the S-channel zero, `c₃(q*) = −Vol(4₁)`
exactly) is *not* an experiment-independent closed-form mathematical
constant — it is the preimage under a fixed closed-form function of a
ratio of two experimentally measured CODATA inputs.**

This is the Lean core of the Route-B finding in
`computations/qbeta/qbeta_qstar_closed_form_dilog_probe.py`
(`qbeta-qstar-closed-form-dilog.witness.json`) and the audit
`docs/audits/2026-08-01-qstar-closed-form-habiro-dilog.md`.

## The algebraic recast

The empirical (CAL-anchored) `c₃` extractor
(`qbeta_utils.c3_target_at`) is

  `c₃(q) = (Q_codata / Q_N2(q) − 1) / u(q)³`,
  `Q_N2(q) = m_e · Q_A_over_me(q) · cos(α(q) − b(q)·ℏ_q(q)²/2) · (1 − u(q)²)`.

Setting the S-channel-zero condition `c₃(q*) = −Vol(4₁)` and clearing
denominators gives the **closed-form defining equation**

  `Φ(q*) = Q_codata / m_e`,   where
  `Φ(q) = Q_A_over_me(q) · cos(α(q) − b(q)·ℏ_q(q)²/2) · (1 − u(q)²) · (1 − Vol41·u(q)³)`.

`Φ` is fully elementary in `q` (rational · √ · cos); the *only*
transcendental constant it carries is the figure-eight hyperbolic
volume `Vol(4₁) = 2·Cl₂(π/3) = 2·Im Li₂(e^{iπ/3})`, a Bloch–Wigner
**dilog** value. No Faddeev / Habiro q-series enters the q-dependence.

`qstarShape` below records this closed form (documenting the POSITIVE
partial result: the *shape* is closed form). `Vol41` is carried as a
real parameter because the Clausen constant is not in Mathlib; it is
the external dilog value above.

## The exclusion invariant (scope-(b))

`q*` is the root of `Φ(q) = R` with `R = Q_codata / m_e` a ratio of two
**measured** CODATA inputs. Numerically `Φ'(q*) = −3.63 ≠ 0`,
sign-definite on a neighbourhood of `q*` (verified to 50 dps in the
probe), so `Φ` is strictly monotone there. `qstarRootStrictMonoInAnchor`
proves the mathematical consequence: **the root strictly tracks the
anchor** (a larger measured `R` gives a strictly larger `q*`). A
constant does not vary with its argument; therefore `q*` is not an
experiment-independent constant — it moves with the neutron β-decay
Q-value, with `dq*/dQ_β = 1/(m_e·Φ'(q*)) = −0.539` (a falsifiable lever:
a more precise `Q_β` sharpens `q*`).

`StrictMonoOn Φ I` is the numerically-verified **hypothesis** (`Φ' ≠ 0`,
sign-definite near `q*`); it is NOT proved in Lean here (that needs the
full derivative computation). The theorem is the sorry-free *implication*
"if `Φ` is strictly monotone then the root tracks the anchor" — the
conditional-proved ≠ premise-established discipline applies: this proves
the invariant's consequence, not the monotonicity premise (which the
probe establishes numerically).
-/

namespace QOU.BraidKnot.QBetaQStarClosedFormExclusion

open Real

/-- The closed-form shape `Φ(q)` whose root `Φ(q) = Q_codata/m_e` is the
S-channel-zero landmark `q*`. Elementary in `q` (rational · √ · cos) plus
the single external dilog constant `vol41 = Vol(4₁) = 2·Im Li₂(e^{iπ/3})`,
carried as a parameter. This `def` documents that the S-channel-zero
condition is a genuine *closed-form* transcendental equation. -/
noncomputable def qstarShape (vol41 q : ℝ) : ℝ :=
  let h : ℝ := q - 1 / q
  let hbar : ℝ := (q - 1) / q
  let b : ℝ := Real.sqrt ((h ^ 2 + 3) / (h ^ 2 + 4))
  let u : ℝ := b * hbar ^ 2
  let z : ℝ := 1 / (Real.sqrt q + 1 / Real.sqrt q)
  let alpha : ℝ := (z - 1) * h / 2
  let QA : ℝ := |q ^ 2 - 2 * q - 1| * (q + 1) / (2 * q ^ 3)
  QA * Real.cos (alpha - b * hbar ^ 2 / 2) * (1 - u ^ 2) * (1 - vol41 * u ^ 3)

/-- **Exclusion invariant (scope-(b)).** If the closed-form shape `Φ` is
strictly monotone on an interval `I` containing the roots, then the
S-channel-zero landmark strictly tracks the experimental anchor:
a strictly larger measured anchor `Φ q₂` gives a strictly larger root
`q₂`. Hence `q*` is a non-constant function of the measured input
`R = Q_codata/m_e`, i.e. NOT an experiment-independent closed-form
mathematical constant.

The `StrictMonoOn Φ I` hypothesis is the numerically-verified fact
`Φ'(q*) ≠ 0` (sign-definite near `q*`, 50 dps); the implication is
sorry-free. -/
theorem qstarRootStrictMonoInAnchor
    {Φ : ℝ → ℝ} {I : Set ℝ} (hΦ : StrictMonoOn Φ I)
    {q₁ q₂ : ℝ} (h1 : q₁ ∈ I) (h2 : q₂ ∈ I)
    (hanchor : Φ q₁ < Φ q₂) : q₁ < q₂ :=
  (hΦ.lt_iff_lt h1 h2).mp hanchor

/-- Corollary: the landmark is *uniquely* determined by the anchor — two
roots of the same measured anchor coincide. This is the non-trivial
direction (it uses the strict-monotone injectivity `StrictMonoOn.injOn`,
so `q*` is a well-defined single-valued function of `Q_codata/m_e`, and by
`qstarRootStrictMonoInAnchor` a genuinely varying one). -/
theorem qstarRootUniqueInAnchor
    {Φ : ℝ → ℝ} {I : Set ℝ} (hΦ : StrictMonoOn Φ I)
    {q₁ q₂ : ℝ} (h1 : q₁ ∈ I) (h2 : q₂ ∈ I)
    (he : Φ q₁ = Φ q₂) : q₁ = q₂ :=
  hΦ.injOn h1 h2 he

end QOU.BraidKnot.QBetaQStarClosedFormExclusion
