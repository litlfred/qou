import Mathlib.Combinatorics.Enumerative.Composition
import Mathlib.GroupTheory.GroupAction.Basic
import Mathlib.GroupTheory.Perm.Basic

/-!
# Young subgroups of a *composition*, and the conjugacy Mathas' Lemma 3.9 opens with

Mathas' Lemma 3.9 is the foundation of the Murphy-basis spanning argument
(3.9 → 3.12 → 3.13 → 3.14 → 3.20; see
[`2026-09-04-mathas-murphy-chain-status.md`](../../../../../docs/audits/2026-09-04-mathas-murphy-chain-status.md)).
It is stated for a **composition** `μ` — parts not weakly decreasing — and its proof
opens:

> *"Choose an element `d ∈ S_n` such that `S_ν = d S_μ d⁻¹` and such that `t^μ d` and
> `t^ν d⁻¹` are both row standard."*

The corpus's Young subgroup (`Specht.rowStab`) is indexed by a `YoungDiagram`, so it
cannot express `S_μ` for a composition. This file supplies that, and reduces the
conjugacy to two facts neither of which needed writing.

## The two free facts

* **Mathlib's `Composition.index : Fin n → Fin c.length`** already *is* the block
  function — "which part does this label fall in" — so a composition's Young subgroup
  is the stabiliser of it, with nothing to construct.
* **Mathlib's `MulAction.stabilizer_smul_eq_stabilizer_map_conj`** already *is* the
  conjugacy: `stabilizer (g • a) = map (conj g) (stabilizer a)`.

What is left is the interface between them, which is `youngOfComp_conj` below: the
conjugating `d` has to carry one block function onto the other **up to relabelling
the blocks**, and relabelling is invisible to a stabiliser (`stabilizer_comp_left`).

## Note on the action instance

`QOU.BraidKnot.Specht.instArrowMulAction` declares the same `σ • f = f ∘ σ⁻¹` action,
but **specialised** to `Fin (nOf μ) → ℕ` and indexed by a `YoungDiagram`, so it does
not apply here. The instance below is the general one. They should eventually be
unified — the specialised one is the odd case — but that is a refactor of
`Specht.lean` and is deliberately not done here; **this file does not import
`Specht.lean`**, so the two never meet and no instance diamond arises.
-/

namespace QOU.BraidKnot.CompositionYoung

open Equiv

variable {n : ℕ}

/-- The permutation action on labelled data, `σ • f = f ∘ σ⁻¹`, for an arbitrary
label type.  Its stabilisers are the Young subgroups. -/
instance arrowMulAction (n : ℕ) (ι : Type*) : MulAction (Perm (Fin n)) (Fin n → ι) where
  smul σ f := fun l => f (σ.symm l)
  one_smul f := by funext l; rfl
  mul_smul σ τ f := by
    funext l
    show f ((σ * τ).symm l) = f (τ.symm (σ.symm l))
    rw [Equiv.Perm.mul_def, Equiv.symm_trans_apply]

theorem smul_arrow_apply {ι : Type*} (σ : Perm (Fin n)) (f : Fin n → ι) (l : Fin n) :
    (σ • f) l = f (σ.symm l) := rfl

/-- **The Young subgroup of a composition**: the permutations preserving each part
setwise.

Stated as the stabiliser of `Composition.index`, which is Mathlib's "which part does
this label fall in" map — so this is a definition with no construction in it. -/
def youngOfComp (c : Composition n) : Subgroup (Perm (Fin n)) :=
  MulAction.stabilizer (Perm (Fin n)) c.index

theorem mem_youngOfComp {c : Composition n} {σ : Perm (Fin n)} :
    σ ∈ youngOfComp c ↔ ∀ l, c.index (σ.symm l) = c.index l := by
  simp only [youngOfComp, MulAction.mem_stabilizer_iff, funext_iff, smul_arrow_apply]

/-- **Relabelling the blocks is invisible to the stabiliser.**

Two compositions of the same `n` have different `length`s in general, so the
conjugating `d` of Lemma 3.9 can only match block functions up to a renaming of the
block indices.  An injective renaming changes nothing. -/
theorem stabilizer_comp_left {ι κ : Type*} {π : ι → κ} (hπ : Function.Injective π)
    (f : Fin n → ι) :
    MulAction.stabilizer (Perm (Fin n)) (π ∘ f)
      = MulAction.stabilizer (Perm (Fin n)) f := by
  ext σ
  simp only [MulAction.mem_stabilizer_iff]
  constructor
  · intro h
    funext l
    have := congrFun h l
    simp only [smul_arrow_apply, Function.comp_apply] at this ⊢
    exact hπ this
  · intro h
    funext l
    have := congrFun h l
    simp only [smul_arrow_apply, Function.comp_apply] at this ⊢
    exact congrArg π this

/-- **The conjugacy criterion of Lemma 3.9.**

If `d` carries `c`'s block function onto `c'`'s, up to an injective renaming of the
blocks, then the two Young subgroups are conjugate by `d`.

This is the whole of *"choose `d` such that `S_ν = d S_μ d⁻¹`"* — given the `d`.
Producing the `d` (the permutation that sorts the parts into decreasing order) is a
separate step and is **not** done here. -/
theorem youngOfComp_conj {c c' : Composition n} (d : Perm (Fin n))
    {π : Fin c'.length → Fin c.length} (hπ : Function.Injective π)
    (h : d • c.index = π ∘ c'.index) :
    youngOfComp c' = (youngOfComp c).map (MulAut.conj d).toMonoidHom := by
  have hstab := MulAction.stabilizer_smul_eq_stabilizer_map_conj d c.index
  rw [h, stabilizer_comp_left hπ] at hstab
  exact hstab

/-! ## Non-vacuity

`youngOfComp_conj` has three hypotheses; a criterion nothing satisfies proves
nothing.  The identity instance below shows they are simultaneously satisfiable and
that the conclusion is the expected one — a genuine two-block worked case would be
stronger, and needs the sorting `d` that the next step supplies. -/

theorem youngOfComp_conj_one (c : Composition n) :
    youngOfComp c = (youngOfComp c).map (MulAut.conj (1 : Perm (Fin n))).toMonoidHom :=
  youngOfComp_conj (c := c) (c' := c) 1 (π := id) Function.injective_id (one_smul _ _)

end QOU.BraidKnot.CompositionYoung
