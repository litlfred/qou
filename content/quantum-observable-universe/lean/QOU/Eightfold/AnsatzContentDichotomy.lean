/-
# The ansatz-content dichotomy

Three results in this directory each say, at a fixed size, when a linear mass
ansatz carries predictive content:

* `GellMannOkuboIdentity.gmo_cannot_discriminate` — the Gell-Mann–Okubo relation
  holds *identically* under the octet-breaking ansatz, so observing it confirms
  nothing.  The prediction is **vacuous**.
* `DecupletEqualSpacing.equal_spacing_cannot_discriminate` — the same shape for
  the decuplet's consecutive mass differences.
* `NonetMixingUnconstrained.mixing_unconstrained` — with the octet entry held
  fixed, *every* pair of physical masses is realised, so no observation can
  refute the ansatz.  The prediction is **empty**.

The first two are three-mass statements; the third is `2 × 2`.  This file gives
the size-free form, and its point is that **the two failure modes are one failure
mode**: an ansatz that cannot be refuted forces only relations that were true
anyway.

Nothing here is numerical.  There is no `q`, no Markov parameter, no anchor and
no convention, so no statement in this file can be convention-C contaminated —
the same property that makes `NonetMixingUnconstrained` safe to build on.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic

namespace QOU.Eightfold.AnsatzContent

universe u

variable {R : Type u} [CommRing R] {p n : ℕ}

/-- An **observable tuple**: the `n` numbers a measurement reports (masses of a
multiplet, say). -/
abbrev Obs (R : Type u) (n : ℕ) := Fin n → R

/-- A **relation** among observables, tested by asking whether `rel obs = 0`.
Gell-Mann–Okubo and decuplet equal spacing are both of this shape. -/
abbrev Rel (R : Type u) (n : ℕ) := Obs R n → R

/-- An **ansatz**: a model carrying `p` parameters to the `n` observables. -/
abbrev Ansatz (R : Type u) (p n : ℕ) := (Fin p → R) → Obs R n

/-- `rel` is **vacuous**: it holds of every observable tuple whatsoever.  A
vacuous relation is not evidence for any ansatz, because it is not evidence for
anything. -/
def Vacuous (rel : Rel R n) : Prop := ∀ obs : Obs R n, rel obs = 0

/-- `A` **forces** `rel`: every parameter choice produces observables satisfying
it.  This is what "the ansatz predicts the relation" means. -/
def Forces (A : Ansatz R p n) (rel : Rel R n) : Prop :=
  ∀ param : Fin p → R, rel (A param) = 0

/-- `A` is **unconstraining**: every observable tuple is realised by some
parameter choice.  No measurement can refute such an ansatz. -/
def Unconstraining (A : Ansatz R p n) : Prop := Function.Surjective A

/-- `rel` **discriminates** for `A`: the ansatz forces it, and it is not true
anyway.  This is exactly what a testable prediction is. -/
def Discriminating (A : Ansatz R p n) (rel : Rel R n) : Prop :=
  Forces A rel ∧ ¬ Vacuous rel

/-- **The dichotomy.**  An unconstraining ansatz forces only vacuous relations.

This is the general form of the contrast drawn in `NonetMixingUnconstrained`:
"empty" and "vacuous" are not two ways for an ansatz to fail, they are one.  If
nothing can refute the model, then anything it appears to predict was already
true of every conceivable measurement. -/
theorem vacuous_of_forces_of_unconstraining
    {A : Ansatz R p n} (hA : Unconstraining A)
    {rel : Rel R n} (h : Forces A rel) : Vacuous rel := by
  intro obs
  obtain ⟨param, rfl⟩ := hA obs
  exact h param

/-- **No discriminating relation survives an unconstraining ansatz.** -/
theorem not_discriminating_of_unconstraining
    {A : Ansatz R p n} (hA : Unconstraining A) (rel : Rel R n) :
    ¬ Discriminating A rel := by
  rintro ⟨hf, hv⟩
  exact hv (vacuous_of_forces_of_unconstraining hA hf)

/-- **The usable direction (contrapositive).**  A genuine prediction certifies
that the ansatz is restrictive.

If a model forces a relation that is *not* true of every observable tuple, then
some observable tuple is out of its reach — so the model has content, and the
measurement is capable of refuting it. -/
theorem not_unconstraining_of_discriminating
    {A : Ansatz R p n} {rel : Rel R n} (h : Discriminating A rel) :
    ¬ Unconstraining A := fun hA => not_discriminating_of_unconstraining hA rel h

/-- Explicitly: a discriminating relation exhibits an **unreachable**
observation.  This is the operational content — it names the measurement that
would falsify the model. -/
theorem exists_unreachable_of_discriminating
    {A : Ansatz R p n} {rel : Rel R n} (h : Discriminating A rel) :
    ∃ obs : Obs R n, ∀ param : Fin p → R, A param ≠ obs := by
  obtain ⟨hf, hv⟩ := h
  simp only [Vacuous, not_forall] at hv
  obtain ⟨obs, hobs⟩ := hv
  exact ⟨obs, fun param hp => hobs (hp ▸ hf param)⟩

section Nonet

/-- The nonet coefficient map of `NonetMixingUnconstrained`, as an `Ansatz`: the
free parameters are the singlet diagonal entry `d₂` and the squared mixing
`esq`, and the observables are the two characteristic-polynomial coefficients
(trace and determinant) with the octet entry `d₁` held fixed. -/
def nonetAnsatz (d₁ : R) : Ansatz R 2 2 :=
  fun v => ![d₁ + v 0, d₁ * v 0 - v 1]

/-- **`mixing_unconstrained` is an instance of this dichotomy.**  The nonet
ansatz is surjective onto the coefficient plane, so by
`not_discriminating_of_unconstraining` it admits no testable prediction about
where the physical states sit or how strongly they mix. -/
theorem nonetAnsatz_unconstraining (d₁ : R) : Unconstraining (nonetAnsatz d₁) := by
  intro obs
  refine ⟨![obs 0 - d₁, d₁ * (obs 0 - d₁) - obs 1], ?_⟩
  funext i
  fin_cases i <;> simp [nonetAnsatz]

/-- Consequently no relation among the nonet's two coefficients discriminates. -/
theorem nonet_no_discriminating (d₁ : R) (rel : Rel R 2) :
    ¬ Discriminating (nonetAnsatz d₁) rel :=
  not_discriminating_of_unconstraining (nonetAnsatz_unconstraining d₁) rel

end Nonet

section NonVacuity

/-- A **restrictive** ansatz, exhibited so that the hypothesis of the dichotomy
is not vacuously satisfiable: the model that predicts two equal observables.
It has one parameter and two observables. -/
def equalPairAnsatz : Ansatz R 1 2 := fun v => ![v 0, v 0]

/-- The relation "the two observables agree", as a `Rel`. -/
def diffRel : Rel R 2 := fun obs => obs 0 - obs 1

theorem equalPairAnsatz_forces_diffRel :
    Forces (equalPairAnsatz (R := R)) diffRel := by
  intro v; simp [equalPairAnsatz, diffRel]

/-- Over a nontrivial ring the relation is **not** vacuous — `(0, 1)` violates
it — so `equalPairAnsatz` genuinely discriminates. -/
theorem equalPairAnsatz_discriminating [Nontrivial R] :
    Discriminating (equalPairAnsatz (R := R)) diffRel := by
  refine ⟨equalPairAnsatz_forces_diffRel, ?_⟩
  intro hv
  have := hv ![0, 1]
  simp [diffRel] at this

/-- And therefore it is **not** unconstraining: some observation refutes it.
This is the case the eightfold-way ansätze are *not* in. -/
theorem equalPairAnsatz_not_unconstraining [Nontrivial R] :
    ¬ Unconstraining (equalPairAnsatz (R := R)) :=
  not_unconstraining_of_discriminating equalPairAnsatz_discriminating

end NonVacuity

end QOU.Eightfold.AnsatzContent
