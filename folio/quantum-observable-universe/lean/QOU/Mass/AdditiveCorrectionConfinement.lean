import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith

/-!
# QOU.Mass.AdditiveCorrectionConfinement — new energy terms are confined to the binding sector

The formalize-first invariant behind the zero-point channel-energy exploration
(2026-07-04 audit `docs/audits/2026-07-04-zero-point-channel-energy-and-information.md`):
the canonical absolute nucleon masses (muon-anchored facade, `canonical_mass.py`) already
reproduce observation. Therefore any *proposed additional* energy term — a q-Casimir
zero-point shift, a channel-information term, any D_ν-interpolation energy — is
quantitatively **confined**: at the free-particle level its magnitude is bounded by twice
the existing match tolerance (`additive_correction_confined`), and if the match is taken
as exact the term vanishes there outright (`additive_correction_zero_of_exact`). New
energy can only live where predictions do *not* already saturate observation — the
binding / convolution-defect sector.

Both statements are elementary order-field algebra, stated over a generic
linearly ordered field (`[Field K] [LinearOrder K] [IsStrictOrderedRing K]`;
§7c: the ordering is the entire content; no `ℝ`-specific construct is used).
-/

namespace QOU.Mass.AdditiveCorrectionConfinement

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Confinement bound.** If a predicted mass already matches observation within `ε`,
then any modified prediction `m_pred + δ` that also matches within `ε` has `|δ| ≤ 2ε`:
a proposed new energy term cannot exceed twice the existing agreement tolerance at the
level where that agreement holds. -/
theorem additive_correction_confined (m_pred m_obs δ ε : K)
    (h1 : |m_pred - m_obs| ≤ ε) (h2 : |m_pred + δ - m_obs| ≤ ε) :
    |δ| ≤ 2 * ε := by
  have h1' := abs_le.mp h1
  have h2' := abs_le.mp h2
  exact abs_le.mpr ⟨by linarith [h1'.1, h1'.2, h2'.1, h2'.2],
    by linarith [h1'.1, h1'.2, h2'.1, h2'.2]⟩

/-- **Exact-match corollary.** If the prediction matches observation exactly both with
and without the additional term, the term is zero — an exact absolute-mass match leaves
no room for a new free-particle energy contribution. -/
theorem additive_correction_zero_of_exact (m_pred m_obs δ : K)
    (h1 : m_pred = m_obs) (h2 : m_pred + δ = m_obs) : δ = 0 := by
  linarith

/-- **Symmetric confinement difference bound (`qou-lhsb`).**
If two modified predictions `m_pred + δ₁` and `m_pred + δ₂` both agree with `m_obs`
within tolerance `ε`, then their shift difference satisfies `|δ₁ - δ₂| ≤ 2 * ε`. -/
theorem additive_correction_diff_confined (m_pred m_obs δ₁ δ₂ ε : K)
    (h1 : |m_pred + δ₁ - m_obs| ≤ ε) (h2 : |m_pred + δ₂ - m_obs| ≤ ε) :
    |δ₁ - δ₂| ≤ 2 * ε := by
  have h1' := abs_le.mp h1
  have h2' := abs_le.mp h2
  exact abs_le.mpr ⟨by linarith [h1'.1, h1'.2, h2'.1, h2'.2],
    by linarith [h1'.1, h1'.2, h2'.1, h2'.2]⟩

end QOU.Mass.AdditiveCorrectionConfinement
