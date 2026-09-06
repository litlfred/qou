import QOU.Mass.CoordinationBulkCriterion
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics
import Mathlib.Tactic

/-!
# QOU.Mass.HyperbolicSurfaceLaw — in `H³` the surface fraction tends to a CONSTANT, so the framework's own geometry predicts no `A^(−1/3)` term at all

Every surface-term tranche on this arc so far (#6761, #6780, #6801, #6886) imported the compact
**Euclidean** surface law `A_surf ∝ A^(2/3)`, and the corpus objected each time: the ambient
geometry of this framework is hyperbolic. `docs/coordination/sm-26-parameter-chip-away.md`
already measured that using `H³` consistently — `R ∼ ½ ln V`, so `ln A` where the Euclidean import
has `A^(1/3)` — *costs* accuracy on a neighbouring quantity, and `qou-rav3` asked for "a packing
argument inside the framework" rather than a citation. This file is that argument, for the
surface fraction, and it is exact.

## The fact

A ball of radius `R` in `H³` (curvature `−1`) has

    V(R) = π (sinh 2R − 2R)          S(R) = 4π sinh² R = 2π (cosh 2R − 1).

In Euclidean space `S/V = 3/R → 0`: the boundary is a vanishing fraction of a large ball, and that
vanishing is the whole origin of the `A^(−1/3)` surface term. **In hyperbolic space it does not
vanish.** Exactly,

    S − 2V = 2π (e^(−2R) + 2R − 1)  ≥  0            since  e^(−x) ≥ 1 − x,

so **`S/V ≥ 2` for every `R > 0`** (`surfaceFraction_ge_two`), with equality only in the limit —
the boundary of a large hyperbolic ball is a *fixed* fraction of its volume, not a vanishing one.

## What that does to the binding law

`CoordinationSurfaceDeficit` puts the whole `A`-dependence of the correction in `A_surf/A`, and
`CoordinationBulkCriterion` needs that fraction to **vanish** for a surface term to exist:
`HasBulk := A_surf → ∞ ∧ A_surf/A → 0`. A hyperbolic-ball cluster — nucleon count extensive in
volume, surface count extensive in area, under **any** radius assignment `R(A) > 0` whatever —
has `A_surf/A ≥ 2` at every `A`, so it **fails `HasBulk`** (`hyperbolic_not_hasBulk`). Its
"surface term" is a **constant shift of the volume coefficient**,

    B/A ≤ εk/2 − ε(k − k')                                    (`hyperbolic_perNucleon_le`)

and the residual `A`-dependence is `f(R) − 2 ≤ 4R/(sinh 2R − 2R)` (`surfaceFraction_sub_two_le`),
which with `V ∼ (π/2) e^(2R)`, i.e. `R ∼ ½ ln A`, is of order **`(ln A)/A`** — a *different
functional form* from `A^(−1/3)`, and one the residual has never been tested against. The
companion probe tests it. The honest expectation, on the record before running: it fits **worse**
than the Euclidean import, because the corpus already measured that consistency costs accuracy.

## Why this is the right kind of negative

A fit that is worse and comes from the framework's own geometry can be iterated: it tells you
what the geometry actually predicts, and the discrepancy is information. A fit that is better and
comes from an imported Euclidean packing cannot — it has already absorbed the discrepancy. The four
tranches before this one all ended on the imported side of that line; this is the first on the
other side.

## Scope

* **Proved:** `S = 2π(cosh 2R − 1)`; `V > 0` for `R > 0`; `2V ≤ S` for all `R`; `S/V ≥ 2`; the
  Euclidean contrast `S/V = 3/R → 0`; a generic lemma that a surface fraction bounded below by a
  positive constant refutes `HasBulk`; `¬HasBulk` for the hyperbolic cluster under any positive
  radius assignment; the per-nucleon bound; and the decay bound on `f − 2`. All exact, no fit.
* **NOT proved here:** the limit `S/V → 2` itself (the bound `f − 2 ≤ 4R/(sinh 2R − 2R)` is
  stated; that its right side tends to `0` is elementary and is checked numerically in the probe,
  not formalised); and the `(ln A)/A` asymptotic form of the correction, which needs the inverse
  `R(A)` and is left to the probe as a measured statement.
* **Assumed:** that the cluster is a metric ball in `H³` of curvature `−1`, with nucleon count
  extensive in volume and surface count extensive in area. This is the hyperbolic analogue of the
  compact-packing hypothesis the Euclidean tranches made — but it is the framework's *own*
  geometry rather than an import, which is the point.
* **NOT derived:** that the substrate emits such a cluster (`qou-brng`'s open input, unchanged),
  nor the radius assignment `R(A)`; every theorem here holds for **all** `R(A) > 0`, so nothing
  about the assignment is used.
* **Not a fit.** No coefficient is chosen against data.

Ground ring `ℝ` (§7c: archimedean — `sinh`, `cosh`, `exp`, limits).

-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/Mass/CoordinationBulkCriterion.lean
-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/Mass/CoordinationSurfaceDeficit.lean
-- Ref: [manuscript] docs/coordination/sm-26-parameter-chip-away.md (the hyperbolic-vs-Euclidean import objection)
-/

namespace QOU.Mass.HyperbolicSurfaceLaw

open Real Filter QOU.Mass.CoordinationBulkCriterion

/-! ## The hyperbolic ball -/

/-- Volume of a ball of radius `R` in `H³` (curvature `−1`): `π (sinh 2R − 2R)`. -/
noncomputable def hypVol (R : ℝ) : ℝ := π * (sinh (2 * R) - 2 * R)

/-- Area of the boundary sphere of that ball: `4π sinh² R`. -/
noncomputable def hypArea (R : ℝ) : ℝ := 4 * π * sinh R ^ 2

theorem hypArea_eq (R : ℝ) : hypArea R = 2 * π * (cosh (2 * R) - 1) := by
  unfold hypArea
  rw [cosh_two_mul, cosh_sq]
  ring

theorem hypVol_pos {R : ℝ} (hR : 0 < R) : 0 < hypVol R := by
  unfold hypVol
  have h : 2 * R < sinh (2 * R) := self_lt_sinh_iff.mpr (by linarith)
  have hπ := Real.pi_pos
  have : 0 < sinh (2 * R) - 2 * R := by linarith
  positivity

/-- **`S − 2V = 2π (e^(−2R) + 2R − 1)`**, exactly. -/
theorem hypArea_sub_two_mul_hypVol (R : ℝ) :
    hypArea R - 2 * hypVol R = 2 * π * (exp (-(2 * R)) + 2 * R - 1) := by
  rw [hypArea_eq]
  unfold hypVol
  have hcs : cosh (2 * R) - sinh (2 * R) = exp (-(2 * R)) := by
    rw [cosh_eq, sinh_eq]; ring
  rw [← hcs]
  ring

/-- **`2V ≤ S` for every `R`** — the whole content is `e^(−x) ≥ 1 − x`. -/
theorem two_mul_hypVol_le_hypArea (R : ℝ) : 2 * hypVol R ≤ hypArea R := by
  have h := add_one_le_exp (-(2 * R))
  have hnn : 0 ≤ exp (-(2 * R)) + 2 * R - 1 := by linarith
  have := mul_nonneg (by positivity : (0 : ℝ) ≤ 2 * π) hnn
  have key := hypArea_sub_two_mul_hypVol R
  linarith

/-- **The hyperbolic surface fraction is at least 2, for every radius.** In Euclidean space it is
`3/R → 0`; here it never drops below a constant. -/
theorem surfaceFraction_ge_two {R : ℝ} (hR : 0 < R) : 2 ≤ hypArea R / hypVol R := by
  rw [le_div_iff₀ (hypVol_pos hR)]
  exact two_mul_hypVol_le_hypArea R

/-- The residual `A`-dependence: `S/V − 2 ≤ 4R/(sinh 2R − 2R)`, which decays like `R e^(−2R)`. -/
theorem surfaceFraction_sub_two_le {R : ℝ} (hR : 0 < R) :
    hypArea R / hypVol R - 2 ≤ 4 * R / (sinh (2 * R) - 2 * R) := by
  have hV := hypVol_pos hR
  have hs : 0 < sinh (2 * R) - 2 * R := by
    have := self_lt_sinh_iff.mpr (by linarith : 0 < 2 * R); linarith
  have hπ := Real.pi_pos
  have hexp : exp (-(2 * R)) ≤ 1 := exp_le_one_iff.mpr (by linarith)
  have hnum : hypArea R - 2 * hypVol R ≤ 4 * π * R := by
    rw [hypArea_sub_two_mul_hypVol]; nlinarith
  have h1 : hypArea R / hypVol R - 2 = (hypArea R - 2 * hypVol R) / hypVol R := by
    field_simp
  rw [h1]
  have h2 : (hypArea R - 2 * hypVol R) / hypVol R ≤ 4 * π * R / hypVol R :=
    div_le_div_of_nonneg_right hnum hV.le
  have h3 : 4 * π * R / hypVol R = 4 * R / (sinh (2 * R) - 2 * R) := by
    unfold hypVol; field_simp
  linarith

/-! ## The Euclidean contrast -/

noncomputable def eucVol (R : ℝ) : ℝ := 4 / 3 * π * R ^ 3
noncomputable def eucArea (R : ℝ) : ℝ := 4 * π * R ^ 2

/-- Euclidean: `S/V = 3/R`. -/
theorem eucFraction_eq {R : ℝ} (hR : 0 < R) : eucArea R / eucVol R = 3 / R := by
  unfold eucArea eucVol
  have hπ := Real.pi_pos
  field_simp

/-- Euclidean: the surface fraction **vanishes** — the origin of every `A^(−1/3)` surface term. -/
theorem eucFraction_tendsto_zero : Tendsto (fun R : ℝ => 3 / R) atTop (nhds 0) := by
  have := tendsto_inv_atTop_zero.const_mul (3 : ℝ)
  simpa [div_eq_mul_inv] using this

/-! ## No bulk -/

/-- **A surface fraction bounded below by a positive constant refutes `HasBulk`.** Generic. -/
theorem not_hasBulk_of_fraction_ge (Asurf : ℝ → ℝ) (c : ℝ) (hc : 0 < c)
    (h : ∀ᶠ A in atTop, c ≤ Asurf A / A) : ¬ HasBulk Asurf := by
  rintro ⟨-, h0⟩
  have h1 : ∀ᶠ A in atTop, Asurf A / A < c := Filter.Tendsto.eventually_lt_const hc h0
  obtain ⟨A, hA1, hA2⟩ := (h.and h1).exists
  linarith

/-- The surface count of a hyperbolic-ball cluster under a radius assignment `Rof`: nucleon count
`A` extensive in volume, surface count extensive in area, so `A_surf = (S/V)(R(A)) · A`. -/
noncomputable def hypSurfaceCount (Rof : ℝ → ℝ) (A : ℝ) : ℝ :=
  hypArea (Rof A) / hypVol (Rof A) * A

theorem hypSurfaceCount_div (Rof : ℝ → ℝ) (A : ℝ) (hA : A ≠ 0) :
    hypSurfaceCount Rof A / A = hypArea (Rof A) / hypVol (Rof A) := by
  unfold hypSurfaceCount
  field_simp

/-- **A hyperbolic-ball cluster has no bulk, under ANY positive radius assignment.** Its surface
fraction is `≥ 2` at every `A`, so it never vanishes. -/
theorem hyperbolic_not_hasBulk (Rof : ℝ → ℝ) (hR : ∀ A, 0 < Rof A) :
    ¬ HasBulk (hypSurfaceCount Rof) := by
  apply not_hasBulk_of_fraction_ge _ 2 (by norm_num)
  filter_upwards [eventually_ne_atTop (0 : ℝ)] with A hA
  rw [hypSurfaceCount_div Rof A hA]
  exact surfaceFraction_ge_two (hR A)

/-- **The hyperbolic "surface term" is a constant shift of the volume coefficient, not a decaying
correction.** With `k' < k` the per-nucleon binding sits at least `ε(k − k')` below the
uniform-degree plateau at every `A`. -/
theorem hyperbolic_perNucleon_le (ε k k' : ℝ) (hε : 0 < ε) (hkk : k' < k)
    (Rof : ℝ → ℝ) (hR : ∀ A, 0 < Rof A) (A : ℝ) (hA : 0 < A) :
    ε * k / 2 - (ε * (k - k') / 2) * (hypSurfaceCount Rof A / A) ≤ ε * k / 2 - ε * (k - k') := by
  rw [hypSurfaceCount_div Rof A (ne_of_gt hA)]
  have hf := surfaceFraction_ge_two (hR A)
  have hc : 0 < ε * (k - k') / 2 := by
    have := sub_pos.mpr hkk
    positivity
  nlinarith

end QOU.Mass.HyperbolicSurfaceLaw
