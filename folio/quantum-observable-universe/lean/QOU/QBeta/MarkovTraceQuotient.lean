import QOU.QBeta.TemperleyLiebTower
import QOU.Machinery.HeckeTowerBasicConstruction
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.RingTheory.TwoSidedIdeal.Basic
import Mathlib.RingTheory.TwoSidedIdeal.Operations

/-!
# QOU.QBeta.MarkovTraceQuotient — the trace radical as an actual ideal

`QOU.QBeta.TemperleyLiebTower` proves the Markov trace radical is closed under
multiplication on both sides, and its docstring says this means "the quotient is
a ring". `QOU.QBeta.MarkovGramDegenerate.pairing_descends` then says the pairing
is constant on radical cosets.

Neither builds the quotient. `traceRadical` is a `Set A`; the two closure lemmas
are about that set; and `pairing_descends` is a congruence statement
(`a - a' ∈ rad → τ(a·b) = τ(a'·b)`), not a descent to a quotient *type*. So the
sentence "the Frobenius structure lives on `H_n / rad τ`" has, up to now, had no
object in Lean to refer to.

This file supplies the object, which the refutation of `qou-vndn` makes load
bearing: the Markov pairing is degenerate on `H_n` at convention D (exactly —
`conventionD_kills_antisymmetriser` plus `gram_det_eq_zero_of_radical_combination`),
so every nondegeneracy claim has to move to the quotient or be abandoned.

## What was missing

Mathlib's `TwoSidedIdeal.mk'` needs six fields. The corpus had **two**:

| field | status before this file |
|---|---|
| `0 ∈ rad` | absent |
| `x, y ∈ rad → x + y ∈ rad` | absent |
| `x ∈ rad → -x ∈ rad` | absent |
| `y ∈ rad → x * y ∈ rad` | `traceRadical_mem_mul` (uses cyclicity) |
| `x ∈ rad → x * y ∈ rad` | `traceRadical_mul_mem` |

The three additive ones are absent because `TemperleyLiebTower` states the
radical for a bare `tr : A → R` with only `[Zero R]` — there is no addition on
the target to close under. They need `τ` **linear**, which the Markov trace is;
that is the only strengthening here.

Note which side needs what: right-closure is associativity alone, left-closure
is the *only* place trace cyclicity is spent, and the additive closures need
only linearity. Cyclicity is a real hypothesis and is threaded explicitly rather
than assumed.

Base ring, per AGENTS.md §7c: `[Module R A]`, not `[Algebra R A]`. Nothing here
needs the algebra structure — `A →ₗ[R] R` types under `Module` alone — and
`MarkovGramDegenerate` asking for `Algebra` is not a reason to inherit it.
-/

namespace QOU.QBeta.MarkovTraceQuotient

open QOU.QBeta.TemperleyLiebTower

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Module R A]

/-- **`0` is in the radical.** `τ(0 · b) = τ(0) = 0` by linearity. -/
theorem traceRadical_zero_mem (tau : A →ₗ[R] R) :
    (0 : A) ∈ traceRadical (⇑tau) := by
  intro b
  simp

/-- **The radical is closed under addition.** `τ((x+y)·b) = τ(x·b) + τ(y·b)`. -/
theorem traceRadical_add_mem (tau : A →ₗ[R] R) {x y : A}
    (hx : x ∈ traceRadical (⇑tau)) (hy : y ∈ traceRadical (⇑tau)) :
    x + y ∈ traceRadical (⇑tau) := by
  intro b
  rw [add_mul, map_add, hx b, hy b, add_zero]

/-- **The radical is closed under negation.** -/
theorem traceRadical_neg_mem (tau : A →ₗ[R] R) {x : A}
    (hx : x ∈ traceRadical (⇑tau)) : -x ∈ traceRadical (⇑tau) := by
  intro b
  rw [neg_mul, map_neg, hx b, neg_zero]

/-- **The trace radical, as a two-sided ideal.**

The object the phrase `H_n / rad τ` needs in order to denote anything. Assembled
from the three additive closures above and the two multiplicative closures in
`TemperleyLiebTower`; `hcyc` (trace cyclicity) is consumed by exactly one of the
five, `traceRadical_mem_mul`. -/
def traceRadicalIdeal (tau : A →ₗ[R] R)
    (hcyc : ∀ x y : A, tau (x * y) = tau (y * x)) : TwoSidedIdeal A :=
  TwoSidedIdeal.mk' (traceRadical (⇑tau))
    (traceRadical_zero_mem tau)
    (fun hx hy => traceRadical_add_mem tau hx hy)
    (fun hx => traceRadical_neg_mem tau hx)
    (fun {_ _} hy => traceRadical_mem_mul (⇑tau) hcyc hy _)
    (fun {_ _} hx => traceRadical_mul_mem (⇑tau) hx _)

/-- **Membership in the ideal is membership in the radical**, definitionally
through `mk'`. Stated so downstream proofs never unfold `mk'`. -/
@[simp]
theorem mem_traceRadicalIdeal (tau : A →ₗ[R] R)
    (hcyc : ∀ x y : A, tau (x * y) = tau (y * x)) (a : A) :
    a ∈ traceRadicalIdeal tau hcyc ↔ a ∈ traceRadical (⇑tau) := by
  simp [traceRadicalIdeal, TwoSidedIdeal.mem_mk']


section Quotient

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Module R A]

/-- **The radical sits inside the kernel of the trace.** Take `b = 1`: an
element pairing to zero against *everything* pairs to zero against the unit.
This is the step that needs `A` unital, and it is what lets the trace descend
to the quotient rather than merely the pairing. -/
theorem traceRadical_apply_eq_zero (tau : A →ₗ[R] R) {a : A}
    (ha : a ∈ traceRadical (⇑tau)) : tau a = 0 := by
  have h := ha 1
  rwa [mul_one] at h

variable (tau : A →ₗ[R] R) (hcyc : ∀ x y : A, tau (x * y) = tau (y * x))

/-- **The quotient `A / rad τ`.** For the Markov trace on `H_n(q)` at convention
D this is the object the corpus calls `TL_n(δ)`. -/
abbrev TraceQuot : Type _ := (traceRadicalIdeal tau hcyc).ringCon.Quotient

/-- **The trace, descended to the quotient.** Well defined because related
elements differ by a radical element, which the trace kills. -/
def quotTrace : TraceQuot tau hcyc → R :=
  Quotient.lift tau fun a b hab => by
    have hmem : a - b ∈ traceRadical (⇑tau) :=
      (mem_traceRadicalIdeal tau hcyc _).mp
        ((TwoSidedIdeal.rel_iff _ a b).mp hab)
    have := traceRadical_apply_eq_zero tau hmem
    rw [map_sub, sub_eq_zero] at this
    exact this

@[simp]
theorem quotTrace_mk (a : A) :
    quotTrace tau hcyc (a : TraceQuot tau hcyc) = tau a := rfl

/-- **A class vanishes exactly on the radical.** -/
theorem quot_eq_zero_iff (a : A) :
    (a : TraceQuot tau hcyc) = 0 ↔ a ∈ traceRadical (⇑tau) := by
  rw [show (0 : TraceQuot tau hcyc) = ((0 : A) : TraceQuot tau hcyc) from rfl,
    RingCon.eq, TwoSidedIdeal.rel_iff, sub_zero, mem_traceRadicalIdeal]

/-- **The descended pairing is non-degenerate — in the shape `WenzlTowerStep`
asks for.**

`WenzlTowerStep.semisimple_ascend` wants its trace to satisfy
`∀ y ≠ 0, ∃ z, tr (y * z) ≠ 0`. On `H_n` at convention D that is **false**
(`MarkovGramDegenerate.gram_det_eq_zero_of_radical_combination`). Here it holds,
for the descended trace on the quotient, and the proof is short because the
radical was quotiented out by construction: a nonzero class is a non-radical
element, and a non-radical element is by definition one the pairing separates.

The content is not the argument; it is that the statement now has a *quotient
ring* to be about, rather than a congruence on `A`. -/
theorem quot_pairing_nondegenerate (x : TraceQuot tau hcyc) (hx : x ≠ 0) :
    ∃ y : TraceQuot tau hcyc, quotTrace tau hcyc (x * y) ≠ 0 := by
  induction x using Quotient.inductionOn with
  | h a =>
    have hnot : a ∉ traceRadical (⇑tau) := fun hmem =>
      hx ((quot_eq_zero_iff tau hcyc a).mpr hmem)
    simp only [traceRadical, Set.mem_setOf_eq, not_forall] at hnot
    obtain ⟨b, hb⟩ := hnot
    exact ⟨(b : TraceQuot tau hcyc), hb⟩

/-! ### Non-vacuity

`quot_pairing_nondegenerate` is near-definitional, and it would hold *trivially*
if the quotient were the zero ring — every `x ≠ 0` hypothesis would be
unsatisfiable. So the statement is worth nothing without a witness that the
quotient can be non-trivial. That is exactly the shape of vacuity AGENTS.md
§"No trivial trues" is about, and the guard is cheap: if the trace does not kill
the unit, the unit's class is nonzero. -/

/-- **The unit is outside the radical whenever `τ 1 ≠ 0`.** -/
theorem one_not_mem_traceRadical (tau : A →ₗ[R] R) (h : tau 1 ≠ 0) :
    (1 : A) ∉ traceRadical (⇑tau) := fun hmem =>
  h (traceRadical_apply_eq_zero tau hmem)

/-- **Non-vacuity guard: the quotient is not the zero ring** when `τ 1 ≠ 0`.
Without this, `quot_pairing_nondegenerate` would be satisfiable by collapsing
everything to `0`. The Markov trace is normalised with `τ 1 = 1`, so the
hypothesis holds in the intended application. -/
theorem quot_one_ne_zero (h : tau 1 ≠ 0) :
    ((1 : A) : TraceQuot tau hcyc) ≠ 0 := fun hzero =>
  one_not_mem_traceRadical tau h ((quot_eq_zero_iff tau hcyc 1).mp hzero)

/-- **And the pairing genuinely separates that class**, rather than the
existential being satisfied by an unreachable witness: `τ̄(1̄ · 1̄) = τ 1 ≠ 0`. -/
theorem quot_pairing_one (h : tau 1 ≠ 0) :
    quotTrace tau hcyc ((1 : A) * (1 : A) : A) ≠ 0 := by
  rwa [mul_one, quotTrace_mk]

end Quotient

section Presentation

/-! ### The braided presentation descends

Brick 2 of `qou-s7z2`. Brick 1 built the quotient; this shows the Hecke
generators survive the passage to it, which is what any `WenzlTowerStep`
instance over `TL_n` needs before it can even be *stated*.

Two steps, and the first is not bookkeeping: `RingCon.mk'` is a **ring** hom,
but `HeckeBraidedPresentationOfRank.hecke_quadratic` reads
`σ i * σ i = (q - q⁻¹) • σ i + 1`, with an `R`-scalar action. A ring hom does
not move `•`. So the quotient needs an `R`-algebra structure, which Mathlib does
not supply for `TwoSidedIdeal` (`Algebra R I.ringCon.Quotient` fails to
synthesize), and supplying it needs the image of `algebraMap` to be central —
true here, inherited from `Algebra.commutes` in `A` through a surjection.

**A scalar-action diamond to know about.** `RingCon` already puts a bare
`SMul R` on its quotient (`instSMulQuotient`), and it is *not* part of a
`Module`, let alone an `Algebra` — Mathlib supplies neither for this quotient.
So the instance below introduces a second `SMul` that Lean will not identify
with the first, and `map_smul` through the algebra hom fails to synthesize
`MulActionHomClass` in the gap. The descent proof therefore avoids `•` crossing
the hom at all: both sides are rewritten into `algebraMap _ * _` form with
`Algebra.smul_def`, so only ring operations and `AlgHom.commutes` are used.
Papering over the diamond with a cast would have been the wrong fix.

Base ring: this section is over `[Field R]`, not brick 1's `[CommRing R]`,
because `HeckeBraidedPresentationOfRank` is itself stated over a field. That is
the presentation class's requirement, not a strengthening chosen here; brick 1
stays at `CommRing`/`Module`.
-/

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A]
variable (tau : A →ₗ[R] R) (hcyc : ∀ x y : A, tau (x * y) = tau (y * x))

/-- **The quotient is an `R`-algebra.** Centrality of `algebraMap`'s image is
inherited from `A`: reduce to a representative and apply `Algebra.commutes`. -/
noncomputable instance instAlgebraTraceQuot :
    Algebra R (TraceQuot tau hcyc) :=
  RingHom.toAlgebra' ((traceRadicalIdeal tau hcyc).ringCon.mk'.comp (algebraMap R A))
    (fun c x => by
      induction x using Quotient.inductionOn with
      | h a =>
        show (traceRadicalIdeal tau hcyc).ringCon.mk' (algebraMap R A c * a)
           = (traceRadicalIdeal tau hcyc).ringCon.mk' (a * algebraMap R A c)
        rw [Algebra.commutes])

/-- **The quotient map, as an algebra hom.** This is the object the descent
needs; `RingCon.mk'` alone is too weak because it does not move `•`. -/
noncomputable def quotMk : A →ₐ[R] TraceQuot tau hcyc where
  toFun := (traceRadicalIdeal tau hcyc).ringCon.mk'
  map_one' := map_one _
  map_mul' := map_mul _
  map_zero' := map_zero _
  map_add' := map_add _
  commutes' _ := rfl

/-- Deliberately NOT `@[simp]`: marking it so lets `simp` strip the algebra-hom
wrapper, which breaks the `hecke_quadratic` descent — the `•` is then stranded
inside the quotient map. -/
theorem quotMk_apply (a : A) :
    quotMk tau hcyc a = ((traceRadicalIdeal tau hcyc).ringCon.mk' a) := rfl

/-- **The braided presentation descends to the quotient.**

Every relation of `HeckeBraidedPresentationOfRank` holds for the images of the
generators, at the same rank. The proof is `map_mul` / `map_smul` / `map_one`
under the algebra hom — the content is that such a hom exists at all, which is
the instance above.

What this does **not** do: it does not produce a `WenzlTowerStep` instance at
the Markov trace. That additionally needs the tower inclusion `Hn →ₐ Hn1` shown
to descend compatibly with the two radicals, which is brick 3 and is not
automatic — the radicals at consecutive ranks are different ideals in different
algebras, and nothing here relates them.

🛑 Measured 2026-09-27: **nothing in the corpus consumes `WenzlTowerStep`** — 27
occurrences, of which 1 class definition, 2 discharge targets and 24 prose mentions,
and **zero** instance-hypothesis positions. So an instance unblocks no consumer, and
at a Hecke carrier its conclusion is free outright
(`isSemisimpleRing_hecke_generic`; see
`QOU.Machinery.HeckeRank.wenzlTowerStep_vacuous_of_isSemisimpleRing`). The sentence
above is kept as the record of what this file did not do; read it as naming an open
question, not a live blocker. Bean `qou-s7z2`.
-/
theorem heckeBraidedPresentationOfRank_quot
    (q : R) (n : ℕ) (σ : ℕ → A)
    [inst : QOU.Machinery.HeckeTower.HeckeBraidedPresentationOfRank q n A σ] :
    QOU.Machinery.HeckeTower.HeckeBraidedPresentationOfRank q n
      (TraceQuot tau hcyc) (fun i => quotMk tau hcyc (σ i)) where
  hecke_quadratic i hi := by
    -- NOT `map_smul`: see the scalar-action note above. Both sides are put in
    -- `algebraMap _ * _` form instead, so only ring operations cross the hom.
    have h := congrArg (quotMk tau hcyc) (inst.hecke_quadratic i hi)
    rw [map_mul, map_add, map_one, Algebra.smul_def, map_mul,
      AlgHom.commutes] at h
    rw [Algebra.smul_def]
    exact h
  braid_adjacent i hi := by
    have h := congrArg (quotMk tau hcyc) (inst.braid_adjacent i hi)
    rw [map_mul, map_mul, map_mul, map_mul] at h
    exact h
  far_commute i j hij hj := by
    have h := congrArg (quotMk tau hcyc) (inst.far_commute i j hij hj)
    rw [map_mul, map_mul] at h
    exact h

end Presentation

end QOU.QBeta.MarkovTraceQuotient
