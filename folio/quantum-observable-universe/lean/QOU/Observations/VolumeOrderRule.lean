/-
# The volume-order rule for the lepton volume carriers

Thread "Derive the electron's categorical weight" (2026-11-27). Owner card: "Volume-order rule
(4₁, then 5₂)". Audit: `docs/audits/2026-11-27-electron-categorical-weight.md` §12. Probe:
`computations/probes/coloured_ladder/volume_order_rule_probe.py`.

The ruled lepton words `Δ, Δ³, Δ⁵` have `Vol = 0` (periodic braids, torus-type closures), so a
volume chart cannot come from them (`prop:vol-through-tau`). The rule tested here assigns the
generation `g ≥ 1` the `g`-th smallest hyperbolic knot volume. This order is a theorem of
hyperbolic geometry, cited and not proved here: `4₁` is the smallest (Cao–Meyerhoff 2001), and
`5₂` is the next (Gabai–Haraway–Meyerhoff–Thurston–Yarmola). On the corpus volume chart
`m_g/m_e = Vol_g/ℏ_q²` this gives, over any ordered field:

* `ratio_q_free`: `m_τ/m_μ = Vol₂/Vol₁`. It does not depend on `q`, so the rule cannot be tuned
  through `q₀`.
* `ratio_gt_one`: the tau is heavier than the muon, because the volumes are ordered.
* `ratio_lt`: if `Vol₂ < c·Vol₁`, then `m_τ/m_μ < c`.

The probe gives `Vol(5₂)/Vol(4₁) = 1.39323`. The measured ratio enters only in the probe's
comparison block. No knot is chosen to match it.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic

namespace QOU.Observations.VolumeOrderRule

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- The volume-order rule: generation `1` (muon) and `2` (tau) carry the first and second
hyperbolic knot volumes, which are positive and strictly ordered. -/
structure Rule (K : Type*) [Field K] [LinearOrder K] where
  vol1 : K
  vol2 : K
  pos1 : 0 < vol1
  lt12 : vol1 < vol2

/-- The volume chart `m_g/m_e = Vol_g/ℏ²`. -/
def massMu (R : Rule K) (h : K) : K := R.vol1 / h ^ 2
def massTau (R : Rule K) (h : K) : K := R.vol2 / h ^ 2

/-- **`m_τ/m_μ = Vol₂/Vol₁`, independent of `ℏ_q`.** -/
theorem ratio_q_free (R : Rule K) (h : K) (hh : h ≠ 0) :
    massTau R h / massMu R h = R.vol2 / R.vol1 := by
  have := R.pos1.ne'
  unfold massTau massMu
  field_simp

theorem ratio_gt_one (R : Rule K) (h : K) (hh : h ≠ 0) : 1 < massTau R h / massMu R h := by
  rw [ratio_q_free R h hh, one_lt_div R.pos1]
  exact R.lt12

theorem ratio_lt (R : Rule K) (h : K) (hh : h ≠ 0) (c : K) (hc : R.vol2 < c * R.vol1) :
    massTau R h / massMu R h < c := by
  rw [ratio_q_free R h hh, div_lt_iff₀ R.pos1]
  exact hc

end QOU.Observations.VolumeOrderRule
