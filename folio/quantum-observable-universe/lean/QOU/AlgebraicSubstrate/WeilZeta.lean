import QOU.AlgebraicSubstrate.LocalQZetaFunction
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Pow.NNReal
import Mathlib.Algebra.Polynomial.Roots

/-!
# QOU.AlgebraicSubstrate.WeilZeta

The two classical Weil inputs as a hypothesis class, and the Hasse–Weil
magnitude derived from them.

## Why this is a library module and not a content-block sibling

It was both, in `hasse-weil-bound.lean`, until the material below had a second
consumer. `cor:spectral-half-line` concludes `Re(ρᵢ) = 1/2` from the magnitude
`‖αᵢ‖ = q^{1/2}`, and took that magnitude as its own hypothesis — because
content-block siblings are outside the package globs (§0a) and cannot import one
another, so it had no way to reach `hasse_weil_bound` where the magnitude is
*derived*. The same hypothesis being assumed in one file and proved in the file
next to it is not a division of labour; it is a gap that happens to close by
coincidence of wording.

So the class and the four-step chain that ends at `hasse_weil_bound` live here,
importable by both. `hasse-weil-bound.lean` keeps everything downstream of the
magnitude — conjugation-closure, the characteristic-polynomial facts, Vieta —
which is the block's actual content.

## What is assumed and what is derived

Assumed, as the two fields of `IsWeilZeta`: the functional equation (as a
permutation) and Castelnuovo–Severi. Both are cited classical results, and
`weilZetaExample` witnesses that they are jointly satisfiable, so the class is
not an empty carrier.

Derived: that the two together force `‖αᵢ‖² = q` exactly rather than `≤` — the
step Weil's argument turns on, and the one piece of the Hasse–Weil argument the
corpus proves itself.

**Ground ring**: `ℝ` (geometric/analytic realisation) — real powers and norms.
-/

set_option autoImplicit false

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
    self-intersection of the correspondence, yielding
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

/-- Direct `[IsWeilZeta Z]` corollary (`qou-ahss`): every eigenvalue satisfies
    `‖Z.eigenvalues i‖ ^ 2 = Z.q` without passing separate `h_cs` / `h_fe` witnesses. -/
theorem eigenvalue_norm_sq_of_isWeilZeta
    (Z : LocalQZetaFunction) [IsWeilZeta Z] (i : Fin 8) :
    ‖Z.eigenvalues i‖ ^ 2 = Z.q :=
  eigenvalue_norm_sq Z i (castelnuovo_severi_bound Z i) (eigenvalue_functional_equation Z i)

/-- Under `[IsWeilZeta Z]` (`qou-ahss`), the product of the squared norms of any two
    eigenvalues equals `Z.q ^ 2`. -/
theorem eigenvalue_norm_sq_mul
    (Z : LocalQZetaFunction) [IsWeilZeta Z] (i j : Fin 8) :
    ‖Z.eigenvalues i * Z.eigenvalues j‖ ^ 2 = Z.q ^ 2 := by
  rw [norm_mul, mul_pow, eigenvalue_norm_sq_of_isWeilZeta Z i,
    eigenvalue_norm_sq_of_isWeilZeta Z j, sq]

/-- **Hasse–Weil bound**: every fundamental local-zeta eigenvalue αᵢ
    of Bring's curve satisfies |αᵢ| = q^{1/2}.

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

end QOU.AlgebraicSubstrate
