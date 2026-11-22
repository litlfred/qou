import Mathlib.Tactic
import QOU.MassTheory.OrbitCount
import QOU.MassTheory.AtomWordShadow

/-!
# The orbit quotient, and the `q = 1` Schur–Weyl trace as a count

Bean `qou-uinl`. Builds on `qou-qro1` (`OrbitCount.lean`) and `qou-tjys`
(`AtomWordShadow.lean`, for `not_sameCycle_of_apply_eq`).

## What this is for

`ClassicalTraceFloor` states its **step 1** as the two hypotheses `hSWfree` /
`hSWatom`, namely `tr_M(β)|_{q=1} = 2^{c(σ_β) − n}`, and says plainly that it is
"NOT formal here" because Mathlib has no Schur–Weyl duality. That is correct and
still true — bean `qou-mpq5` measured it (a grep finds only `SchurZassenhaus`,
Schur's *lemma*, and `Matrix.SchurComplement`) and scoped the **q-deformed**
double-centralizer as a multi-week gap it deliberately refused to fake.

🛑 **This file does not close that gap.** What it closes is the *combinatorial core*
of the `q = 1` case, which is much smaller and self-contained:

> the character of `σ` permuting the factors of `V^{⊗n}` is `(dim V)^{c(σ)}`,
> because `σ` fixes exactly the basis vectors constant on each cycle.

In the monomial basis that character **is** a count of invariant functions, and this
file proves that count: `orbitCount_invariant_functions` gives

    #{f : α → β // ∀ x, f (σ x) = f x}  =  (card β) ^ orbitCount σ

which at `card β = 2` is the `2^{c(σ)}` step 1 needs. What remains between here and
`hSWfree`/`hSWatom` is the **linear-algebra wrapper** — identifying this count with a
trace over an actual tensor power — and, for `q ≠ 1`, the whole of quantum
Schur–Weyl. Neither is here, and neither is claimed.

## What Mathlib is missing, measured

Mathlib has `Equiv.Perm.SameCycle.setoid`, but **nothing** relating the resulting
orbit quotient to `cycleType`, no count of invariant functions, and no permutation
character. `Fintype.card_quotient_le` is the only quotient-counting lemma in range,
and an inequality is not what is needed. So the bridge

    Fintype.card (Quotient (SameCycle.setoid σ)) = orbitCount σ

is built here from an explicit equivalence: **every orbit is either a fixed point or
one of the cycle factors** — which is exactly the split `orbitCount` is defined by,
so the bridge is what makes `orbitCount` a genuine count of orbits rather than a
`cycleType` bookkeeping device.

-- Ref: [leitner2026] bean qou-uinl; the permutation character on a tensor power is
-- classical, and the `d^{c(σ)}` form is standard in any treatment of Schur–Weyl.
-/

namespace QOU.MassTheory

open Equiv Equiv.Perm Finset

variable {α : Type*} [Fintype α] [DecidableEq α]

noncomputable instance fintypeQuotientSameCycle (σ : Perm α) :
    Fintype (Quotient (SameCycle.setoid σ)) := by
  classical
  exact Fintype.ofSurjective (Quotient.mk _) Quotient.mk_surjective

/-- A point of a cycle factor's support. Choice is genuine: a cycle factor is a
cycle, hence has nonempty support, but nothing picks a point for us. -/
noncomputable def cyclePoint {σ : Perm α}
    (c : {c : Perm α // c ∈ σ.cycleFactorsFinset}) : α :=
  (mem_cycleFactorsFinset_iff.mp c.2).1.nonempty_support.choose

theorem cyclePoint_mem {σ : Perm α} (c : {c : Perm α // c ∈ σ.cycleFactorsFinset}) :
    cyclePoint c ∈ (c : Perm α).support :=
  (mem_cycleFactorsFinset_iff.mp c.2).1.nonempty_support.choose_spec

/-- A cycle factor's chosen point is moved by `σ` itself, not merely by the factor. -/
theorem apply_cyclePoint_ne {σ : Perm α} (c : {c : Perm α // c ∈ σ.cycleFactorsFinset}) :
    σ (cyclePoint c) ≠ cyclePoint c :=
  mem_support.mp (mem_cycleFactorsFinset_support_le c.2 (cyclePoint_mem c))

/-- **Every orbit is either a fixed point or a cycle factor.** -/
noncomputable def quotientSameCycleEquiv (σ : Perm α) :
    Quotient (SameCycle.setoid σ) ≃
      {x : α // σ x = x} ⊕ {c : Perm α // c ∈ σ.cycleFactorsFinset} where
  toFun := Quotient.lift
    (fun x => if h : σ x = x then Sum.inl ⟨x, h⟩
      else Sum.inr ⟨σ.cycleOf x, cycleOf_mem_cycleFactorsFinset_iff.mpr (mem_support.mpr h)⟩)
    (by
      intro x y hxy
      have hsc : σ.SameCycle x y := hxy
      by_cases hx : σ x = x
      · have hyx : y = x := by
          by_contra hne
          exact not_sameCycle_of_apply_eq hx hne hsc.symm
        subst hyx; rfl
      · have hy : σ y ≠ y := by
          intro hy
          exact hx (by
            have : x = y := by
              by_contra hne
              exact not_sameCycle_of_apply_eq hy hne hsc
            rw [this]; exact hy)
        show dite _ _ _ = dite _ _ _
        rw [dif_neg hx, dif_neg hy]
        exact congrArg Sum.inr (Subtype.ext hsc.cycleOf_eq))
  invFun := Sum.elim (fun x => ⟦(x : α)⟧) (fun c => ⟦cyclePoint c⟧)
  left_inv := by
    refine Quotient.ind fun x => ?_
    by_cases hx : σ x = x
    · show Sum.elim _ _ (dite _ _ _) = _
      rw [dif_pos hx]; rfl
    · show Sum.elim _ _ (dite _ _ _) = _
      rw [dif_neg hx]
      refine Quotient.sound ?_
      have hmem := cyclePoint_mem
        (σ := σ) ⟨σ.cycleOf x, cycleOf_mem_cycleFactorsFinset_iff.mpr (mem_support.mpr hx)⟩
      exact ((mem_support_cycleOf_iff.mp hmem).1).symm
  right_inv := by
    rintro (⟨x, hx⟩ | ⟨c, hc⟩)
    · show dite _ _ _ = _
      rw [dif_pos hx]
    · have hne := apply_cyclePoint_ne (σ := σ) ⟨c, hc⟩
      show dite _ _ _ = _
      rw [dif_neg hne]
      exact congrArg Sum.inr (Subtype.ext
        (cycle_is_cycleOf (cyclePoint_mem (σ := σ) ⟨c, hc⟩) hc).symm)

/-- **The bridge.** The number of orbits of `σ` — genuinely, as the cardinality of the
`SameCycle` quotient — is `orbitCount σ`.

Mathlib has the setoid but nothing connecting it to `cycleType`; this is that
connection, and it is what makes `orbitCount` a count of orbits rather than a
`cycleType` bookkeeping device. -/
theorem card_quotient_sameCycle (σ : Perm α) :
    Fintype.card (Quotient (SameCycle.setoid σ)) = orbitCount σ := by
  classical
  rw [Fintype.card_congr (quotientSameCycleEquiv σ), Fintype.card_sum]
  have hfix : Fintype.card {x : α // σ x = x} = Fintype.card α - #σ.support := by
    rw [Fintype.card_subtype]
    have hc : (univ.filter fun x => σ x = x) = σ.supportᶜ := by
      ext y; simp [mem_support]
    rw [hc, card_compl]
  have hcyc : Fintype.card {c : Perm α // c ∈ σ.cycleFactorsFinset}
      = Multiset.card σ.cycleType := by
    rw [Fintype.card_coe, cycleType, Multiset.card_map]
    rfl
  have hle : #σ.support ≤ Fintype.card α :=
    (card_le_univ _).trans_eq Finset.card_univ
  have hle2 := card_cycleType_le_card_support σ
  rw [hfix, hcyc, orbitCount, orbitDefect]
  omega

omit [Fintype α] [DecidableEq α] in
/-- Invariance under `σ` propagates to every natural power. -/
theorem apply_pow_eq_of_invariant {β : Type*} {σ : Perm α} {f : α → β}
    (hf : ∀ x, f (σ x) = f x) : ∀ (n : ℕ) (x : α), f ((σ ^ n) x) = f x
  | 0, x => by simp
  | n + 1, x => by
      rw [pow_succ, Perm.mul_apply, apply_pow_eq_of_invariant hf n (σ x), hf]

omit [DecidableEq α] in
/-- An invariant function is constant on each orbit. Routed through
`SameCycle.exists_pow_eq'`, which supplies a **natural** power, so no `ℤ` induction is
needed. -/
theorem eq_of_sameCycle_of_invariant {β : Type*} {σ : Perm α} {f : α → β}
    (hf : ∀ x, f (σ x) = f x) {x y : α} (h : σ.SameCycle x y) : f x = f y := by
  obtain ⟨i, _, hi⟩ := h.exists_pow_eq'
  rw [← hi, apply_pow_eq_of_invariant hf]

/-- **The `q = 1` Schur–Weyl trace, as a count.** A function `α → β` is invariant
under precomposition with `σ` exactly when it is constant on each orbit, so there are
`(card β) ^ orbitCount σ` of them.

With `card β = 2` this is the `2^{c(σ)}` that `ClassicalTraceFloor`'s step 1 assumes:
`σ` permuting the factors of `(ℂ²)^{⊗n}` fixes exactly the basis vectors constant on
each cycle. 🛑 Identifying this count with a trace over an actual tensor power is a
further step and is **not** in this file. -/
theorem orbitCount_invariant_functions (σ : Perm α) (β : Type*) [Fintype β] [DecidableEq β] :
    Fintype.card {f : α → β // ∀ x, f (σ x) = f x} = Fintype.card β ^ orbitCount σ := by
  classical
  have e : {f : α → β // ∀ x, f (σ x) = f x} ≃ (Quotient (SameCycle.setoid σ) → β) :=
    { toFun := fun f => Quotient.lift f.1 (fun _ _ h => eq_of_sameCycle_of_invariant f.2 h)
      invFun := fun g => ⟨fun x => g ⟦x⟧, fun x =>
        congrArg g (Quotient.sound ⟨-1, by simp⟩)⟩
      left_inv := fun _ => rfl
      right_inv := fun g => funext (Quotient.ind fun _ => rfl) }
  rw [Fintype.card_congr e, Fintype.card_fun, card_quotient_sameCycle]

/-! ### Smoke tests

Two endpoints where the answer is known independently, so a direction or off-by-one
error in the count fails the build rather than sitting unnoticed. -/

/-- At `σ = 1` every function is invariant, and there are `|β|^|α|` of them. -/
example (β : Type*) [Fintype β] [DecidableEq β] :
    Fintype.card {f : α → β // ∀ x, f ((1 : Perm α) x) = f x}
      = Fintype.card β ^ Fintype.card α := by
  rw [orbitCount_invariant_functions, orbitCount_one]

/-- At a transposition, one orbit is lost: the two swapped points must agree, so the
count drops by exactly one factor of `|β|`. -/
example (β : Type*) [Fintype β] [DecidableEq β] {a b : α} (h : a ≠ b) :
    Fintype.card {f : α → β // ∀ x, f (swap a b x) = f x}
      = Fintype.card β ^ (Fintype.card α - 1) := by
  rw [orbitCount_invariant_functions, orbitCount, orbitDefect_swap h]

end QOU.MassTheory
