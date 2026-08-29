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
  /-- Functional-equation pairing: `αᵢ ↦ q/αᵢ` permutes the eigenvalues. -/
  functional_equation :
    ∀ i : Fin 8, ∃ j : Fin 8, Z.eigenvalues j = ↑Z.q / Z.eigenvalues i
  /-- Castelnuovo–Severi: `|αᵢ|² ≤ q`. -/
  castelnuovo_severi : ∀ i : Fin 8, ‖Z.eigenvalues i‖ ^ 2 ≤ Z.q

/-- The functional equation of the local zeta function constrains
    eigenvalue norms: if αᵢ is an eigenvalue, so is q/αᵢ.
    This pairs eigenvalues such that |αᵢ| · |q/αᵢ| = q. -/
theorem eigenvalue_functional_equation
    (Z : LocalQZetaFunction) [IsWeilZeta Z] (i : Fin 8) :
    ∃ (j : Fin 8), Z.eigenvalues j = ↑Z.q / Z.eigenvalues i :=
  IsWeilZeta.functional_equation i

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
  functional_equation := by
    intro i; exact ⟨i, by simp [weilZetaExample]; norm_num⟩
  castelnuovo_severi := by
    intro i; simp [weilZetaExample]; norm_num

end QOU.AlgebraicSubstrate
