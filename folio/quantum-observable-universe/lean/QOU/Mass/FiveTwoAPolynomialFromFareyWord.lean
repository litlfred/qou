import Mathlib.Tactic

/-!
# The 5₂ A-polynomial recovered from the derived triangulation — exact identities

Companion to `computations/probes/two_bridge_cusp_rows_apoly_probe.py` (bean `qou-yvyd`). From
the two-bridge triangulation of `S³ ∖ 5₂` built from the Farey word `RL` (no SnapPy input), that
probe takes λ as the primitive cusp class dying in `H₁(M)`, pins the meridian among `μ₀ + kλ` by
the Dehn-filling test (a nondegenerate solution of the gluing equations with `H(μ₀+kλ) = 1` and
`H(λ) ≠ 1` factors through the filling, whose `π₁` is then nontrivial; the meridian filling is
`S³`, so only the meridian's frame carries no such point — Property P, [kronheimer2004]), samples
the deformation curve and fits, with integer coefficients verified on fresh samples to `1e-41`,

  `A(L, M) = L³ + L²(M¹⁰ − M⁸ + 2M⁴ + 2M² − 1) + L(−M¹⁴ + 2M¹² + 2M¹⁰ − M⁶ + M⁴) + M¹⁴`.

This file states the two exact identities the probe checks numerically and that a reader can
check by hand, as theorems over any commutative ring:

* **meridian filling**: `A(L, ±1) = (L + 1)³`, so every point of the curve over `M² = 1` has
  `L = −1` — no representation factors through the meridian filling, the Property-P consistency
  the frame identification rests on;
* **the involution**: `L³ M¹⁴ · A(L⁻¹, M⁻¹) = A(L, M)`, the symmetry every knot A-polynomial has
  under reversing the orientation of the boundary torus (over a field, `L, M ≠ 0`).

Nothing geometric is asserted here; the Newton-polygon slopes `{−10, −4, 0}` (the literature's
`{0, 4, 10}` for the mirror) are read off the polynomial in the probe.

-- Ref: [leitner2026] computations/probes/two_bridge_cusp_rows_apoly_probe.py
-- Ref: [kronheimer2004] Kronheimer–Mrowka, Witten's conjecture and Property P.
-/

namespace QOU.Mass.FiveTwoAPolynomialFromFareyWord

variable {K : Type*} [CommRing K]

/-- The recovered A-polynomial of the derived 5₂ triangulation. -/
def A (L M : K) : K :=
  L ^ 3 + L ^ 2 * (M ^ 10 - M ^ 8 + 2 * M ^ 4 + 2 * M ^ 2 - 1)
    + L * (-M ^ 14 + 2 * M ^ 12 + 2 * M ^ 10 - M ^ 6 + M ^ 4) + M ^ 14

/-- Over `M = 1` the curve has only the parabolic point `L = −1`, with multiplicity three. -/
theorem A_at_M_one (L : K) : A L 1 = (L + 1) ^ 3 := by
  unfold A; ring

/-- Likewise over `M = −1` (the other lift of the meridian eigenvalue). -/
theorem A_at_M_neg_one (L : K) : A L (-1) = (L + 1) ^ 3 := by
  unfold A; ring

/-- The complete structure `(L, M) = (−1, 1)` lies on the curve. -/
theorem A_complete_point : A (-1 : K) 1 = 0 := by
  rw [A_at_M_one]; ring

/-- The boundary-orientation involution: over a field, for `L, M ≠ 0`,
`L³ M¹⁴ · A(L⁻¹, M⁻¹) = A(L, M)` — the symmetry every knot A-polynomial carries. -/
theorem A_involution {F : Type*} [Field F] (L M : F) (hL : L ≠ 0) (hM : M ≠ 0) :
    L ^ 3 * M ^ 14 * A L⁻¹ M⁻¹ = A L M := by
  unfold A
  field_simp
  ring

/-! ## The chirality, pinned against a held table (added 2026-09-07, bean `qou-lrvc`)

Culler's census A-polynomial for `K3_2` (= SnapPy's Rolfsen-table `5_2` = `m015`), read from
`library/A_census.tgz` in SnapPy's `(μ, λ)` framing, is

    1 + L(M¹⁰ − M⁸ + 2M⁴ + 2M² − 1) + L²(−M¹⁴ + 2M¹² + 2M¹⁰ − M⁶ + M⁴) + L³M¹⁴.

The mirror image of a knot has `A_{K̄}(L, M) = A_K(L⁻¹, M)` up to a unit, so the identity below
says the derived triangulation is the **mirror** of the census `5_2` — the same conclusion the
cusp shape (`−conj τ` to 38 digits) and the slopes (`{0,4,10}` against `{−10,−4,0}`) give in
`fivetwo_chirality_frame_vs_snappy_probe.py`. -/

/-- Culler's `A_{K3_2}`, transcribed from the held census tarball. -/
def A_census (L M : K) : K :=
  1 + L * (M ^ 10 - M ^ 8 + 2 * M ^ 4 + 2 * M ^ 2 - 1)
    + L ^ 2 * (-M ^ 14 + 2 * M ^ 12 + 2 * M ^ 10 - M ^ 6 + M ^ 4) + L ^ 3 * M ^ 14

/-- **The census `5_2` is the derived polynomial under `L ↦ L⁻¹`**: over a field, for `L ≠ 0`,
`L³ · A(L⁻¹, M) = A_census(L, M)`. -/
theorem A_census_eq_mirror {F : Type*} [Field F] (L M : F) (hL : L ≠ 0) :
    L ^ 3 * A L⁻¹ M = A_census L M := by
  unfold A A_census
  field_simp

/-- And the derived polynomial is **not** the census one as it stands: at `(L, M) = (2, 0)` the
derived `A` is `8` and the census polynomial is `1`. -/
theorem A_ne_A_census : A (2 : ℚ) 0 ≠ A_census (2 : ℚ) 0 := by
  unfold A A_census; norm_num

end QOU.Mass.FiveTwoAPolynomialFromFareyWord
