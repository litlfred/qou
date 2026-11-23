import QOU.QBeta.ObservableComplexVolumeVsFullPotential
import QOU.QBeta.OhtsukiKappaVsCkSign

set_option autoImplicit false

/-!
# QOU.QBeta.OhtsukiNZBridgeScale — the order-b² match locks bridge scale to the A-binary (B1)

The B1 consistency-forcing search (bean `qou-uxwc`, 2026-08-15 attack-options
ledger): hunt the sorry-free assets for an independent pin of the order-`u²`
Im normalization. Finding: the corpus carries TWO exact order-b² expansions
of the 4₁ complex volume —

* the **Ohtsuki tower** `𝔙_b = 𝔙₀ + κ₁·(2πb²) + O(b⁴)` with the DERIVED
  real rung `κ₁ = 11√3π/108 > 0` (`OhtsukiKappaVsCkSign.kappa1`,
  PSLQ-exact, Lean-pinned);
* the **NZ geometric deformation** `𝔙(u) = 𝔙₀ + i·κ_A·u² + O(u⁴)` with
  `κ_A ∈ {κ_pot, κ_shape}` — the open A-binary (`TauNormalizationChoice`).

**Conditional on a linear bridge `u = c·b` identifying the two deformation
directions** (the quantum fluctuation `b` with the geometric meridian `u` —
this identification is exactly the open fibre→observable functor content and
is NOT asserted here), matching the order-`b²` terms forces

    i·κ_A·c² = 2π·κ₁      ⇒      c² = −i·(2πκ₁/κ_A).

Consequences, each proved below from that single matching hypothesis:

1. `c²` is **purely imaginary** (`bridge_sq_re_zero`) — the bridge ratio
   lies at `arg c ∈ {−π/4, 3π/4}`, reproducing the diagonal-ray geometry
   (`ModularRayDiagonalPrune`) as a CONSEQUENCE of the match rather than an
   input;
2. the **scale is locked to the A-binary**: `‖c‖² = 2πκ₁/κ_A`
   (`bridge_normSq`), so the two conventions demand bridge scales differing
   by exactly 2 (`conventions_scale_ratio_two`) — any independent pin of
   the bridge scale `‖c‖` decides the A-binary, and conversely.

**B1 verdict encoded here: at order b² the binary is genuinely undetermined
by the current sorry-free assets** — each convention is consistent with the
match under its own bridge scale; no asset independently pins `‖c‖`. The
search either ends at an independent `‖c‖` pin (decides A) or this
double-consistency stands (proved undetermined at this order).

## Honesty (§3b-cond; anti-laundering)

The matching hypothesis (`hmatch`) is explicit and conditional — the
deformation-identification bridge is open conjecture territory
(`conj:stokes-dt-bps-bridge` adjacent); nothing here asserts it holds.
No numerical `S`, no `c_k`, no instance wired.

## References

- [neumann-zagier1985] Neumann & Zagier, Topology 24 (1985). https://doi.org/10.1016/0040-9383(85)90004-7
- [andersen-hansen2006] https://doi.org/10.1142/S0218216506004555 (the κ-tower)
- [leitner2026] docs/coordination/2026-08-02-c3-odd-aomega-unification.md (the single open question).
-/

namespace QOU.QBeta.OhtsukiNZBridgeScale

open QOU.QBeta.ObservableComplexVolumeVsFullPotential
open QOU.QBeta.OhtsukiKappaVsCkSign

/-- The order-b² matching condition: under a linear bridge `u = c·b`, the NZ
term `i·κ_A·(c·b)² ` equals the Ohtsuki term `κ₁·2π·b²` for all `b` iff the
coefficients match. We take the coefficient identity as the hypothesis. -/
def OrderTwoMatch (κA : ℝ) (c : ℂ) : Prop :=
  Complex.I * (κA : ℂ) * c ^ 2 = ((2 * Real.pi * kappa1 : ℝ) : ℂ)

/-- Under the match, `κ_A·c² = −(i·2πκ₁)` (division-free form). -/
theorem bridge_sq_mul {κA : ℝ} {c : ℂ} (h : OrderTwoMatch κA c) :
    (κA : ℂ) * c ^ 2 = -(Complex.I * ((2 * Real.pi * kappa1 : ℝ) : ℂ)) := by
  have h' := congrArg (fun z => Complex.I * z) h
  simp only at h'
  rw [show Complex.I * (Complex.I * (κA : ℂ) * c ^ 2)
        = Complex.I * Complex.I * ((κA : ℂ) * c ^ 2) by ring,
      Complex.I_mul_I, neg_one_mul] at h'
  exact neg_eq_iff_eq_neg.mp h'

/-- **Consequence 1: the bridge ratio squared is purely imaginary** — the
match forces `arg c ∈ {−π/4, 3π/4}`, i.e. the diagonal-ray geometry of
`ModularRayDiagonalPrune`, derived rather than assumed. -/
theorem bridge_sq_re_zero {κA : ℝ} (hκ : κA ≠ 0) {c : ℂ}
    (h : OrderTwoMatch κA c) : (c ^ 2).re = 0 := by
  have hm := congrArg Complex.re (bridge_sq_mul h)
  simp [Complex.mul_re] at hm
  rcases hm with h0 | h0
  · exact absurd h0 hκ
  · exact h0

/-- **Consequence 2: the bridge scale is locked to the normalization.**
`κ_A²·‖c²‖ = (2πκ₁)²` (division-free): an independent pin of the bridge
scale decides the A-binary, and conversely. -/
theorem bridge_normSq {κA : ℝ} {c : ℂ} (h : OrderTwoMatch κA c) :
    κA ^ 2 * Complex.normSq (c ^ 2) = (2 * Real.pi * kappa1) ^ 2 := by
  have hm := congrArg Complex.normSq (bridge_sq_mul h)
  simp only [Complex.normSq_neg, Complex.normSq_mul, Complex.normSq_I,
    Complex.normSq_ofReal, one_mul] at hm
  linear_combination hm

/-- **Consequence 3: the two conventions demand bridge scales in ratio 2.**
`κ_shape = 2·κ_pot`, so the full-potential convention's `‖c‖²` target is
exactly half the complex-volume one — the A-binary IS a bridge-scale
binary. -/
theorem conventions_scale_ratio_two :
    2 * Real.pi * kappa1 / kappaCV = 2 * (2 * Real.pi * kappa1 / kappaFull) := by
  rw [kappaFull_eq_two_mul_kappaCV]
  have h : kappaCV ≠ 0 := kappaCV_pos.ne'
  field_simp

/-- Sign-inversion invariance of the order-`b^2` matching condition: `OrderTwoMatch κA (-c)`
holds if and only if `OrderTwoMatch κA c` holds. -/
theorem orderTwoMatch_neg (κA : ℝ) (c : ℂ) :
    OrderTwoMatch κA (-c) ↔ OrderTwoMatch κA c := by
  dsimp [OrderTwoMatch]
  rw [neg_sq]

end QOU.QBeta.OhtsukiNZBridgeScale
