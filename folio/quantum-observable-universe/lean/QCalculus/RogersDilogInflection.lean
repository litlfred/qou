/-
# The trefoil's flat shape `z = 1/2` is an inflection point of the Rogers dilogarithm

**The `H(q₀)` coloring-map derivation, structural core.** The deuteron `σ₁³` closure is the trefoil
`T(2,3)` — a torus knot with a *flat* (degenerate, real) ideal-triangulation shape `z = 1/2`
(SnapPy; `deuteron_octahedral_gluing_probe.py`). The μ₀ −9% binding closure needs the **bar-even**
(order `h² = (q−q⁻¹)²`) coefficient `g₂ ≈ 1.0087`. This file records *why the single-tetrahedron
shape deformation cannot supply it*.

The single-tetrahedron binding amplitude is the **Rogers dilogarithm** `L(z) = Li₂(z) + ½·log z·
log(1−z)` (the real phase of the octahedral state integral; the imaginary/volume side vanishes on
the flat shape). Its second derivative has the elementary closed form

  `L''(z) = −½·( log z / (1−z)² − log(1−z) / z² )`

(using `Li₂'(z) = −log(1−z)/z`, a standard dilogarithm identity — `-- Ref:` below; the `Li₂` values
themselves never enter, only its elementary derivative). The bracket is **antisymmetric under the
Abel reflection `z ↦ 1−z`**, whose fixed point is `z = 1/2`; hence `L''(1/2) = 0`: the flat trefoil
shape is an **inflection point**. Consequently the leading (second-order) bar-even correction from
deforming the single shape modulus vanishes identically, and `g₂` must instead come from the
**pairwise `e₂` coupling** of the four octahedral tetrahedra (`FourDilogFirstOrder.e2`), not from the
single modulus. Scope-(a): this prunes the single-modulus route; it does not exclude the octahedral
`e₂` route.

§7c: archimedean (`Real.log`, ordering) ⇒ base ring is `ℝ`, placed after the substrate wall.
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.MassTheory

open Real

/-- The **elementary closed form of the Rogers-dilogarithm second derivative**
`L''(z) = −½·( log z / (1−z)² − log(1−z) / z² )`.  (Only the elementary derivative
`Li₂'(z) = −log(1−z)/z` is used to obtain this form; no `Li₂` value is needed.)
-- Ref: [hakimoglu-brown2025] https://arxiv.org/abs/2506.10206 (Rogers L-function, eq. 4) -/
noncomputable def rogersL2 (z : ℝ) : ℝ :=
  -(1 / 2) * (Real.log z / (1 - z) ^ 2 - Real.log (1 - z) / z ^ 2)

/-- The defining bracket of `rogersL2`, isolated for the antisymmetry statement. -/
noncomputable def rogersL2Bracket (z : ℝ) : ℝ :=
  Real.log z / (1 - z) ^ 2 - Real.log (1 - z) / z ^ 2

/-- **Abel-reflection antisymmetry.** The bracket flips sign under `z ↦ 1−z`. This is the structural
reason for the inflection: `z = 1/2` is the reflection's fixed point. -/
theorem rogersL2Bracket_reflect (z : ℝ) :
    rogersL2Bracket (1 - z) = - rogersL2Bracket z := by
  unfold rogersL2Bracket
  have h : (1 : ℝ) - (1 - z) = z := by ring
  rw [h]
  ring

/-- **The flat trefoil shape `z = 1/2` is an inflection point of the Rogers dilogarithm:**
`L''(1/2) = 0`.  Hence the single-tetrahedron bar-even (second-order) shape correction vanishes; the
μ₀ closure's `g₂` (order `h²`) cannot come from the single modulus and must be the octahedral
`e₂` pairwise term. -/
theorem rogersL2_half_eq_zero : rogersL2 (1 / 2) = 0 := by
  unfold rogersL2
  norm_num

/-- **The inflection is forced by the reflection symmetry.** The bracket vanishes at the fixed point
`z = 1/2` of `z ↦ 1−z` because it is antisymmetric there (`B(1/2) = B(1 − 1/2) = −B(1/2)`). -/
theorem rogersL2Bracket_half_eq_zero : rogersL2Bracket (1 / 2) = 0 := by
  have h := rogersL2Bracket_reflect (1 / 2)
  norm_num at h
  linarith

end QOU.MassTheory
