import QOU.Hecke.TwMul

/-!
# QOU.BraidKnot.HeckeMurphy — the Murphy element `x_J`, and its `q`-eigenvector property

Murphy's basis of `H_n(q)` is `m_{st} = T_{d(s)}^* · x_λ · T_{d(t)}`, where
`x_λ = Σ_{w ∈ S_λ} T_w` is the sum over the Young subgroup of the partition `λ`.
Everything else in that construction is conjugation by coset representatives; the
**defining property** of `x_λ`, and the only thing about it that is not bookkeeping, is
that it is a **`q`-eigenvector** for every generator of that subgroup:

    σ_i · x_λ = q · x_λ      for every `s_i ∈ S_λ`.

This file proves exactly that, for an arbitrary finite set of permutations closed under
right multiplication by `s_i` — which is weaker than being a Young subgroup, and is all
the eigenvector property actually needs.

## The proof, and why it needs no case analysis at the level of the sum

The multiplication rule (`QOU.Hecke.TwBasis.σ_mul_Tw`) has two branches, on whether `w`
ascends or descends at `i`. Summing over `S` and splitting into ascents and descents
would need a bijection between the two halves.

That work is avoidable. The two branches are **exactly complementary on a pair**
`{w, w s_i}`: whichever of the two ascends, the other descends, and the coefficients
recombine identically either way — so

    σ_i · (T_w + T_{w s_i}) = q · (T_w + T_{w s_i})

holds **unconditionally** (`σ_mul_Tw_pair`). Restated as `f w + f (w s_i) = 0` for
`f w = σ_i T_w − q T_w`, that is precisely the hypothesis of `Finset.sum_involution`,
with `w ↦ w s_i` the involution. So the sum vanishes with no partition of `S`, and — the
point worth having — **no hypothesis on the characteristic**. The tempting one-line route
(sum the pair identity over all of `S` to get `2σx = 2qx`) does need `2` invertible; this
one does not.

## Scope

This is the eigenvector property, not the Murphy basis. Still open, and deliberately not
claimed here: that the `m_{st}` are a **basis**, and the cellular axioms (C1) and (C3) that
the basis makes statable.

> **Correction (2026-08-30, same day).** This paragraph first read *"Those need
> standard-tableau combinatorics and the dominance order, **neither of which is in the
> corpus**."* That is **false in both halves**, and it was written without running the
> corpus-grep checklist on the claim itself. What is actually there:
>
> * **Standard Young tableaux** — `StandardYoungTableau (μ : YoungDiagram)` exists twice
>   (`QOU/BraidKnot/`, `QOU/Mathlib/`) with a `Finite` instance, `numSYT`, `hookLength`,
>   `hookProduct`, and roughly seventy supporting files (`SYTEnumeration`, `SYTHookFormula*`,
>   the Schensted group, `SYTBranching*`). Note Mathlib itself has `YoungDiagram` and
>   `SemistandardTableau` but **no** `StandardYoungTableau`, so this is all local.
> * **The dominance order** — `partitionDom` at `QOU/BraidKnot/SpechtClassification.lean`,
>   with `partitionDom_refl` and `partitionDom_antisymm` proved, plus `domRel` on tabloids in
>   `SpechtDominanceCore` and the classification direction `dom_of_intertwiner`.
> * **A reference tableau `t^λ`** — `colSuperstandard (μ) : Specht.Tableau μ` and
>   `colSuperstandardSYT`, which is exactly the `t^λ` that `d(t)` is defined against.
>
> **What is genuinely missing is the `q`-deformation, and that is a different statement.**
> The whole 21-file Specht cluster is the **`q = 1` symmetric-group** theory — it works over
> `Representation k (Perm (Fin n))`, and no file in it imports the Hecke algebra. Murphy's
> basis is the `q`-analogue of that story over `H_n(q)`, and *that* is what does not exist.
>
> **Nor is the cluster a finished foundation to build on:** it carries **310 `sorry`s**
> across those 21 files, concentrated in `SpechtStandardBasisCore` (107), `SpechtIrreducible`
> (57) and `SpechtDominanceCore` (51). So the combinatorial inputs exist as *definitions and
> partial theory*, not as a settled base.
>
> The cost of the original wording, had it stood: it tells the next agent to rebuild seventy
> files that are already here. Recorded rather than silently patched, because the failure was
> not the fact but the method — a "the corpus does not have X" claim shipped without the
> six-path check that exists precisely to catch it.

Bean `qou-phir`.

Ground ring: `[Field K]`, inherited from `QOU.Hecke.TwMul` — the `T_w` basis is a field
statement (`QOU/Hecke/TwBasisField.lean`). Nothing here needs more than that.
-/

namespace QOU.BraidKnot.HeckeMurphy

open QOU.Hecke.TwBasis
open QOU.Hecke.IwahoriHecke (σ)

variable (K : Type*) [Field K] (q : K) (n : ℕ)

/-- The adjacent transposition `s_i`, as a permutation of `Fin (n+1)`.

`n` is bound implicitly *here* rather than taken from the `variable` block above: that block
declares `n` explicit, which would make this `sw (n) (i)` and silently elaborate `sw i` as
`sw (n := i)` — `i` read as the rank. -/
abbrev sw {n : ℕ} (i : Fin n) : Equiv.Perm (Fin (n + 1)) := Equiv.swap i.castSucc i.succ

variable {K q n}

theorem sw_ne_one (i : Fin n) : sw i ≠ (1 : Equiv.Perm (Fin (n + 1))) := by
  intro h
  have hne : i.castSucc ≠ i.succ := (Fin.castSucc_lt_succ i).ne
  have := congrArg (fun f => f i.castSucc) h
  simp only [sw, Equiv.swap_apply_left, Equiv.Perm.coe_one, id_eq] at this
  exact hne this.symm

theorem mul_sw_ne (v : Equiv.Perm (Fin (n + 1))) (i : Fin n) : v * sw i ≠ v := by
  intro h
  refine sw_ne_one i (mul_left_cancel (a := v) ?_)
  rw [mul_one]
  exact h

theorem mul_sw_sw (v : Equiv.Perm (Fin (n + 1))) (i : Fin n) : v * sw i * sw i = v := by
  rw [mul_assoc, sw, Equiv.swap_mul_self, mul_one]

theorem mul_sw_castSucc (v : Equiv.Perm (Fin (n + 1))) (i : Fin n) :
    (v * sw i) i.castSucc = v i.succ := by
  rw [Equiv.Perm.mul_apply]
  simp [sw]

theorem mul_sw_succ (v : Equiv.Perm (Fin (n + 1))) (i : Fin n) :
    (v * sw i) i.succ = v i.castSucc := by
  rw [Equiv.Perm.mul_apply]
  simp [sw]

variable (K q n)

/-- **The pair identity — the whole content of this file.**  `T_w + T_{w s_i}` is a
`q`-eigenvector of `σ_i`, for **every** `w`, with no ascent/descent hypothesis.

Whichever of `w`, `w s_i` ascends at `i`, the other descends, and the two branches of the
multiplication rule recombine to the same thing: the ascending one contributes its partner
with coefficient `1`, the descending one contributes `(q-1)` of itself and `q` of its
partner, and `1 + (q-1) = q`. -/
theorem σ_mul_Tw_pair (i : Fin n) (v : Equiv.Perm (Fin (n + 1))) :
    σ K q n i * (Tw K q n v + Tw K q n (v * sw i))
      = q • (Tw K q n v + Tw K q n (v * sw i)) := by
  have hback : v * sw i * sw i = v := mul_sw_sw v i
  by_cases h : v i.castSucc < v i.succ
  · -- `v` ascends, so `v s_i` descends.
    have hdown : ¬ (v * sw i) i.castSucc < (v * sw i) i.succ := by
      rw [mul_sw_castSucc, mul_sw_succ]; exact not_lt.mpr h.le
    rw [mul_add, σ_mul_Tw_of_lt K q n i v h, σ_mul_Tw_of_not_lt K q n i _ hdown, hback]
    module
  · -- `v` descends, so `v s_i` ascends — strictly, because `v` is injective.
    have hne : v i.castSucc ≠ v i.succ := fun hv =>
      (Fin.castSucc_lt_succ i).ne (v.injective hv)
    have hup : (v * sw i) i.castSucc < (v * sw i) i.succ := by
      rw [mul_sw_castSucc, mul_sw_succ]
      exact lt_of_le_of_ne (not_lt.mp h) (Ne.symm hne)
    rw [mul_add, σ_mul_Tw_of_not_lt K q n i v h, σ_mul_Tw_of_lt K q n i _ hup, hback]
    module

/-- **The Murphy element of a set of permutations**, `x_S = Σ_{w ∈ S} T_w`.  For `S` a
Young subgroup `S_λ` this is Murphy's `x_λ`. -/
noncomputable def murphySum (S : Finset (Equiv.Perm (Fin (n + 1)))) :
    QOU.Hecke.IwahoriHecke K q n :=
  ∑ w ∈ S, Tw K q n w

@[simp] theorem murphySum_empty : murphySum K q n ∅ = 0 := by
  simp [murphySum]

/-- **The defining eigenvector property of the Murphy element**:
`σ_i · x_S = q · x_S`, whenever `S` is closed under right multiplication by `s_i`.

A Young subgroup containing `s_i` is closed in this sense, so this covers Murphy's `x_λ`
for every generator of `S_λ` — but the hypothesis is weaker than being a subgroup, which
is the honest statement of what the proof uses. -/
theorem σ_mul_murphySum (i : Fin n) (S : Finset (Equiv.Perm (Fin (n + 1))))
    (hS : ∀ w ∈ S, w * sw i ∈ S) :
    σ K q n i * murphySum K q n S = q • murphySum K q n S := by
  have key : ∑ w ∈ S, (σ K q n i * Tw K q n w - q • Tw K q n w) = 0 := by
    refine Finset.sum_involution (fun w _ => w * sw i) ?_ ?_ (fun w hw => hS w hw) ?_
    · intro w _
      have := σ_mul_Tw_pair K q n i w
      rw [mul_add] at this
      -- `(σT_w − qT_w) + (σT_{ws} − qT_{ws}) = σ(T_w + T_{ws}) − q(T_w + T_{ws}) = 0`
      rw [smul_add] at this
      linear_combination (norm := module) this
    · intro w _ _
      exact mul_sw_ne w i
    · intro w _
      exact mul_sw_sw w i
  have hsplit : ∑ w ∈ S, (σ K q n i * Tw K q n w - q • Tw K q n w)
      = σ K q n i * murphySum K q n S - q • murphySum K q n S := by
    rw [Finset.sum_sub_distrib, murphySum, Finset.mul_sum, Finset.smul_sum]
  rw [hsplit] at key
  exact sub_eq_zero.mp key

/-- **The Young-subgroup form — Murphy's `x_λ` proper.**

A Young subgroup `S_λ ≤ S_{n+1}` is generated by the simple reflections it contains, so for
each such `s_i` it is in particular closed under right multiplication by `s_i`, and this
corollary applies. Stating it for an arbitrary subgroup rather than for the Young subgroups
specifically costs nothing and avoids having to define the composition-to-subgroup map here:
what the eigenvector property needs is closure, and a subgroup containing `s_i` has it.

`x_λ = Σ_{w ∈ S_λ} T_w` is then a `q`-eigenvector for **every** generator of `S_λ` — which
is Murphy's defining property, and the hypothesis under which `m_{st} = T_{d(s)}^* x_λ
T_{d(t)}` is the right object to build a cellular basis on. -/
theorem σ_mul_murphySum_subgroup (i : Fin n)
    (H : Subgroup (Equiv.Perm (Fin (n + 1)))) [DecidablePred (· ∈ H)] (hi : sw i ∈ H) :
    σ K q n i * murphySum K q n {w | w ∈ H}
      = q • murphySum K q n {w | w ∈ H} := by
  refine σ_mul_murphySum K q n i _ ?_
  intro w hw
  simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hw ⊢
  exact H.mul_mem hw hi

end QOU.BraidKnot.HeckeMurphy
