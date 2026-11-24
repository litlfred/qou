/-
  Machine-generated Lean proofs of the edge gluing equations, with exact certificates.

  Bean `qou-glnl`.  Generated from SnapPy's integer exponent matrices; every proof is a
  single `linear_combination` whose cofactor came from exact polynomial division, and
  every non-vanishing fact from a Bézout certificate.  Nothing here was guessed and
  nothing is numerical.

  ═══ THE FORMULATION, AND WHY IT IS THE ONE THAT WORKS ═══

  Each theorem is stated for an **arbitrary root** `t` of the shape field's minimal
  polynomial, not for the geometric one:

      theorem edge_k {t : ℂ} (ht : minpoly t = 0) : … = …

  The verification lives in `ℚ[x]/(P)`, so the identity holds at *every* root.  That
  sidesteps the whole root-selection problem — proving a quartic or quintic has a root
  with `Im > 0` would otherwise block every knot past `5₂`.  Which root is the geometric
  one is a separate, numerical matter, settled in Route 75 by a Bloch–Wigner volume
  cross-check against SnapPy; Lean is not the right tool for it and does not attempt it.

  ═══ WHY THE EQUATIONS APPEAR WITH DENOMINATORS CLEARED ═══

  Since `z′ = 1/(1−z)` and `z″ = (z−1)/z`, the gluing equation `∏ zᵃ z′ᵇ z″ᶜ = 1` is
  equivalent to the polynomial identity

      ∏ zⱼ^{aⱼ} · ∏ (zⱼ − 1)^{cⱼ}  =  ∏ (1 − zⱼ)^{bⱼ} · ∏ zⱼ^{cⱼ}

  and *that* form is provable by one `linear_combination` with a computed cofactor.  The
  natural quotient form would need `field_simp`, whose normal form is not predictable and
  therefore cannot be code-generated — a lesson from the hand-written `4₁`/`5₂` proofs,
  which cost several wrong-cofactor iterations.  The non-vanishing lemmas
  (`zⱼ_ne_zero`, `one_sub_zⱼ_ne_zero`) are proved anyway, so the quotient form is
  available to any caller that wants it.

  ═══ ⚠ SCOPE ═══

  **Edge equations only.**  Cusp equations carry negative exponents and need inverses as
  explicit polynomials; Route 75 verifies those in Python, Lean does not yet.

  Nothing here says any of this is a triangulation *of* a knot complement — that is
  Thurston hyperbolisation plus Mostow rigidity, needing hyperbolic 3-manifolds that
  neither Mathlib nor QOU has.  See `QOU/MathlibExt/IdealTriangulation.lean`.

  -- Ref: [thurston1978] Ch. 4
  -- Ref: [neumann-zagier1985]
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Tactic.LinearCombination

namespace QOU.Knot.GeneratedGluing

/-! ### `4_1` — 2 tetrahedra, shape field of degree 2

Minimal polynomial `x^2 - x + 1`. -/

namespace K41

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 2 + (-1) * t + 1

/-- Shape `z0` of `4_1`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `4_1`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := 1 * t

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t + 1) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t + 1) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t) * h + (1) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `4_1`, exponents `[2, 1, 0, 2, 1, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 2 * z1 t ^ 2 = (1 - z0 t) ^ 1 * (1 - z1 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1]
  linear_combination (1 * t ^ 2 + 1 * t + (-1)) * ht

/-- **Edge 1** of `4_1`, exponents `[0, 1, 2, 0, 1, 2]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 2 * (z1 t - 1) ^ 2 = (1 - z0 t) ^ 1 * z0 t ^ 2 * (1 - z1 t) ^ 1 * z1 t ^ 2 := by
  simp only [minpoly] at ht
  simp only [z0, z1]
  linear_combination ((-1) * t ^ 4 + 1 * t ^ 3 + 2 * t ^ 2 + (-3) * t + 1) * ht

end K41

/-! ### `5_2` — 3 tetrahedra, shape field of degree 3

Minimal polynomial `x^3 - 2*x^2 + 3*x - 1`. -/

namespace K52

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 3 + (-2) * t ^ 2 + 3 * t + (-1)

/-- Shape `z0` of `5_2`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `5_2`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := 1 * t ^ 2 + (-1) * t + 2

/-- Shape `z2` of `5_2`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := 1 * t

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 2 + (-2) * t + 3) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 2 + (-1) * t + 2) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t + 1) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 2 + 2 * t + (-2)) * h + ((-1) * t + 1) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 2 + (-2) * t + 3) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 2 + (-1) * t + 2) * h + (1) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `5_2`, exponents `[1, 0, 1, 1, 2, 0, 1, 0, 1]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z0 t - 1) ^ 1 * z1 t ^ 1 * z2 t ^ 1 * (z2 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 2 * z2 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2]
  linear_combination ((-1) * t ^ 2) * ht

/-- **Edge 1** of `5_2`, exponents `[0, 1, 1, 0, 0, 2, 0, 1, 1]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z1 t - 1) ^ 2 * (z2 t - 1) ^ 1 = (1 - z0 t) ^ 1 * z0 t ^ 1 * z1 t ^ 2 * (1 - z2 t) ^ 1 * z2 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2]
  linear_combination ((-1) * t ^ 5 + 2 * t ^ 4 + (-2) * t ^ 3 + 1 * t ^ 2 + 1 * t + (-1)) * ht

/-- **Edge 2** of `5_2`, exponents `[1, 1, 0, 1, 0, 0, 1, 1, 0]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * z1 t ^ 1 * z2 t ^ 1 = (1 - z0 t) ^ 1 * (1 - z2 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2]
  linear_combination (1 * t + 1) * ht

end K52

/-! ### `6_1` — 4 tetrahedra, shape field of degree 4

Minimal polynomial `x^4 - 3*x^3 + 6*x^2 - 5*x + 2`. -/

namespace K61

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 4 + (-3) * t ^ 3 + 6 * t ^ 2 + (-5) * t + 2

/-- Shape `z0` of `6_1`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `6_1`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := 1 * t ^ 3 + (-2) * t ^ 2 + 4 * t + (-1)

/-- Shape `z2` of `6_1`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := 1 * t ^ 2 + (-1) * t + 1

/-- Shape `z3` of `6_1`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := (-1 / 2) * t ^ 3 + (3 / 2) * t ^ 2 + (-2) * t + (3 / 2)

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 2) * t ^ 3 + (3 / 2) * t ^ 2 + (-3) * t + (5 / 2)) * h + ((1 / 2)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 3 + (-2) * t ^ 2 + 4 * t + (-1)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t + 1) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 2) * t ^ 3 + (-3 / 2) * t ^ 2 + 3 * t + (-3 / 2)) * h + ((1 / 2) * t ^ 2 + (-1) * t + 2) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 2 + (-2) * t + 3) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 2) * t ^ 3 + (-1 / 2) * t ^ 2 + 1 * t + (3 / 2)) * h + ((1 / 2) * t + (1 / 2)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 3 + (-2) * t ^ 2 + 3 * t) * h + ((1 / 2) * t ^ 2 + (-1) * t + (1 / 2)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 3 + 3 * t ^ 2 + (-5) * t + 4) * h + ((1 / 2) * t ^ 2 + (-3 / 2) * t + (3 / 2)) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `6_1`, exponents `[1, 0, 1, 1, 2, 0, 0, 0, 1, 0, 1, 1]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z0 t - 1) ^ 1 * z1 t ^ 1 * (z2 t - 1) ^ 1 * (z3 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 2 * z2 t ^ 1 * (1 - z3 t) ^ 1 * z3 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3]
  linear_combination ((1 / 4) * t ^ 11 + (-2) * t ^ 10 + (17 / 2) * t ^ 9 + (-24) * t ^ 8 + (195 / 4) * t ^ 7 + (-295 / 4) * t ^ 6 + (167 / 2) * t ^ 5 + (-139 / 2) * t ^ 4 + (77 / 2) * t ^ 3 + (-12) * t ^ 2 + (3 / 2) * t) * ht

/-- **Edge 1** of `6_1`, exponents `[0, 1, 1, 0, 0, 2, 0, 1, 1, 1, 0, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z1 t - 1) ^ 2 * (z2 t - 1) ^ 1 * z3 t ^ 1 = (1 - z0 t) ^ 1 * z0 t ^ 1 * z1 t ^ 2 * (1 - z2 t) ^ 1 * z2 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3]
  linear_combination ((-3 / 2) * t ^ 8 + 7 * t ^ 7 + (-39 / 2) * t ^ 6 + 34 * t ^ 5 + (-39) * t ^ 4 + 31 * t ^ 3 + (-15) * t ^ 2 + 3 * t) * ht

/-- **Edge 2** of `6_1`, exponents `[0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    z1 t ^ 1 * z2 t ^ 1 * (z3 t - 1) ^ 1 = (1 - z0 t) ^ 1 * z3 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3]
  linear_combination ((-1 / 2) * t ^ 4 + (3 / 2) * t ^ 3 + (-5 / 2) * t ^ 2 + (3 / 2) * t + (-1)) * ht

/-- **Edge 3** of `6_1`, exponents `[1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * z2 t ^ 1 * z3 t ^ 1 = (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z2, z3]
  linear_combination ((-1 / 2) * t ^ 2 + 1 * t) * ht

end K61

/-! ### `7_2` — 4 tetrahedra, shape field of degree 5

Minimal polynomial `x^5 - 2*x^4 + x^3 + 3*x^2 - 5*x + 3`. -/

namespace K72

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 5 + (-2) * t ^ 4 + 1 * t ^ 3 + 3 * t ^ 2 + (-5) * t + 3

/-- Shape `z0` of `7_2`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `7_2`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := (1 / 3) * t ^ 4 + (-2 / 3) * t ^ 3 + (1 / 3) * t ^ 2 + 1 * t + (-2 / 3)

/-- Shape `z2` of `7_2`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := 1 * t ^ 4 + (-1) * t ^ 3 + 3 * t + (-2)

/-- Shape `z3` of `7_2`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := (1 / 9) * t ^ 4 + (4 / 9) * t ^ 3 + (-2 / 9) * t ^ 2 + (13 / 9)

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 3) * t ^ 4 + (2 / 3) * t ^ 3 + (-1 / 3) * t ^ 2 + (-1) * t + (5 / 3)) * h + ((1 / 3)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 4 + (-1) * t ^ 3 + 3 * t + (-2)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 4 + 1 * t ^ 3 + (-3) * t + 3) * h + ((1 / 3) * t ^ 3 + (-1 / 3) * t ^ 2 + 1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t) * h + ((1 / 3)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t + 1) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 3) * t ^ 4 + (-2 / 3) * t ^ 3 + (1 / 3) * t ^ 2 + 1 * t + (-2 / 3)) * h + ((1 / 3) * t ^ 3 + (-1 / 3) * t ^ 2 + 1) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 3 + 1 * t ^ 2) * h + ((1 / 9) * t ^ 2 + (5 / 9) * t + (1 / 3)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (2 * t ^ 4 + (-2) * t ^ 3 + (-1) * t ^ 2 + 5 * t + (-3)) * h + ((2 / 9) * t ^ 3 + (10 / 9) * t ^ 2 + (5 / 9) * t + (-1 / 9)) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `7_2`, exponents `[1, 1, 0, 2, 0, 0, 1, 0, 1, 0, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * z1 t ^ 2 * z2 t ^ 1 * (z2 t - 1) ^ 1 = (1 - z0 t) ^ 1 * z2 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2]
  linear_combination ((1 / 9) * t ^ 12 + (-4 / 9) * t ^ 11 + (2 / 3) * t ^ 10 + (5 / 9) * t ^ 9 + (-3) * t ^ 8 + (31 / 9) * t ^ 7 + (13 / 9) * t ^ 6 + (-58 / 9) * t ^ 5 + (40 / 9) * t ^ 4 + (20 / 9) * t ^ 3 + (-4) * t ^ 2 + (1 / 3) * t + (2 / 3)) * ht

/-- **Edge 1** of `7_2`, exponents `[0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 2]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * z2 t ^ 1 * (z3 t - 1) ^ 2 = (1 - z0 t) ^ 1 * z1 t ^ 1 * z3 t ^ 2 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3]
  linear_combination ((1 / 243) * t ^ 11 + (7 / 243) * t ^ 10 + (4 / 243) * t ^ 9 + (-8 / 81) * t ^ 8 + (19 / 81) * t ^ 7 + (41 / 243) * t ^ 6 + (-175 / 243) * t ^ 5 + (70 / 243) * t ^ 4 + (19 / 27) * t ^ 3 + (-299 / 243) * t ^ 2 + (-13 / 27) * t + (166 / 243)) * ht

/-- **Edge 2** of `7_2`, exponents `[1, 0, 1, 0, 2, 1, 0, 1, 1, 1, 0, 0]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z0 t - 1) ^ 1 * (z1 t - 1) ^ 1 * (z2 t - 1) ^ 1 * z3 t ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 2 * z1 t ^ 1 * (1 - z2 t) ^ 1 * z2 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3]
  linear_combination ((1 / 27) * t ^ 16 + (-2 / 9) * t ^ 15 + (5 / 9) * t ^ 14 + (-8 / 27) * t ^ 13 + (-17 / 9) * t ^ 12 + (140 / 27) * t ^ 11 + (-109 / 27) * t ^ 10 + (-173 / 27) * t ^ 9 + (163 / 9) * t ^ 8 + (-118 / 9) * t ^ 7 + (-98 / 9) * t ^ 6 + (250 / 9) * t ^ 5 + (-433 / 27) * t ^ 4 + (-8) * t ^ 3 + (46 / 3) * t ^ 2 + (-55 / 9) * t) * ht

/-- **Edge 3** of `7_2`, exponents `[0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 2, 0]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * z3 t ^ 1 = z0 t ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 2 := by
  simp only [minpoly] at ht
  simp only [z0, z2, z3]
  linear_combination ((1 / 81) * t ^ 8 + (1 / 9) * t ^ 7 + (7 / 27) * t ^ 6 + (5 / 81) * t ^ 5 + (16 / 81) * t ^ 4 + (38 / 81) * t ^ 3 + (-1 / 9) * t ^ 2 + (-14 / 27) * t + (-13 / 27)) * ht

end K72

/-! ### `s776` — 6 tetrahedra, shape field of degree 2

Minimal polynomial `2*x^2 + x + 1`. -/

namespace Ks776

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 2 * t ^ 2 + 1 * t + 1

/-- Shape `z0` of `s776`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `s776`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := 2 * t + 1

/-- Shape `z2` of `s776`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := 2 * t + 1

/-- Shape `z3` of `s776`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := 2 * t + 1

/-- Shape `z4` of `s776`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := 2 * t + 1

/-- Shape `z5` of `s776`, as an element of `ℚ(θ)`. -/
noncomputable def z5 (t : ℂ) : ℂ := 1 * t

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-2) * t + (-1)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 2) * t + (3 / 4)) * h + ((1 / 4)) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t + (1 / 2)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t + (1 / 2)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t + (1 / 2)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t + (1 / 2)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-2) * t + (-1)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 2) * t + (3 / 4)) * h + ((1 / 4)) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `s776`, exponents `[1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * z1 t ^ 1 * z2 t ^ 1 * z5 t ^ 1 = 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z5]
  linear_combination (2 * t ^ 2 + 1 * t + (-1)) * ht

/-- **Edge 1** of `s776`, exponents `[0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    z1 t ^ 1 * (z1 t - 1) ^ 1 * z2 t ^ 1 * (z2 t - 1) ^ 1 * (z3 t - 1) ^ 1 * (z4 t - 1) ^ 1 = (1 - z0 t) ^ 1 * z1 t ^ 1 * z2 t ^ 1 * z3 t ^ 1 * z4 t ^ 1 * (1 - z5 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4, z5]
  linear_combination (24 * t ^ 4 + 20 * t ^ 3 + (-2) * t ^ 2 + (-5) * t + (-1)) * ht

/-- **Edge 2** of `s776`, exponents `[0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z5 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 * (1 - z4 t) ^ 1 * z5 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4, z5]
  linear_combination ((-8) * t ^ 4 + 4 * t ^ 3 + 2 * t ^ 2 + (-3) * t + 1) * ht

/-- **Edge 3** of `s776`, exponents `[0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z5 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 * (1 - z4 t) ^ 1 * z5 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4, z5]
  linear_combination ((-8) * t ^ 4 + 4 * t ^ 3 + 2 * t ^ 2 + (-3) * t + 1) * ht

/-- **Edge 4** of `s776`, exponents `[0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * (z2 t - 1) ^ 1 * z3 t ^ 1 * (z3 t - 1) ^ 1 * z4 t ^ 1 * (z4 t - 1) ^ 1 = (1 - z0 t) ^ 1 * z1 t ^ 1 * z2 t ^ 1 * z3 t ^ 1 * z4 t ^ 1 * (1 - z5 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4, z5]
  linear_combination (24 * t ^ 4 + 20 * t ^ 3 + (-2) * t ^ 2 + (-5) * t + (-1)) * ht

/-- **Edge 5** of `s776`, exponents `[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]`, denominators cleared. -/
theorem edge_5 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * z3 t ^ 1 * z4 t ^ 1 * z5 t ^ 1 = 1 := by
  simp only [minpoly] at ht
  simp only [z0, z3, z4, z5]
  linear_combination (2 * t ^ 2 + 1 * t + (-1)) * ht

end Ks776

/-! ### `12n242` — 3 tetrahedra, shape field of degree 3

Minimal polynomial `x^3 - x^2 + 2*x - 1`. -/

namespace K12n242

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 3 + (-1) * t ^ 2 + 2 * t + (-1)

/-- Shape `z0` of `12n242`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `12n242`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := (-1) * t ^ 2 + 1 * t + (-1)

/-- Shape `z2` of `12n242`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := 1 * t ^ 2 + 2

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 2 + (-1) * t + 2) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 2 + 2) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 2 + (-1)) * h + ((-1) * t) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t + 1) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 2 + 1 * t + (-1)) * h + ((-1) * t) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `12n242`, exponents `[1, 0, 1, 1, 1, 0, 2, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z0 t - 1) ^ 1 * z1 t ^ 1 * z2 t ^ 2 = z0 t ^ 1 * (1 - z1 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2]
  linear_combination ((-1) * t ^ 5 + 1 * t ^ 4 + (-3) * t ^ 3 + 3 * t ^ 2 + (-2) * t) * ht

/-- **Edge 1** of `12n242`, exponents `[0, 1, 1, 1, 0, 1, 0, 2, 1]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * z1 t ^ 1 * (z1 t - 1) ^ 1 * (z2 t - 1) ^ 1 = (1 - z0 t) ^ 1 * z0 t ^ 1 * z1 t ^ 1 * (1 - z2 t) ^ 2 * z2 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2]
  linear_combination ((-1) * t ^ 7 + 1 * t ^ 6 + (-3) * t ^ 5 + 4 * t ^ 4 + (-5) * t ^ 3 + 5 * t ^ 2 + (-3) * t + 2) * ht

/-- **Edge 2** of `12n242`, exponents `[1, 1, 0, 0, 1, 1, 0, 0, 1]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z1 t - 1) ^ 1 * (z2 t - 1) ^ 1 = (1 - z0 t) ^ 1 * (1 - z1 t) ^ 1 * z1 t ^ 1 * z2 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2]
  linear_combination ((-1) * t ^ 4 + 2 * t ^ 3 + (-5) * t ^ 2 + 4 * t + (-4)) * ht

end K12n242

/-! ### `7_4` — 6 tetrahedra, shape field of degree 3

Minimal polynomial `2*x^3 - 7*x^2 + 10*x - 4`. -/

namespace K74

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 2 * t ^ 3 + (-7) * t ^ 2 + 10 * t + (-4)

/-- Shape `z0` of `7_4`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `7_4`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := 1 * t ^ 2 + (-3 / 2) * t + 1

/-- Shape `z2` of `7_4`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := (1 / 2) * t ^ 2 + (-3 / 4) * t + 1

/-- Shape `z3` of `7_4`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := 2 * t ^ 2 + (-5) * t + 5

/-- Shape `z4` of `7_4`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := 2 * t ^ 2 + (-5) * t + 6

/-- Shape `z5` of `7_4`, as an element of `ℚ(θ)`. -/
noncomputable def z5 (t : ℂ) : ℂ := 1 * t ^ 2 + (-3 / 2) * t + 1

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 2) * t ^ 2 + (-7 / 4) * t + (5 / 2)) * h + ((-1 / 4)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (2 * t ^ 2 + (-5) * t + 5) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 2 + (-7 / 2) * t + 4) * h + ((-1 / 2) * t + (3 / 4)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 2 + (-5 / 2) * t + 3) * h + ((1 / 2) * t + (-1 / 4)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t + 2) * h + ((1 / 4)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (2 * t ^ 2 + (-5) * t + 6) * h + ((1 / 2) * t + (-1 / 4)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t + 1) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 2) * t ^ 2 + (7 / 4) * t + (-3 / 2)) * h + ((-1 / 2) * t + (5 / 4)) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 2) * t ^ 2 + (3 / 4) * t) * h + ((1 / 2) * t + (-1 / 4)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t + (-1)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 2 + (-7 / 2) * t + 4) * h + ((-1 / 2) * t + (3 / 4)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 2 + (-5 / 2) * t + 3) * h + ((1 / 2) * t + (-1 / 4)) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `7_4`, exponents `[1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * z1 t ^ 1 * z2 t ^ 1 * (z4 t - 1) ^ 1 = (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * z4 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z4]
  linear_combination ((1 / 2) * t ^ 4 + (-3 / 2) * t ^ 3 + (21 / 8) * t ^ 2 + (-5 / 4) * t) * ht

/-- **Edge 1** of `7_4`, exponents `[0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z1 t - 1) ^ 1 * (z3 t - 1) ^ 1 * (z5 t - 1) ^ 1 = (1 - z0 t) ^ 1 * z0 t ^ 1 * (1 - z1 t) ^ 1 * z1 t ^ 1 * z3 t ^ 1 * (1 - z4 t) ^ 1 * z5 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z3, z4, z5]
  linear_combination (2 * t ^ 9 + (-14) * t ^ 8 + 45 * t ^ 7 + (-86) * t ^ 6 + (841 / 8) * t ^ 5 + (-653 / 8) * t ^ 4 + (293 / 8) * t ^ 3 + (-57 / 8) * t ^ 2) * ht

/-- **Edge 2** of `7_4`, exponents `[0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * z1 t ^ 1 * z4 t ^ 1 * z5 t ^ 1 = z0 t ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4, z5]
  linear_combination (1 * t ^ 4 + (-3) * t ^ 3 + (17 / 4) * t ^ 2 + (-7 / 2) * t + (3 / 2)) * ht

/-- **Edge 3** of `7_4`, exponents `[0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    (z2 t - 1) ^ 1 * z3 t ^ 1 = (1 - z0 t) ^ 1 * z2 t ^ 1 * (1 - z4 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z2, z3, z4]
  linear_combination ((-1 / 2) * t ^ 2 + (5 / 4) * t + (-5 / 4)) * ht

/-- **Edge 4** of `7_4`, exponents `[1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z1 t - 1) ^ 1 * (z2 t - 1) ^ 1 * z3 t ^ 1 * (z5 t - 1) ^ 1 = z1 t ^ 1 * z2 t ^ 1 * (1 - z3 t) ^ 1 * (1 - z5 t) ^ 1 * z5 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z5]
  linear_combination ((-1 / 2) * t ^ 7 + 3 * t ^ 6 + (-31 / 4) * t ^ 5 + (43 / 4) * t ^ 4 + (-281 / 32) * t ^ 3 + (19 / 4) * t ^ 2 + (-3 / 2) * t) * ht

/-- **Edge 5** of `7_4`, exponents `[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0]`, denominators cleared. -/
theorem edge_5 {t : ℂ} (ht : minpoly t = 0) :
    z2 t ^ 1 * (z3 t - 1) ^ 1 * z4 t ^ 1 * (z4 t - 1) ^ 1 * z5 t ^ 1 = z3 t ^ 1 * z4 t ^ 1 * (1 - z5 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z2, z3, z4, z5]
  linear_combination (2 * t ^ 7 + (-14) * t ^ 6 + 49 * t ^ 5 + (-106) * t ^ 4 + (1237 / 8) * t ^ 3 + (-1221 / 8) * t ^ 2 + (385 / 4) * t + (-30)) * ht

end K74

/-! ### `9_35` — 9 tetrahedra, shape field of degree 3

Minimal polynomial `3*x^3 - 7*x^2 + 7*x - 1`. -/

namespace K935

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 3 * t ^ 3 + (-7) * t ^ 2 + 7 * t + (-1)

/-- Shape `z0` of `9_35`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `9_35`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := (-1) * t ^ 2 + (10 / 3) * t + (-8 / 3)

/-- Shape `z2` of `9_35`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := 1 * t ^ 2 + (-1 / 3) * t + (-1 / 3)

/-- Shape `z3` of `9_35`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := 2 * t ^ 2 + (-11 / 3) * t + (10 / 3)

/-- Shape `z4` of `9_35`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := 2 * t ^ 2 + (-11 / 3) * t + (10 / 3)

/-- Shape `z5` of `9_35`, as an element of `ℚ(θ)`. -/
noncomputable def z5 (t : ℂ) : ℂ := 1 * t ^ 2 + (-1 / 3) * t + (-1 / 3)

/-- Shape `z6` of `9_35`, as an element of `ℚ(θ)`. -/
noncomputable def z6 (t : ℂ) : ℂ := 1 * t

/-- Shape `z7` of `9_35`, as an element of `ℚ(θ)`. -/
noncomputable def z7 (t : ℂ) : ℂ := 2 * t ^ 2 + (-11 / 3) * t + (10 / 3)

/-- Shape `z8` of `9_35`, as an element of `ℚ(θ)`. -/
noncomputable def z8 (t : ℂ) : ℂ := 2 * t ^ 2 + (-11 / 3) * t + (10 / 3)

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (3 * t ^ 2 + (-7) * t + 7) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((3 / 2) * t ^ 2 + (-2) * t + (3 / 2)) * h + ((1 / 2)) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 2 + (4 / 3) * t + (-2 / 3)) * h + ((-1 / 3) * t + (7 / 9)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 2) * t ^ 2 + (-1 / 6) * t + (1 / 3)) * h + ((-1 / 6) * t + (2 / 9)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-2) * t ^ 2 + (11 / 3) * t + (-10 / 3)) * h + ((2 / 3) * t + (1 / 9)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 2) * t ^ 2 + (-2 / 3) * t + (5 / 6)) * h + ((1 / 6) * t + (1 / 9)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 2 + (1 / 3) * t + (1 / 3)) * h + ((2 / 3) * t + (1 / 9)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 2) * t ^ 2 + (5 / 3) * t + (-5 / 6)) * h + ((-1 / 3) * t + (17 / 18)) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 2 + (1 / 3) * t + (1 / 3)) * h + ((2 / 3) * t + (1 / 9)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 2) * t ^ 2 + (5 / 3) * t + (-5 / 6)) * h + ((-1 / 3) * t + (17 / 18)) * ht
  exact absurd this one_ne_zero

theorem z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-2) * t ^ 2 + (11 / 3) * t + (-10 / 3)) * h + ((2 / 3) * t + (1 / 9)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 2) * t ^ 2 + (-2 / 3) * t + (5 / 6)) * h + ((1 / 6) * t + (1 / 9)) * ht
  exact absurd this one_ne_zero

theorem z6_ne_zero {t : ℂ} (ht : minpoly t = 0) : z6 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z6] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (3 * t ^ 2 + (-7) * t + 7) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z6_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z6 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z6] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((3 / 2) * t ^ 2 + (-2) * t + (3 / 2)) * h + ((1 / 2)) * ht
  exact absurd this one_ne_zero

theorem z7_ne_zero {t : ℂ} (ht : minpoly t = 0) : z7 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z7] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 2 + (1 / 3) * t + (1 / 3)) * h + ((2 / 3) * t + (1 / 9)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z7_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z7 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z7] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 2) * t ^ 2 + (5 / 3) * t + (-5 / 6)) * h + ((-1 / 3) * t + (17 / 18)) * ht
  exact absurd this one_ne_zero

theorem z8_ne_zero {t : ℂ} (ht : minpoly t = 0) : z8 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z8] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 2 + (1 / 3) * t + (1 / 3)) * h + ((2 / 3) * t + (1 / 9)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z8_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z8 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z8] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 2) * t ^ 2 + (5 / 3) * t + (-5 / 6)) * h + ((-1 / 3) * t + (17 / 18)) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `9_35`, exponents `[1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * z1 t ^ 1 * z2 t ^ 1 * z4 t ^ 1 * z7 t ^ 1 = 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z4, z7]
  linear_combination ((-4 / 3) * t ^ 6 + (20 / 3) * t ^ 5 + (-115 / 9) * t ^ 4 + (940 / 81) * t ^ 3 + (-238 / 81) * t ^ 2 + (-233 / 81) * t + 1) * ht

/-- **Edge 1** of `9_35`, exponents `[0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * (z3 t - 1) ^ 1 = (1 - z0 t) ^ 1 * z1 t ^ 1 * z3 t ^ 1 * (1 - z5 t) ^ 1 * (1 - z6 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z3, z5, z6]
  linear_combination ((-2 / 3) * t ^ 5 + (31 / 9) * t ^ 4 + (-152 / 27) * t ^ 3 + (38 / 27) * t ^ 2 + (116 / 27) * t + (-89 / 27)) * ht

/-- **Edge 2** of `9_35`, exponents `[0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * z2 t ^ 1 * z5 t ^ 1 * (z6 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * z6 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z5, z6]
  linear_combination ((1 / 3) * t ^ 3 + (-1 / 9) * t ^ 2 + (-7 / 9) * t + (-1 / 9)) * ht

/-- **Edge 3** of `9_35`, exponents `[0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z4 t - 1) ^ 1 * (z5 t - 1) ^ 1 * (z8 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 * z4 t ^ 1 * z5 t ^ 1 * z8 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4, z5, z8]
  linear_combination ((-8 / 3) * t ^ 10 + (172 / 9) * t ^ 9 + (-1574 / 27) * t ^ 8 + (7229 / 81) * t ^ 7 + (-12250 / 243) * t ^ 6 + (-38170 / 729) * t ^ 5 + (84023 / 729) * t ^ 4 + (-680 / 9) * t ^ 3 + (2561 / 729) * t ^ 2 + (14357 / 729) * t + (-196 / 27)) * ht

/-- **Edge 4** of `9_35`, exponents `[1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z2 t - 1) ^ 1 * z3 t ^ 1 * (z7 t - 1) ^ 1 = (1 - z0 t) ^ 1 * (1 - z2 t) ^ 1 * z2 t ^ 1 * z7 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z2, z3, z7]
  linear_combination ((2 / 3) * t ^ 4 + (-13 / 9) * t ^ 3 + (17 / 27) * t ^ 2 + (34 / 27) * t + (-40 / 27)) * ht

/-- **Edge 5** of `9_35`, exponents `[0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_5 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * (z2 t - 1) ^ 1 * (z8 t - 1) ^ 1 = z1 t ^ 1 * z2 t ^ 1 * (1 - z4 t) ^ 1 * (1 - z5 t) ^ 1 * (1 - z6 t) ^ 1 * (1 - z7 t) ^ 1 * z8 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z1, z2, z4, z5, z6, z7, z8]
  linear_combination ((8 / 3) * t ^ 10 + (-196 / 9) * t ^ 9 + (1982 / 27) * t ^ 8 + (-10223 / 81) * t ^ 7 + (23164 / 243) * t ^ 6 + (27124 / 729) * t ^ 5 + (-4009 / 27) * t ^ 4 + (92978 / 729) * t ^ 3 + (-23963 / 729) * t ^ 2 + (-4037 / 243) * t + (7364 / 729)) * ht

/-- **Edge 6** of `9_35`, exponents `[0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]`, denominators cleared. -/
theorem edge_6 {t : ℂ} (ht : minpoly t = 0) :
    z1 t ^ 1 * z3 t ^ 1 * z5 t ^ 1 * z6 t ^ 1 * z8 t ^ 1 = 1 := by
  simp only [minpoly] at ht
  simp only [z1, z3, z5, z6, z8]
  linear_combination ((-4 / 3) * t ^ 6 + (20 / 3) * t ^ 5 + (-115 / 9) * t ^ 4 + (940 / 81) * t ^ 3 + (-238 / 81) * t ^ 2 + (-233 / 81) * t + 1) * ht

/-- **Edge 7** of `9_35`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0]`, denominators cleared. -/
theorem edge_7 {t : ℂ} (ht : minpoly t = 0) :
    (z3 t - 1) ^ 1 * (z4 t - 1) ^ 1 * (z6 t - 1) ^ 1 * z7 t ^ 1 = (1 - z3 t) ^ 1 * z3 t ^ 1 * z4 t ^ 1 * z6 t ^ 1 * (1 - z7 t) ^ 1 * (1 - z8 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z3, z4, z6, z7, z8]
  linear_combination ((32 / 3) * t ^ 8 + (-656 / 9) * t ^ 7 + (2128 / 9) * t ^ 6 + (-37784 / 81) * t ^ 5 + (147818 / 243) * t ^ 4 + (-43349 / 81) * t ^ 3 + (25162 / 81) * t ^ 2 + (-26551 / 243) * t + (490 / 27)) * ht

/-- **Edge 8** of `9_35`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0]`, denominators cleared. -/
theorem edge_8 {t : ℂ} (ht : minpoly t = 0) :
    z4 t ^ 1 * (z5 t - 1) ^ 1 * z6 t ^ 1 * (z7 t - 1) ^ 1 * z8 t ^ 1 = (1 - z4 t) ^ 1 * z5 t ^ 1 * z7 t ^ 1 * (1 - z8 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z4, z5, z6, z7, z8]
  linear_combination ((8 / 3) * t ^ 6 + (-12) * t ^ 5 + (194 / 9) * t ^ 4 + (-1313 / 81) * t ^ 3 + (-206 / 81) * t ^ 2 + (959 / 81) * t + (-490 / 81)) * ht

end K935

/-! ### `v3227` — 7 tetrahedra, shape field of degree 3

Minimal polynomial `x^3 - 3*x^2 - x - 1`. -/

namespace Kv3227

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 3 + (-3) * t ^ 2 + (-1) * t + (-1)

/-- Shape `z0` of `v3227`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `v3227`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := (-1) * t ^ 2 + 3 * t + 1

/-- Shape `z2` of `v3227`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := (-1) * t ^ 2 + 3 * t + 1

/-- Shape `z3` of `v3227`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := (-1 / 2) * t ^ 2 + 1 * t + (1 / 2)

/-- Shape `z4` of `v3227`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := (-1 / 2) * t ^ 2 + 1 * t + (1 / 2)

/-- Shape `z5` of `v3227`, as an element of `ℚ(θ)`. -/
noncomputable def z5 (t : ℂ) : ℂ := (-1 / 2) * t ^ 2 + 1 * t + (1 / 2)

/-- Shape `z6` of `v3227`, as an element of `ℚ(θ)`. -/
noncomputable def z6 (t : ℂ) : ℂ := (-1 / 2) * t ^ 2 + 1 * t + (1 / 2)

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 2 + (-3) * t + (-1)) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 4) * t ^ 2 + (1 / 2) * t + (3 / 4)) * h + ((-1 / 4)) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 4) * t ^ 2 + 1 * t + (1 / 4)) * h + ((1 / 4) * t + (-1)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 4) * t ^ 2 + 1 * t + (1 / 4)) * h + ((1 / 4) * t + (-1)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 2) * t ^ 2 + (-2) * t + (1 / 2)) * h + ((1 / 4) * t + (-3 / 4)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 2) * t ^ 2 + (3 / 2) * t + 1) * h + ((1 / 4) * t + (-1 / 2)) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 2) * t ^ 2 + (-2) * t + (1 / 2)) * h + ((1 / 4) * t + (-3 / 4)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 2) * t ^ 2 + (3 / 2) * t + 1) * h + ((1 / 4) * t + (-1 / 2)) * ht
  exact absurd this one_ne_zero

theorem z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 2) * t ^ 2 + (-2) * t + (1 / 2)) * h + ((1 / 4) * t + (-3 / 4)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 2) * t ^ 2 + (3 / 2) * t + 1) * h + ((1 / 4) * t + (-1 / 2)) * ht
  exact absurd this one_ne_zero

theorem z6_ne_zero {t : ℂ} (ht : minpoly t = 0) : z6 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z6] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 2) * t ^ 2 + (-2) * t + (1 / 2)) * h + ((1 / 4) * t + (-3 / 4)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z6_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z6 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z6] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 2) * t ^ 2 + (3 / 2) * t + 1) * h + ((1 / 4) * t + (-1 / 2)) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `v3227`, exponents `[2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 2 * z1 t ^ 1 * z2 t ^ 1 = 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2]
  linear_combination (1 * t ^ 3 + (-3) * t ^ 2 + (-1) * t + 1) * ht

/-- **Edge 1** of `v3227`, exponents `[0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 2 * (z2 t - 1) ^ 2 = (1 - z0 t) ^ 2 * z1 t ^ 2 * z2 t ^ 2 * (1 - z3 t) ^ 1 * (1 - z4 t) ^ 1 * (1 - z5 t) ^ 1 * (1 - z6 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4, z5, z6]
  linear_combination ((-1 / 16) * t ^ 15 + (19 / 16) * t ^ 14 + (-159 / 16) * t ^ 13 + (773 / 16) * t ^ 12 + (-605 / 4) * t ^ 11 + (1271 / 4) * t ^ 10 + (-3577 / 8) * t ^ 9 + (3145 / 8) * t ^ 8 + (-1205 / 8) * t ^ 7 + (-683 / 8) * t ^ 6 + (559 / 4) * t ^ 5 + (-237 / 4) * t ^ 4 + (19 / 16) * t ^ 3 + (-29 / 16) * t ^ 2 + (1 / 16) * t + (1 / 16)) * ht

/-- **Edge 2** of `v3227`, exponents `[0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z4 t - 1) ^ 1 * (z6 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * z4 t ^ 1 * z6 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z4, z6]
  linear_combination ((-1 / 4) * t ^ 6 + (7 / 4) * t ^ 5 + (-15 / 4) * t ^ 4 + (5 / 4) * t ^ 3 + (13 / 4) * t ^ 2 + (-3 / 2) * t + (1 / 4)) * ht

/-- **Edge 3** of `v3227`, exponents `[0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z3 t - 1) ^ 1 * (z5 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * z3 t ^ 1 * z5 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z5]
  linear_combination ((-1 / 4) * t ^ 6 + (7 / 4) * t ^ 5 + (-15 / 4) * t ^ 4 + (5 / 4) * t ^ 3 + (13 / 4) * t ^ 2 + (-3 / 2) * t + (1 / 4)) * ht

/-- **Edge 4** of `v3227`, exponents `[0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    z1 t ^ 1 * z2 t ^ 1 * z3 t ^ 1 * z4 t ^ 1 * z5 t ^ 1 * z6 t ^ 1 = 1 := by
  simp only [minpoly] at ht
  simp only [z1, z2, z3, z4, z5, z6]
  linear_combination ((1 / 16) * t ^ 9 + (-11 / 16) * t ^ 8 + (43 / 16) * t ^ 7 + (-59 / 16) * t ^ 6 + (-15 / 8) * t ^ 5 + (57 / 8) * t ^ 4 + (15 / 16) * t ^ 3 + (-91 / 16) * t ^ 2 + (-29 / 16) * t + (15 / 16)) * ht

/-- **Edge 5** of `v3227`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_5 {t : ℂ} (ht : minpoly t = 0) :
    z3 t ^ 1 * (z4 t - 1) ^ 1 * z5 t ^ 1 * (z6 t - 1) ^ 1 = (1 - z3 t) ^ 1 * z4 t ^ 1 * (1 - z5 t) ^ 1 * z6 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z3, z4, z5, z6]
  linear_combination (0) * ht

/-- **Edge 6** of `v3227`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0]`, denominators cleared. -/
theorem edge_6 {t : ℂ} (ht : minpoly t = 0) :
    (z3 t - 1) ^ 1 * z4 t ^ 1 * (z5 t - 1) ^ 1 * z6 t ^ 1 = z3 t ^ 1 * (1 - z4 t) ^ 1 * z5 t ^ 1 * (1 - z6 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z3, z4, z5, z6]
  linear_combination (0) * ht

end Kv3227

/-! ### `7_7` — 8 tetrahedra, shape field of degree 4

Minimal polynomial `x^4 - 2*x^3 + 3*x^2 - 3*x + 2`. -/

namespace K77

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 4 + (-2) * t ^ 3 + 3 * t ^ 2 + (-3) * t + 2

/-- Shape `z0` of `7_7`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `7_7`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := (-1) * t ^ 2 + 1 * t + (-1)

/-- Shape `z2` of `7_7`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := 1 * t ^ 3 + (-1) * t ^ 2 + 2 * t + (-1)

/-- Shape `z3` of `7_7`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := (-1) * t ^ 3 + 1 * t ^ 2 + (-1) * t + 2

/-- Shape `z4` of `7_7`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := (-1) * t ^ 3 + 1 * t ^ 2 + (-1) * t + 2

/-- Shape `z5` of `7_7`, as an element of `ℚ(θ)`. -/
noncomputable def z5 (t : ℂ) : ℂ := 1 * t ^ 3 + (-1) * t ^ 2 + 2 * t + (-1)

/-- Shape `z6` of `7_7`, as an element of `ℚ(θ)`. -/
noncomputable def z6 (t : ℂ) : ℂ := (-1 / 4) * t ^ 3 + (1 / 4) * t + (1 / 4)

/-- Shape `z7` of `7_7`, as an element of `ℚ(θ)`. -/
noncomputable def z7 (t : ℂ) : ℂ := 1 * t

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 2) * t ^ 3 + 1 * t ^ 2 + (-3 / 2) * t + (3 / 2)) * h + ((1 / 2)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 3 + (-1) * t ^ 2 + 2 * t + (-1)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 3 + (-1) * t ^ 2 + 1 * t + (-1)) * h + (1 * t) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 4) * t ^ 3 + (1 / 4) * t + (1 / 4)) * h + ((1 / 4) * t + (1 / 4)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t + 1) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 2) * t ^ 3 + (-1) * t ^ 2 + (3 / 2) * t + (-1 / 2)) * h + ((1 / 2) * t ^ 2 + (-1 / 2) * t + 1) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 4) * t ^ 3 + (-1 / 4) * t + (3 / 4)) * h + ((1 / 4) * t ^ 2 + (1 / 4) * t + (-1 / 4)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 2 + 1 * t + (-1)) * h + (1 * t) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 4) * t ^ 3 + (-1 / 4) * t + (3 / 4)) * h + ((1 / 4) * t ^ 2 + (1 / 4) * t + (-1 / 4)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 2 + 1 * t + (-1)) * h + (1 * t) * ht
  exact absurd this one_ne_zero

theorem z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t + 1) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 2) * t ^ 3 + (-1) * t ^ 2 + (3 / 2) * t + (-1 / 2)) * h + ((1 / 2) * t ^ 2 + (-1 / 2) * t + 1) * ht
  exact absurd this one_ne_zero

theorem z6_ne_zero {t : ℂ} (ht : minpoly t = 0) : z6 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z6] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 2 + (-1) * t + 2) * h + ((1 / 4) * t + (1 / 4)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z6_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z6 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z6] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 3 + 1 * t ^ 2 + (-1) * t + 2) * h + ((1 / 4) * t ^ 2 + (1 / 4) * t + (-1 / 4)) * ht
  exact absurd this one_ne_zero

theorem z7_ne_zero {t : ℂ} (ht : minpoly t = 0) : z7 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z7] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 2) * t ^ 3 + 1 * t ^ 2 + (-3 / 2) * t + (3 / 2)) * h + ((1 / 2)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z7_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z7 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z7] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 3 + (-1) * t ^ 2 + 2 * t + (-1)) * h + (1) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `7_7`, exponents `[1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z0 t - 1) ^ 1 * z1 t ^ 1 * z2 t ^ 1 * z4 t ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z4]
  linear_combination (1 * t ^ 6 + (-2) * t ^ 5 + 3 * t ^ 4 + (-4) * t ^ 3 + 2 * t ^ 2 + (-2) * t) * ht

/-- **Edge 1** of `7_7`, exponents `[0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z1 t - 1) ^ 1 * (z3 t - 1) ^ 1 = (1 - z0 t) ^ 1 * z0 t ^ 1 * z1 t ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 * z3 t ^ 1 * (1 - z6 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z6]
  linear_combination ((-1 / 4) * t ^ 12 + (3 / 4) * t ^ 11 + (-5 / 4) * t ^ 10 + (5 / 4) * t ^ 9 + (1 / 2) * t ^ 8 + (-4) * t ^ 7 + (35 / 4) * t ^ 6 + (-47 / 4) * t ^ 5 + (47 / 4) * t ^ 4 + (-39 / 4) * t ^ 3 + (11 / 2) * t ^ 2 + (-5 / 2) * t + 1) * ht

/-- **Edge 2** of `7_7`, exponents `[0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z2 t - 1) ^ 1 * (z5 t - 1) ^ 1 = (1 - z0 t) ^ 1 * (1 - z2 t) ^ 1 * z2 t ^ 1 * (1 - z5 t) ^ 1 * z5 t ^ 1 * (1 - z7 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z2, z5, z7]
  linear_combination ((-1) * t ^ 10 + 4 * t ^ 9 + (-12) * t ^ 8 + 27 * t ^ 7 + (-45) * t ^ 6 + 63 * t ^ 5 + (-68) * t ^ 4 + 56 * t ^ 3 + (-36) * t ^ 2 + 12 * t) * ht

/-- **Edge 3** of `7_7`, exponents `[1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z2 t - 1) ^ 1 * z3 t ^ 1 * (z4 t - 1) ^ 1 = (1 - z1 t) ^ 1 * z2 t ^ 1 * z4 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination (1 * t ^ 6 + (-1) * t ^ 5 + 3 * t ^ 4 + (-5) * t ^ 3 + 3 * t ^ 2 + (-5) * t + 2) * ht

/-- **Edge 4** of `7_7`, exponents `[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * (z4 t - 1) ^ 1 * (z7 t - 1) ^ 1 = z1 t ^ 1 * (1 - z4 t) ^ 1 * z4 t ^ 1 * (1 - z5 t) ^ 1 * (1 - z6 t) ^ 1 * (1 - z7 t) ^ 1 * z7 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z1, z4, z5, z6, z7]
  linear_combination ((-1 / 4) * t ^ 12 + (3 / 4) * t ^ 11 + (-5 / 4) * t ^ 10 + (5 / 4) * t ^ 9 + (1 / 2) * t ^ 8 + (-4) * t ^ 7 + (35 / 4) * t ^ 6 + (-47 / 4) * t ^ 5 + (47 / 4) * t ^ 4 + (-39 / 4) * t ^ 3 + (11 / 2) * t ^ 2 + (-5 / 2) * t + 1) * ht

/-- **Edge 5** of `7_7`, exponents `[0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]`, denominators cleared. -/
theorem edge_5 {t : ℂ} (ht : minpoly t = 0) :
    z1 t ^ 1 * z2 t ^ 1 * z5 t ^ 1 * (z6 t - 1) ^ 1 = (1 - z3 t) ^ 1 * (1 - z4 t) ^ 1 * z6 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z1, z2, z3, z4, z5, z6]
  linear_combination ((1 / 4) * t ^ 7 + (-1 / 4) * t ^ 6 + (3 / 4) * t ^ 5 + (3 / 4) * t ^ 4 + (-3 / 2) * t ^ 3 + 2 * t ^ 2 + (-3 / 2) * t + (1 / 4)) * ht

/-- **Edge 6** of `7_7`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1]`, denominators cleared. -/
theorem edge_6 {t : ℂ} (ht : minpoly t = 0) :
    z3 t ^ 1 * z5 t ^ 1 * z6 t ^ 1 * (z6 t - 1) ^ 1 * z7 t ^ 1 * (z7 t - 1) ^ 1 = z6 t ^ 1 * z7 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z3, z5, z6, z7]
  linear_combination ((-1 / 16) * t ^ 10 + (1 / 16) * t ^ 9 + (1 / 16) * t ^ 8 + (-1 / 8) * t ^ 7 + (1 / 4) * t ^ 6 + (-1 / 8) * t ^ 5 + (1 / 8) * t ^ 4 + (-1 / 16) * t ^ 3 + (-1 / 16) * t ^ 2 + (-5 / 16) * t) * ht

/-- **Edge 7** of `7_7`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0]`, denominators cleared. -/
theorem edge_7 {t : ℂ} (ht : minpoly t = 0) :
    (z3 t - 1) ^ 1 * z4 t ^ 1 * (z5 t - 1) ^ 1 * z6 t ^ 1 * z7 t ^ 1 = z3 t ^ 1 * z5 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z3, z4, z5, z6, z7]
  linear_combination ((-1 / 4) * t ^ 9 + (1 / 4) * t ^ 8 + (-1 / 4) * t ^ 7 + 1 * t ^ 6 + (1 / 4) * t ^ 5 + (1 / 4) * t ^ 4 + (-5 / 4) * t ^ 3 + (-1 / 2) * t ^ 2 + (-3 / 2) * t + 1) * ht

end K77

/-! ### `8_21` — 7 tetrahedra, shape field of degree 4

Minimal polynomial `4*x^4 - 10*x^3 + 13*x^2 - 8*x + 2`. -/

namespace K821

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 4 * t ^ 4 + (-10) * t ^ 3 + 13 * t ^ 2 + (-8) * t + 2

/-- Shape `z0` of `8_21`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `8_21`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := 4 * t ^ 3 + (-6) * t ^ 2 + 7 * t + (-1)

/-- Shape `z2` of `8_21`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := 2 * t ^ 3 + (-3) * t ^ 2 + (7 / 2) * t + (-1 / 2)

/-- Shape `z3` of `8_21`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := 4 * t ^ 3 + (-6) * t ^ 2 + 7 * t + (-1)

/-- Shape `z4` of `8_21`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := (-4) * t ^ 3 + 8 * t ^ 2 + (-8) * t + (7 / 2)

/-- Shape `z5` of `8_21`, as an element of `ℚ(θ)`. -/
noncomputable def z5 (t : ℂ) : ℂ := 1 * t

/-- Shape `z6` of `8_21`, as an element of `ℚ(θ)`. -/
noncomputable def z6 (t : ℂ) : ℂ := (-4) * t ^ 3 + 8 * t ^ 2 + (-8) * t + 3

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-2) * t ^ 3 + 5 * t ^ 2 + (-13 / 2) * t + 4) * h + ((1 / 2)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (4 * t ^ 3 + (-6) * t ^ 2 + 7 * t + (-1)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t + 1) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (2 * t ^ 3 + (-5) * t ^ 2 + (13 / 2) * t + (-3)) * h + (2 * t ^ 2 + (-3) * t + (7 / 2)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-2) * t + 2) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (8 * t ^ 3 + (-16) * t ^ 2 + 18 * t + (-6)) * h + (4 * t ^ 2 + (-4) * t + 5) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t + 1) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (2 * t ^ 3 + (-5) * t ^ 2 + (13 / 2) * t + (-3)) * h + (2 * t ^ 2 + (-3) * t + (7 / 2)) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (4 * t ^ 3 + (-8) * t ^ 2 + 8 * t + (-2)) * h + (4 * t ^ 2 + (-6) * t + 4) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-8) * t ^ 3 + 16 * t ^ 2 + (-16) * t + 6) * h + (8 * t ^ 2 + (-12) * t + 8) * ht
  exact absurd this one_ne_zero

theorem z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-2) * t ^ 3 + 5 * t ^ 2 + (-13 / 2) * t + 4) * h + ((1 / 2)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (4 * t ^ 3 + (-6) * t ^ 2 + 7 * t + (-1)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z6_ne_zero {t : ℂ} (ht : minpoly t = 0) : z6 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z6] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (8 * t ^ 3 + (-16) * t ^ 2 + 16 * t + (-5)) * h + (8 * t ^ 2 + (-12) * t + 8) * ht
  exact absurd this one_ne_zero

theorem one_sub_z6_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z6 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z6] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-4) * t ^ 3 + 8 * t ^ 2 + (-8) * t + (7 / 2)) * h + (4 * t ^ 2 + (-6) * t + 4) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `8_21`, exponents `[1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * z1 t ^ 1 * z2 t ^ 1 * z4 t ^ 1 * z5 t ^ 1 * (z6 t - 1) ^ 1 = z6 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z4, z5, z6]
  linear_combination (32 * t ^ 10 + (-144) * t ^ 9 + 360 * t ^ 8 + (-556) * t ^ 7 + 582 * t ^ 6 + (-395) * t ^ 5 + 164 * t ^ 4 + (-30) * t ^ 3 + (-1 / 2) * t ^ 2 + (-2) * t + (-3 / 2)) * ht

/-- **Edge 1** of `8_21`, exponents `[0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * z2 t ^ 1 * (z3 t - 1) ^ 1 = (1 - z0 t) ^ 1 * z1 t ^ 1 * z3 t ^ 1 * (1 - z4 t) ^ 1 * (1 - z6 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4, z6]
  linear_combination (64 * t ^ 9 + (-352) * t ^ 8 + 1008 * t ^ 7 + (-1816) * t ^ 6 + 2228 * t ^ 5 + (-1862) * t ^ 4 + 1032 * t ^ 3 + (-336) * t ^ 2 + (111 / 2) * t + (-7 / 2)) * ht

/-- **Edge 2** of `8_21`, exponents `[0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z5 t - 1) ^ 1 * (z6 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z3 t) ^ 1 * (1 - z4 t) ^ 1 * z5 t ^ 1 * z6 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z3, z4, z5, z6]
  linear_combination (64 * t ^ 10 + (-288) * t ^ 9 + 720 * t ^ 8 + (-1144) * t ^ 7 + 1260 * t ^ 6 + (-950) * t ^ 5 + 474 * t ^ 4 + (-135) * t ^ 3 + (27 / 2) * t ^ 2 + (-2) * t + 1) * ht

/-- **Edge 3** of `8_21`, exponents `[1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z0 t - 1) ^ 1 * z3 t ^ 1 * z4 t ^ 1 * z5 t ^ 1 = z0 t ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z2, z3, z4, z5]
  linear_combination ((-4) * t ^ 5 + 8 * t ^ 4 + (-10) * t ^ 3 + (9 / 2) * t ^ 2 + (-3 / 2) * t) * ht

/-- **Edge 4** of `8_21`, exponents `[0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    z1 t ^ 1 * (z2 t - 1) ^ 1 * (z4 t - 1) ^ 1 * z6 t ^ 1 = (1 - z0 t) ^ 1 * z2 t ^ 1 * z4 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z4, z6]
  linear_combination (32 * t ^ 8 + (-144) * t ^ 7 + 360 * t ^ 6 + (-572) * t ^ 5 + 630 * t ^ 4 + (-477) * t ^ 3 + 239 * t ^ 2 + (-137 / 2) * t + (13 / 2)) * ht

/-- **Edge 5** of `8_21`, exponents `[0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0]`, denominators cleared. -/
theorem edge_5 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * (z3 t - 1) ^ 1 * (z5 t - 1) ^ 1 = (1 - z1 t) ^ 1 * z1 t ^ 1 * (1 - z2 t) ^ 1 * z3 t ^ 1 * (1 - z5 t) ^ 1 * z5 t ^ 1 * (1 - z6 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z1, z2, z3, z5, z6]
  linear_combination (128 * t ^ 13 + (-832) * t ^ 12 + 2944 * t ^ 11 + (-6928) * t ^ 10 + 11872 * t ^ 9 + (-15316) * t ^ 8 + 15054 * t ^ 7 + (-11180) * t ^ 6 + 6082 * t ^ 5 + (-2287) * t ^ 4 + 522 * t ^ 3 + (-68) * t ^ 2 + 11 * t + (-2)) * ht

/-- **Edge 6** of `8_21`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]`, denominators cleared. -/
theorem edge_6 {t : ℂ} (ht : minpoly t = 0) :
    (z2 t - 1) ^ 1 * z3 t ^ 1 * (z4 t - 1) ^ 1 * z6 t ^ 1 = z2 t ^ 1 * z4 t ^ 1 * (1 - z5 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z2, z3, z4, z5, z6]
  linear_combination (32 * t ^ 8 + (-144) * t ^ 7 + 360 * t ^ 6 + (-572) * t ^ 5 + 630 * t ^ 4 + (-477) * t ^ 3 + 239 * t ^ 2 + (-137 / 2) * t + (13 / 2)) * ht

end K821

/-! ### `m371` — 5 tetrahedra, shape field of degree 4

Minimal polynomial `x^4 - 3*x^3 + 10*x^2 - 12*x + 8`. -/

namespace Km371

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 4 + (-3) * t ^ 3 + 10 * t ^ 2 + (-12) * t + 8

/-- Shape `z0` of `m371`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `m371`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := (1 / 16) * t ^ 3 + (-1 / 16) * t ^ 2 + (1 / 2) * t + (1 / 4)

/-- Shape `z2` of `m371`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := (1 / 4) * t ^ 3 + (-1 / 2) * t ^ 2 + (7 / 4) * t + (-1 / 2)

/-- Shape `z3` of `m371`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := (1 / 4) * t ^ 3 + (-1 / 2) * t ^ 2 + (7 / 4) * t + (-1 / 2)

/-- Shape `z4` of `m371`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := 1 * t

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 8) * t ^ 3 + (3 / 8) * t ^ 2 + (-5 / 4) * t + (3 / 2)) * h + ((1 / 8)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 4) * t ^ 3 + (-1 / 2) * t ^ 2 + 2 * t + (-1)) * h + ((1 / 4)) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t + 2) * h + ((1 / 16)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 4) * t ^ 3 + (-1 / 2) * t ^ 2 + 2 * t) * h + ((1 / 64) * t ^ 2 + (1 / 8)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 4) * t ^ 3 + (1 / 4) * t ^ 2 + (-1) * t + 1) * h + ((1 / 16) * t ^ 2 + (3 / 16)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 4) * t ^ 3 + (-3 / 4) * t ^ 2 + 2 * t + (-1)) * h + ((1 / 16) * t ^ 2 + (-1 / 8) * t + (5 / 16)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 4) * t ^ 3 + (1 / 4) * t ^ 2 + (-1) * t + 1) * h + ((1 / 16) * t ^ 2 + (3 / 16)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 4) * t ^ 3 + (-3 / 4) * t ^ 2 + 2 * t + (-1)) * h + ((1 / 16) * t ^ 2 + (-1 / 8) * t + (5 / 16)) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 8) * t ^ 3 + (3 / 8) * t ^ 2 + (-5 / 4) * t + (3 / 2)) * h + ((1 / 8)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 4) * t ^ 3 + (-1 / 2) * t ^ 2 + 2 * t + (-1)) * h + ((1 / 4)) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `m371`, exponents `[2, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 2 * z1 t ^ 2 * z2 t ^ 1 * z3 t ^ 1 * z4 t ^ 2 = 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination ((1 / 4096) * t ^ 12 + (-3 / 4096) * t ^ 11 + (3 / 512) * t ^ 10 + (-15 / 2048) * t ^ 9 + (141 / 4096) * t ^ 8 + (45 / 4096) * t ^ 7 + (113 / 2048) * t ^ 6 + (129 / 1024) * t ^ 5 + (53 / 512) * t ^ 4 + (-1 / 8) * t ^ 2 + (-3 / 16) * t + (-1 / 8)) * ht

/-- **Edge 1** of `m371`, exponents `[0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 2 = (1 - z0 t) ^ 1 * z1 t ^ 2 * (1 - z4 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z4]
  linear_combination ((-1 / 256) * t ^ 4 + (1 / 256) * t ^ 3 + (-1 / 32) * t ^ 2 + (-1 / 64) * t + (1 / 16)) * ht

/-- **Edge 2** of `m371`, exponents `[0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * z2 t ^ 1 * (z4 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z3 t) ^ 2 * z4 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination ((1 / 256) * t ^ 7 + (-1 / 128) * t ^ 6 + (7 / 128) * t ^ 5 + (-7 / 64) * t ^ 4 + (49 / 256) * t ^ 3 + (-41 / 128) * t ^ 2 + (1 / 4) * t + (-1 / 16)) * ht

/-- **Edge 3** of `m371`, exponents `[0, 0, 1, 0, 1, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * z3 t ^ 1 * (z4 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 2 * z4 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination ((1 / 256) * t ^ 7 + (-1 / 128) * t ^ 6 + (7 / 128) * t ^ 5 + (-7 / 64) * t ^ 4 + (49 / 256) * t ^ 3 + (-41 / 128) * t ^ 2 + (1 / 4) * t + (-1 / 16)) * ht

/-- **Edge 4** of `m371`, exponents `[0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 1, 0]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    (z2 t - 1) ^ 2 * (z3 t - 1) ^ 2 = (1 - z0 t) ^ 1 * z2 t ^ 2 * z3 t ^ 2 * (1 - z4 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z2, z3, z4]
  linear_combination ((-1 / 256) * t ^ 10 + (7 / 256) * t ^ 9 + (-37 / 256) * t ^ 8 + (119 / 256) * t ^ 7 + (-291 / 256) * t ^ 6 + (473 / 256) * t ^ 5 + (-487 / 256) * t ^ 4 + (141 / 256) * t ^ 3 + (25 / 16) * t ^ 2 + (-121 / 64) * t + (5 / 8)) * ht

end Km371

/-! ### `6_2` — 5 tetrahedra, shape field of degree 5

Minimal polynomial `x^5 - 3*x^4 + 5*x^3 - 5*x^2 + 4*x - 1`. -/

namespace K62

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 5 + (-3) * t ^ 4 + 5 * t ^ 3 + (-5) * t ^ 2 + 4 * t + (-1)

/-- Shape `z0` of `6_2`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `6_2`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := 1 * t ^ 2 + (-1) * t + 1

/-- Shape `z2` of `6_2`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := (-1) * t ^ 4 + 3 * t ^ 3 + (-5) * t ^ 2 + 5 * t + (-3)

/-- Shape `z3` of `6_2`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := 1 * t ^ 4 + (-3) * t ^ 3 + 5 * t ^ 2 + (-4) * t + 3

/-- Shape `z4` of `6_2`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := 1 * t ^ 4 + (-3) * t ^ 3 + 5 * t ^ 2 + (-4) * t + 3

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 4 + (-3) * t ^ 3 + 5 * t ^ 2 + (-5) * t + 4) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 4 + (-2) * t ^ 3 + 3 * t ^ 2 + (-2) * t + 2) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 4 + (-3) * t ^ 3 + 4 * t ^ 2 + (-3) * t + 2) * h + ((-1) * t + 1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (2 * t ^ 4 + (-5) * t ^ 3 + 8 * t ^ 2 + (-7) * t + 6) * h + (2 * t + (-1)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 4 + 2 * t ^ 3 + (-3) * t ^ 2 + 2 * t + (-1)) * h + ((-1) * t ^ 3 + 2 * t ^ 2 + (-3) * t + 2) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 3 + 2 * t ^ 2 + (-2) * t + 1) * h + (1 * t ^ 2 + (-2) * t + 2) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 4 + 3 * t ^ 3 + (-4) * t ^ 2 + 4 * t + (-2)) * h + ((-1) * t ^ 3 + 3 * t ^ 2 + (-4) * t + 3) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 3 + 2 * t ^ 2 + (-2) * t + 1) * h + (1 * t ^ 2 + (-2) * t + 2) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 4 + 3 * t ^ 3 + (-4) * t ^ 2 + 4 * t + (-2)) * h + ((-1) * t ^ 3 + 3 * t ^ 2 + (-4) * t + 3) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `6_2`, exponents `[1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * z1 t ^ 1 * (z1 t - 1) ^ 1 * z2 t ^ 1 * z3 t ^ 1 * z4 t ^ 1 = (1 - z0 t) ^ 1 * z1 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination ((-1) * t ^ 12 + 8 * t ^ 11 + (-33) * t ^ 10 + 89 * t ^ 9 + (-174) * t ^ 8 + 257 * t ^ 7 + (-292) * t ^ 6 + 254 * t ^ 5 + (-166) * t ^ 4 + 77 * t ^ 3 + (-22) * t ^ 2 + 2 * t + 1) * ht

/-- **Edge 1** of `6_2`, exponents `[1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z0 t - 1) ^ 1 * z3 t ^ 1 * (z4 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 * z4 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination ((-1) * t ^ 10 + 7 * t ^ 9 + (-25) * t ^ 8 + 57 * t ^ 7 + (-92) * t ^ 6 + 109 * t ^ 5 + (-96) * t ^ 4 + 61 * t ^ 3 + (-26) * t ^ 2 + 6 * t) * ht

/-- **Edge 2** of `6_2`, exponents `[0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z2 t - 1) ^ 1 * (z3 t - 1) ^ 1 * z4 t ^ 1 = z0 t ^ 1 * (1 - z2 t) ^ 1 * z2 t ^ 1 * z3 t ^ 1 * (1 - z4 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z2, z3, z4]
  linear_combination ((-1) * t ^ 12 + 9 * t ^ 11 + (-42) * t ^ 10 + 130 * t ^ 9 + (-297) * t ^ 8 + 526 * t ^ 7 + (-742) * t ^ 6 + 840 * t ^ 5 + (-762) * t ^ 4 + 543 * t ^ 3 + (-294) * t ^ 2 + 110 * t + (-24)) * ht

/-- **Edge 3** of `6_2`, exponents `[0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    z1 t ^ 1 * (z2 t - 1) ^ 1 * (z3 t - 1) ^ 1 = (1 - z0 t) ^ 1 * z2 t ^ 1 * z3 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3]
  linear_combination ((-1) * t ^ 5 + 3 * t ^ 4 + (-5) * t ^ 3 + 4 * t ^ 2 + (-2) * t + (-1)) * ht

/-- **Edge 4** of `6_2`, exponents `[0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * z2 t ^ 1 * (z4 t - 1) ^ 1 = (1 - z1 t) ^ 1 * z1 t ^ 1 * (1 - z3 t) ^ 1 * (1 - z4 t) ^ 1 * z4 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z1, z2, z3, z4]
  linear_combination (1 * t ^ 11 + (-8) * t ^ 10 + 33 * t ^ 9 + (-88) * t ^ 8 + 167 * t ^ 7 + (-234) * t ^ 6 + 245 * t ^ 5 + (-189) * t ^ 4 + 103 * t ^ 3 + (-36) * t ^ 2 + 6 * t) * ht

end K62

/-! ### `8_20` — 5 tetrahedra, shape field of degree 5

Minimal polynomial `x^5 - x^3 - 3*x^2 + 4`. -/

namespace K820

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 5 + (-1) * t ^ 3 + (-3) * t ^ 2 + 4

/-- Shape `z0` of `8_20`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `8_20`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := (-3 / 8) * t ^ 4 + (-1 / 4) * t ^ 3 + (-1 / 8) * t ^ 2 + (11 / 8) * t + (5 / 4)

/-- Shape `z2` of `8_20`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := (3 / 8) * t ^ 4 + (1 / 4) * t ^ 3 + (1 / 8) * t ^ 2 + (-3 / 8) * t + (-1 / 4)

/-- Shape `z3` of `8_20`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := (3 / 8) * t ^ 4 + (1 / 4) * t ^ 3 + (1 / 8) * t ^ 2 + (-3 / 8) * t + (-1 / 4)

/-- Shape `z4` of `8_20`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := (-3 / 8) * t ^ 4 + (-1 / 4) * t ^ 3 + (-1 / 8) * t ^ 2 + (11 / 8) * t + (5 / 4)

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 4) * t ^ 4 + (1 / 4) * t ^ 2 + (3 / 4) * t) * h + ((1 / 4)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 4 + 1 * t ^ 3 + (-3) * t + (-3)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 4) * t ^ 4 + (1 / 2) * t ^ 3 + (1 / 4) * t ^ 2 + (1 / 4) * t + (-1 / 2)) * h + ((-3 / 32) * t ^ 3 + (1 / 8) * t ^ 2 + (3 / 32) * t + (13 / 32)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 4) * t ^ 4 + (-1 / 2) * t ^ 3 + (-3 / 4) * t ^ 2 + (1 / 4) * t + (3 / 2)) * h + ((3 / 32) * t ^ 3 + (1 / 4) * t ^ 2 + (17 / 32) * t + (11 / 32)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 4) * t ^ 4 + (-1 / 2) * t ^ 3 + (1 / 4) * t ^ 2 + (1 / 4) * t + (3 / 2)) * h + ((3 / 32) * t ^ 3 + (1 / 4) * t ^ 2 + (5 / 32) * t + (11 / 32)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((3 / 4) * t ^ 4 + (1 / 2) * t ^ 3 + (1 / 4) * t ^ 2 + (-7 / 4) * t + (-1 / 2)) * h + ((9 / 32) * t ^ 3 + (3 / 8) * t ^ 2 + (19 / 32) * t + (13 / 32)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 4) * t ^ 4 + (-1 / 2) * t ^ 3 + (1 / 4) * t ^ 2 + (1 / 4) * t + (3 / 2)) * h + ((3 / 32) * t ^ 3 + (1 / 4) * t ^ 2 + (5 / 32) * t + (11 / 32)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((3 / 4) * t ^ 4 + (1 / 2) * t ^ 3 + (1 / 4) * t ^ 2 + (-7 / 4) * t + (-1 / 2)) * h + ((9 / 32) * t ^ 3 + (3 / 8) * t ^ 2 + (19 / 32) * t + (13 / 32)) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 4) * t ^ 4 + (1 / 2) * t ^ 3 + (1 / 4) * t ^ 2 + (1 / 4) * t + (-1 / 2)) * h + ((-3 / 32) * t ^ 3 + (1 / 8) * t ^ 2 + (3 / 32) * t + (13 / 32)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 4) * t ^ 4 + (-1 / 2) * t ^ 3 + (-3 / 4) * t ^ 2 + (1 / 4) * t + (3 / 2)) * h + ((3 / 32) * t ^ 3 + (1 / 4) * t ^ 2 + (17 / 32) * t + (11 / 32)) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `8_20`, exponents `[1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * z1 t ^ 1 * z2 t ^ 1 * (z4 t - 1) ^ 1 = z4 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z4]
  linear_combination ((27 / 512) * t ^ 8 + (27 / 256) * t ^ 7 + (45 / 256) * t ^ 6 + (-23 / 256) * t ^ 5 + (-153 / 512) * t ^ 4 + (-37 / 64) * t ^ 3 + (-185 / 512) * t ^ 2 + (-93 / 256) * t + (-5 / 16)) * ht

/-- **Edge 1** of `8_20`, exponents `[0, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * (z2 t - 1) ^ 1 * (z3 t - 1) ^ 1 * (z4 t - 1) ^ 1 = (1 - z0 t) ^ 2 * z1 t ^ 1 * z2 t ^ 1 * z3 t ^ 1 * z4 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination ((-81 / 4096) * t ^ 13 + (-27 / 2048) * t ^ 12 + (27 / 4096) * t ^ 11 + (795 / 4096) * t ^ 10 + (923 / 4096) * t ^ 9 + (33 / 512) * t ^ 8 + (-1019 / 2048) * t ^ 7 + (-3243 / 4096) * t ^ 6 + (-2375 / 4096) * t ^ 5 + (1161 / 4096) * t ^ 4 + (1277 / 2048) * t ^ 3 + (907 / 1024) * t ^ 2 + (105 / 512) * t) * ht

/-- **Edge 2** of `8_20`, exponents `[0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * z1 t ^ 1 * (z2 t - 1) ^ 1 * (z3 t - 1) ^ 1 * z4 t ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * z2 t ^ 1 * (1 - z3 t) ^ 1 * z3 t ^ 1 * (1 - z4 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination ((-729 / 262144) * t ^ 20 + (-729 / 65536) * t ^ 19 + (-7047 / 262144) * t ^ 18 + (-6021 / 262144) * t ^ 17 + (4347 / 131072) * t ^ 16 + (10197 / 65536) * t ^ 15 + (8029 / 32768) * t ^ 14 + (17133 / 131072) * t ^ 13 + (-50759 / 262144) * t ^ 12 + (-73509 / 131072) * t ^ 11 + (-136745 / 262144) * t ^ 10 + (-57129 / 262144) * t ^ 9 + (29637 / 262144) * t ^ 8 + (26629 / 131072) * t ^ 7 + (28233 / 262144) * t ^ 6 + (188015 / 262144) * t ^ 5 + (15971 / 16384) * t ^ 4 + (23093 / 32768) * t ^ 3 + (-2065 / 16384) * t ^ 2 + (-18025 / 16384) * t + (-625 / 1024)) * ht

/-- **Edge 3** of `8_20`, exponents `[0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * z2 t ^ 1 * z3 t ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 * (1 - z4 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination ((-81 / 4096) * t ^ 12 + (-27 / 512) * t ^ 11 + (-405 / 4096) * t ^ 10 + (-15 / 4096) * t ^ 9 + (893 / 4096) * t ^ 8 + (1025 / 2048) * t ^ 7 + (1031 / 2048) * t ^ 6 + (-271 / 4096) * t ^ 5 + (-1573 / 4096) * t ^ 4 + (-3457 / 4096) * t ^ 3 + (-137 / 512) * t ^ 2 + (-57 / 1024) * t + (-1 / 64)) * ht

/-- **Edge 4** of `8_20`, exponents `[1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z1 t - 1) ^ 1 * z3 t ^ 1 * z4 t ^ 1 = z1 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z3, z4]
  linear_combination ((27 / 512) * t ^ 8 + (27 / 256) * t ^ 7 + (45 / 256) * t ^ 6 + (-23 / 256) * t ^ 5 + (-153 / 512) * t ^ 4 + (-37 / 64) * t ^ 3 + (-185 / 512) * t ^ 2 + (-93 / 256) * t + (-5 / 16)) * ht

end K820

/-! ### `9_42` — 5 tetrahedra, shape field of degree 5

Minimal polynomial `4*x^5 - 8*x^4 + 7*x^3 - 6*x^2 + 3*x - 1`. -/

namespace K942

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 4 * t ^ 5 + (-8) * t ^ 4 + 7 * t ^ 3 + (-6) * t ^ 2 + 3 * t + (-1)

/-- Shape `z0` of `9_42`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `9_42`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := (-4) * t ^ 4 + 8 * t ^ 3 + (-7) * t ^ 2 + 6 * t + (-1)

/-- Shape `z2` of `9_42`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := 4 * t ^ 4 + (-4) * t ^ 3 + 1 * t ^ 2 + (-2) * t

/-- Shape `z3` of `9_42`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := 4 * t ^ 4 + (-8) * t ^ 3 + 5 * t ^ 2 + (-3) * t + 2

/-- Shape `z4` of `9_42`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := 1 * t

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (4 * t ^ 4 + (-8) * t ^ 3 + 7 * t ^ 2 + (-6) * t + 3) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-4) * t ^ 4 + 4 * t ^ 3 + (-3) * t ^ 2 + 3 * t) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (2 * t ^ 4 + (-3) * t ^ 3 + 2 * t ^ 2 + (-2) * t + 1) * h + (2 * t ^ 3 + (-3) * t ^ 2 + 2 * t + (-2)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-4) * t ^ 4 + 4 * t ^ 3 + (-3) * t ^ 2 + 3 * t + (-1)) * h + (4 * t ^ 3 + (-4) * t ^ 2 + 3 * t + (-3)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-4) * t ^ 4 + 8 * t ^ 3 + (-5) * t ^ 2 + 3 * t + (-1)) * h + (4 * t ^ 3 + (-4) * t ^ 2 + (-1) * t + (-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-2) * t ^ 2 + 1 * t) * h + ((-2) * t + (-1)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (2 * t ^ 2 + (-1) * t + 1) * h + ((-2) * t + 1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (4 * t ^ 4 + (-4) * t ^ 3 + 1 * t ^ 2 + (-2) * t) * h + (4 * t ^ 3 + (-4) * t ^ 2 + (-1) * t + (-1)) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (4 * t ^ 4 + (-8) * t ^ 3 + 7 * t ^ 2 + (-6) * t + 3) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-4) * t ^ 4 + 4 * t ^ 3 + (-3) * t ^ 2 + 3 * t) * h + ((-1)) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `9_42`, exponents `[2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 2 * z1 t ^ 1 * z2 t ^ 1 * z3 t ^ 1 = 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3]
  linear_combination ((-16) * t ^ 9 + 48 * t ^ 8 + (-56) * t ^ 7 + 48 * t ^ 6 + (-33) * t ^ 5 + 9 * t ^ 4 + (-6) * t ^ 3 + 3 * t ^ 2 + 3 * t + 1) * ht

/-- **Edge 1** of `9_42`, exponents `[0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z1 t - 1) ^ 1 * z2 t ^ 1 * (z3 t - 1) ^ 1 * (z4 t - 1) ^ 1 = (1 - z0 t) ^ 1 * z0 t ^ 1 * z1 t ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 * z3 t ^ 1 * (1 - z4 t) ^ 1 * z4 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination (64 * t ^ 15 + (-448) * t ^ 14 + 1392 * t ^ 13 + (-2624) * t ^ 12 + 3484 * t ^ 11 + (-3500) * t ^ 10 + 2665 * t ^ 9 + (-1474) * t ^ 8 + 510 * t ^ 7 + 22 * t ^ 6 + (-186) * t ^ 5 + 146 * t ^ 4 + (-71) * t ^ 3 + 24 * t ^ 2 + (-4) * t) * ht

/-- **Edge 2** of `9_42`, exponents `[0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z4 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 2 * z4 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z4]
  linear_combination ((-4) * t ^ 5 + 8 * t ^ 4 + (-7) * t ^ 3 + 6 * t ^ 2 + (-1) * t + (-1)) * ht

/-- **Edge 3** of `9_42`, exponents `[0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * (z2 t - 1) ^ 1 * z3 t ^ 1 * (z3 t - 1) ^ 1 = (1 - z0 t) ^ 1 * z1 t ^ 1 * (1 - z2 t) ^ 1 * z2 t ^ 1 * z3 t ^ 1 * (1 - z4 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination ((-64) * t ^ 13 + 384 * t ^ 12 + (-1072) * t ^ 11 + 1936 * t ^ 10 + (-2572) * t ^ 9 + 2624 * t ^ 8 + (-2109) * t ^ 7 + 1349 * t ^ 6 + (-655) * t ^ 5 + 219 * t ^ 4 + (-32) * t ^ 3 + (-18) * t ^ 2 + 14 * t + (-4)) * ht

/-- **Edge 4** of `9_42`, exponents `[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 2, 0, 0]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    z1 t ^ 1 * (z2 t - 1) ^ 1 * z4 t ^ 2 = z2 t ^ 1 * (1 - z3 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z1, z2, z3, z4]
  linear_combination ((-4) * t ^ 5 + 4 * t ^ 4 + 3 * t ^ 3 + (-2) * t ^ 2 + 2 * t) * ht

end K942

/-! ### `o9_00000` — 9 tetrahedra, shape field of degree 5

Minimal polynomial `256*x^5 - 640*x^4 + 560*x^3 - 200*x^2 + 24*x + 1`. -/

namespace Ko900000

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 256 * t ^ 5 + (-640) * t ^ 4 + 560 * t ^ 3 + (-200) * t ^ 2 + 24 * t + 1

/-- Shape `z0` of `o9_00000`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `o9_00000`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := 256 * t ^ 4 + (-640) * t ^ 3 + 560 * t ^ 2 + (-200) * t + 26

/-- Shape `z2` of `o9_00000`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := 256 * t ^ 4 + (-640) * t ^ 3 + 560 * t ^ 2 + (-200) * t + 26

/-- Shape `z3` of `o9_00000`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := (-192) * t ^ 4 + 416 * t ^ 3 + (-276) * t ^ 2 + 50 * t + 2

/-- Shape `z4` of `o9_00000`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := (-192) * t ^ 4 + 416 * t ^ 3 + (-276) * t ^ 2 + 50 * t + 2

/-- Shape `z5` of `o9_00000`, as an element of `ℚ(θ)`. -/
noncomputable def z5 (t : ℂ) : ℂ := 32 * t ^ 4 + (-72) * t ^ 3 + 60 * t ^ 2 + (-22) * t + (7 / 2)

/-- Shape `z6` of `o9_00000`, as an element of `ℚ(θ)`. -/
noncomputable def z6 (t : ℂ) : ℂ := 32 * t ^ 4 + (-72) * t ^ 3 + 60 * t ^ 2 + (-22) * t + (7 / 2)

/-- Shape `z7` of `o9_00000`, as an element of `ℚ(θ)`. -/
noncomputable def z7 (t : ℂ) : ℂ := 64 * t ^ 4 + (-112) * t ^ 3 + 60 * t ^ 2 + (-9) * t

/-- Shape `z8` of `o9_00000`, as an element of `ℚ(θ)`. -/
noncomputable def z8 (t : ℂ) : ℂ := 64 * t ^ 4 + (-112) * t ^ 3 + 60 * t ^ 2 + (-9) * t

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-256) * t ^ 4 + 640 * t ^ 3 + (-560) * t ^ 2 + 200 * t + (-24)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (256 * t ^ 4 + (-384) * t ^ 3 + 176 * t ^ 2 + (-24) * t) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-64) * t ^ 4 + 128 * t ^ 3 + (-76) * t ^ 2 + 12 * t + (1 / 2)) * h + (64 * t ^ 3 + (-128) * t ^ 2 + 76 * t + (-12)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (256 * t ^ 4 + (-384) * t ^ 3 + 176 * t ^ 2 + (-24) * t + (-1)) * h + (256 * t ^ 3 + (-384) * t ^ 2 + 176 * t + (-24)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-64) * t ^ 4 + 128 * t ^ 3 + (-76) * t ^ 2 + 12 * t + (1 / 2)) * h + (64 * t ^ 3 + (-128) * t ^ 2 + 76 * t + (-12)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (256 * t ^ 4 + (-384) * t ^ 3 + 176 * t ^ 2 + (-24) * t + (-1)) * h + (256 * t ^ 3 + (-384) * t ^ 2 + 176 * t + (-24)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (64 * t ^ 4 + (-176) * t ^ 3 + 168 * t ^ 2 + (-64) * t + 9) * h + (48 * t ^ 3 + (-116) * t ^ 2 + 86 * t + (-17)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (256 * t ^ 4 + (-384) * t ^ 3 + 176 * t ^ 2 + (-28) * t) * h + ((-192) * t ^ 3 + 224 * t ^ 2 + (-52) * t + 1) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (64 * t ^ 4 + (-176) * t ^ 3 + 168 * t ^ 2 + (-64) * t + 9) * h + (48 * t ^ 3 + (-116) * t ^ 2 + 86 * t + (-17)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (256 * t ^ 4 + (-384) * t ^ 3 + 176 * t ^ 2 + (-28) * t) * h + ((-192) * t ^ 3 + 224 * t ^ 2 + (-52) * t + 1) * ht
  exact absurd this one_ne_zero

theorem z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-8) * t ^ 2 + 8 * t + (1 / 2)) * h + (1 * t + (-3 / 4)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (256 * t ^ 4 + (-384) * t ^ 3 + 160 * t ^ 2 + (-16) * t + (-1)) * h + (32 * t ^ 3 + (-40) * t ^ 2 + 18 * t + (-3 / 2)) * ht
  exact absurd this one_ne_zero

theorem z6_ne_zero {t : ℂ} (ht : minpoly t = 0) : z6 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z6] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-8) * t ^ 2 + 8 * t + (1 / 2)) * h + (1 * t + (-3 / 4)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z6_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z6 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z6] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (256 * t ^ 4 + (-384) * t ^ 3 + 160 * t ^ 2 + (-16) * t + (-1)) * h + (32 * t ^ 3 + (-40) * t ^ 2 + 18 * t + (-3 / 2)) * ht
  exact absurd this one_ne_zero

theorem z7_ne_zero {t : ℂ} (ht : minpoly t = 0) : z7 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z7] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-64) * t ^ 4 + 112 * t ^ 3 + (-56) * t ^ 2 + 4 * t + 3) * h + (16 * t ^ 3 + (-16) * t ^ 2 + 3 * t + 1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z7_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z7 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z7] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (256 * t ^ 4 + (-448) * t ^ 3 + 240 * t ^ 2 + (-40) * t) * h + (64 * t ^ 3 + (-64) * t ^ 2 + 16 * t + 1) * ht
  exact absurd this one_ne_zero

theorem z8_ne_zero {t : ℂ} (ht : minpoly t = 0) : z8 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z8] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-64) * t ^ 4 + 112 * t ^ 3 + (-56) * t ^ 2 + 4 * t + 3) * h + (16 * t ^ 3 + (-16) * t ^ 2 + 3 * t + 1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z8_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z8 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z8] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (256 * t ^ 4 + (-448) * t ^ 3 + 240 * t ^ 2 + (-40) * t) * h + (64 * t ^ 3 + (-64) * t ^ 2 + 16 * t + 1) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `o9_00000`, exponents `[2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 1, 0, 2, 1, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 2 * z1 t ^ 2 * z2 t ^ 2 * z3 t ^ 2 * z4 t ^ 2 * z5 t ^ 2 * z6 t ^ 2 * z7 t ^ 2 * z8 t ^ 2 = (1 - z7 t) ^ 1 * (1 - z8 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4, z5, z6, z7, z8]
  linear_combination (401092572728463209067316248576 * t ^ 61 + (-12901811089432233224998672662528) * t ^ 60 + 202911061324276502203784176336896 * t ^ 59 + (-2079534541665442042067567253651456) * t ^ 58 + 15616933235571778275806244398694400 * t ^ 57 + (-91627929622372748658739267137175552) * t ^ 56 + 437309297117756739945588767473008640 * t ^ 55 + (-1745430538849753175126850075552120832) * t ^ 54 + 5944372846554531921380684065123860480 * t ^ 53 + (-17539274573043096196189323998942724096) * t ^ 52 + 45370977816615415500919542557981016064 * t ^ 51 + (-103878140543269360734866129202578456576) * t ^ 50 + 212127432802406688629852295926982377472 * t ^ 49 + (-388824785620086980280879291493836128256) * t ^ 48 + 643119380457623626169693505938949931008 * t ^ 47 + (-964131333318115119657349015202143666176) * t ^ 46 + 1314958848200018586210974617992517648384 * t ^ 45 + (-1636789265234434739072590808494316191744) * t ^ 44 + 1864398866843546817373901938080283099136 * t ^ 43 + (-1947728588198939633735740789409175306240) * t ^ 42 + 1869734595301465140474579106148697243648 * t ^ 41 + (-1651847171064800982746457282377834037248) * t ^ 40 + 1344764971998769183503188618978395160576 * t ^ 39 + (-1009810647707897176352557695796170981376) * t ^ 38 + 699955913509991928709900595417006997504 * t ^ 37 + (-448078052001542441008315388921049513984) * t ^ 36 + 264973143930412045046201667896372887552 * t ^ 35 + (-144752823973555108397506149517392609280) * t ^ 34 + 73036300813801054291401481513609461760 * t ^ 33 + (-34020531196233105118822573977448218624) * t ^ 32 + 14619315832551331043048215752801779712 * t ^ 31 + (-5789891635086020462067633991247200256) * t ^ 30 + 2110640929198155624483764296424095744 * t ^ 29 + (-707059178191154393685572434131943424) * t ^ 28 + 217232497345237410154931366465110016 * t ^ 27 + (-61060043741059403001806991420030976) * t ^ 26 + 15655126611181497982514881707900928 * t ^ 25 + (-3647909913858937690966533655756800) * t ^ 24 + 769105161418407291638892425379840 * t ^ 23 + (-145911216357122323075382423060480) * t ^ 22 + 24736875352423544753733465014272 * t ^ 21 + (-3714350906471417813485713555456) * t ^ 20 + 488145889674453398871993942016 * t ^ 19 + (-55225236280266515137906032640) * t ^ 18 + 5245449724672754270279716864 * t ^ 17 + (-400876564678892711680346112) * t ^ 16 + 22535040679254708278304768 * t ^ 15 + (-685282515257530064994048) * t ^ 14 + (-18502813638182017306880) * t ^ 13 + 3491419593581729220096 * t ^ 12 + (-174894366642297085440) * t ^ 11 + 1540642420173225488 * t ^ 10 + 248476441064532672 * t ^ 9 + (-9892123066528928) * t ^ 8 + (-47349401538880) * t ^ 7 + 7198427337552 * t ^ 6 + 9591536 * t ^ 5 + (-308952) * t ^ 4 + 9936 * t ^ 3 + (-305) * t ^ 2 + 6 * t + (-1)) * ht

/-- **Edge 1** of `o9_00000`, exponents `[0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 2 = (1 - z0 t) ^ 1 * z1 t ^ 2 * (1 - z3 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z3]
  linear_combination (49152 * t ^ 8 + (-278528) * t ^ 7 + 673792 * t ^ 6 + (-905216) * t ^ 5 + 735680 * t ^ 4 + (-369024) * t ^ 3 + 111344 * t ^ 2 + (-18500) * t + 1301) * ht

/-- **Edge 2** of `o9_00000`, exponents `[0, 0, 2, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 2 = z0 t ^ 2 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2]
  linear_combination ((-256) * t ^ 5 + 640 * t ^ 4 + (-560) * t ^ 3 + 200 * t ^ 2 + (-26) * t + 1) * ht

/-- **Edge 3** of `o9_00000`, exponents `[0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    (z2 t - 1) ^ 2 = (1 - z0 t) ^ 1 * z2 t ^ 2 * (1 - z4 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z2, z4]
  linear_combination (49152 * t ^ 8 + (-278528) * t ^ 7 + 673792 * t ^ 6 + (-905216) * t ^ 5 + 735680 * t ^ 4 + (-369024) * t ^ 3 + 111344 * t ^ 2 + (-18500) * t + 1301) * ht

/-- **Edge 4** of `o9_00000`, exponents `[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    (z3 t - 1) ^ 2 = (1 - z1 t) ^ 1 * z3 t ^ 2 * (1 - z5 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z1, z3, z5]
  linear_combination ((-1179648) * t ^ 11 + 7766016 * t ^ 10 + (-22642688) * t ^ 9 + 38449152 * t ^ 8 + (-42013696) * t ^ 7 + 30746112 * t ^ 6 + (-15154592) * t ^ 5 + 4904968 * t ^ 4 + (-972224) * t ^ 3 + 99074 * t ^ 2 + (-2224) * t + (-249)) * ht

/-- **Edge 5** of `o9_00000`, exponents `[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_5 {t : ℂ} (ht : minpoly t = 0) :
    (z4 t - 1) ^ 2 = (1 - z2 t) ^ 1 * z4 t ^ 2 * (1 - z6 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z2, z4, z6]
  linear_combination ((-1179648) * t ^ 11 + 7766016 * t ^ 10 + (-22642688) * t ^ 9 + 38449152 * t ^ 8 + (-42013696) * t ^ 7 + 30746112 * t ^ 6 + (-15154592) * t ^ 5 + 4904968 * t ^ 4 + (-972224) * t ^ 3 + 99074 * t ^ 2 + (-2224) * t + (-249)) * ht

/-- **Edge 6** of `o9_00000`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_6 {t : ℂ} (ht : minpoly t = 0) :
    (z5 t - 1) ^ 2 = (1 - z3 t) ^ 1 * z5 t ^ 2 * (1 - z7 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z3, z5, z7]
  linear_combination (49152 * t ^ 11 + (-290816) * t ^ 10 + 768000 * t ^ 9 + (-1191424) * t ^ 8 + 1202368 * t ^ 7 + (-825072) * t ^ 6 + 389728 * t ^ 5 + (-124556) * t ^ 4 + 25247 * t ^ 3 + (-5311 / 2) * t ^ 2 + (59 / 4) * t + (37 / 2)) * ht

/-- **Edge 7** of `o9_00000`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0]`, denominators cleared. -/
theorem edge_7 {t : ℂ} (ht : minpoly t = 0) :
    (z6 t - 1) ^ 2 = (1 - z4 t) ^ 1 * z6 t ^ 2 * (1 - z8 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z4, z6, z8]
  linear_combination (49152 * t ^ 11 + (-290816) * t ^ 10 + 768000 * t ^ 9 + (-1191424) * t ^ 8 + 1202368 * t ^ 7 + (-825072) * t ^ 6 + 389728 * t ^ 5 + (-124556) * t ^ 4 + 25247 * t ^ 3 + (-5311 / 2) * t ^ 2 + (59 / 4) * t + (37 / 2)) * ht

/-- **Edge 8** of `o9_00000`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 2]`, denominators cleared. -/
theorem edge_8 {t : ℂ} (ht : minpoly t = 0) :
    (z7 t - 1) ^ 2 * (z8 t - 1) ^ 2 = (1 - z5 t) ^ 1 * (1 - z6 t) ^ 1 * z7 t ^ 2 * z8 t ^ 2 := by
  simp only [minpoly] at ht
  simp only [z5, z6, z7, z8]
  linear_combination ((-67108864) * t ^ 19 + 603979776 * t ^ 18 + (-2533359616) * t ^ 17 + 6570377216 * t ^ 16 + (-11785207808) * t ^ 15 + 15488385024 * t ^ 14 + (-15410921472) * t ^ 13 + 11827281920 * t ^ 12 + (-7065775104) * t ^ 11 + 3292184576 * t ^ 10 + (-1190912256) * t ^ 9 + 330733984 * t ^ 8 + (-69195100) * t ^ 7 + 10606926 * t ^ 6 + (-1152136) * t ^ 5 + (351307 / 4) * t ^ 4 + (-5068) * t ^ 3 + 158 * t ^ 2 + 12 * t + 1) * ht

end Ko900000

/-! ### `6_3` — 6 tetrahedra, shape field of degree 6

Minimal polynomial `x^6 + 2*x^5 - x^4 - 3*x^3 + 4*x^2 - 3*x + 1`. -/

namespace K63

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 6 + 2 * t ^ 5 + (-1) * t ^ 4 + (-3) * t ^ 3 + 4 * t ^ 2 + (-3) * t + 1

/-- Shape `z0` of `6_3`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `6_3`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := (-5 / 3) * t ^ 5 + (-14 / 3) * t ^ 4 + (-5 / 3) * t ^ 3 + (14 / 3) * t ^ 2 + (-7 / 3) * t + (7 / 3)

/-- Shape `z2` of `6_3`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := (4 / 3) * t ^ 5 + (10 / 3) * t ^ 4 + (1 / 3) * t ^ 3 + (-10 / 3) * t ^ 2 + (14 / 3) * t + (-5 / 3)

/-- Shape `z3` of `6_3`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := (-5 / 3) * t ^ 5 + (-14 / 3) * t ^ 4 + (-5 / 3) * t ^ 3 + (14 / 3) * t ^ 2 + (-7 / 3) * t + (7 / 3)

/-- Shape `z4` of `6_3`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := (4 / 3) * t ^ 5 + (10 / 3) * t ^ 4 + (1 / 3) * t ^ 3 + (-10 / 3) * t ^ 2 + (14 / 3) * t + (-5 / 3)

/-- Shape `z5` of `6_3`, as an element of `ℚ(θ)`. -/
noncomputable def z5 (t : ℂ) : ℂ := 1 * t

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 5 + (-2) * t ^ 4 + 1 * t ^ 3 + 3 * t ^ 2 + (-4) * t + 3) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 5 + 3 * t ^ 4 + 2 * t ^ 3 + (-1) * t ^ 2 + 3 * t) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 3) * t ^ 5 + (4 / 3) * t ^ 4 + (4 / 3) * t ^ 3 + (-1 / 3) * t ^ 2 + (-1 / 3) * t + (1 / 3)) * h + ((5 / 9) * t ^ 4 + (8 / 3) * t ^ 3 + (38 / 9) * t ^ 2 + (20 / 9) * t + (2 / 9)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-8 / 3) * t ^ 5 + (-23 / 3) * t ^ 4 + (-11 / 3) * t ^ 3 + (17 / 3) * t ^ 2 + (-16 / 3) * t + (10 / 3)) * h + ((40 / 9) * t ^ 4 + (49 / 3) * t ^ 3 + (163 / 9) * t ^ 2 + (13 / 9) * t + (49 / 9)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-4 / 3) * t ^ 5 + (-10 / 3) * t ^ 4 + (-1 / 3) * t ^ 3 + (10 / 3) * t ^ 2 + (-11 / 3) * t + (8 / 3)) * h + ((16 / 9) * t ^ 4 + (16 / 3) * t ^ 3 + (28 / 9) * t ^ 2 + (-20 / 9) * t + (49 / 9)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((11 / 3) * t ^ 5 + (29 / 3) * t ^ 4 + (8 / 3) * t ^ 3 + (-26 / 3) * t ^ 2 + (28 / 3) * t + (-16 / 3)) * h + ((44 / 9) * t ^ 4 + (46 / 3) * t ^ 3 + (101 / 9) * t ^ 2 + (-37 / 9) * t + (137 / 9)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 3) * t ^ 5 + (4 / 3) * t ^ 4 + (4 / 3) * t ^ 3 + (-1 / 3) * t ^ 2 + (-1 / 3) * t + (1 / 3)) * h + ((5 / 9) * t ^ 4 + (8 / 3) * t ^ 3 + (38 / 9) * t ^ 2 + (20 / 9) * t + (2 / 9)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-8 / 3) * t ^ 5 + (-23 / 3) * t ^ 4 + (-11 / 3) * t ^ 3 + (17 / 3) * t ^ 2 + (-16 / 3) * t + (10 / 3)) * h + ((40 / 9) * t ^ 4 + (49 / 3) * t ^ 3 + (163 / 9) * t ^ 2 + (13 / 9) * t + (49 / 9)) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-4 / 3) * t ^ 5 + (-10 / 3) * t ^ 4 + (-1 / 3) * t ^ 3 + (10 / 3) * t ^ 2 + (-11 / 3) * t + (8 / 3)) * h + ((16 / 9) * t ^ 4 + (16 / 3) * t ^ 3 + (28 / 9) * t ^ 2 + (-20 / 9) * t + (49 / 9)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((11 / 3) * t ^ 5 + (29 / 3) * t ^ 4 + (8 / 3) * t ^ 3 + (-26 / 3) * t ^ 2 + (28 / 3) * t + (-16 / 3)) * h + ((44 / 9) * t ^ 4 + (46 / 3) * t ^ 3 + (101 / 9) * t ^ 2 + (-37 / 9) * t + (137 / 9)) * ht
  exact absurd this one_ne_zero

theorem z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 5 + (-2) * t ^ 4 + 1 * t ^ 3 + 3 * t ^ 2 + (-4) * t + 3) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 5 + 3 * t ^ 4 + 2 * t ^ 3 + (-1) * t ^ 2 + 3 * t) * h + (1) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `6_3`, exponents `[1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * z1 t ^ 1 * z2 t ^ 1 * z3 t ^ 1 * z5 t ^ 1 = 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z5]
  linear_combination ((100 / 27) * t ^ 11 + (610 / 27) * t ^ 10 + (1289 / 27) * t ^ 9 + (682 / 27) * t ^ 8 + (-637 / 27) * t ^ 7 + (32 / 27) * t ^ 6 + (506 / 27) * t ^ 5 + (-1000 / 27) * t ^ 4 + (31 / 3) * t ^ 3 + (-380 / 27) * t ^ 2 + (-3) * t + (-1)) * ht

/-- **Edge 1** of `6_3`, exponents `[0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 1, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 2 * (z3 t - 1) ^ 2 = (1 - z0 t) ^ 1 * (1 - z1 t) ^ 1 * z1 t ^ 2 * (1 - z3 t) ^ 1 * z3 t ^ 2 * (1 - z5 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z3, z5]
  linear_combination ((-15625 / 729) * t ^ 26 + (-200000 / 729) * t ^ 25 + (-1037500 / 729) * t ^ 24 + (-2481875 / 729) * t ^ 23 + (-1169125 / 729) * t ^ 22 + (2436010 / 243) * t ^ 21 + (13668844 / 729) * t ^ 20 + (-2389801 / 729) * t ^ 19 + (-24555469 / 729) * t ^ 18 + (-2148737 / 243) * t ^ 17 + (20918195 / 729) * t ^ 16 + (-1219706 / 243) * t ^ 15 + (-10898389 / 729) * t ^ 14 + (8192651 / 243) * t ^ 13 + (-5513552 / 729) * t ^ 12 + (-2438966 / 81) * t ^ 11 + (25045844 / 729) * t ^ 10 + (-9982271 / 729) * t ^ 9 + (-13093930 / 729) * t ^ 8 + (26216924 / 729) * t ^ 7 + (-8445736 / 243) * t ^ 6 + (5876108 / 243) * t ^ 5 + (-9127895 / 729) * t ^ 4 + (136429 / 27) * t ^ 3 + (-378787 / 243) * t ^ 2 + (240488 / 729) * t + (-36112 / 729)) * ht

/-- **Edge 2** of `6_3`, exponents `[0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z5 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * (1 - z4 t) ^ 1 * z5 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z4, z5]
  linear_combination ((-80 / 27) * t ^ 11 + (-464 / 27) * t ^ 10 + (-892 / 27) * t ^ 9 + (-308 / 27) * t ^ 8 + (395 / 27) * t ^ 7 + (-604 / 27) * t ^ 6 + (-490 / 27) * t ^ 5 + (1163 / 27) * t ^ 4 + (-67 / 3) * t ^ 3 + (256 / 27) * t ^ 2 + 1 * t + 1) * ht

/-- **Edge 3** of `6_3`, exponents `[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z5 t - 1) ^ 1 = z0 t ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 * (1 - z4 t) ^ 1 * z5 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z2, z3, z4, z5]
  linear_combination ((-80 / 27) * t ^ 11 + (-464 / 27) * t ^ 10 + (-892 / 27) * t ^ 9 + (-308 / 27) * t ^ 8 + (395 / 27) * t ^ 7 + (-604 / 27) * t ^ 6 + (-490 / 27) * t ^ 5 + (1163 / 27) * t ^ 4 + (-67 / 3) * t ^ 3 + (256 / 27) * t ^ 2 + 1 * t + 1) * ht

/-- **Edge 4** of `6_3`, exponents `[0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 1, 0, 2, 0, 1, 0]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    z2 t ^ 1 * (z2 t - 1) ^ 2 * z4 t ^ 1 * (z4 t - 1) ^ 2 = (1 - z0 t) ^ 1 * z2 t ^ 2 * z4 t ^ 2 * (1 - z5 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z2, z4, z5]
  linear_combination ((4096 / 729) * t ^ 24 + (53248 / 729) * t ^ 23 + (287744 / 729) * t ^ 22 + (785408 / 729) * t ^ 21 + (322048 / 243) * t ^ 20 + (29440 / 729) * t ^ 19 + (-424640 / 729) * t ^ 18 + (1914944 / 729) * t ^ 17 + (2072032 / 729) * t ^ 16 + (-422192 / 81) * t ^ 15 + (-601348 / 243) * t ^ 14 + (2607196 / 243) * t ^ 13 + (-2594939 / 729) * t ^ 12 + (-10635622 / 729) * t ^ 11 + (11976737 / 729) * t ^ 10 + (3110009 / 729) * t ^ 9 + (-1934936 / 81) * t ^ 8 + (1513301 / 81) * t ^ 7 + (3399334 / 729) * t ^ 6 + (-5487898 / 243) * t ^ 5 + (17197787 / 729) * t ^ 4 + (-10417379 / 729) * t ^ 3 + (4014776 / 729) * t ^ 2 + (-308555 / 243) * t + (96775 / 729)) * ht

/-- **Edge 5** of `6_3`, exponents `[1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]`, denominators cleared. -/
theorem edge_5 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * z1 t ^ 1 * z3 t ^ 1 * z4 t ^ 1 * z5 t ^ 1 = 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z3, z4, z5]
  linear_combination ((100 / 27) * t ^ 11 + (610 / 27) * t ^ 10 + (1289 / 27) * t ^ 9 + (682 / 27) * t ^ 8 + (-637 / 27) * t ^ 7 + (32 / 27) * t ^ 6 + (506 / 27) * t ^ 5 + (-1000 / 27) * t ^ 4 + (31 / 3) * t ^ 3 + (-380 / 27) * t ^ 2 + (-3) * t + (-1)) * ht

end K63

/-! ### `7_3` — 5 tetrahedra, shape field of degree 6

Minimal polynomial `3*x^6 - 7*x^5 + 8*x^4 + x^3 - 9*x^2 + 6*x - 1`. -/

namespace K73

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 3 * t ^ 6 + (-7) * t ^ 5 + 8 * t ^ 4 + 1 * t ^ 3 + (-9) * t ^ 2 + 6 * t + (-1)

/-- Shape `z0` of `7_3`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `7_3`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := (39 / 23) * t ^ 5 + (-94 / 23) * t ^ 4 + (90 / 23) * t ^ 3 + (45 / 23) * t ^ 2 + (-147 / 23) * t + (84 / 23)

/-- Shape `z2` of `7_3`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := (-12 / 23) * t ^ 5 + (13 / 23) * t ^ 4 + (-33 / 23) * t ^ 3 + (-5 / 23) * t ^ 2 + (1 / 23) * t + (-17 / 23)

/-- Shape `z3` of `7_3`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := (39 / 23) * t ^ 5 + (-94 / 23) * t ^ 4 + (90 / 23) * t ^ 3 + (45 / 23) * t ^ 2 + (-147 / 23) * t + (84 / 23)

/-- Shape `z4` of `7_3`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := (-15 / 23) * t ^ 5 + (-1 / 23) * t ^ 4 + (-1 / 23) * t ^ 3 + (-35 / 23) * t ^ 2 + (-16 / 23) * t + (19 / 23)

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (3 * t ^ 5 + (-7) * t ^ 4 + 8 * t ^ 3 + 1 * t ^ 2 + (-9) * t + 6) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (3 * t ^ 5 + (-4) * t ^ 4 + 4 * t ^ 3 + 5 * t ^ 2 + (-4) * t + 2) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((15 / 23) * t ^ 5 + (1 / 23) * t ^ 4 + (1 / 23) * t ^ 3 + (35 / 23) * t ^ 2 + (16 / 23) * t + (4 / 23)) * h + ((-195 / 529) * t ^ 4 + (2 / 529) * t ^ 3 + (93 / 529) * t ^ 2 + (-402 / 529) * t + (-193 / 529)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-129 / 23) * t ^ 5 + (226 / 23) * t ^ 4 + (-211 / 23) * t ^ 3 + (-163 / 23) * t ^ 2 + (304 / 23) * t + (-85 / 23)) * h + ((-1677 / 529) * t ^ 4 + (3067 / 529) * t ^ 3 + (-2066 / 529) * t ^ 2 + (-3103 / 529) * t + (4656 / 529)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((3 / 23) * t ^ 5 + (14 / 23) * t ^ 4 + (-32 / 23) * t ^ 3 + (30 / 23) * t ^ 2 + (17 / 23) * t + (-36 / 23)) * h + ((12 / 529) * t ^ 4 + (71 / 529) * t ^ 3 + (-22 / 529) * t ^ 2 + (173 / 529) * t + (83 / 529)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-3 / 23) * t ^ 5 + (-14 / 23) * t ^ 4 + (32 / 23) * t ^ 3 + (-30 / 23) * t ^ 2 + (6 / 23) * t + (13 / 23)) * h + ((12 / 529) * t ^ 4 + (71 / 529) * t ^ 3 + (-22 / 529) * t ^ 2 + (173 / 529) * t + (-9 / 529)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((15 / 23) * t ^ 5 + (1 / 23) * t ^ 4 + (1 / 23) * t ^ 3 + (35 / 23) * t ^ 2 + (16 / 23) * t + (4 / 23)) * h + ((-195 / 529) * t ^ 4 + (2 / 529) * t ^ 3 + (93 / 529) * t ^ 2 + (-402 / 529) * t + (-193 / 529)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-129 / 23) * t ^ 5 + (226 / 23) * t ^ 4 + (-211 / 23) * t ^ 3 + (-163 / 23) * t ^ 2 + (304 / 23) * t + (-85 / 23)) * h + ((-1677 / 529) * t ^ 4 + (3067 / 529) * t ^ 3 + (-2066 / 529) * t ^ 2 + (-3103 / 529) * t + (4656 / 529)) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((129 / 23) * t ^ 5 + (-226 / 23) * t ^ 4 + (211 / 23) * t ^ 3 + (163 / 23) * t ^ 2 + (-304 / 23) * t + (108 / 23)) * h + ((645 / 529) * t ^ 4 + (418 / 529) * t ^ 3 + (278 / 529) * t ^ 2 + (1634 / 529) * t + (1523 / 529)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((39 / 23) * t ^ 5 + (-94 / 23) * t ^ 4 + (90 / 23) * t ^ 3 + (45 / 23) * t ^ 2 + (-147 / 23) * t + (84 / 23)) * h + ((-195 / 529) * t ^ 4 + (2 / 529) * t ^ 3 + (93 / 529) * t ^ 2 + (-402 / 529) * t + (-193 / 529)) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `7_3`, exponents `[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * z1 t ^ 1 * z2 t ^ 1 * (z2 t - 1) ^ 1 * (z3 t - 1) ^ 1 = z2 t ^ 1 * (1 - z3 t) ^ 1 * z3 t ^ 1 * (1 - z4 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination ((73008 / 279841) * t ^ 15 + (-431028 / 279841) * t ^ 14 + (1343124 / 279841) * t ^ 13 + (-2405596 / 279841) * t ^ 12 + (2069940 / 279841) * t ^ 11 + (1281476 / 279841) * t ^ 10 + (-6370684 / 279841) * t ^ 9 + (362160 / 12167) * t ^ 8 + (-3701544 / 279841) * t ^ 7 + (-4240880 / 279841) * t ^ 6 + (8031268 / 279841) * t ^ 5 + (-5105048 / 279841) * t ^ 4 + (125292 / 279841) * t ^ 3 + (2100852 / 279841) * t ^ 2 + (-1469916 / 279841) * t + (348432 / 279841)) * ht

/-- **Edge 1** of `7_3`, exponents `[0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    z1 t ^ 1 * (z1 t - 1) ^ 1 * (z3 t - 1) ^ 1 * z4 t ^ 1 = (1 - z0 t) ^ 1 * z1 t ^ 1 * z3 t ^ 1 * (1 - z4 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z3, z4]
  linear_combination ((-296595 / 279841) * t ^ 14 + (1432782 / 279841) * t ^ 13 + (-2965131 / 279841) * t ^ 12 + (1353344 / 279841) * t ^ 11 + (6582684 / 279841) * t ^ 10 + (-14269668 / 279841) * t ^ 9 + (297111 / 12167) * t ^ 8 + (720633 / 12167) * t ^ 7 + (-28231952 / 279841) * t ^ 6 + (7007255 / 279841) * t ^ 5 + (23345488 / 279841) * t ^ 4 + (-23908641 / 279841) * t ^ 3 + (-152583 / 279841) * t ^ 2 + (11954481 / 279841) * t + (-5289564 / 279841)) * ht

/-- **Edge 2** of `7_3`, exponents `[0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z1 t - 1) ^ 1 * z2 t ^ 1 * z3 t ^ 1 * z4 t ^ 1 * (z4 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * z1 t ^ 1 * z4 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination ((-1368900 / 6436343) * t ^ 20 + (6074055 / 6436343) * t ^ 19 + (-14370669 / 6436343) * t ^ 18 + (11482104 / 6436343) * t ^ 17 + (899527 / 279841) * t ^ 16 + (-74957094 / 6436343) * t ^ 15 + (78724642 / 6436343) * t ^ 14 + (30831185 / 6436343) * t ^ 13 + (-180470582 / 6436343) * t ^ 12 + (177937734 / 6436343) * t ^ 11 + (44130448 / 6436343) * t ^ 10 + (-246118662 / 6436343) * t ^ 9 + (185636870 / 6436343) * t ^ 8 + (45016545 / 6436343) * t ^ 7 + (-156079580 / 6436343) * t ^ 6 + (84842704 / 6436343) * t ^ 5 + (-412339 / 279841) * t ^ 4 + (-8733507 / 6436343) * t ^ 3 + (27663885 / 6436343) * t ^ 2 + (-25422768 / 6436343) * t + (6620208 / 6436343)) * ht

/-- **Edge 3** of `7_3`, exponents `[0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z4 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 * z4 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination ((91260 / 279841) * t ^ 15 + (-319761 / 279841) * t ^ 14 + (659601 / 279841) * t ^ 13 + (-356702 / 279841) * t ^ 12 + (-871809 / 279841) * t ^ 11 + (2477428 / 279841) * t ^ 10 + (-87002 / 12167) * t ^ 9 + (-61501 / 12167) * t ^ 8 + (4567872 / 279841) * t ^ 7 + (-3664951 / 279841) * t ^ 6 + (-2045273 / 279841) * t ^ 5 + (4945997 / 279841) * t ^ 4 + (-2739857 / 279841) * t ^ 3 + (-1535452 / 279841) * t ^ 2 + (2389948 / 279841) * t + (-4 / 23)) * ht

/-- **Edge 4** of `7_3`, exponents `[1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z2 t - 1) ^ 1 * z3 t ^ 1 = (1 - z0 t) ^ 1 * (1 - z2 t) ^ 1 * z2 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z2, z3]
  linear_combination ((-204 / 529) * t ^ 5 + (221 / 529) * t ^ 4 + (-561 / 529) * t ^ 3 + (-85 / 529) * t ^ 2 + (17 / 529) * t + (-680 / 529)) * ht

end K73

/-! ### `8_1` — 5 tetrahedra, shape field of degree 6

Minimal polynomial `x^6 - 4*x^5 + 40*x^4 - 96*x^3 + 160*x^2 - 163*x + 63`. -/

namespace K81

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 6 + (-4) * t ^ 5 + 40 * t ^ 4 + (-96) * t ^ 3 + 160 * t ^ 2 + (-163) * t + 63

/-- Shape `z0` of `8_1`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `8_1`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := (-64072 / 1481781) * t ^ 5 + (200176 / 1481781) * t ^ 4 + (-2375917 / 1481781) * t ^ 3 + (1349877 / 493927) * t ^ 2 + (-6221368 / 1481781) * t + (5032099 / 1481781)

/-- Shape `z2` of `8_1`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := (281 / 15489) * t ^ 5 + (-602 / 15489) * t ^ 4 + (9350 / 15489) * t ^ 3 + (-2449 / 5163) * t ^ 2 + (4964 / 15489) * t + (6523 / 15489)

/-- Shape `z3` of `8_1`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := (-64072 / 1481781) * t ^ 5 + (200176 / 1481781) * t ^ 4 + (-2375917 / 1481781) * t ^ 3 + (1349877 / 493927) * t ^ 2 + (-6221368 / 1481781) * t + (5032099 / 1481781)

/-- Shape `z4` of `8_1`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := (-22841 / 70561) * t ^ 5 + (71484 / 70561) * t ^ 4 + (-850147 / 70561) * t ^ 3 + (1449749 / 70561) * t ^ 2 + (-2342905 / 70561) * t + (1700790 / 70561)

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 63) * t ^ 5 + (4 / 63) * t ^ 4 + (-40 / 63) * t ^ 3 + (32 / 21) * t ^ 2 + (-160 / 63) * t + (163 / 63)) * h + ((1 / 63)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 5 + (-3) * t ^ 4 + 37 * t ^ 3 + (-59) * t ^ 2 + 101 * t + (-62)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((5633 / 70561) * t ^ 5 + (-16894 / 70561) * t ^ 4 + (207221 / 70561) * t ^ 3 + (-330006 / 70561) * t ^ 2 + (507748 / 70561) * t + (-242340 / 70561)) * h + ((360917576 / 104555949141) * t ^ 4 + (-766353472 / 104555949141) * t ^ 3 + (1791465827 / 14936564163) * t ^ 2 + (-3370619739 / 34851983047) * t + (21016425727 / 104555949141)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-22841 / 70561) * t ^ 5 + (71484 / 70561) * t ^ 4 + (-850147 / 70561) * t ^ 3 + (1449749 / 70561) * t ^ 2 + (-2342905 / 70561) * t + (1700790 / 70561)) * h + ((209066936 / 14936564163) * t ^ 4 + (-157069936 / 4978854721) * t ^ 3 + (51315703261 / 104555949141) * t ^ 2 + (-6815782289 / 14936564163) * t + (97506369847 / 104555949141)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-58 / 1721) * t ^ 5 + (210 / 1721) * t ^ 4 + (-2181 / 1721) * t ^ 3 + (4444 / 1721) * t ^ 2 + (-5814 / 1721) * t + (5409 / 1721)) * h + ((16298 / 26656569) * t ^ 4 + (-9578 / 8885523) * t ^ 3 + (171575 / 8885523) * t ^ 2 + (-178484 / 26656569) * t + (-15214 / 2961841)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((289 / 1721) * t ^ 5 + (-809 / 1721) * t ^ 4 + (10541 / 1721) * t ^ 3 + (-15022 / 1721) * t ^ 2 + (26774 / 1721) * t + (-12798 / 1721)) * h + ((81209 / 26656569) * t ^ 4 + (-76471 / 26656569) * t ^ 3 + (2596945 / 26656569) * t ^ 2 + (988387 / 26656569) * t + (2244499 / 26656569)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((5633 / 70561) * t ^ 5 + (-16894 / 70561) * t ^ 4 + (207221 / 70561) * t ^ 3 + (-330006 / 70561) * t ^ 2 + (507748 / 70561) * t + (-242340 / 70561)) * h + ((360917576 / 104555949141) * t ^ 4 + (-766353472 / 104555949141) * t ^ 3 + (1791465827 / 14936564163) * t ^ 2 + (-3370619739 / 34851983047) * t + (21016425727 / 104555949141)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-22841 / 70561) * t ^ 5 + (71484 / 70561) * t ^ 4 + (-850147 / 70561) * t ^ 3 + (1449749 / 70561) * t ^ 2 + (-2342905 / 70561) * t + (1700790 / 70561)) * h + ((209066936 / 14936564163) * t ^ 4 + (-157069936 / 4978854721) * t ^ 3 + (51315703261 / 104555949141) * t ^ 2 + (-6815782289 / 14936564163) * t + (97506369847 / 104555949141)) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((64072 / 1481781) * t ^ 5 + (-200176 / 1481781) * t ^ 4 + (2375917 / 1481781) * t ^ 3 + (-1349877 / 493927) * t ^ 2 + (6221368 / 1481781) * t + (-3550318 / 1481781)) * h + ((209066936 / 14936564163) * t ^ 4 + (-157069936 / 4978854721) * t ^ 3 + (51315703261 / 104555949141) * t ^ 2 + (-6815782289 / 14936564163) * t + (97506369847 / 104555949141)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-5633 / 70561) * t ^ 5 + (16894 / 70561) * t ^ 4 + (-207221 / 70561) * t ^ 3 + (330006 / 70561) * t ^ 2 + (-507748 / 70561) * t + (312901 / 70561)) * h + ((128663353 / 4978854721) * t ^ 4 + (-273891814 / 4978854721) * t ^ 3 + (4487562232 / 4978854721) * t ^ 2 + (-3621869169 / 4978854721) * t + (8175859350 / 4978854721)) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `8_1`, exponents `[2, 0, 0, 1, 0, 0, 2, 1, 0, 1, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 2 * z1 t ^ 1 * z2 t ^ 2 * z3 t ^ 1 = (1 - z2 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3]
  linear_combination ((324152369909824 / 526762442928498316281) * t ^ 16 + (-235304653734656 / 58529160325388701809) * t ^ 15 + (12501762995573360 / 175587480976166105427) * t ^ 14 + (-174047889011969872 / 526762442928498316281) * t ^ 13 + (473037314598009043 / 175587480976166105427) * t ^ 12 + (-504227667364535158 / 58529160325388701809) * t ^ 11 + (19563859369853733097 / 526762442928498316281) * t ^ 10 + (-12962249446427575876 / 175587480976166105427) * t ^ 9 + (7126907933192910886 / 58529160325388701809) * t ^ 8 + (-19129556404844391323 / 175587480976166105427) * t ^ 7 + (8727381571655790619 / 175587480976166105427) * t ^ 6 + (780496270269791651 / 19509720108462900603) * t ^ 5 + (-5019729575257354520 / 75251777561214045183) * t ^ 4 + (42938758594278218 / 3583417979105430723) * t ^ 3 + (-4270698700862036 / 58529160325388701809) * t ^ 2 + (-1148726 / 61475841) * t + (-8966 / 975807)) * ht

/-- **Edge 1** of `8_1`, exponents `[0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * (z3 t - 1) ^ 1 = (1 - z0 t) ^ 1 * z1 t ^ 1 * z3 t ^ 1 * (1 - z4 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z3, z4]
  linear_combination ((13395336723392 / 22132716982014303) * t ^ 10 + (-85436874522304 / 22132716982014303) * t ^ 9 + (7929544577276816 / 154929018874100121) * t ^ 8 + (-11505909005955296 / 51643006291366707) * t ^ 7 + (62424867555816299 / 51643006291366707) * t ^ 6 + (-530630535691424239 / 154929018874100121) * t ^ 5 + (378567777091790158 / 51643006291366707) * t ^ 4 + (-254493107920641427 / 22132716982014303) * t ^ 3 + (644652204566788547 / 51643006291366707) * t ^ 2 + (-511596615274754725 / 51643006291366707) * t + (74374067422532679 / 17214335430455569)) * ht

/-- **Edge 2** of `8_1`, exponents `[0, 0, 2, 1, 1, 0, 0, 1, 0, 1, 1, 0, 2, 1, 0]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 2 * z1 t ^ 1 * z3 t ^ 1 * z4 t ^ 2 = z0 t ^ 2 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 * (1 - z4 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination ((2907993649281169280 / 14055359786711201105847) * t ^ 16 + (-30095423344569091072 / 14055359786711201105847) * t ^ 15 + (3049484137813278094240 / 98387518506978407740929) * t ^ 14 + (-523071403554354062368 / 2399695573340936774169) * t ^ 13 + (154685344389506156414210 / 98387518506978407740929) * t ^ 12 + (-763328265889741612466036 / 98387518506978407740929) * t ^ 11 + (3335045141730460487407186 / 98387518506978407740929) * t ^ 10 + (-11314587892650419618206102 / 98387518506978407740929) * t ^ 9 + (10192716019201102213248452 / 32795839502326135913643) * t ^ 8 + (-22177290765496478461400998 / 32795839502326135913643) * t ^ 7 + (116488017533106461078038792 / 98387518506978407740929) * t ^ 6 + (-165126740488806200299180967 / 98387518506978407740929) * t ^ 5 + (187269745397612134878298705 / 98387518506978407740929) * t ^ 4 + (-55193651661586054541518675 / 32795839502326135913643) * t ^ 3 + (109599901164938756490474887 / 98387518506978407740929) * t ^ 2 + (-6936873338687574681713600 / 14055359786711201105847) * t + (23728108049720313994300 / 223100948995415890569)) * ht

/-- **Edge 3** of `8_1`, exponents `[0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    (z2 t - 1) ^ 2 = (1 - z0 t) ^ 1 * z2 t ^ 2 := by
  simp only [minpoly] at ht
  simp only [z0, z2]
  linear_combination ((78961 / 239909121) * t ^ 5 + (-22480 / 239909121) * t ^ 4 + (2368744 / 239909121) * t ^ 3 + (856006 / 79969707) * t ^ 2 + (-211472 / 239909121) * t + (349 / 139401)) * ht

/-- **Edge 4** of `8_1`, exponents `[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 2]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * (z3 t - 1) ^ 1 * (z4 t - 1) ^ 2 = (1 - z1 t) ^ 1 * z1 t ^ 1 * (1 - z3 t) ^ 1 * z3 t ^ 1 * z4 t ^ 2 := by
  simp only [minpoly] at ht
  simp only [z1, z3, z4]
  linear_combination ((-179435045933054322719985664 / 489857161005944316825987296575809) * t ^ 24 + (882593832502338287535013888 / 163285720335314772275329098858603) * t ^ 23 + (-339540401981090476895274711040 / 3429000127041610217781911076030663) * t ^ 22 + (1132566885664107769139566471168 / 1143000042347203405927303692010221) * t ^ 21 + (-239135850498264317519893902470528 / 24003000889291271524473377532214641) * t ^ 20 + (1760457376377666186936490539222272 / 24003000889291271524473377532214641) * t ^ 19 + (-4048451135931773286716625011951456 / 8001000296430423841491125844071547) * t ^ 18 + (2519001050238015386754439226480672 / 889000032936713760165680649341283) * t ^ 17 + (-5467390547977069726788614445822239 / 381000014115734468642434564003407) * t ^ 16 + (5153573600708339590776828339987472 / 83634149440039273604436855512943) * t ^ 15 + (-69176199341247503671119311859171028 / 296333344312237920055226883113761) * t ^ 14 + (18287538992073264564656977135999979888 / 24003000889291271524473377532214641) * t ^ 13 + (-51726712641838110648381778044479184826 / 24003000889291271524473377532214641) * t ^ 12 + (126199927488937017112181664336158808097 / 24003000889291271524473377532214641) * t ^ 11 + (-265776016496732113153585391172166092926 / 24003000889291271524473377532214641) * t ^ 10 + (161045166301297942776280957345837665986 / 8001000296430423841491125844071547) * t ^ 9 + (-756188356573805096998133330333066900588 / 24003000889291271524473377532214641) * t ^ 8 + (1015837679348145674257609410563383635572 / 24003000889291271524473377532214641) * t ^ 7 + (-1161601747562760520100108405925802180268 / 24003000889291271524473377532214641) * t ^ 6 + (372402157711326873681566708845853961269 / 8001000296430423841491125844071547) * t ^ 5 + (-885875670092566336701225215816555064593 / 24003000889291271524473377532214641) * t ^ 4 + (186677300193026639594659622035142753996 / 8001000296430423841491125844071547) * t ^ 3 + (-267256477969645636061277959827488898792 / 24003000889291271524473377532214641) * t ^ 2 + (85631704078128271674295235648683865332 / 24003000889291271524473377532214641) * t + (-642274262678779572694874124818853412 / 1143000042347203405927303692010221)) * ht

end K81

end QOU.Knot.GeneratedGluing
