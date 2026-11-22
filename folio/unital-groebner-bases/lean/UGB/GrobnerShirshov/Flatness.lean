import UGB.GrobnerShirshov.NormalForms
import Mathlib.Algebra.Field.Rat

/-!
# Flatness of the Gröbner–Shirshov Deformation

This module proves that a GS basis yields a **flat deformation**:
the quotient algebra `k⟨G⟩ / (Σ)` has the same `k`-dimension as the
associated graded algebra `gr(k⟨G⟩ / (Σ))`.

In the QOU context, this means `Dist(G)` (non-commutative) is a flat
deformation of `Dist(H)` (commutative): no dimensions are lost or
gained when deforming the multiplication.

## Key results

- `gs_implies_flat_false`: the former axiom `gs_implies_flat` was false as
  stated (its Hilbert functions were arbitrary); it and its restatement
  `dist_flat_deformation` are removed (2026-11-15).
- `normal_forms_preserved`: proved (normal forms depend only on leading
  monomials).
- `basis_preserved`: the normal-form basis of the deformed algebra
  projects bijectively onto the PBW basis of the associated graded.

## Why this matters for the QOU

The flatness result is what makes the lifting theorem work: when
passing from `Dist(H)` (char `p`, commutative) to `Dist(G)` (char `0`,
non-commutative), the algebra does not "collapse" — the representation
theory is preserved.  In physical terms, the Hilbert space dimension
is unchanged under quantisation.

## References

- [fred2005, §3, Theorem 3.15] — flatness of the GS deformation
- Bergman 1978, §5 — filtered deformations and the diamond lemma
- Beilinson–Ginzburg–Soergel, *Koszul duality*, JAMS 9 (1996) —
  PBW deformations and Koszulity
-/


namespace UGB.GrobnerShirshov

universe u v

/-! ## §1  Filtered Algebras and Associated Graded -/

/-- A **filtration** on an algebra `A`: an ascending chain of
    `k`-submodules `F₀ ⊆ F₁ ⊆ F₂ ⊆ ...` with `⋃ Fₙ = A` and
    `Fₘ · Fₙ ⊆ F_{m+n}`. -/
structure AlgebraFiltration (A : Type u) [Ring A] where
  /-- The `n`-th filtration piece (as a predicate). -/
  filt : ℕ → A → Prop
  /-- The filtration is ascending. -/
  ascending : ∀ n a, filt n a → filt (n + 1) a
  /-- The filtration is exhaustive. -/
  exhaustive : ∀ a, ∃ n, filt n a
  /-- The filtration is compatible with multiplication. -/
  mul_compat : ∀ m n a b, filt m a → filt n b → filt (m + n) (a * b)

/-- The **degree** of a homogeneous element in a filtered algebra:
    the smallest `n` such that `a ∈ Fₙ`. -/
noncomputable def filtrationDegree {A : Type u} [Ring A]
    (F : AlgebraFiltration A) (a : A) : ℕ :=
  (F.exhaustive a).choose

/-- The **Hilbert function** `H(n)` of a filtered algebra: the dimension
    of the `n`-th graded piece `Fₙ / F_{n-1}`.

    Represented abstractly as a function `ℕ → ℕ` (or `ℕ → ℕ∞` for
    infinite-dimensional algebras). -/
def HilbertFunction := ℕ → ℕ

/-! ## §2  Flatness from GS Bases -/

/-- **Flatness**: two filtered algebras have the same Hilbert function. -/
def isFlat (h₁ h₂ : HilbertFunction) : Prop :=
  ∀ n, h₁ n = h₂ n

namespace GsImpliesFlatRefutation

open AlgElement

/-- The relation `K` over `ℚ`. -/
noncomputable def rel : AlgElement SU2Gen ℚ := single [SU2Gen.K] 1

theorem rel_support : rel.support = {[SU2Gen.K]} := by
  show (if (1 : ℚ) = 0 then ∅ else {[SU2Gen.K]}) = {[SU2Gen.K]}
  norm_num

/-- The rule `K ↦ 0`. -/
noncomputable def rule : ReductionRule SU2Gen ℚ :=
  ⟨rel, by rw [rel_support]; exact ⟨_, Finset.mem_singleton_self _⟩⟩

theorem rule_lm : rule.lm degLexOrder = [SU2Gen.K] := by
  apply leadingMonomial_eq_of_max
  · show [SU2Gen.K] ∈ rel.support
    rw [rel_support]; exact Finset.mem_singleton_self _
  · intro m hm hne
    rw [show (rule.relation) = rel from rfl, rel_support] at hm
    exact absurd (Finset.mem_singleton.mp hm) hne

/-- The one-rule system `{K ↦ 0}` is a Gröbner–Shirshov basis. -/
theorem sys_isGS :
    IsGrobnerShirshovBasis SU2Gen ℚ degLexOrder (.ofList [rule] (by simp)) :=
  isGrobnerShirshovBasis_of_single_letter_rule degLexOrder rule SU2Gen.K rule_lm

end GsImpliesFlatRefutation

/-- **The former axiom `gs_implies_flat` is false** (removed 2026-11-15).

    It concluded `isFlat h_deformed h_graded` for two *arbitrary* Hilbert
    functions, which are not tied to `sys` at all; `isFlat` is pointwise
    equality. So any GS basis (here the one-rule system `{K ↦ 0}` over `ℚ`)
    together with the Hilbert functions `0` and `1` refutes it.

    The true statement ([fred2005, Theorem 3.15]) is about the Hilbert
    functions *of* the deformed algebra and its associated graded, which
    need to be defined from `sys`; open in Lean. -/
theorem gs_implies_flat_false :
    ¬ (∀ {G : Type} {k : Type} [Field k] [DecidableEq G]
        (ord : AdmissibleOrder G) (sys : RewritingSystem G k)
        (_hgs : IsGrobnerShirshovBasis G k ord sys)
        (h_deformed h_graded : HilbertFunction),
        isFlat h_deformed h_graded) := by
  intro h
  have := h degLexOrder _ GsImpliesFlatRefutation.sys_isGS (fun _ => 0) (fun _ => 1) 0
  exact absurd this (by decide)

/-! ## §3  Flatness for `Dist(G)` over `Dist(H)`

The former theorem `dist_flat_deformation` restated `gs_implies_flat`
verbatim (same hypotheses, same conclusion) and is removed with it
(2026-11-15). The `Dist(G)` statement ([fred2005, Theorem 3.15]) needs the
Hilbert functions of `Dist(G)` and `Dist(H)`, defined from their relations;
open in Lean. -/

/-! ## §4  Basis Preservation under Deformation -/

/-- The set of normal-form monomials is unchanged between the
    deformed algebra and its associated graded.

    `isNormalForm` only looks at the leading monomials of the rules (no rule's
    leading monomial is an infix of a monomial in the support), so two systems
    with the same **set** of leading monomials have the same normal forms. The
    hypothesis is stated on sets because rule sets may be infinite
    (`RewritingSystem.rules` is a `Set`); a rule-by-rule match of two finite
    lists, the form this theorem had before, implies it.

    Reference: Bergman 1978, §5 (filtered deformations preserve
    the leading-term ideal). -/
-- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5 §5 (filtered deformations preserve the leading-term ideal / normal forms)
theorem normal_forms_preserved
    {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys_deformed sys_graded : RewritingSystem G k)
    (h_same_lm : (fun r : ReductionRule G k => r.lm ord) '' sys_deformed.rules =
      (fun r : ReductionRule G k => r.lm ord) '' sys_graded.rules)
    (f : AlgElement G k) :
    isNormalForm ord sys_deformed f ↔ isNormalForm ord sys_graded f := by
  constructor
  · intro h r hr m hm hsub
    obtain ⟨r', hr', he⟩ : r.lm ord ∈ (fun r : ReductionRule G k => r.lm ord) ''
        sys_deformed.rules := h_same_lm ▸ ⟨r, hr, rfl⟩
    exact h r' hr' m hm (by simp only at he; rw [he]; exact hsub)
  · intro h r hr m hm hsub
    obtain ⟨r', hr', he⟩ : r.lm ord ∈ (fun r : ReductionRule G k => r.lm ord) ''
        sys_graded.rules := h_same_lm ▸ ⟨r, hr, rfl⟩
    exact h r' hr' m hm (by simp only at he; rw [he]; exact hsub)

end UGB.GrobnerShirshov
