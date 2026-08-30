import QOU.AlgebraicSubstrate.LocalQZetaFunction
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Pow.NNReal
import Mathlib.Data.Fin.Basic

/-!
# QOU.AlgebraicSubstrate.hasse_weil_bound

The Hasse–Weil bound: all 8 fundamental Frobenius eigenvalues of
Bring's curve have absolute value q^{1/2}.

The proof decomposes into three steps:
1. The functional equation constrains eigenvalue norms (symmetry)
2. The Castelnuovo–Severi inequality bounds intersection numbers
3. Combined, these force |αᵢ| = q^{1/2} exactly

LaTeX label: `thm:hasse-weil-bound`

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.

## Why the two Weil inputs are a CLASS and not axioms (bean `qou-hwax`)

Until 2026-08-29 the two classical inputs were global axioms, each
universally quantified over an arbitrary `LocalQZetaFunction`:

```lean
axiom castelnuovo_severi_bound_axiom :
    ∀ (Z : LocalQZetaFunction) (i : Fin 8), ‖Z.eigenvalues i‖ ^ 2 ≤ Z.q
```

**Both proved `False`.** `LocalQZetaFunction` records the *shape* of a zeta
function — a real field size, eight nonzero complex numbers, and a degree-8
polynomial that factors over them — but nothing ties that data to an actual
curve. The datum `q := 1`, `eigenvalues := fun _ => 2` satisfies every field
(the product `∏ (X - C 2)` over `Fin 8` is monic of degree 8), and then
Castelnuovo–Severi reads `4 ≤ 1`. The functional-equation axiom falls the same
way: with `q := 4` and all eigenvalues `1` it demands some `αⱼ = 4`. Both
`False` derivations were machine-checked, each depending on its own axiom plus
only `propext`/`Classical.choice`/`Quot.sound`.

This is the `qou-rhax` defect class one file over — an external theorem
asserted for every inhabitant of a structure that does not carry the theorem's
hypotheses. The classical results hold for the zeta function of a smooth
projective geometrically irreducible curve over `𝔽_q`; `LocalQZetaFunction`
does not say that its inhabitant is one.

The fix is the §3b-cond conditional-class pattern: the two Weil inputs become
fields of `IsWeilZeta`, carried as an explicit `[IsWeilZeta Z]` hypothesis.
`hasse_weil_bound` is then a genuine conditional theorem — sorry-free, and
`#print axioms`-clean apart from Lean's own three. `weilZetaExample` below
exhibits an instance, so the class is *inhabited*: unlike the axioms it
replaces, its fields are jointly consistent.
-/

set_option autoImplicit false


open Complex Real

namespace QOU.AlgebraicSubstrate

/-- **Weil datum.** The hypothesis that `Z` is the zeta function of a smooth
    projective geometrically irreducible curve over `𝔽_q`, recorded through the
    two consequences the Hasse–Weil argument consumes.

    Both fields are classical theorems *about such curves*, not properties of an
    arbitrary `LocalQZetaFunction` — see the module docstring for the `False`
    derivations that follow from asserting them universally.

    * `functional_equation` — the functional equation of the zeta function of a
      curve pairs each eigenvalue `αᵢ` with `q/αᵢ`.
      See [weil1948] §IV, or [rosen2002] Ch 5, Thm 5.9.
    * `castelnuovo_severi` — the Castelnuovo–Severi inequality on `B × B`
      (Hodge index theorem) bounds the self-intersection of the Frobenius
      correspondence, giving `|αᵢ|² ≤ q`.
      See [weil1948] §V; [milne2013] §27; [rosen2002] Ch 5, Thm 5.10. -/
-- Ref: [weil1948] Weil, "Sur les courbes algébriques et les variétés qui s'en déduisent," Hermann, Paris (1948)
-- Ref: [rosen2002] Rosen, "Number Theory in Function Fields," Springer GTM 210, 2002
-- Ref: [milne2013] https://www.jmilne.org/math/CourseNotes/LEC.pdf §27
class IsWeilZeta (Z : LocalQZetaFunction) : Prop where
  /-- Functional-equation pairing: `αᵢ ↦ q/αᵢ` **permutes** the eigenvalues.

      Stated as a permutation rather than as `∀ i, ∃ j`. The existential form is
      strictly weaker and loses multiplicities — it is satisfied by families in
      which two eigenvalues share a partner and a third has none — so nothing
      about the root *multiset* follows from it, and `charPoly_map_conj` below
      is exactly such a multiset statement. Weil's functional equation does
      supply the bijection, so this is the faithful form, not a strengthening
      of the cited result. -/
  functional_equation :
    ∃ σ : Equiv.Perm (Fin 8), ∀ i : Fin 8,
      Z.eigenvalues (σ i) = ↑Z.q / Z.eigenvalues i
  /-- Castelnuovo–Severi: `|αᵢ|² ≤ q`. -/
  castelnuovo_severi : ∀ i : Fin 8, ‖Z.eigenvalues i‖ ^ 2 ≤ Z.q

/-- The functional equation of the local zeta function constrains
    eigenvalue norms: if αᵢ is an eigenvalue, so is q/αᵢ.
    This pairs eigenvalues such that |αᵢ| · |q/αᵢ| = q. -/
theorem eigenvalue_functional_equation
    (Z : LocalQZetaFunction) [IsWeilZeta Z] (i : Fin 8) :
    ∃ (j : Fin 8), Z.eigenvalues j = ↑Z.q / Z.eigenvalues i := by
  obtain ⟨σ, hσ⟩ := IsWeilZeta.functional_equation (Z := Z)
  exact ⟨σ i, hσ i⟩

/-- The Castelnuovo–Severi inequality on B × B bounds the
    self-intersection of the Frobenius correspondence, yielding
    |αᵢ|² ≤ q for all i. -/
theorem castelnuovo_severi_bound
    (Z : LocalQZetaFunction) [IsWeilZeta Z] (i : Fin 8) :
    ‖Z.eigenvalues i‖ ^ 2 ≤ Z.q :=
  IsWeilZeta.castelnuovo_severi i

/-- The functional equation + Castelnuovo–Severi together force
    |αᵢ|² = q (not just ≤).

    The functional equation gives |αᵢ| · |q/αᵢ| = q for paired
    eigenvalues, so |αᵢ|² ≥ q. Combined with CS, equality holds.
    See [rosen2002] Ch 5, proof of Thm 5.12.

    This step is *derived*, not assumed: it is the one piece of the Hasse–Weil
    argument the corpus proves itself. -/
-- Ref: [rosen2002] Rosen, "Number Theory in Function Fields," Springer GTM 210, 2002
theorem eigenvalue_norm_sq
    (Z : LocalQZetaFunction) [IsWeilZeta Z] (i : Fin 8)
    (h_cs : ‖Z.eigenvalues i‖ ^ 2 ≤ Z.q)
    (h_fe : ∃ j, Z.eigenvalues j = ↑Z.q / Z.eigenvalues i) :
    ‖Z.eigenvalues i‖ ^ 2 = Z.q := by
  obtain ⟨j, hj⟩ := h_fe
  have hq : 0 < Z.q := Z.q_pos
  have hnorm : ‖Z.eigenvalues i‖ ≠ 0 := norm_ne_zero_iff.mpr (Z.eigenvalues_ne_zero i)
  have hsq : (0 : ℝ) < ‖Z.eigenvalues i‖ ^ 2 := by positivity
  -- The paired eigenvalue has norm q / ‖αᵢ‖ …
  have hj_norm : ‖Z.eigenvalues j‖ = Z.q / ‖Z.eigenvalues i‖ := by
    rw [hj, norm_div, Complex.norm_real, Real.norm_eq_abs, abs_of_pos hq]
  -- … and Castelnuovo–Severi applies to it too, giving the reverse bound.
  have h_cs_j := castelnuovo_severi_bound Z j
  rw [hj_norm, div_pow, div_le_iff₀ hsq] at h_cs_j
  nlinarith [h_cs, h_cs_j, hq, hsq]

/-- **Hasse–Weil bound**: every fundamental Frobenius eigenvalue αᵢ
    of Bring's curve satisfies |αᵢ| = q^{1/2}.

    This is the Riemann hypothesis for curves over finite fields,
    proved by Weil via the Castelnuovo–Severi inequality on the
    self-product B × B.

    Stated **conditionally on `[IsWeilZeta Z]`** (§3b-cond): the two Weil
    inputs are hypotheses, and everything else is derived. The proof combines:
    - `eigenvalue_functional_equation` (symmetry of the zeta function)
    - `castelnuovo_severi_bound` (Hodge index theorem on B × B)
    - `eigenvalue_norm_sq` (combining the two forces equality) -/
theorem hasse_weil_bound
    (Z : LocalQZetaFunction) [IsWeilZeta Z]
    (i : Fin 8) :
    ‖Z.eigenvalues i‖ = Z.q ^ (1 / 2 : ℝ) := by
  have h_cs := castelnuovo_severi_bound Z i
  have h_fe := eigenvalue_functional_equation Z i
  have h_sq := eigenvalue_norm_sq Z i h_cs h_fe
  -- |αᵢ|² = q  implies  |αᵢ| = q^{1/2}  (since |αᵢ| ≥ 0, q > 0)
  have h_nn : (0 : ℝ) ≤ ‖Z.eigenvalues i‖ := norm_nonneg _
  -- q^{1/2} = √q = √(|α|²) = |α|, the middle step being h_sq.
  rw [← Real.sqrt_eq_rpow, ← h_sq, Real.sqrt_sq h_nn]

/-! ## Non-vacuity

`IsWeilZeta` is a hypothesis class, so it is worth nothing unless it is
*inhabited*: an empty carrier would make `hasse_weil_bound` conditional on a
proposition no datum satisfies, which is the failure mode
`proof-no-empty-prop-carrier` exists to catch. The witness below is the
supersingular shape `q = 4`, `αᵢ = 2` for all `i` — a genuine Weil datum, with
`|αᵢ|² = 4 = q` and `q/αᵢ = 2 = αⱼ`. -/

/-- A concrete `LocalQZetaFunction` with `q = 4` and all eigenvalues `2`. -/
noncomputable def weilZetaExample : LocalQZetaFunction where
  q := 4
  q_pos := by norm_num
  eigenvalues := fun _ => 2
  eigenvalues_ne_zero := by intro i; norm_num
  charPoly := ∏ _i : Fin 8, (Polynomial.X - Polynomial.C (2 : ℂ))
  charPoly_degree := by
    rw [Polynomial.natDegree_prod _ _ (fun i _ => Polynomial.X_sub_C_ne_zero (2 : ℂ))]
    simp [bringsGenus]
  charPoly_roots := rfl

/-- The example is a Weil datum, so `IsWeilZeta` is inhabited and its two
    fields are jointly consistent — unlike the global axioms it replaces. -/
instance : IsWeilZeta weilZetaExample where
  functional_equation := ⟨Equiv.refl _, by intro i; simp [weilZetaExample]; norm_num⟩
  castelnuovo_severi := by
    intro i; simp [weilZetaExample]; norm_num

/-! ## The spectrum is conjugation-closed

`hasse_weil_bound` gives the magnitude `|αᵢ| = q^{1/2}`. Composed with the
functional equation and `weil_partner_eq_conj` (in the shared
`LocalQZetaFunction` module, because content-block siblings cannot import one
another), it gives the *structural* statement: the Frobenius eigenvalue multiset
is closed under complex conjugation.

That is the standard characterisation of Weil numbers, and it is what makes the
critical line a line of symmetry rather than an arbitrary vertical — see
`spectral_half_line_is_fixed_locus` in the `cor:spectral-half-line` sibling. -/

/-- The `q^{1/2}` magnitude, squared: `‖αᵢ‖² = q`. -/
theorem eigenvalue_norm_sq_eq (Z : LocalQZetaFunction) [IsWeilZeta Z] (i : Fin 8) :
    ‖Z.eigenvalues i‖ ^ 2 = Z.q := by
  have hq : (0 : ℝ) < Z.q := Z.q_pos
  rw [hasse_weil_bound Z i, ← Real.rpow_natCast (Z.q ^ (1 / 2 : ℝ)) 2,
    ← Real.rpow_mul (le_of_lt hq)]
  norm_num

/-- **The Frobenius spectrum is closed under conjugation.** For every eigenvalue
    `αᵢ` there is an eigenvalue `αⱼ` equal to `conj αᵢ`.

    Derived, not assumed: the functional equation supplies *some* partner
    `αⱼ = q/αᵢ`, and the Hasse–Weil magnitude is exactly the condition under
    which that partner is the conjugate. Neither input alone gives it. -/
theorem eigenvalues_conj_closed (Z : LocalQZetaFunction) [IsWeilZeta Z] (i : Fin 8) :
    ∃ j : Fin 8, Z.eigenvalues j = (starRingEnd ℂ) (Z.eigenvalues i) := by
  obtain ⟨j, hj⟩ := eigenvalue_functional_equation Z i
  exact ⟨j, hj.trans (weil_partner_eq_conj Z.q (Z.eigenvalues i)
    (Z.eigenvalues_ne_zero i) (eigenvalue_norm_sq_eq Z i))⟩

/-! ## The Frobenius determinant

`|det(Fr_q)| = q^g`, here `q^4` since Bring's curve has genus 4. Two forms: over
the eigenvalue family, and over `charPoly` — the latter finally consuming
`charPoly_roots`, a structure field that until now nothing used.

This is the third consequence of the same two inputs, after the magnitude bound
and conjugation-closure, and it is the one that pins the *degree*: the product of
eight eigenvalues each of modulus `q^{1/2}` is forced to modulus `q^4`. -/

/-- `‖∏ αᵢ‖ = q^4` — the Frobenius determinant has modulus `q^g`, `g = 4`. -/
theorem norm_prod_eigenvalues (Z : LocalQZetaFunction) [IsWeilZeta Z] :
    ‖∏ i : Fin 8, Z.eigenvalues i‖ = Z.q ^ (4 : ℕ) := by
  have hq : (0 : ℝ) < Z.q := Z.q_pos
  rw [norm_prod]
  simp only [hasse_weil_bound Z]
  rw [Finset.prod_const, Finset.card_univ, Fintype.card_fin,
    ← Real.rpow_natCast (Z.q ^ (1 / 2 : ℝ)) 8, ← Real.rpow_mul (le_of_lt hq),
    ← Real.rpow_natCast Z.q 4]
  norm_num

/-- The same, read off the characteristic polynomial: `‖P̃(0)‖ = q^4`.

    Uses `charPoly_roots`, i.e. `P̃ = ∏ (X − αᵢ)`. Evaluating at `0` gives
    `∏ (−αᵢ)`, whose norm is the product of the norms. -/
theorem norm_charPoly_eval_zero (Z : LocalQZetaFunction) [IsWeilZeta Z] :
    ‖Z.charPoly.eval 0‖ = Z.q ^ (4 : ℕ) := by
  have hq : (0 : ℝ) < Z.q := Z.q_pos
  rw [Z.charPoly_roots, Polynomial.eval_prod]
  simp only [Polynomial.eval_sub, Polynomial.eval_X, Polynomial.eval_C, zero_sub]
  rw [norm_prod]
  simp only [norm_neg, hasse_weil_bound Z]
  rw [Finset.prod_const, Finset.card_univ, Fintype.card_fin,
    ← Real.rpow_natCast (Z.q ^ (1 / 2 : ℝ)) 8, ← Real.rpow_mul (le_of_lt hq),
    ← Real.rpow_natCast Z.q 4]
  norm_num

/-! ## The characteristic polynomial has real coefficients

Conjugation-closure at the level of the *multiset* — which the permutation form
of the functional equation supplies and the existential form does not — says
`P̃` is fixed by coefficientwise conjugation. For a curve over `𝔽_q` the
coefficients are in fact integers; `ℝ` is what follows from the two hypotheses
carried here, and it is a genuine constraint: an arbitrary degree-8 monic
complex polynomial does not satisfy it. -/

/-- The functional-equation permutation carries each eigenvalue to its
    conjugate. Sharpens `eigenvalues_conj_closed` from "some `j`" to "this
    permutation", which is what a multiset argument needs. -/
theorem eigenvalues_conj_perm (Z : LocalQZetaFunction) [IsWeilZeta Z] :
    ∃ σ : Equiv.Perm (Fin 8), ∀ i,
      Z.eigenvalues (σ i) = (starRingEnd ℂ) (Z.eigenvalues i) := by
  obtain ⟨σ, hσ⟩ := IsWeilZeta.functional_equation (Z := Z)
  exact ⟨σ, fun i => (hσ i).trans (weil_partner_eq_conj Z.q (Z.eigenvalues i)
    (Z.eigenvalues_ne_zero i) (eigenvalue_norm_sq_eq Z i))⟩

/-- **`P̃` is fixed by coefficientwise conjugation** — equivalently, all its
    coefficients are real.

    Derived by reindexing `∏ (X − C ᾱᵢ)` along the functional-equation
    permutation. The existential pairing could not do this: it does not rule out
    two eigenvalues sharing a partner while a third has none, and the product is
    sensitive to exactly that. -/
theorem charPoly_map_conj (Z : LocalQZetaFunction) [IsWeilZeta Z] :
    Z.charPoly.map (starRingEnd ℂ) = Z.charPoly := by
  obtain ⟨σ, hσ⟩ := eigenvalues_conj_perm Z
  conv_rhs => rw [Z.charPoly_roots]
  rw [Z.charPoly_roots, Polynomial.map_prod]
  simp only [Polynomial.map_sub, Polynomial.map_X, Polynomial.map_C]
  exact Fintype.prod_equiv σ
    (fun x => Polynomial.X - Polynomial.C ((starRingEnd ℂ) (Z.eigenvalues x)))
    (fun j => Polynomial.X - Polynomial.C (Z.eigenvalues j))
    (fun x => by simp only [hσ x])

/-- Every coefficient of `P̃` is real. -/
theorem charPoly_coeff_isReal (Z : LocalQZetaFunction) [IsWeilZeta Z] (n : ℕ) :
    (starRingEnd ℂ) (Z.charPoly.coeff n) = Z.charPoly.coeff n := by
  have h := congrArg (fun p => Polynomial.coeff p n) (charPoly_map_conj Z)
  simpa using h

/-! ## `det(Fr_q) = ±q^g` — the determinant pinned, not just bounded

`norm_prod_eigenvalues` gives `‖∏ αᵢ‖ = q⁴`, a statement about modulus only. The
functional equation pins the value itself: the multiset is stable under
`α ↦ q/α`, so the product is invariant under that map, and a product of eight
terms each replaced by `q/αᵢ` is `q⁸ / ∏ αᵢ`. Equating gives `(∏ αᵢ)² = q⁸`,
hence `∏ αᵢ = ±q⁴` — the classical `det(Fr_q) = ±q^g` for `g = 4`.

The sign is the genuinely arithmetic datum (it distinguishes the two square
roots and is not determined by the hypotheses carried here), which is why the
statement is a disjunction rather than an equality. -/

/-- The eigenvalue product is nonzero. -/
theorem prod_eigenvalues_ne_zero (Z : LocalQZetaFunction) :
    ∏ i : Fin 8, Z.eigenvalues i ≠ 0 :=
  Finset.prod_ne_zero_iff.mpr fun i _ => Z.eigenvalues_ne_zero i

/-- The product is invariant under the functional-equation pairing: replacing
    every `αᵢ` by its partner `q/αᵢ` leaves the product unchanged. Reindexing
    along the permutation, exactly as for `charPoly_map_conj`. -/
theorem prod_partner_eq (Z : LocalQZetaFunction) [IsWeilZeta Z] :
    ∏ i : Fin 8, ((Z.q : ℂ) / Z.eigenvalues i) = ∏ i : Fin 8, Z.eigenvalues i := by
  obtain ⟨σ, hσ⟩ := IsWeilZeta.functional_equation (Z := Z)
  exact Fintype.prod_equiv σ
    (fun i => (Z.q : ℂ) / Z.eigenvalues i)
    (fun j => Z.eigenvalues j)
    (fun i => by simp only [hσ i])

/-- `(∏ αᵢ)² = q⁸`. -/
theorem prod_eigenvalues_sq (Z : LocalQZetaFunction) [IsWeilZeta Z] :
    (∏ i : Fin 8, Z.eigenvalues i) ^ 2 = (Z.q : ℂ) ^ 8 := by
  have hP := prod_eigenvalues_ne_zero Z
  have h := prod_partner_eq Z
  rw [Finset.prod_div_distrib, Finset.prod_const, Finset.card_univ,
    Fintype.card_fin] at h
  field_simp at h
  linear_combination -h

/-- **`det(Fr_q) = ±q^g`.** The Frobenius determinant is exactly `+q⁴` or `−q⁴`.

    Upgrades `norm_prod_eigenvalues` from a modulus to a value. The sign is not
    determined by the two hypotheses carried here — it is the arithmetic datum
    that distinguishes the two square roots — so the conclusion is a
    disjunction, honestly. -/
theorem prod_eigenvalues_eq_pm (Z : LocalQZetaFunction) [IsWeilZeta Z] :
    (∏ i : Fin 8, Z.eigenvalues i) = (Z.q : ℂ) ^ 4 ∨
      (∏ i : Fin 8, Z.eigenvalues i) = -((Z.q : ℂ) ^ 4) := by
  have h : (∏ i : Fin 8, Z.eigenvalues i) ^ 2 - ((Z.q : ℂ) ^ 4) ^ 2 = 0 := by
    rw [← pow_mul]; norm_num [prod_eigenvalues_sq Z]
  have hf : ((∏ i : Fin 8, Z.eigenvalues i) - (Z.q : ℂ) ^ 4) *
      ((∏ i : Fin 8, Z.eigenvalues i) + (Z.q : ℂ) ^ 4) = 0 := by
    linear_combination h
  rcases mul_eq_zero.mp hf with h1 | h2
  · exact Or.inl (by linear_combination h1)
  · exact Or.inr (by linear_combination h2)

end QOU.AlgebraicSubstrate
