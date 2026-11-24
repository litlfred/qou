-- Ref: [leitner2026] docs/audits/2026-06-20-hoefsmit-b-bar-parity-correction.md
--
-- Bar-parity of the Hoefsmit ladder base `b` and the Q_β expansion
-- variable `u = b·ℏ_q²`.
--
-- The canonical Hoefsmit ladder base (the one whose substrate value
-- reproduces `u ≈ 0.00852`, used by the mainstream c_k probes and grounded
-- in `SilverAnchorGrounding.lean` via `b² = (q⁴+q²+1)/(q²+1)²`) is
--
--   b(q) = √( (q⁴+q²+1) / (q²+1)² )  =  √( (h²+3)/(h²+4) ),   h = q − q⁻¹.
--
-- Because `h = q − q⁻¹` is bar-ODD (`h(q⁻¹) = −h(q)`), `h²` is bar-EVEN,
-- hence `b²` — a function of `h²` alone — is **bar-EVEN**: `b(q⁻¹) = b(q)`.
--
-- Consequently `u = b·ℏ_q²` is bar-EVEN-covariant: `u(q⁻¹) = q²·u(q)`
-- (`u ↦ +q²·u`), since `ℏ_q = 1 − q⁻¹` is bar-odd-covariant
-- (`ℏ_q(q⁻¹) = −q·ℏ_q(q)`), so `ℏ_q²(q⁻¹) = q²·ℏ_q²(q)`.
--
-- This CORRECTS the criterion-2b prune
-- (`docs/audits/2026-06-20-qbeta-barparity-criterion-2b-prune.md`), which
-- used a non-canonical `b = (q−q⁻¹)/(q+q⁻¹)` (bar-ODD, and giving the wrong
-- `u ≈ 0.00102`) and therefore asserted `u ↦ −q²·u` with a spurious
-- `(−1)^k` in the bar-even-kernel law. The correct law is
-- `c_k(q⁻¹) = q^{−2k}·c_k(q)` (no sign alternation). The prune's *verdict*
-- (criterion 2b cannot be imposed: `c₂ = −1` fails the law since
-- `−1 ≠ −q^{−4}`) still holds, but the "parity-split ladder" mechanism does
-- not — `u` carries no per-rung sign.
--
-- Statements are over `ℝ` (the substrate parameter `q`); they use no
-- `Real.sqrt` — we work with `b²` and `u²`, so they are field identities
-- (positivity only discharges the `q²+1 > 0` denominators).

import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

namespace QOU.QBeta

/-- The square of the canonical Hoefsmit ladder base,
`b² = (q⁴ + q² + 1)/(q² + 1)²`. -/
noncomputable def hoefsmitBSq (q : ℝ) : ℝ := (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2

/-- `b²` written through the Hecke parameter `h = q − q⁻¹`:
`b² = (h² + 3)/(h² + 4)` (the form used by the mainstream `c_k` probes).
This makes bar-evenness manifest, since `h²` is bar-even. -/
theorem hoefsmitBSq_eq_h (q : ℝ) (hq : q ≠ 0) :
    hoefsmitBSq q = ((q - q⁻¹) ^ 2 + 3) / ((q - q⁻¹) ^ 2 + 4) := by
  unfold hoefsmitBSq
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  have hden : (q - q⁻¹) ^ 2 + 4 ≠ 0 := by positivity
  field_simp
  ring

/-- **`b²` is bar-even**: `b²(q⁻¹) = b²(q)`. The Hoefsmit ladder base is
invariant under the bar involution `q ↦ q⁻¹`. -/
theorem hoefsmitBSq_bar_even (q : ℝ) (hq : q ≠ 0) :
    hoefsmitBSq q⁻¹ = hoefsmitBSq q := by
  unfold hoefsmitBSq
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  have h2 : (q⁻¹) ^ 2 + 1 ≠ 0 := by positivity
  field_simp
  ring

/-- `ℏ_q = 1 − q⁻¹`. -/
noncomputable def hbarQ (q : ℝ) : ℝ := 1 - q⁻¹

/-- `ℏ_q` is **bar-odd-covariant**: `ℏ_q(q⁻¹) = −q·ℏ_q(q)`. -/
theorem hbarQ_bar_odd_covariant (q : ℝ) (hq : q ≠ 0) :
    hbarQ q⁻¹ = -q * hbarQ q := by
  unfold hbarQ
  field_simp
  ring

/-- The squared Q_β expansion variable `u² = b²·(ℏ_q²)²`.  (Working with the
square avoids `Real.sqrt`, keeping everything a field identity.) -/
noncomputable def uSq (q : ℝ) : ℝ := hoefsmitBSq q * (hbarQ q ^ 2) ^ 2

/-- **The corrected ladder covariance**: `u²(q⁻¹) = q⁴·u²(q)`, i.e.
`u ↦ +q²·u` under the bar involution — `u` is bar-EVEN-covariant.

This is the load-bearing correction: the criterion-2b prune asserted
`u ↦ −q²·u` (bar-odd-covariant) from a non-canonical `b`; the canonical
`b` (bar-even) gives `+q²` with **no sign**, so the bar-even-kernel law on
the coefficients is `c_k(q⁻¹) = q^{−2k}·c_k(q)` with no `(−1)^k`. -/
theorem uSq_bar_covariance (q : ℝ) (hq : q ≠ 0) :
    uSq q⁻¹ = q ^ 4 * uSq q := by
  unfold uSq
  rw [hoefsmitBSq_bar_even q hq, hbarQ_bar_odd_covariant q hq]
  ring

end QOU.QBeta
