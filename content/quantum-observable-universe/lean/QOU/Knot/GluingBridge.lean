/-
  The bridge from a cleared gluing identity to `SatisfiesEdgeEquations`.

  Bean `qou-glhi`.  Successor to `qou-glnl`.

  ═══ THE GAP THIS CLOSES ═══

  `QOU/Knot/GeneratedGluing.lean` proves 312 edge identities in **cleared** form,

      ∏ zⱼ^{aⱼ} · ∏ (zⱼ − 1)^{cⱼ}  =  ∏ (1 − zⱼ)^{bⱼ} · ∏ zⱼ^{cⱼ},

  because that form is a polynomial identity and therefore code-generable by a single
  `linear_combination` with an exactly computed cofactor.  `SatisfiesEdgeEquations`
  (`QOU/Knot/FlatTetrahedra.lean`) is stated in **product** form,

      ∏ᵢ ∏ⱼ (param i j) ^ exp = 1,

  with `param = (z, 1/(1−z), 1 − 1/z)`.  The two are equivalent given non-vanishing, but
  the passage between them is exactly the `field_simp` step that the generator could not
  emit — `field_simp`'s normal form is not predictable, which is why `glnl` avoided it.

  **So do it once, generically, here.**  `param_pow_prod` converts one tetrahedron's
  contribution to a single quotient; the products then compose, and `div_eq_one_iff_eq`
  finishes.  No per-knot cofactor is ever needed again.

  ═══ WHY THIS TARGETS THE FLAT-TOLERANT STRUCTURE ═══

  The generated identities hold for an **arbitrary root** of the shape field's minimal
  polynomial — that is what made them provable without exhibiting a root in the upper half
  plane.  So they live naturally over `Shape` (`z ∈ ℂ ∖ {0,1}`, flat shapes allowed) and
  **not** over `IdealTetrahedron`, which carries `im_pos`.  Wiring them to the
  `im_pos`-bearing structure would re-import a hypothesis the proofs do not use and cannot
  supply.

  -- Ref: [thurston1978] Ch. 4
  -- Ref: [neumann-zagier1985]
-/
import QOU.Knot.FlatTetrahedra

namespace QOU.Knot.FlatTet

open QOU.MathlibExt

namespace Shape

variable (S : Shape)

/-- **One tetrahedron's contribution, as a single quotient.**

`z^a · (1/(1−z))^b · (1 − 1/z)^c = z^a (z−1)^c / ((1−z)^b z^c)`.

This is the whole bridge: it turns the three edge parameters — two of which are
quotients — into one numerator over one denominator, in a form that composes across
tetrahedra. -/
theorem param_pow_prod (a b c : ℕ) :
    S.param 0 ^ a * S.param 1 ^ b * S.param 2 ^ c
      = (S.z ^ a * (S.z - 1) ^ c) / ((1 - S.z) ^ b * S.z ^ c) := by
  have h0 := S.ne_zero
  have h1 := S.one_sub_ne_zero
  have hb : (1 - S.z) ^ b ≠ 0 := pow_ne_zero _ h1
  have hc : S.z ^ c ≠ 0 := pow_ne_zero _ h0
  -- Rewrite each parameter as an explicit quotient FIRST.  Going straight to
  -- `field_simp` leaves `(1-z)⁻¹^b * (1-z)^b` uncancelled: it does not cancel an
  -- inverse against a power when the exponent is a variable.
  have e2 : S.param 2 = (S.z - 1) / S.z := by
    simp only [param_two]; field_simp
  have e1 : S.param 1 = 1 / (1 - S.z) := rfl
  rw [param_zero, e1, e2, div_pow, div_pow, one_pow]
  field_simp

/-- The denominator appearing in `param_pow_prod` is nonzero — needed to turn a quotient
equation into an equation of numerators. -/
theorem param_pow_den_ne_zero (b c : ℕ) :
    ((1 - S.z) ^ b * S.z ^ c) ≠ 0 :=
  mul_ne_zero (pow_ne_zero _ S.one_sub_ne_zero) (pow_ne_zero _ S.ne_zero)

end Shape

/-! ### The single-tetrahedron edge equation

Stated separately because it is the shape every generated theorem already has: a cleared
identity plus non-vanishing gives the product form, with no `field_simp` at the call
site. -/

/-- **Cleared form ⟹ product form**, for one tetrahedron.

The hypothesis is exactly what `GeneratedGluing` proves; the conclusion is exactly what
`SatisfiesEdgeEquations` requires of a single factor. -/
theorem satisfies_of_cleared_one (S : Shape) {a b c : ℕ}
    (h : S.z ^ a * (S.z - 1) ^ c = (1 - S.z) ^ b * S.z ^ c) :
    S.param 0 ^ a * S.param 1 ^ b * S.param 2 ^ c = 1 := by
  rw [S.param_pow_prod a b c, h]
  exact div_self (S.param_pow_den_ne_zero b c)

/-! ### Two tetrahedra

The composition step, written out at `n = 2` so the pattern is visible and checkable.
`Finset.prod_div_distrib` makes the general case routine; it is not needed for the
manifolds `glnl` covers, whose products are unfolded by `Fin.prod_univ_*` anyway. -/

/-- **Cleared form ⟹ product form**, for two tetrahedra.

Note the hypothesis multiplies the two numerators and the two denominators — which is
precisely how the generated theorems state a multi-tetrahedron edge equation. -/
theorem satisfies_of_cleared_two (S T : Shape) {a b c d e f : ℕ}
    (h : (S.z ^ a * (S.z - 1) ^ c) * (T.z ^ d * (T.z - 1) ^ f)
        = ((1 - S.z) ^ b * S.z ^ c) * ((1 - T.z) ^ e * T.z ^ f)) :
    (S.param 0 ^ a * S.param 1 ^ b * S.param 2 ^ c)
      * (T.param 0 ^ d * T.param 1 ^ e * T.param 2 ^ f) = 1 := by
  rw [S.param_pow_prod a b c, T.param_pow_prod d e f, div_mul_div_comm, h]
  exact div_self (mul_ne_zero (S.param_pow_den_ne_zero b c) (T.param_pow_den_ne_zero e f))

/-! ### The general `n`-tetrahedron composition

`satisfies_of_cleared_two` written for arbitrary `n`, which is what the 19 manifolds in
`GeneratedGluing` need.  `Finset.prod_div_distrib` does the work: each tetrahedron becomes
one quotient by `param_pow_prod`, the quotients compose into a single quotient of
products, and the cleared hypothesis says numerator equals denominator. -/

/-- **Cleared form ⟹ `SatisfiesEdgeEquations`, for one edge, at any `n`.**

The hypothesis is the cleared identity for edge `k` — exactly the shape
`GeneratedGluing` proves, once its explicit products are read as `Finset` products.  The
conclusion is one conjunct of `SatisfiesEdgeEquations`. -/
theorem satisfies_edge_of_cleared {n e : ℕ} (T : ShapedTriangulation n)
    (G : GluingData n e) (k : Fin e)
    (h : (∏ i, ((T.tet i).z ^ G.exp k i 0 * ((T.tet i).z - 1) ^ G.exp k i 2))
        = (∏ i, ((1 - (T.tet i).z) ^ G.exp k i 1 * (T.tet i).z ^ G.exp k i 2))) :
    (∏ i, ∏ j, (T.tet i).param j ^ G.exp k i j) = 1 := by
  have hden : (∏ i, ((1 - (T.tet i).z) ^ G.exp k i 1 * (T.tet i).z ^ G.exp k i 2)) ≠ 0 :=
    Finset.prod_ne_zero_iff.mpr fun i _ => (T.tet i).param_pow_den_ne_zero _ _
  have hstep : ∀ i, (∏ j, (T.tet i).param j ^ G.exp k i j)
      = ((T.tet i).z ^ G.exp k i 0 * ((T.tet i).z - 1) ^ G.exp k i 2)
        / ((1 - (T.tet i).z) ^ G.exp k i 1 * (T.tet i).z ^ G.exp k i 2) := by
    intro i
    rw [Fin.prod_univ_three]
    exact (T.tet i).param_pow_prod _ _ _
  simp only [hstep]
  rw [Finset.prod_div_distrib, h]
  exact div_self hden

/-- **The whole edge system**, from the cleared identity at every edge. -/
theorem satisfiesEdgeEquations_of_cleared {n e : ℕ} (T : ShapedTriangulation n)
    (G : GluingData n e)
    (h : ∀ k : Fin e,
      (∏ i, ((T.tet i).z ^ G.exp k i 0 * ((T.tet i).z - 1) ^ G.exp k i 2))
        = (∏ i, ((1 - (T.tet i).z) ^ G.exp k i 1 * (T.tet i).z ^ G.exp k i 2))) :
    T.SatisfiesEdgeEquations G :=
  fun k => satisfies_edge_of_cleared T G k (h k)

/-! ### Worked instance: the trefoil, certified against `SatisfiesEdgeEquations`

`QOU/Knot/FlatTetrahedra.lean` proves the trefoil's two edge equations directly.  Here
they are assembled into the structure, which is what `glhi` asks for: the identities stop
being standalone and start certifying a `ShapedTriangulation`.

The trefoil is the right first case precisely because its shapes are **flat** — it
exercises the flat-tolerant structure that an `IdealTriangulation` could not represent. -/

/-- The trefoil's edge exponent data, from SnapPy: rows `[1,2,2, 2,1,2]` and
`[1,0,0, 0,1,0]`. -/
def trefoilGluing : GluingData 2 2 where
  exp := ![![![1, 2, 2], ![2, 1, 2]], ![![1, 0, 0], ![0, 1, 0]]]

/-- **The trefoil satisfies its first edge equation in product form.**

Derived from `satisfies_of_cleared_two` — no `field_simp`, no cofactor, just the cleared
identity plus non-vanishing.  Both shapes are real, so this is a statement about a
genuinely degenerate solution, which is the point of the flat-tolerant structure. -/
theorem trefoil_edge_zero_product :
    (trefoilShape₀.param 0 ^ 1 * trefoilShape₀.param 1 ^ 2 * trefoilShape₀.param 2 ^ 2)
      * (trefoilShape₁.param 0 ^ 2 * trefoilShape₁.param 1 ^ 1
          * trefoilShape₁.param 2 ^ 2) = 1 := by
  refine satisfies_of_cleared_two trefoilShape₀ trefoilShape₁ ?_
  show ((-1 : ℂ) ^ 1 * ((-1 : ℂ) - 1) ^ 2) * ((2 : ℂ) ^ 2 * ((2 : ℂ) - 1) ^ 2)
      = ((1 - (-1 : ℂ)) ^ 2 * (-1 : ℂ) ^ 2) * ((1 - (2 : ℂ)) ^ 1 * (2 : ℂ) ^ 2)
  norm_num

/-- **The trefoil satisfies its second edge equation in product form**: `z₀ · z₁′ = 1`. -/
theorem trefoil_edge_one_product :
    (trefoilShape₀.param 0 ^ 1 * trefoilShape₀.param 1 ^ 0 * trefoilShape₀.param 2 ^ 0)
      * (trefoilShape₁.param 0 ^ 0 * trefoilShape₁.param 1 ^ 1
          * trefoilShape₁.param 2 ^ 0) = 1 := by
  refine satisfies_of_cleared_two trefoilShape₀ trefoilShape₁ ?_
  show ((-1 : ℂ) ^ 1 * ((-1 : ℂ) - 1) ^ 0) * ((2 : ℂ) ^ 0 * ((2 : ℂ) - 1) ^ 0)
      = ((1 - (-1 : ℂ)) ^ 0 * (-1 : ℂ) ^ 0) * ((1 - (2 : ℂ)) ^ 1 * (2 : ℂ) ^ 0)
  norm_num

/-- **The trefoil triangulation satisfies its edge gluing equations**, as an inhabitant of
`ShapedTriangulation.SatisfiesEdgeEquations` rather than as loose identities.

This is what `glhi` asks for: the generated identities stop being standalone and start
*certifying* a structure the rest of the corpus can consume.  The products are unfolded by
`Fin.prod_univ_two` / `Fin.prod_univ_three` and discharged by the two theorems above. -/
theorem trefoil_satisfiesEdgeEquations :
    trefoilTriangulation.SatisfiesEdgeEquations trefoilGluing := by
  intro k
  fin_cases k <;>
    simp only [ShapedTriangulation.SatisfiesEdgeEquations, trefoilTriangulation,
      trefoilGluing, Fin.prod_univ_two, Fin.prod_univ_three, Matrix.cons_val_zero,
      Matrix.cons_val_one, Matrix.head_cons]
  · exact trefoil_edge_zero_product
  · exact trefoil_edge_one_product

end QOU.Knot.FlatTet
