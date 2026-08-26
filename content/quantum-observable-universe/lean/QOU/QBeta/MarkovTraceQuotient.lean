import QOU.QBeta.TemperleyLiebTower
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

end QOU.QBeta.MarkovTraceQuotient
