import QOU.QBeta.BarParityZeta4Swap

/-!
# The figure-eight cusp shape in bar-parity coordinates — `barEven = 1`, `barOdd² = −3`

The **cusp side** of the pole→cusp story (`conj:algebraic-geometric-dilog-equivalence`;
the *pole* side is proved in `QOU.QBeta.QPochhammerPoles`).  The complete
hyperbolic structure on the figure-eight complement `S³∖4₁` has both ideal
tetrahedra at the **shape** `ω = e^{iπ/3}`, the primitive sixth root of unity —
the root of the cyclotomic `Φ₆(z) = z² − z + 1` whose splitting field is the
figure-eight **trace field `ℚ(√−3)`**.

This file makes the shape explicit **in the bar-parity coordinates** of
`QOU.QBeta.BarParityZeta4Swap` (reusing `barEven`/`barOdd`), and proves — over a
generic field, no archimedean structure — that the shape's bar-parity split is
**exactly the `𝔙 = Vol + i·CS` split**:

* `barEven ω = ω + ω⁻¹ = 1` — the **bar-even / mass / `Re 𝔙` = `Vol`** coordinate
  (rational, `= 2cos(π/3)`; the amphichiral, anchor-stable part `−Vol(4₁)`);
* `barOdd ω = ω − ω⁻¹ = 2ω − 1` with `(barOdd ω)² = −3` — the **bar-odd /
  decay=binding / `Im 𝔙` = `CS`** coordinate, whose square is the **cusp modulus
  `τ ∝ √−3`** (`= 2i·sin(π/3) = √−3` archimedean).

So the two faces of the complex volume `𝔙` (`binding-qbeta-complex-volume.lean`,
`𝔈_bind = Re 𝔙`, `𝔔_β = Im 𝔙`) are the two bar-parity coordinates of the ONE
cusp shape `ω`, and the `√−3` that drives the Neumann–Zagier deformation
`CVol(u) = Vol − (τ/4)u² + …` is `barOdd(ω)`.  The `q₀ ↦ u` meridian-holonomy map
(the open link) is what deforms `ω` off this complete point; everything here is
the **complete-point (`u = 0`) coordinate data**, proved exactly.

Also proved: `ω` is a primitive sixth root of unity (`ω³ = −1`, `ω⁶ = 1`) — the
root-of-unity structure the bar-odd phase channel accumulates in.

Generic field, §7c. No `c_k` wired; no archimedean evaluation.

-- Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
-- Ref: [leitner2026] conj:algebraic-geometric-dilog-equivalence
-- Ref: [leitner2026] docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md
-/

namespace QOU.QBeta.CuspShapeBarParity

open QOU.QBeta.BarParityZeta4Swap

variable {R : Type*} [Field R]

/-- The figure-eight cusp shape `ω` is a root of the cyclotomic `Φ₆(z) = z²−z+1`
(trace field `ℚ(√−3)`).  We take that minimal polynomial as the defining
hypothesis; the archimedean realisation is `ω = e^{iπ/3}`. -/
def IsCuspShape (ω : R) : Prop := ω ^ 2 - ω + 1 = 0

/-- The cusp shape is nonzero (`Φ₆(0) = 1 ≠ 0`). -/
theorem cuspShape_ne_zero {ω : R} (hω : IsCuspShape ω) : ω ≠ 0 := by
  intro h
  have hp : ω ^ 2 - ω + 1 = 0 := hω
  rw [h] at hp; norm_num at hp

/-- `ω² = ω − 1` (the minimal-polynomial rewrite). -/
theorem cuspShape_sq {ω : R} (hω : IsCuspShape ω) : ω ^ 2 = ω - 1 := by
  have hp : ω ^ 2 - ω + 1 = 0 := hω
  linear_combination hp

/-- **The inverse in shape coordinates:** `ω⁻¹ = 1 − ω`.  The bar involution
`ω ↦ ω⁻¹` acts as the reflection `ω ↦ 1 − ω` on the cusp shape (the
`z ↦ 1 − 1/z ↦ …` tetrahedral symmetry, here at the symmetric point). -/
theorem cuspShape_inv {ω : R} (hω : IsCuspShape ω) : ω⁻¹ = 1 - ω := by
  refine inv_eq_of_mul_eq_one_right ?_
  have h2 := cuspShape_sq hω
  linear_combination -h2

/-- **Bar-even coordinate `= 1`** (`Re 𝔙 = Vol` side): `barEven ω = ω + ω⁻¹ = 1`,
the amphichiral / anchor-stable part.  Archimedean: `2cos(π/3) = 1`. -/
theorem cuspShape_barEven {ω : R} (hω : IsCuspShape ω) : barEven ω = 1 := by
  unfold barEven; rw [cuspShape_inv hω]; ring

/-- **Bar-odd coordinate `= 2ω − 1`** (`Im 𝔙 = CS` side): `barOdd ω = ω − ω⁻¹`. -/
theorem cuspShape_barOdd {ω : R} (hω : IsCuspShape ω) : barOdd ω = 2 * ω - 1 := by
  unfold barOdd; rw [cuspShape_inv hω]; ring

/-- **The cusp modulus `√−3`:** the bar-odd coordinate squares to `−3`, i.e.
`(barOdd ω)² = −3`.  This is the figure-eight trace-field discriminant / the
Neumann–Zagier cusp modulus `τ ∝ √−3` — proved exactly, generic field.
Archimedean: `barOdd ω = 2i·sin(π/3) = √−3`. -/
theorem cuspShape_barOdd_sq {ω : R} (hω : IsCuspShape ω) : (barOdd ω) ^ 2 = -3 := by
  rw [cuspShape_barOdd hω]
  have h2 := cuspShape_sq hω
  linear_combination 4 * h2

/-- `ω³ = −1`: the cusp shape is a primitive sixth root of unity (`ω = e^{iπ/3}`),
so `ω³ = e^{iπ} = −1`.  The root-of-unity structure the bar-odd phase channel
accumulates in. -/
theorem cuspShape_cube {ω : R} (hω : IsCuspShape ω) : ω ^ 3 = -1 := by
  have h2 := cuspShape_sq hω
  linear_combination (ω + 1) * h2

/-- `ω⁶ = 1`: primitive sixth root of unity. -/
theorem cuspShape_sixth {ω : R} (hω : IsCuspShape ω) : ω ^ 6 = 1 := by
  have h3 := cuspShape_cube hω
  linear_combination (ω ^ 3 - 1) * h3

/-- **Reconstruction (Re/Im of `𝔙` from one shape):** the bar-even and bar-odd
coordinates reconstruct `2ω`: `barEven ω + barOdd ω = 2ω`.  With
`barEven ω = 1` and `(barOdd ω)² = −3` this says `2ω = 1 + √−3`, i.e.
`ω = (1 + √−3)/2 = e^{iπ/3}` — the complete cusp shape recovered from its
`Vol`(=1) and `CS`(=√−3) coordinates. -/
theorem cuspShape_reconstruct (ω : R) : barEven ω + barOdd ω = 2 * ω := by
  unfold barEven barOdd; ring

/-! ## The degenerate (golden-ratio) branch — why a real pole cannot reach the cusp

The complete figure-eight gluing equation `(z(z−1))² = 1` factors into **two**
branches, `z(z−1) = ±1`:

* `z² − z + 1 = 0` — the **cusp** shape `e^{iπ/3}` (`IsCuspShape`), complex,
  discriminant `−3`: the hyperbolic structure, `barOdd² = −3` (`√−3` = CS).
* `z² − z − 1 = 0` — the **golden ratio** `φ = (1+√5)/2` (`IsGoldenShape`), real,
  discriminant `+5`: the **degenerate** structure (`Vol = 0`, no hyperbolic geometry).

The two branches **swap bar-parity roles**, and the swap is exactly a **sign flip
in the discriminant** `−3 ↦ +5`:

| branch | poly | `barEven` | `barOdd` | special coord |
|---|---|---|---|---|
| cusp (hyperbolic) | `z²−z+1` | `= 1` (rational) | `² = −3` | `barOdd = √−3` (imaginary ⇒ **CS**) |
| golden (degenerate) | `z²−z−1` | `² = +5` | `= 1` (rational) | `barEven = √5` (**real** ⇒ **no CS**) |

This is the algebraic shadow of the pole→cusp phase obstruction: seeding
Thurston's Newton with the **real** substrate pole `q₀^{-k}` flows to the golden
(real, `√5`) branch — `Vol = 0`, `CS = 0` — never the cusp. Only **complexifying**
the seed (the phase `φ(q₀)`) moves the special coordinate from the real `√5` to the
imaginary `√−3`, i.e. turns on the CS = bar-odd `S`. The phase is precisely the
branch selector, and no real datum can supply it.

-- Ref: [leitner2026] docs/audits/2026-07-11-qbeta-c3-pole-cusp-phase-tractability.md
-/

/-- The degenerate (golden-ratio) branch: `ω² − ω − 1 = 0`, real root `φ=(1+√5)/2`. -/
def IsGoldenShape (ω : R) : Prop := ω ^ 2 - ω - 1 = 0

/-- `ω² = ω + 1` (golden minimal-polynomial rewrite). -/
theorem goldenShape_sq {ω : R} (hω : IsGoldenShape ω) : ω ^ 2 = ω + 1 := by
  have hp : ω ^ 2 - ω - 1 = 0 := hω
  linear_combination hp

/-- Golden inverse in shape coordinates: `ω⁻¹ = ω − 1`. -/
theorem goldenShape_inv {ω : R} (hω : IsGoldenShape ω) : ω⁻¹ = ω - 1 := by
  refine inv_eq_of_mul_eq_one_right ?_
  have h2 := goldenShape_sq hω
  linear_combination h2

/-- **Golden bar-odd `= 1`** (rational): on the degenerate branch the bar-ODD
coordinate is rational — the roles are swapped vs the cusp (where bar-EVEN = 1). -/
theorem goldenShape_barOdd {ω : R} (hω : IsGoldenShape ω) : barOdd ω = 1 := by
  unfold barOdd; rw [goldenShape_inv hω]; ring

/-- **Golden bar-even `= √5`** (`(barEven ω)² = 5`, REAL): the degenerate branch's
special coordinate is the **real** `√5`, not the cusp's imaginary `√−3`. A real
pole seeds this branch — real coordinate, hence **no CS / no bar-odd `S`**. -/
theorem goldenShape_barEven_sq {ω : R} (hω : IsGoldenShape ω) : (barEven ω) ^ 2 = 5 := by
  unfold barEven; rw [goldenShape_inv hω]
  have h2 := goldenShape_sq hω
  linear_combination 4 * h2

end QOU.QBeta.CuspShapeBarParity
