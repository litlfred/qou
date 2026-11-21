import Mathlib.Algebra.Lie.Classical
import Mathlib.Algebra.Lie.Abelian

/-!
# QOU.QuantumObservableUniverse.exists_axiom_2_observability

**Canonical declaration** for content block
[`lem:qou-exists-axiom-2`](../../../quantum-observable-universe/quantum-observable-universes/qou-exists-axiom-2.md):
the adjoint representation of `𝔰𝔩₂` has no invariant vectors, i.e.
`Hom(𝟙, V₁) = 0` for the spin-1 adjoint module `V₁`.
-/

namespace QOU.QuantumObservableUniverse

open LieAlgebra.SpecialLinear

/-- **Lemma.** Over a field `K` with `2 ≠ 0`, the adjoint module of
`𝔰𝔩₂(K)` has trivial invariant submodule:
`LieModule.maxTrivSubmodule K 𝔰𝔩₂ 𝔰𝔩₂ = ⊥`.

`maxTrivSubmodule` is the submodule of `x` with `⁅y, x⁆ = 0` for every `y`,
which is the image of `Hom(𝟙, Ad)` (a module map from the trivial module is
determined by the image of `1`, an invariant vector). So the statement is
`Hom(𝟙, V₁) = 0` for the adjoint (spin-1) module `V₁`.

The hypothesis `2 ≠ 0` is needed: in characteristic 2 the identity matrix
is traceless and central, so it is a nonzero invariant.

Scope. This is the Lie-algebra (`q = 1`) statement. The `U_q(𝔰𝔩₂)` statement
at generic `q` follows because the type-1 modules there are classified by
the same highest weights and `V₁` stays simple; that step is cited, not
formalised [kassel1995, Ch. VII]. Until 2026-11-21 this file stated the
claim over a class of free natural numbers (`hom_dim = total_hom_dim - 1`),
which did not encode the representation (round-trip audit pass 2, C06; QA
on #8888). -/
theorem exists_axiom_2_observability {K : Type*} [Field K] (h2 : (2 : K) ≠ 0) :
    LieModule.maxTrivSubmodule K (sl (Fin 2) K) (sl (Fin 2) K) = ⊥ := by
  ext x
  simp only [LieSubmodule.mem_bot, LieModule.mem_maxTrivSubmodule]
  constructor
  · intro hx
    -- test `x` against the raising and lowering elements `E₀₁`, `E₁₀`
    have e01 := congrArg Subtype.val (hx (single (0 : Fin 2) 1 (by decide) (1 : K)))
    have e10 := congrArg Subtype.val (hx (single (1 : Fin 2) 0 (by decide) (1 : K)))
    have ht : Matrix.trace (x : Matrix (Fin 2) (Fin 2) K) = 0 := x.2
    simp only [LieSubalgebra.coe_bracket, val_single, Ring.lie_def,
      ZeroMemClass.coe_zero] at e01 e10
    have a := congrFun (congrFun e01 0) 0
    have b := congrFun (congrFun e01 0) 1
    have c := congrFun (congrFun e10 1) 1
    simp [Matrix.mul_apply, Matrix.single, Matrix.of_apply] at a b c
    simp [Matrix.trace, Fin.sum_univ_two] at ht
    apply Subtype.ext
    ext i j
    fin_cases i <;> fin_cases j <;> simp
    · have h : (2 : K) * (x : Matrix (Fin 2) (Fin 2) K) 0 0 = 0 := by
        linear_combination ht - b
      exact (mul_eq_zero.mp h).resolve_left h2
    · exact c
    · exact a
    · have h : (2 : K) * (x : Matrix (Fin 2) (Fin 2) K) 1 1 = 0 := by
        linear_combination ht + b
      exact (mul_eq_zero.mp h).resolve_left h2
  · rintro rfl y
    simp

end QOU.QuantumObservableUniverse
