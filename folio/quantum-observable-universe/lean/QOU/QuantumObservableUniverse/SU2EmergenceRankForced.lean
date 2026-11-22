/-
# `thm:su2-emergence`, with the rank derived instead of assumed

## The defect this file repairs

`thm:su2-emergence` claims `Aut^⊗(τ) ≅ SU(2)`, and
`VolumeConstraintForcesFibreTwo.lean` records — correctly — that neither the
corpus proof nor the Lean carries that claim:

* `prf:su2-emergence` argues `G = SL(2) ∩ U(2) = SU(2)` from two lemmas whose
  conclusions are *stated* as `G ⊆ SL(2,ℂ)` and `G ⊆ U(2)`. The rank is an
  **input** to both, not an output of either. `VolumeForm.lean`'s own §2
  heading says so: "SU(2) from **rank-2** + dagger".
* The block's `lean.ref` resolves to `QOU.SU2Emergence`, a `structure` whose
  fields are `gaugeGroupType`, `ext_sq_action` and
  `det_one : ∀ g, ext_sq_action g = 𝟙 exteriorSquare`. It never mentions
  `SU(2)` and never mentions the rank.
* The two supporting lemmas are `class SU2EmergenceVolumeDeterminant
  (det_g : ℝ) : Prop where det_eq_one : det_g = 1` and its dagger twin —
  each restating its own conclusion, with docstrings saying the witness is
  "pending".

So the block asserted a theorem the formalisation did not have.

## What was already there, and what was missing

Two things **were** proved, sorry-free, in `su2_emergence_volume_determinant.lean`
and `su2_emergence_dagger_unitarity.lean`: that `det g = 1` lifts `g` into
`SL(2,ℂ)`, and (`su2_emergence_combined`) that `g * star g = 1` together with
`det g = 1` puts `g` in `Matrix.specialUnitaryGroup (Fin 2) ℂ`. Those are real
derivations, not restatements.

What was missing is the **rank**, and it is now available:
`exteriorSquareDim_eq_one_iff : exteriorSquareDim N = 1 ↔ N = 2`
(`BraidsAndKnots/VolumeConstraintForcesFibreTwo.lean`, sorry-free) derives it
from the volume constraint `Λ²V ≅ 𝟙` — the non-degenerate volume form that
defines the fibre — rather than assuming it.

## The honest decomposition, which is the point of this file

Joining the two halves separates what the corpus proof conflated:

* **which subgroup** — `unitary ∧ det = 1 ⇒ special unitary` — holds at
  **every** `N`. It says nothing about the rank, and `su2_emergence_combined`
  is a `Fin 2` instance of a general fact.
* **which rank** — `N = 2` — is exactly what the volume constraint supplies,
  and is the only place `2` enters.

`su2_emergence_rank_forced` below states both conjuncts of one theorem, so the
two cannot be silently traded for one another again. Its non-vacuity is
`su2_emergence_rank_hypothesis_is_load_bearing`: at `N = 3` the volume
hypothesis **fails**, so the rank conjunct is doing work rather than following
from the unitarity half.

## What is still NOT proved, and is not claimed

That `Aut^⊗(τ)` — the tensor-automorphism group of the fibre functor — *is*
this matrix group. The statements below quantify over a set of matrices
satisfying the two constraints; identifying `Aut^⊗(τ)` with such a set is the
content of `QOU.SU2Emergence`'s fields and remains an assumption. This file
narrows the gap from "the rank and the subgroup are both assumed" to "the
realisation is assumed"; it does not close it.

`-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/su2-emergence.md`
-/
import QOU.su2_emergence_volume_determinant
import QOU.BraidsAndKnots.VolumeConstraintForcesFibreTwo

namespace QOU

open QOU.BraidsAndKnots

/-- **The subgroup half is rank-free.** For any `n`, a unitary matrix of
determinant one is special unitary. Stated at general `n` precisely to make
visible that this half carries no rank content — the `Fin 2` in
`su2_emergence_combined` is an instance, not a consequence. -/
theorem mem_specialUnitary_of_unitary_of_det_one
    {n : Type*} [DecidableEq n] [Fintype n]
    (g : Matrix n n ℂ) (h_dag : g * star g = 1) (h_det : g.det = 1) :
    g ∈ Matrix.specialUnitaryGroup n ℂ := by
  rw [Matrix.mem_specialUnitaryGroup_iff]
  exact ⟨Matrix.mem_unitaryGroup_iff.mpr h_dag, h_det⟩

/-- **`thm:su2-emergence` with the rank derived.**

Given the volume constraint in its strong form — `dim Λ²V = 1`, i.e.
`Λ²V ≅ 𝟙` — and a set `G` of automorphisms of the fibre each preserving the
volume form (`det g = 1`) and the Frobenius dagger (`g · g† = 1`), BOTH
conclusions follow:

* `N = 2`, from the volume constraint alone; and
* `G ⊆ SU(N)`, from the two constraints alone.

The conjunction is the statement `prf:su2-emergence` intended. Neither
conjunct implies the other, which is why they are stated together. -/
theorem su2_emergence_rank_forced
    {N : ℕ} (hvol : exteriorSquareDim N = 1)
    (G : Set (Matrix (Fin N) (Fin N) ℂ))
    (h_dag : ∀ g ∈ G, g * star g = 1)
    (h_det : ∀ g ∈ G, g.det = 1) :
    N = 2 ∧ ∀ g ∈ G, g ∈ Matrix.specialUnitaryGroup (Fin N) ℂ :=
  ⟨(exteriorSquareDim_eq_one_iff N).mp hvol,
   fun g hg => mem_specialUnitary_of_unitary_of_det_one g (h_dag g hg) (h_det g hg)⟩

/-- **The rank conjunct is load-bearing, not decorative.**

If it followed from the unitarity half it would hold at every `N`. It does
not: at `N = 3` the volume hypothesis `exteriorSquareDim N = 1` is false
(`dim Λ²V = 3`), so `su2_emergence_rank_forced` has no `N = 3` instance —
while `mem_specialUnitary_of_unitary_of_det_one` applies at `N = 3` perfectly
well. That contrast is the anti-vacuity check: the two halves are independent,
and only the volume constraint distinguishes rank 2. -/
theorem su2_emergence_rank_hypothesis_is_load_bearing :
    exteriorSquareDim 3 ≠ 1 ∧ exteriorSquareDim 2 = 1 :=
  ⟨exteriorSquareDim_three_ne_one, exteriorSquareDim_two⟩

/-- **Contrapositive form**: a fibre whose gauge group is not special unitary
at rank 2 cannot satisfy the volume constraint. Recorded because this is the
direction a falsification would come from — exhibit a fibre automorphism
violating `det = 1` or `g·g† = 1`, and the volume form is what breaks. -/
theorem volume_constraint_fails_of_not_rank_two
    {N : ℕ} (hN : N ≠ 2) : exteriorSquareDim N ≠ 1 :=
  fun h => hN ((exteriorSquareDim_eq_one_iff N).mp h)

/-- **A single fibre satisfying the volume constraint has no three-dimensional
fundamental.**

Immediate from `exteriorSquareDim_eq_one_iff`, and recorded separately because
it is the form the flavour question needs: the eightfold-way sector requires a
three-dimensional `W`, and this says one fibre cannot supply it.

**This is a SECOND route to a confinement the corpus already has, not a new
result.** `eightfold-open-problems` states — correctly — that *"the search is
confined to the groupoid level is now a theorem, not an extrapolation"*, on the
strength of the `Sym²` gate (`Sym2Gate.lean`, `Sym2GateParity.lean`): a
three-dimensional `W` must have `Sym²(W)` irreducible, and the gate decides
that for an irreducible summand.

The two arguments are independent. The `Sym²` route constrains `W` by the
representation theory of its symmetric square; this one constrains the *fibre*
by the non-degeneracy of its volume form, and never mentions `W`'s symmetric
square at all. Two independent derivations of the same negative is worth
having; neither supplies the construction that is actually open, which is a
three-dimensional `W` in the **multi-fibre groupoid**. Nothing here bears on
that, and nothing here should be read as narrowing it. -/
theorem no_three_dimensional_fundamental_in_one_fibre
    {N : ℕ} (hvol : exteriorSquareDim N = 1) : N ≠ 3 := by
  rw [(exteriorSquareDim_eq_one_iff N).mp hvol]
  decide

end QOU
