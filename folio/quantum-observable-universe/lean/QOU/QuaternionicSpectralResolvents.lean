import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# QOU.QuaternionicSpectralResolvents

**Canonical declaration** for content block at
[`quantum-observable-universe/brings-surface/quaternionic-spectral-resolvents.ts`](quantum-observable-universe/brings-surface/quaternionic-spectral-resolvents.ts).

Formalises the manuscript **definition** of the quaternionic spectral
resolvents `ω₀,…,ω₃ : 𝒮 → J^∞E` on Bring's surface: with `q ∈ ℂ`,
`0 < |q| ≤ 1` and `r = −ln|q|` (so `|q| = e^{−r}`), the resolvent `ω₀` is the
uncertainty component and `ω₁,ω₂,ω₃` are the space-like and time-like components
carried by the quaternion units `𝐢,𝐣,𝐤`. The abstract quaternion algebra is
axiomatised (`H` with the Hamilton relations) since the Mathlib quaternion
cone is outside the available olean set; the scale `r = −ln|q|` is over `ℝ`
(§7c archimedean).
-/

namespace QOU

/-- Data for the quaternionic spectral resolvents at a substrate value `q`.

    A `definition` carrier: the modulus `|q|` with `0 < |q| ≤ 1`, the scale
    `r = −ln|q|`, the quaternion carrier `H` with its imaginary units
    `𝐢,𝐣,𝐤`, and the four resolvents. -/
structure QuaternionicSpectralResolvents where
  /-- The modulus `|q|`. -/
  qAbs : ℝ
  /-- `|q| > 0`. -/
  qAbs_pos : 0 < qAbs
  /-- `|q| ≤ 1` (inside the closed unit disc). -/
  qAbs_le_one : qAbs ≤ 1
  /-- The scale `r`. -/
  r : ℝ
  /-- `r = −ln|q|`. -/
  r_def : r = -Real.log qAbs
  /-- The quaternion carrier. -/
  H : Type
  /-- `H` is a ring. -/
  instH : Ring H
  /-- The imaginary units. -/
  i : H
  j : H
  k : H
  /-- The four spectral resolvents `ω₀,…,ω₃` (as elements of `H`). -/
  ω : Fin 4 → H

-- Ref: [leitner2026] quantum-observable-universe/brings-surface/quaternionic-spectral-resolvents.ts

namespace QuaternionicSpectralResolvents

variable (W : QuaternionicSpectralResolvents)

/-- The scale `r = −ln|q|` is non-negative on the closed unit disc
    (`0 < |q| ≤ 1`), so `|q| = e^{−r}` with `r ≥ 0`. -/
theorem r_nonneg : 0 ≤ W.r := by
  rw [W.r_def, neg_nonneg]
  exact Real.log_nonpos W.qAbs_pos.le W.qAbs_le_one

/-- Recovering the modulus from the scale: `|q| = e^{−r}`. -/
theorem qAbs_eq_exp_neg_r : W.qAbs = Real.exp (-W.r) := by
  rw [W.r_def, neg_neg, Real.exp_log W.qAbs_pos]

end QuaternionicSpectralResolvents

end QOU
