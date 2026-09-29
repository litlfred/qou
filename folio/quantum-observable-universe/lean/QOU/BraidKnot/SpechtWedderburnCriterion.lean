import QOU.BraidKnot.SpechtActionInjective
import QOU.BraidKnot.SpechtStandardBasis

/-!
# QOU.BraidKnot.SpechtWedderburnCriterion — W1+W3 reduces to one number

Brick 5 of **W1+W3** of the Wedderburn epic (`qou-bxw4`), after #5189 (injectivity).

`SpechtActionInjective` proved `spechtProduct : k[S_n] →ₐ[k] ∏_{μ ⊢ n} End_k(S^μ)` injective,
hence `n! ≤ Σ_μ (dim S^μ)²`. Since both sides are finite-dimensional, that is all the *algebra*
needed: an injective linear map between spaces of equal dimension is onto. So

> **`spechtProduct` is an algebra isomorphism as soon as `Σ_μ (dim_k S^μ)² = n!`.**

and the whole of W1+W3 — the labelling, the block sizes, the division-ring collapse — is
already discharged by bricks 1–4c. What remains is a single numeric identity.

## What that buys: the residue is combinatorial, not representation-theoretic

`SpechtStandardBasis.specht_finrank_eq_numSYT` gives `dim_k S^μ = #SYT(μ)`, so the criterion
restates as

  `Σ_{μ ⊢ n} (#SYT μ)² = n!`,

which is the **RSK identity** — a bijection between permutations of `n` and pairs of standard
Young tableaux of the same shape. That is a statement about tableaux with no algebra in it, and
it may be attacked combinatorially (an explicit RSK correspondence) rather than through the
representation theory this epic has been climbing. Whoever closes it, in either direction, gets
the algebra isomorphism for free from `spechtEquiv_of_sum_sq` below.

Note that `OVTopAssembly.sum_numSYT_sq_eq_factorial` *states* this identity but carries
`sorryAx` (see `docs/audits/2026-08-07-ov-cone-axiom-audit-overclaim-correction.md`); nothing
here consumes it, and this file deliberately does not import that cone.

## Honest scope

The identity is **not proved here** — this file converts an open representation-theory problem
into an open combinatorics problem, which is progress of a specific and limited kind.
`sn_isotypic_specht_split` remains open, and the keystones inheriting `sorryAx` from it keep
their labels.

## Base ring (§7c)

`variable {k : Type} [Field k] [CharZero k]`. No `ℝ`.
-/

namespace QOU.BraidKnot.SpechtWedderburnCriterion

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtClassification
open QOU.BraidKnot.SpechtActionInjective
open Equiv (Perm)
open Module

variable {k : Type} [Field k] [CharZero k]

omit [CharZero k] in
/-- An injective linear map between finite-dimensional spaces of equal dimension is onto.

Mathlib has the endomorphism case but not this one at the pinned version (`exact?` fails on the
statement); it is two steps — injectivity preserves the rank, and a full-rank submodule is
everything. -/
theorem surjective_of_injective_of_finrank_eq {V W : Type*} [AddCommGroup V] [Module k V]
    [AddCommGroup W] [Module k W] [FiniteDimensional k W]
    (f : V →ₗ[k] W) (hinj : Function.Injective f)
    (hdim : finrank k V = finrank k W) : Function.Surjective f := by
  have hrange : finrank k (LinearMap.range f) = finrank k W := by
    rw [LinearMap.finrank_range_of_inj hinj, hdim]
  exact LinearMap.range_eq_top.mp (Submodule.eq_top_of_finrank_eq hrange)

/-- **The criterion.** `spechtProduct` is bijective as soon as the block dimensions sum to `n!`.

Everything else W1+W3 asks for is already in place: the map is partition-indexed by
construction (so there is no labelling to choose), each block is `End_k(S^μ)` with `dim S^μ` the
Specht dimension (so the sizes are right by construction), and the commutant is the base field
(W2, #5139) — the three items the `SnWedderburnPartitionBridge` residual lists. -/
theorem spechtProduct_bijective_of_sum_sq (n : ℕ)
    (h : ∑ i : PartitionIndex n, (finrank k (SpechtSubmodule (k := k) i.diagram)) ^ 2
      = Nat.factorial n) :
    Function.Bijective (spechtProduct (k := k) n) := by
  refine ⟨spechtProduct_injective (k := k) n, ?_⟩
  refine surjective_of_injective_of_finrank_eq (k := k)
    (V := MonoidAlgebra k (Perm (Fin n)))
    (W := ∀ i : PartitionIndex n, Module.End k (SpechtSubmodule (k := k) i.diagram))
    (spechtProduct (k := k) n).toLinearMap (spechtProduct_injective (k := k) n) ?_
  rw [SpechtBlockDimension.finrank_group_algebra (k := k) n,
    SpechtBlockDimension.finrank_specht_blocks (k := k) n, h]

/-- **The algebra isomorphism, conditional on the dimension count.**

`k[S_n] ≃ₐ[k] ∏_{μ ⊢ n} End_k(S^μ)`, partition-indexed, with block `μ` acting on `S^μ`. This is
the shape `sn_isotypic_specht_split` wants (modulo `End_k(S^μ) ≃ₐ Matrix (Fin (dim S^μ)) k`,
which is a basis choice). -/
noncomputable def spechtEquiv_of_sum_sq (n : ℕ)
    (h : ∑ i : PartitionIndex n, (finrank k (SpechtSubmodule (k := k) i.diagram)) ^ 2
      = Nat.factorial n) :
    MonoidAlgebra k (Perm (Fin n)) ≃ₐ[k]
      (∀ i : PartitionIndex n, Module.End k (SpechtSubmodule (k := k) i.diagram)) :=
  AlgEquiv.ofBijective (spechtProduct (k := k) n) (spechtProduct_bijective_of_sum_sq (k := k) n h)

/-- **The residue is combinatorial.** Restating the criterion's hypothesis through
`dim_k S^μ = #SYT(μ)`: the open input is the RSK identity `Σ_{μ ⊢ n} (#SYT μ)² = n!`, a statement
about tableaux with no algebra in it.

Anyone who proves the tableau identity — combinatorially or otherwise — gets the algebra
isomorphism from `spechtEquiv_of_sum_sq`. -/
theorem sum_sq_of_numSYT (n : ℕ)
    (h : ∑ i : PartitionIndex n, (numSYT i.diagram) ^ 2 = Nat.factorial n) :
    ∑ i : PartitionIndex n, (finrank k (SpechtSubmodule (k := k) i.diagram)) ^ 2
      = Nat.factorial n := by
  rw [← h]
  exact Finset.sum_congr rfl
    (fun i _ => by rw [SpechtStandardBasis.specht_finrank_eq_numSYT (k := k) i.diagram])

end QOU.BraidKnot.SpechtWedderburnCriterion
