import QOU.BraidKnot.SpechtSchurDiagonal
import QOU.MathlibExt.RegularHom
import Mathlib.LinearAlgebra.FreeModule.Finite.Matrix

/-!
# QOU.BraidKnot.SpechtBlockDimension — the target side of the Wedderburn count

Fourth brick of **W1+W3** of the Wedderburn epic (`qou-bxw4`), after #5139 (W2), #5151
(Schur orthonormality) and #5156 (`Hom_G(k[G], V) ≃ V`).

The Wedderburn statement `sn_isotypic_specht_split` asserts an algebra isomorphism

  `k[S_n] ≃ₐ[k] ∏_{μ ⊢ n} Matrix (Fin (dim S^μ)) (Fin (dim S^μ)) k`.

Its **target** has `k`-dimension `Σ_μ (dim S^μ)²`, and its **source** has dimension `n!`. So
the identity `n! = Σ_μ (dim S^μ)²` — the RSK sum-of-squares, which `OVTopAssembly` currently
carries as a `sorryAx` — is a dimension count of that isomorphism.

This file computes the two dimensions and nothing else. It is pure linear algebra; no
representation theory enters, and it claims no isomorphism.

## What is *not* here

The isomorphism itself, and hence the identity. Establishing either needs the decomposition
of the regular module, which is the next brick. Recording the two sides separately keeps that
brick honest: a later `n! = Σ_μ (dim S^μ)²` must come from an actual map, not from these two
computations sitting next to each other.

## Base ring (§7c)

`variable {k : Type} [Field k] [CharZero k]` for the Specht layer; the `Fin`-indexed product
computation is over a generic field.
-/

namespace QOU.BraidKnot.SpechtBlockDimension

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtClassification
open Module

variable {k : Type} [Field k] [CharZero k]

omit [CharZero k] in
/-- `dim_k (∏_i End_k V_i) = Σ_i (dim_k V_i)²` for a finite family of finite free modules. -/
theorem finrank_pi_end {ι : Type} [Fintype ι] (V : ι → Type)
    [∀ i, AddCommGroup (V i)] [∀ i, Module k (V i)]
    [∀ i, Module.Free k (V i)] [∀ i, Module.Finite k (V i)] :
    finrank k (∀ i, Module.End k (V i)) = ∑ i, (finrank k (V i)) ^ 2 := by
  classical
  rw [finrank_pi_fintype k]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [finrank_linearMap, sq]

omit [CharZero k] in
/-- **The target side.** The Wedderburn target `∏_{μ ⊢ n} End_k (S^μ)` has `k`-dimension
`Σ_μ (dim_k S^μ)²`.

This is the right-hand side of the RSK sum-of-squares. It is a statement about the *target*
of the conjectured isomorphism, not about `k[S_n]`. -/
theorem finrank_specht_blocks (n : ℕ) :
    finrank k (∀ i : PartitionIndex n, Module.End k (SpechtSubmodule (k := k) i.diagram))
      = ∑ i : PartitionIndex n, (finrank k (SpechtSubmodule (k := k) i.diagram)) ^ 2 :=
  finrank_pi_end (k := k) _

omit [CharZero k] in
/-- **The source side.** `dim_k k[S_n] = n!`.

`MonoidAlgebra k G` is `G →₀ k`, free on `G`, so its dimension is `|G| = n!`. -/
theorem finrank_group_algebra (n : ℕ) :
    finrank k (MonoidAlgebra k (Equiv.Perm (Fin n))) = Nat.factorial n := by
  classical
  have hcard : Fintype.card (Equiv.Perm (Fin n)) = Nat.factorial n := by
    rw [Fintype.card_perm, Fintype.card_fin]
  -- rewrite the ℕ on the right; rewriting the carrier type on the left is not motive-correct
  -- (`MonoidAlgebra`'s `AddCommMonoid` instance does not transport through the equation).
  rw [show Nat.factorial n = Fintype.card (Equiv.Perm (Fin n)) from hcard.symm]
  exact Module.finrank_finsupp_self (R := k) (ι := Equiv.Perm (Fin n))

omit [CharZero k] in
/-- Zero-subtracted difference between `dim_k k[S_n]` and `n!` vanishes. -/
theorem finrank_group_algebra_sub_factorial_eq_zero (n : ℕ) :
    finrank k (MonoidAlgebra k (Equiv.Perm (Fin n))) - Nat.factorial n = 0 := by
  rw [finrank_group_algebra (k := k) n]
  exact Nat.sub_self (Nat.factorial n)

end QOU.BraidKnot.SpechtBlockDimension
