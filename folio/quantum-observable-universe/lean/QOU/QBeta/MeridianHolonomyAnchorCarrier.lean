import QOU.Knot.CuspShapeBarParity

/-!
# The meridian-holonomy `q₀↦u` deformation MAGNITUDE is anchor-smooth — an exact
amplification bound from the boost hyperbola

**The c₃ bar-odd anchor-carrier question, in one exact inequality.**

`C1` (`QOU.QBeta.BarOddAntisymOffDiagonal`, PR #4282, sorry-free) proved the
bar-odd datum is the ι-odd antisymmetric off-diagonal `ω(β,p,q)=β·p−β⁻¹·q`, and
its numerical companion showed `ω` is **anchor-smooth** (≈ 4.56 ppm swing across
the muon↔proton `q₀` anchors) while the target `c₃` swings ≈ 3.47 % (`≈ 7.6×10³×`
larger). `CuspShapeBarParity` located the remaining freedom in the
**meridian-holonomy `q₀ ↦ u` deformation** — the Neumann–Zagier
`CVol(u) = Vol − (τ/4)u² + …` off the complete point `u=0`, cusp modulus
`τ ∝ √−3` (`barOdd(ω)`, proved).

This file asks — and answers, exactly, over a generic field for the algebra and
over `ℝ` for the ordering — whether the deformation's **magnitude channel** can
supply the percent-level anchor swing. The meridian holonomy is multiplication by
`q` (`meridian-holonomy-boost.md`), so the bar-odd deformation shape is
`barOdd q = q − q⁻¹` (`= 2 sinh(log q) = u + O(u³)`, the substrate meridian
coordinate `u = 2 log q₀`). The observable enters as `S ∝ u²` (NZ leading term),
so the deformation-magnitude's logarithmic `q`-sensitivity is the amplification we
must size.

## The result

The logarithmic sensitivity of `barOdd q` to the holonomy `q` is the ratio
`barEven q / barOdd q` (`d log|barOdd q| / d log q`, since
`d(barOdd q)/d(log q) = barEven q`). The **boost hyperbola**
`barEven² − barOdd² = 4` (`QOU.Knot.CuspShapeBarParity.holonomy_hyperbola`) pins
its square **exactly**:

* `sensitivity_sq` — `(barEven q / barOdd q)² = 1 + 4/(barOdd q)²` (generic field).

Two immediate consequences (over `ℝ`), which together are the anchor-smoothness
bound:

* `barOdd_sq_le_of_amplification` — reaching amplification `ρ ≥ N` **forces**
  `(barOdd q)² ≤ 4/(N²−1)`: a large deformation-magnitude amplification requires
  `q` near the **compact / root-of-unity locus** `barOdd = 0` (`q = ±1`).
* `amplification_le_of_barOdd_sq_ge` — the contrapositive: away from the compact
  locus (`(barOdd q)² ≥ δ`), amplification is bounded by `1 + 4/δ`.

**Consequence for c₃.** At the substrate `q₀ ≈ 1.10998`, `barOdd q₀ ≈ 0.20906`,
so `(barOdd q₀)² ≈ 0.0437` and the magnitude amplification is
`√(1 + 4/0.0437) ≈ 9.62 = O(10)` — **not** the `O(10⁶)` demanded by
`dc₃/dq₀ ≈ 3.84×10⁶` (corrected 2026-08-29 from `4.66×10⁶`, the secant taken
with the pre-#1422 superseded muon `c₃ = -2.0097`; bean `qou-kt8o`. Both are
`O(10⁶)`, so nothing below changes — the `ρ ≈ 3×10⁶` inversion was already
quoted at an order under either value). Inverting
`barOdd_sq_le_of_amplification`, reaching
`ρ ≈ 3×10⁶` would require `|barOdd q₀| ≲ 7×10⁻⁷`, i.e. `q₀` within `~3×10⁻⁷` of
`1`; the substrate is `≈ 0.11` away — **~5 orders of magnitude too far.** So the
meridian-holonomy deformation **magnitude** is provably anchor-smooth at the
substrate: the `S ∝ u²` channel produces an anchor swing of order
`(anchor spacing) × 2ρ(q₀) ≈ 11.5 ppb × 19 ≈ sub-ppm`, not the percent swing.

This is an **exact, generic-field** sharpening of the `#3639` smooth-boost
negative (`dζ/dq₀ = 1/q₀ = O(1)`; `docs/audits/2026-07-12-c3-meridian-boost-smooth-negative.md`):
it replaces the numerical `O(1)` estimate with the closed form
`ρ² = 1 + 4/barOdd²`, and it *unifies the bound with the #4283 in-block route* —
both the in-block module maps (anchor-smooth, C1) and the holonomy-deformation
magnitude (this bound) are anchor-smooth, so **every smooth/magnitude object is
excluded as the sole seat**; the percent swing lives only in the near-singular /
non-perturbative **phase** `arg(u)` (consistent with `#3818`'s ξ-frame phase law:
no perturbative odd phase at the meridian).

**Scope.** This is a **scope-(a)** magnitude/anchor-behaviour negative on the
deformation-magnitude channel — NOT a structural exclusion of the meridian
deformation (whose phase channel remains the open
`conj:algebraic-geometric-dilog-equivalence`). No `c_k` value is produced;
nothing inverts `Q_β`/CODATA; nothing is wired.

Base ring: `sensitivity_sq` is generic `Field R` (§7c-clean, no ordering); the
two inequality corollaries specialise to `ℝ` (they are genuinely archimedean —
they order magnitudes), which is the correct wall placement.

-- Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
-- Ref: [leitner2026] docs/audits/2026-07-25-meridian-holonomy-c3-anchor.md
-- Ref: [leitner2026] docs/audits/2026-07-12-c3-meridian-boost-smooth-negative.md
-/

namespace QOU.QBeta.MeridianHolonomyAnchorCarrier

open QOU.QBeta.BarParityZeta4Swap
open QOU.Knot.CuspShapeBarParity

/-- **Boost-hyperbola sensitivity identity.** The logarithmic `q`-sensitivity of
the bar-odd meridian-deformation shape `barOdd q = q − q⁻¹` is the ratio
`barEven q / barOdd q` (`d(barOdd q)/d(log q) = barEven q`); its SQUARE is pinned
exactly by the boost hyperbola `barEven² − barOdd² = 4` to
`1 + 4/(barOdd q)²`. Generic field, no archimedean structure (§7c). -/
theorem sensitivity_sq {R : Type*} [Field R] {q : R} (hq : q ≠ 0)
    (hodd : barOdd q ≠ 0) :
    (barEven q / barOdd q) ^ 2 = 1 + 4 / (barOdd q) ^ 2 := by
  have hhyp : barEven q ^ 2 - barOdd q ^ 2 = 4 := holonomy_hyperbola hq
  have hodd2 : (barOdd q) ^ 2 ≠ 0 := pow_ne_zero 2 hodd
  field_simp
  linear_combination hhyp

/-- **A large deformation-magnitude amplification forces the compact locus.**
Over `ℝ`: if the amplification `ρ = |barEven q / barOdd q|` reaches a threshold
`N > 1` (`N² ≤ ρ²`) then `(barOdd q)² ≤ 4/(N²−1)`. So a big magnitude
amplification requires `|barOdd q|` small, i.e. `q` close to the compact /
root-of-unity locus `barOdd = 0` (`q = ±1`). This is the exact statement that the
holonomy-deformation magnitude is anchor-smooth wherever `q` is bounded away from
`±1` — in particular at the substrate `q₀ ≈ 1.11`. -/
theorem barOdd_sq_le_of_amplification {q : ℝ} (hq : q ≠ 0) (hodd : barOdd q ≠ 0)
    {N : ℝ} (hN : 1 < N) (hamp : N ^ 2 ≤ (barEven q / barOdd q) ^ 2) :
    (barOdd q) ^ 2 ≤ 4 / (N ^ 2 - 1) := by
  have hs := sensitivity_sq hq hodd
  have hpos : (0 : ℝ) < (barOdd q) ^ 2 := by positivity
  have hN1 : (0 : ℝ) < N ^ 2 - 1 := by nlinarith
  have h1 : N ^ 2 - 1 ≤ 4 / (barOdd q) ^ 2 := by rw [hs] at hamp; linarith
  rw [le_div_iff₀ hN1]
  rw [le_div_iff₀ hpos] at h1
  nlinarith [h1]

/-- **Contrapositive — the anchor-smoothness bound.** Away from the compact locus
(`(barOdd q)² ≥ δ > 0`), the deformation-magnitude amplification is bounded:
`(barEven q / barOdd q)² ≤ 1 + 4/δ`. At the substrate `δ ≈ (barOdd q₀)² ≈ 0.0437`
this gives `≤ 1 + 91.5 ≈ 92.5`, `ρ ≤ 9.62 = O(10)` — far below the `O(10⁶)` the
c₃ swing demands. -/
theorem amplification_le_of_barOdd_sq_ge {q : ℝ} (hq : q ≠ 0)
    {δ : ℝ} (hδ : 0 < δ) (hb : δ ≤ (barOdd q) ^ 2) :
    (barEven q / barOdd q) ^ 2 ≤ 1 + 4 / δ := by
  have hodd : barOdd q ≠ 0 := by
    intro h; rw [h] at hb; norm_num at hb; linarith
  rw [sensitivity_sq hq hodd]
  have hmono : 4 / (barOdd q) ^ 2 ≤ 4 / δ := by gcongr
  linarith

end QOU.QBeta.MeridianHolonomyAnchorCarrier
