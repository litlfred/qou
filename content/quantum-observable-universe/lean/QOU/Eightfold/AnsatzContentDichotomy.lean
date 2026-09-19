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
import QOU.Eightfold.GellMannOkuboIdentity
import QOU.Eightfold.DecupletEqualSpacing

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

section EightfoldInstances

/-! ### The two fixed-size cases, as instances — and they land on the OTHER side

`nonetAnsatz_unconstraining` above wires `NonetMixingUnconstrained`.  The file's
header also names `gmo_cannot_discriminate` and
`equal_spacing_cannot_discriminate`; this section wires those, and doing so
**corrects the header's implicit reading of them.**

The word "discriminate" is used in two different senses and they point opposite
ways:

* In `GellMannOkuboIdentity` and `DecupletEqualSpacing`, *"cannot discriminate"*
  means the relation takes the **same value for every parameter choice**
  `(a,b,c)`.  That is exactly `Forces` here — the ansatz predicts the relation.
  It says the relation cannot separate two *mechanisms* inside the first-order
  octet class.
* `Discriminating` here means `Forces ∧ ¬ Vacuous` — the relation is predicted
  **and** is not true of every conceivable measurement, so it can **refute the
  class itself**.

Both hold.  GMO and equal spacing are parameter-blind *and* falsifiable, and
the second fact is what the general theorem detects: by
`not_unconstraining_of_discriminating`, **neither ansatz is unconstraining.**
They have content.  That is the opposite of the nonet, whose ansatz reaches
every observable and therefore predicts nothing at all.

So the eightfold chapter carries ansätze on **both** sides of the dichotomy, and
the two failure modes the header describes as "one failure mode" are correctly
attributed to the nonet alone.  This is consistent with both source files' own
prose — each says the testable content is the *deviation* (~6 % on GMO, ~9.2 %
across the decuplet spacings), which presupposes the relation is falsifiable.
-/

open QOU.Eightfold.GellMannOkuboIdentity in
/-- The first-order `SU(3)`-breaking ansatz of `GellMannOkuboIdentity` as an
`Ansatz`: the three breaking parameters `(a, b, c)` to the three observables
GMO is stated on, `(4m²_π, 4m²_η, 2·(4m²_K))`. -/
def gmoAnsatz : Ansatz R 3 3 := fun v =>
  ![pionMassSq (v 0) (v 1) (v 2),
    etaMassSq (v 0) (v 1) (v 2),
    kaonAvgMassSqDoubled (v 0) (v 1) (v 2)]

/-- The Gell-Mann–Okubo combination `4m²_K − 3m²_η − m²_π`, as a `Rel`. -/
def gmoRel : Rel R 3 := fun obs => 2 * obs 2 - (3 * obs 1 + obs 0)

open QOU.Eightfold.GellMannOkuboIdentity in
/-- The ansatz forces GMO — this is `gmo_combination_vanishes` restated in the
dichotomy's vocabulary. -/
theorem gmoAnsatz_forces_gmoRel : Forces (gmoAnsatz (R := R)) gmoRel := by
  intro v
  simp only [gmoAnsatz, gmoRel, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.head_cons, Matrix.cons_val_two, Matrix.tail_cons,
    pionMassSq, etaMassSq, kaonAvgMassSqDoubled, kaonPlusMassSq,
    kaonMinusMassSq, massSqQuadrupled]
  ring

/-- But GMO is **not** vacuous: the observable triple `(1, 0, 0)` violates it.
So the relation does say something about the observables. -/
theorem gmoRel_not_vacuous [Nontrivial R] : ¬ Vacuous (gmoRel (R := R)) := by
  intro h
  have hv := h ![1, 0, 0]
  simp only [gmoRel, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons,
    Matrix.cons_val_two, Matrix.tail_cons] at hv
  have : (1 : R) = 0 := by linear_combination -hv
  exact one_ne_zero this

/-- **Therefore GMO is a discriminating relation**, and by
`not_unconstraining_of_discriminating` the first-order octet ansatz is *not*
unconstraining. -/
theorem gmoAnsatz_discriminating [Nontrivial R] :
    Discriminating (gmoAnsatz (R := R)) gmoRel :=
  ⟨gmoAnsatz_forces_gmoRel, gmoRel_not_vacuous⟩

theorem gmoAnsatz_not_unconstraining [Nontrivial R] :
    ¬ Unconstraining (gmoAnsatz (R := R)) :=
  not_unconstraining_of_discriminating gmoAnsatz_discriminating

/-- The operational form: some measurement is out of the ansatz's reach, i.e.
GMO names a triple of meson masses that would falsify first-order octet
breaking. -/
theorem gmo_exists_unreachable [Nontrivial R] :
    ∃ obs : Obs R 3, ∀ param : Fin 3 → R, gmoAnsatz param ≠ obs :=
  exists_unreachable_of_discriminating gmoAnsatz_discriminating

open QOU.Eightfold.GellMannOkuboIdentity in
/-- **And the other sense, separately.**  The ansatz map is not injective — the
breaking strength `b` is invisible to all three GMO observables, since the pion
and eta sit at `Y = 0` and the two kaon hypercharges cancel in the average.
`(0,0,0)` and `(0,1,0)` are different mechanisms with identical observables.

This is `gmo_independent_of_breaking_strength` as a statement about the map, and
it is what *"cannot discriminate"* means in the source file — a different claim
from `Discriminating` above, and compatible with it. -/
theorem gmoAnsatz_not_injective [Nontrivial R] :
    ¬ Function.Injective (gmoAnsatz (R := R)) := by
  intro hinj
  have hcollide : gmoAnsatz (R := R) ![0, 0, 0] = gmoAnsatz (R := R) ![0, 1, 0] := by
    funext i
    fin_cases i <;>
      simp [gmoAnsatz, pionMassSq, etaMassSq, kaonAvgMassSqDoubled,
        kaonPlusMassSq, kaonMinusMassSq, massSqQuadrupled]
  have := congrFun (hinj hcollide) 1
  simp at this

open QOU.Eightfold.DecupletEqualSpacing in
/-- The decuplet ansatz: the same three breaking parameters to the four decuplet
masses `(Δ, Σ*, Ξ*, Ω)`. -/
def decupletAnsatz : Ansatz R 3 4 := fun v =>
  ![deltaMass (v 0) (v 1) (v 2), sigmaStarMass (v 0) (v 1) (v 2),
    xiStarMass (v 0) (v 1) (v 2), omegaMass (v 0) (v 1) (v 2)]

/-- The equal-spacing relation as a `Rel`: the second difference
`(Ω − Ξ*) − (Ξ* − Σ*)`. -/
def decupletRel : Rel R 4 := fun obs => (obs 3 - obs 2) - (obs 2 - obs 1)

open QOU.Eightfold.DecupletEqualSpacing in
/-- The ansatz forces equal spacing — `second_difference_vanishes` restated. -/
theorem decupletAnsatz_forces_decupletRel :
    Forces (decupletAnsatz (R := R)) decupletRel := by
  intro v
  simp only [decupletAnsatz, decupletRel, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.head_cons, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.tail_cons,
    deltaMass, sigmaStarMass, xiStarMass, omegaMass, massQuadrupled]
  ring

/-- Equal spacing is not vacuous: `(0, 0, 0, 1)` violates it. -/
theorem decupletRel_not_vacuous [Nontrivial R] : ¬ Vacuous (decupletRel (R := R)) := by
  intro h
  have hv := h ![0, 0, 0, 1]
  simp only [decupletRel, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons,
    Matrix.cons_val_two, Matrix.cons_val_three, Matrix.tail_cons] at hv
  have : (1 : R) = 0 := by linear_combination hv
  exact one_ne_zero this

/-- **So the decuplet ansatz is discriminating too** — Gell-Mann's `Ω`
extrapolation is a falsifiable claim about the four masses, even though it
extracts no information about which mechanism produced them. -/
theorem decupletAnsatz_discriminating [Nontrivial R] :
    Discriminating (decupletAnsatz (R := R)) decupletRel :=
  ⟨decupletAnsatz_forces_decupletRel, decupletRel_not_vacuous⟩

theorem decupletAnsatz_not_unconstraining [Nontrivial R] :
    ¬ Unconstraining (decupletAnsatz (R := R)) :=
  not_unconstraining_of_discriminating decupletAnsatz_discriminating

/-- **The contrast, in one statement.**  Within the same chapter: the decuplet
ansatz has content and the nonet ansatz does not.  This is the dichotomy doing
the work it was written for — telling apart two ansätze that both look like
"a linear mass formula with a few parameters". -/
theorem decuplet_has_content_nonet_does_not [Nontrivial R] (d₁ : R) :
    ¬ Unconstraining (decupletAnsatz (R := R)) ∧ Unconstraining (nonetAnsatz d₁) :=
  ⟨decupletAnsatz_not_unconstraining, nonetAnsatz_unconstraining d₁⟩

end EightfoldInstances

end QOU.Eightfold.AnsatzContent
