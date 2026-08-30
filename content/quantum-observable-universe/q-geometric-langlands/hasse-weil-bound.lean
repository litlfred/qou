import QOU.AlgebraicSubstrate.WeilZeta
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Pow.NNReal
import Mathlib.Data.Fin.Basic
import Mathlib.Algebra.Polynomial.Roots

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
## Where the two Weil inputs live (moved 2026-08-30)

`IsWeilZeta`, the chain `eigenvalue_functional_equation` →
`castelnuovo_severi_bound` → `eigenvalue_norm_sq` → `hasse_weil_bound`, and the
`weilZetaExample` instance moved to the library module
`QOU/AlgebraicSubstrate/WeilZeta.lean`, which this file imports. They are
unchanged; only their location is.

The reason is `cor:spectral-half-line`. It concludes `Re(ρᵢ) = 1/2` from the
magnitude `‖αᵢ‖ = q^{1/2}` and used to take that magnitude as its own
hypothesis, having no way to reach the proof next door — content-block siblings
are outside the package globs (§0a) and cannot import one another. So the same
fact was assumed in one file and derived in the other. Now it is derived once
and imported twice.

This file keeps everything **downstream** of the magnitude, which is the block's
own content: conjugation-closure of the spectrum, the characteristic-polynomial
facts, and the Vieta bounds.

-/

set_option autoImplicit false


open Complex Real

namespace QOU.AlgebraicSubstrate

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

/-! ## The trace of Frobenius: real, and bounded by `2g√q`

`∑ αᵢ` is the trace of `Fr_q` on `H¹`, and it is the arithmetically meaningful
one: for a curve over `𝔽_q` the point count is `|ℬ(𝔽_q)| = q + 1 − ∑ αᵢ`, so a
bound on the trace *is* a bound on the point count. The two hypotheses give both
halves of the classical statement.

`sum_eigenvalues_isReal` needs the permutation form of the functional equation
for the same reason `charPoly_map_conj` did — a sum over the family is a multiset
quantity, and the existential pairing does not control it.

`norm_sum_eigenvalues_le` is the **Hasse–Weil point-count bound**: with
`2g = 8`, `|∑ αᵢ| ≤ 2g√q`, i.e. `||ℬ(𝔽_q)| − (q+1)| ≤ 2g√q`. It follows from the
magnitude bound by the triangle inequality alone — no further input. -/

/-- **The trace of Frobenius is real.** `conj (∑ αᵢ) = ∑ αᵢ`, by reindexing the
    conjugated sum along the functional-equation permutation. -/
theorem sum_eigenvalues_isReal (Z : LocalQZetaFunction) [IsWeilZeta Z] :
    (starRingEnd ℂ) (∑ i : Fin 8, Z.eigenvalues i) = ∑ i : Fin 8, Z.eigenvalues i := by
  obtain ⟨σ, hσ⟩ := eigenvalues_conj_perm Z
  rw [map_sum]
  exact Fintype.sum_equiv σ
    (fun i => (starRingEnd ℂ) (Z.eigenvalues i))
    (fun j => Z.eigenvalues j)
    (fun i => by simp only [hσ i])

/-- **The Hasse–Weil point-count bound.** `‖∑ αᵢ‖ ≤ 2g · q^{1/2}` with `2g = 8`.

    Since `|ℬ(𝔽_q)| = q + 1 − ∑ αᵢ` for a curve, this is exactly
    `| |ℬ(𝔽_q)| − (q+1) | ≤ 2g√q` — the statement the theory is named for.
    Derived from the magnitude bound by the triangle inequality; the functional
    equation is not needed for this half. -/
theorem norm_sum_eigenvalues_le (Z : LocalQZetaFunction) [IsWeilZeta Z] :
    ‖∑ i : Fin 8, Z.eigenvalues i‖ ≤ 8 * Z.q ^ (1 / 2 : ℝ) := by
  calc ‖∑ i : Fin 8, Z.eigenvalues i‖
      ≤ ∑ i : Fin 8, ‖Z.eigenvalues i‖ := norm_sum_le _ _
    _ = 8 * Z.q ^ (1 / 2 : ℝ) := by
        simp only [hasse_weil_bound Z, Finset.sum_const, Finset.card_univ,
          Fintype.card_fin, nsmul_eq_mul]
        norm_num

/-- The degree field is redundant given `charPoly_roots`: a product of eight
    monic linear factors is monic of degree eight, so `charPoly_degree` is
    derivable rather than independent. Recorded because a structure carrying a
    consequence of its own field is a place where an inconsistent pair can be
    written — an instance could in principle be refused for the wrong reason. -/
theorem charPoly_natDegree_of_roots (α : Fin 8 → ℂ) :
    (∏ i : Fin 8, (Polynomial.X - Polynomial.C (α i))).natDegree = 8 := by
  rw [Polynomial.natDegree_prod _ _ (fun i _ => Polynomial.X_sub_C_ne_zero (α i))]
  simp

/-! ## Vieta: the trace is a coefficient of `P̃`

Everything above about `∑ αᵢ` is a statement about the eigenvalue family. Vieta
turns it into a statement about the polynomial: the `X⁷` coefficient of a monic
degree-8 `∏ (X − αᵢ)` is `−∑ αᵢ`.

That closes the loop. `P̃` and the eigenvalue family were two presentations of
the same object with nothing connecting them; `norm_charPoly_eval_zero` tied the
constant term to the determinant, and this ties the sub-leading term to the
trace. Both structure fields — `charPoly_roots` and, via
`charPoly_natDegree_of_roots`, the degree — now carry weight. -/

/-- `P̃` is monic. -/
theorem charPoly_monic (Z : LocalQZetaFunction) : Z.charPoly.Monic := by
  rw [Z.charPoly_roots]
  exact Polynomial.monic_prod_of_monic _ _ fun i _ => Polynomial.monic_X_sub_C (Z.eigenvalues i)

/-- **Vieta.** The `X⁷` coefficient of `P̃` is minus the trace of Frobenius. -/
theorem charPoly_coeff_seven (Z : LocalQZetaFunction) :
    Z.charPoly.coeff 7 = -∑ i : Fin 8, Z.eigenvalues i := by
  have hnd : Z.charPoly.natDegree = 8 := by
    rw [Z.charPoly_roots]; exact charPoly_natDegree_of_roots Z.eigenvalues
  have hnext : Z.charPoly.nextCoeff = -∑ i : Fin 8, Z.eigenvalues i := by
    rw [Z.charPoly_roots]; exact Polynomial.prod_X_sub_C_nextCoeff Z.eigenvalues
  rwa [Polynomial.nextCoeff_of_natDegree_pos (by omega), hnd] at hnext

/-- **The point-count bound, read off `P̃`.** `‖P̃.coeff 7‖ ≤ 2g·q^{1/2}`.

    The same Hasse–Weil bound as `norm_sum_eigenvalues_le`, now stated about the
    polynomial rather than the eigenvalue family — which is the form a reader
    holding only `P̃` can check. -/
theorem norm_charPoly_coeff_seven_le (Z : LocalQZetaFunction) [IsWeilZeta Z] :
    ‖Z.charPoly.coeff 7‖ ≤ 8 * Z.q ^ (1 / 2 : ℝ) := by
  rw [charPoly_coeff_seven Z, norm_neg]
  exact norm_sum_eigenvalues_le Z

/-! ## Hasse–Weil over every extension field

`norm_sum_eigenvalues_le` bounds the point count over `𝔽_q` alone. The theorem
the theory is named for bounds it over **every** finite extension: the Frobenius
of `𝔽_{q^r}` acts with eigenvalues `αᵢ^r`, so

  `| |ℬ(𝔽_{q^r})| − (q^r + 1) | ≤ 2g·q^{r/2}`.

That is one line from the magnitude bound, since `‖αᵢ^r‖ = ‖αᵢ‖^r`, and it is
worth having stated: the `r = 1` case alone is a weaker statement than the name
promises, and the growth rate in `r` is what makes the bound sharp enough to be
useful.

Note the **`r = 0` degeneracy**, which is why the exponent bound is stated for
all `r` rather than assuming `r ≥ 1`: at `r = 0` every `αᵢ^0 = 1`, the sum is
`8` and the bound reads `8 ≤ 8`. True, and tight, but carrying no arithmetic —
`𝔽_{q^0}` is not a field. The statement holds there vacuously rather than
meaningfully, and nothing downstream should read the `r = 0` instance as a
point count. -/

/-- The `r`-th power of a Frobenius eigenvalue has magnitude `q^{r/2}`.

    The eigenvalues of Frobenius on `𝔽_{q^r}` are the `r`-th powers of those on
    `𝔽_q`, so this is the Hasse–Weil magnitude at every level of the tower. -/
theorem norm_eigenvalue_pow (Z : LocalQZetaFunction) [IsWeilZeta Z]
    (i : Fin 8) (r : ℕ) :
    ‖Z.eigenvalues i ^ r‖ = (Z.q ^ (1 / 2 : ℝ)) ^ r := by
  rw [norm_pow, hasse_weil_bound Z]

/-- **Hasse–Weil over `𝔽_{q^r}`**: `|∑ αᵢ^r| ≤ 2g·q^{r/2}` with `2g = 8`.

    The point-count statement the theory is named for, at every level of the
    tower rather than only at `r = 1`. Combined with the Lefschetz trace formula
    `|ℬ(𝔽_{q^r})| = q^r + 1 − ∑ αᵢ^r` — which is not formalised here — this is
    `| |ℬ(𝔽_{q^r})| − (q^r + 1) | ≤ 2g·q^{r/2}`.

    See the section note on the `r = 0` degeneracy: the bound holds there but
    carries no arithmetic. -/
theorem norm_sum_eigenvalue_pow_le (Z : LocalQZetaFunction) [IsWeilZeta Z] (r : ℕ) :
    ‖∑ i : Fin 8, Z.eigenvalues i ^ r‖ ≤ 8 * (Z.q ^ (1 / 2 : ℝ)) ^ r := by
  calc ‖∑ i : Fin 8, Z.eigenvalues i ^ r‖
      ≤ ∑ i : Fin 8, ‖Z.eigenvalues i ^ r‖ := norm_sum_le _ _
    _ = 8 * (Z.q ^ (1 / 2 : ℝ)) ^ r := by
        simp only [norm_eigenvalue_pow Z _ r, Finset.sum_const, Finset.card_univ,
          Fintype.card_fin, nsmul_eq_mul]
        norm_num

/-- The power sums are **real**, at every level of the tower.

    `sum_eigenvalues_isReal` is the `r = 1` case. The general statement is what
    the trace formula needs: `|ℬ(𝔽_{q^r})|` is an integer, so a `∑ αᵢ^r` with a
    nonzero imaginary part would be an inconsistency rather than a bound. It
    follows from conjugation-closure, since `conj` commutes with powers and the
    conjugation permutation reindexes the sum. -/
theorem sum_eigenvalue_pow_isReal (Z : LocalQZetaFunction) [IsWeilZeta Z] (r : ℕ) :
    (starRingEnd ℂ) (∑ i : Fin 8, Z.eigenvalues i ^ r)
      = ∑ i : Fin 8, Z.eigenvalues i ^ r := by
  obtain ⟨σ, hσ⟩ := eigenvalues_conj_perm Z
  rw [map_sum]
  simp only [map_pow]
  rw [← Equiv.sum_comp σ (fun i => Z.eigenvalues i ^ r)]
  exact Finset.sum_congr rfl fun x _ => by rw [hσ x]

/-- **The extension bound is tight at every level**, not only at `r = 1`.

    On the supersingular witness (`q = 4`, all `αᵢ = 2`) the power sum is
    `8·2^r` and the bound is `8·(4^{1/2})^r = 8·2^r`. Equality for all `r`.

    Worth checking rather than assuming: a bound that is tight at `r = 1` could
    still be loose in the tower, and then the growth rate — which is the part of
    Hasse–Weil that does the work — would be unattested. It is not loose. -/
theorem norm_sum_eigenvalue_pow_tight (r : ℕ) :
    ‖∑ i : Fin 8, weilZetaExample.eigenvalues i ^ r‖
      = 8 * (weilZetaExample.q ^ (1 / 2 : ℝ)) ^ r := by
  have hq : weilZetaExample.q ^ (1 / 2 : ℝ) = 2 := by
    show (4 : ℝ) ^ (1 / 2 : ℝ) = 2
    rw [show (4 : ℝ) = 2 ^ (2 : ℕ) by norm_num, ← Real.rpow_natCast (2 : ℝ) 2,
      ← Real.rpow_mul (by norm_num)]
    norm_num
  rw [hq]
  simp [weilZetaExample]

end QOU.AlgebraicSubstrate
