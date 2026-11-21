import QOU.IwahoriHecke.TensorEmbedding
import QOU.MassTheory.TensorTraceCharacter

/-!
# The trace of the braiding, and its `q = 1` identification with the classical character

Two halves of quantum Schur–Weyl were built separately in this corpus and never met.

* The **character** half. `QOU.MassTheory.TensorTraceCharacter` computes the trace of a
  permutation of tensor factors — `(card κ)^{orbitCount σ}`, which at `card κ = 2` is the
  `2^{c(σ)}` that `ClassicalTraceFloor` assumes — and
  `QOU.MassTheory.WeightedPermutationCharacter` deforms it, one `q`-factor per orbit.
* The **braiding** half. `QOU.IwahoriHecke.RMatrixSl2` and
  `QOU.IwahoriHecke.TensorEmbedding` build Jimbo's `Ř`, prove its three Hecke relations at
  general `n`, and assemble the action `H_{m+1}(q) → End(V^{⊗(m+1)})`.

`RMatrixSl2.rCheck_one` already showed `Ř` degenerates to the *flip* at `q = 1`. This file
takes the step that actually connects the two halves:

> **`braidAt_one_eq_permMatrix`** — at `q = qi = 1` the braiding at sites `i ≠ j` is not
> merely flip-like, it **is** `permMatrixOf (indexPerm (swap i j) (Fin 2))`, the very matrix
> `TensorTraceCharacter` computes the trace of.

so the character follows with no new computation:

> **`trace_braidAt_one`** — `tr(Ř_{ij}) = 2^{orbitCount (swap i j)}` at `q = 1`.

The classical `2^{c(σ)}` is therefore the `q → 1` limit of the braiding's trace, *checked*
rather than asserted by analogy.

## The `q ≠ 1` trace

`trace_braidAt_eq_sum` gives the trace at general `q` as an explicit sum over basis states —
`q` on the diagonal `a i = a j`, `q − qi` on the ascent `a i < a j`, `0` on the descent. It
is stated as a sum rather than in closed form on purpose: turning it into
`2^{n−2}(3q − qi)` needs the count `#{a | (a i, a j) = (x, y)} = 2^{n−2}`, which is a
separate combinatorial lemma and carries `ℕ`-subtraction in the exponent.

## 🛑 What this is NOT

It is **not** the Markov trace, and it does not connect the braiding to
`WeightedPermutationCharacter`'s deformed character. Those are different objects:

* `weighted_permutation_character` traces `K^{⊗n} ∘ σ` for a *diagonal* weight `K` and a
  *permutation* `σ`; this file traces `Ř` itself. At `q = 1` both specialise to the same
  classical character, which is exactly why the identification below is the right bridge —
  and exactly why it does not by itself relate them at `q ≠ 1`.
* The Markov trace on `H_n(q)` — the thing the Jones polynomial needs — is still
  `noncomputable opaque` in `QOU.IwahoriHecke.MarkovTrace`, constructed nowhere.

So: the `q = 1` corner is joined; the `q ≠ 1` bridge between braiding and character is open.

-- Ref: [jimbo1986]; [leitner2026] bean qou-k4oq
-/

namespace QOU.IwahoriHecke.BraidingTrace

open QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix QOU.MassTheory
open Equiv Finset

variable {R : Type*} [CommRing R] {n : ℕ} {i j : Fin n}

/-! ## The `q = 1` identification -/

/-- The braiding's matrix condition and the transposition's are the same condition.

`Ř` at `q = 1` sends `a ↦ b` with weight `1` exactly when `a` and `b` agree away from the
two sites and are swapped on them — which is precisely `b ∘ (i j) = a`. -/
theorem swap_indexPerm_iff (a b : Fin n → Fin 2) :
    indexPerm (Equiv.swap i j) (Fin 2) b = a
      ↔ ((∀ m, m ≠ i → m ≠ j → a m = b m) ∧ (a i, a j) = (b j, b i)) := by
  rw [funext_iff]
  constructor
  · intro h
    refine ⟨fun m hmi hmj => ?_, Prod.ext ?_ ?_⟩
    · have hm := h m
      rw [indexPerm_apply, Equiv.symm_swap, Equiv.swap_apply_of_ne_of_ne hmi hmj] at hm
      exact hm.symm
    · have hm := h i
      rw [indexPerm_apply, Equiv.symm_swap, Equiv.swap_apply_left] at hm
      exact hm.symm
    · have hm := h j
      rw [indexPerm_apply, Equiv.symm_swap, Equiv.swap_apply_right] at hm
      exact hm.symm
  · rintro ⟨hoff, hpair⟩ x
    rw [indexPerm_apply, Equiv.symm_swap]
    by_cases hxi : x = i
    · subst hxi; rw [Equiv.swap_apply_left]; exact (congrArg Prod.fst hpair).symm
    · by_cases hxj : x = j
      · subst hxj; rw [Equiv.swap_apply_right]; exact (congrArg Prod.snd hpair).symm
      · rw [Equiv.swap_apply_of_ne_of_ne hxi hxj]; exact (hoff x hxi hxj).symm

/-- **At `q = 1` the braiding IS the transposition's permutation matrix.**

Not "degenerates to something flip-like" — literally the matrix
`permMatrixOf (indexPerm (swap i j) (Fin 2))` whose trace `TensorTraceCharacter` computes.
This is the joint between the braiding half of quantum Schur–Weyl and the character half.

No `i ≠ j` hypothesis is needed, and the degenerate case is not vacuous: at `i = j` both
sides are the identity matrix — `swap i i = 1`, and the braiding's condition collapses to
`a = b` — so the trace below reads `2^{orbitCount 1} = 2^n`, the dimension of `V^{⊗n}`. -/
theorem braidAt_one_eq_permMatrix :
    braidAt (1 : R) (1 : R) i j = permMatrixOf (indexPerm (Equiv.swap i j) (Fin 2)) R := by
  classical
  ext a b
  rw [braidAt, rCheck_one, embedPair_apply, permMatrixOf]
  simp only [RMatrix.flip, Matrix.of_apply]
  by_cases h : (∀ m, m ≠ i → m ≠ j → a m = b m) ∧ (a i, a j) = (b j, b i)
  · rw [if_pos h.1, if_pos h.2, if_pos ((swap_indexPerm_iff a b).mpr h)]
  · rw [if_neg (fun hc => h ((swap_indexPerm_iff a b).mp hc))]
    by_cases h1 : ∀ m, m ≠ i → m ≠ j → a m = b m
    · rw [if_pos h1, if_neg (fun hc => h ⟨h1, hc⟩)]
    · rw [if_neg h1]

/-- **The classical character, from the braiding.** At `q = 1` the trace of the braiding at
sites `i ≠ j` is `2^{orbitCount (i j)}` — the `2^{c(σ)}` of `ClassicalTraceFloor`, obtained
from `Ř` rather than assumed alongside it.

No new computation: this is `TensorTraceCharacter.trace_permMatrixOf_indexPerm` read through
the identification above. -/
theorem trace_braidAt_one :
    Matrix.trace (braidAt (1 : R) (1 : R) i j)
      = (2 ^ orbitCount (Equiv.swap i j) : ℕ) := by
  rw [braidAt_one_eq_permMatrix, trace_permMatrixOf_indexPerm]
  simp

/-! ## The trace at general `q` -/

/-- **The braiding's trace as an explicit sum over basis states.**

The diagonal entry at `a` depends only on the two site values: `q` when `a i = a j` (the
symmetric channel), `q − qi` when `a i < a j`, and `0` when `a i > a j` — the asymmetry
being the ordering built into Jimbo's `Ř`.

Left as a sum rather than a closed form deliberately: collapsing it to `2^{n−2}(3q − qi)`
needs the state count `#{a | (a i, a j) = (x, y)} = 2^{n−2}`, a separate lemma that also
drags `ℕ`-subtraction into the exponent. -/
theorem trace_braidAt_eq_sum (q qi : R) :
    Matrix.trace (braidAt q qi i j)
      = ∑ a : Fin n → Fin 2, (if a i = a j then q else if a i < a j then q - qi else 0) := by
  classical
  refine Finset.sum_congr rfl (fun a _ => ?_)
  rw [Matrix.diag_apply, braidAt, embedPair_apply, if_pos (fun m _ _ => rfl), rCheck_apply,
    if_pos rfl]

/-- Consistency: at `q = qi = 1` the general-`q` sum counts the states fixed by the
transposition, and agrees with `trace_braidAt_one`. -/
theorem trace_braidAt_one_eq_card :
    (∑ a : Fin n → Fin 2,
        (if a i = a j then (1 : R) else if a i < a j then (1 : R) - 1 else 0))
      = (2 ^ orbitCount (Equiv.swap i j) : ℕ) := by
  rw [← trace_braidAt_eq_sum, trace_braidAt_one]

end QOU.IwahoriHecke.BraidingTrace
