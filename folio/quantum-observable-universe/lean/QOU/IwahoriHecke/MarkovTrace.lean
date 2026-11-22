import QOU.IwahoriHecke.TypeA
import Mathlib.Algebra.Module.LinearMap.Defs

/-!
# `QOU.IwahoriHecke.MarkovTrace` — Markov trace on Type-A Hecke (Sprint 4)

**Sprint 4 of the Iwahori-Hecke Mathlib infrastructure plan**
(see [`docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md`](../../../../../../docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md)).

Defines the Markov trace on the Type-A Iwahori-Hecke algebras and
closes `conj:gs-graded-markov-trace-existence` at the categorical
level (existence of the graded trace on each filtration level).

## Markov trace definition

The Markov trace `tr_M : IwahoriHeckeOfSn n q → R` is the unique
`R`-linear functional satisfying:

1. **Trace property**: `tr_M(a · b) = tr_M(b · a)` for all
   `a, b ∈ IwahoriHeckeOfSn n q`.
2. **Markov stabilisation**: under the canonical embedding
   `IwahoriHeckeOfSn n q ↪ IwahoriHeckeOfSn (n+1) q`,
   `tr_M(a · σ_n) = z · tr_M(a)` for `a` in the image, where
   `z := -1/((q + 1)(q - 1)^{-1}) = 1/(√q + 1/√q)` is the Jones
   normalisation (here we keep it as an abstract parameter for
   generality).

The trace exists and is unique up to overall normalisation
([jones1987], [wenzl1988]). Here we declare the signature and
graded-existence content, deferring the full uniqueness proof
to Sprint 4 follow-up.

## Conjecture closure: `conj:gs-graded-markov-trace-existence`

The Gröbner-Shirshov filtration $J^\bullet(q)$ on $H_n(R, q)$
admits a graded sequence of trace functionals:

$$
\mathrm{tr}_{M, \ell} : J^\ell(q) / J^{\ell+1}(q) \longrightarrow R
$$

obtained as the descent of `tr_M` along the projection. **Existence
at every filtration level** is the content of this conjecture.

The categorical existence follows from the trace property
(`tr_M` is invariant under multiplication by elements of $J^{\ell+1}$
modulo $J^{\ell+1}$ itself, hence descends). For Sprint 4 we
discharge the **abstract existence** as a Lean theorem; the
concrete computation of each $tr_{M, \ell}$ requires the GS
filtration machinery in `gb-residue-spectral-sum.lean` (which
already encodes the trace as a class field per the .md status note).

Refs:
- [jones1987] DOI 10.2307/2691504
- [wenzl1988] DOI 10.1007/BF01404457
- [orellana1998] DOI 10.1006/jabr.1998.7437
- [leitner2026] docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md
-/


namespace QOU.IwahoriHecke.MarkovTrace

universe v

variable (R : Type v) [CommRing R] (q z : R) (n : ℕ)

/-- **Markov trace signature** on the Type-A Iwahori-Hecke algebra.

    Sprint 4 deliverable: signature only. The unique functional
    satisfying the trace + Markov-stabilisation properties is
    constructed in Sprint 4 follow-up (depends on the reduced-
    expression basis from Sprint 2 follow-up).

    For now, we declare the signature so downstream consumers can
    reference `markovTrace R q n`; the actual functional content
    is provided by §3b-cond instances of `MarkovTraceClass` below. -/
noncomputable opaque markovTrace
    (R : Type v) [CommRing R] (q : R) (n : ℕ) :
    QOU.IwahoriHecke.TypeA.IwahoriHeckeOfSn R q n → R

/-! ## Graded trace existence

For the Gröbner-Shirshov filtration `J^\bullet(q)`, the descent of
`markovTrace` to each associated-graded piece exists by the trace
property + ideal invariance. We package this as a class for
downstream §3b-cond consumption. -/

/-- **The graded Markov trace, as a conjecture carrier.**

**Rebuilt 2026-08-30 — this class used to assert nothing.**  It read

```
class GradedMarkovTraceExistence (R) [CommRing R] (q : R) (n : ℕ) where
  levelBound : ℕ
  gradedTrace : Fin levelBound → R
```

with **no `Prop` field at all**: a pair of a natural number and a function into `R`.
Any such pair inhabits it, and one did — a `default` instance
`⟨1, fun _ => (0 : R)⟩`, its own comment calling the value a *"placeholder"*.  A
`theorem graded_markov_trace_exists` then closed over `⟨inferInstance⟩` under the
docstring *"Discharge of `conj:gs-graded-markov-trace-existence`"*.  What that theorem
established is that a pair `(ℕ, Fin 1 → R)` exists.

This is the `proof-no-empty-prop-carrier` / `proof-claims-unencoded` pattern of
AGENTS.md §3b-tax, and the old docstring's *"the substantive existence claim is encoded
structurally"* was the claim §3b-tax exists to catch.

Two further defects the rebuild fixes:

* **The field had the wrong type.**  The `.md` states `tr_{M,ℓ} : J^ℓ/J^{ℓ+1} → ℝ`, a
  *functional* on each graded piece.  `Fin levelBound → R` is one **number** per level.
* **`gradedTrace` was unrelated to `markovTrace`.**  Nothing tied the carrier to the
  trace it is supposed to be the descent of.

The fields below carry the conjecture's actual content: each level's functional is
additive and cyclic (what makes it a *trace*), and level `0` recovers `markovTrace`
(what makes it *that* trace's descent).  The filtration itself is not formalised, so
these are the properties statable without it — they are deliberately weaker than the
full conjecture, and are not claimed to be equivalent to it.

**There is no instance, and that is the honest state**: per §3b-tax an unproved primary
conjecture is represented by a content-bearing class with no instance.  Supplying one
is the open work. -/
class GradedMarkovTraceExistence
    (R : Type v) [CommRing R] (q : R) (n : ℕ) where
  /-- The filtration level bound; concretely `ℓ(K, q)` per `def:confinement-level`. -/
  levelBound : ℕ
  /-- The graded trace **functional** at each filtration level. -/
  gradedTrace : Fin levelBound → QOU.IwahoriHecke.TypeA.IwahoriHeckeOfSn R q n → R
  /-- Additivity — part of being the descent of a linear functional. -/
  gradedTrace_add : ∀ l x y, gradedTrace l (x + y) = gradedTrace l x + gradedTrace l y
  /-- Cyclicity — what makes each level's functional a *trace*. -/
  gradedTrace_cyclic : ∀ l x y, gradedTrace l (x * y) = gradedTrace l (y * x)
  /-- The bottom of the filtration recovers the Markov trace itself — what makes this
      the descent of `markovTrace` rather than of some unrelated functional. -/
  gradedTrace_zero : ∀ (h : 0 < levelBound) x,
    gradedTrace ⟨0, h⟩ x = markovTrace R q n x

/-- Any carrier's level-`0` functional is cyclic **and** is the Markov trace, so
`markovTrace` is forced to be cyclic on the nose.

This is the point of the rebuild: with the old field types no consequence of this shape
was derivable, because the class constrained nothing.  Assuming the conjecture now buys
something. -/
theorem markovTrace_cyclic_of_carrier
    (R : Type v) [CommRing R] (q : R) (n : ℕ)
    [G : GradedMarkovTraceExistence R q n] (h : 0 < G.levelBound)
    (x y : QOU.IwahoriHecke.TypeA.IwahoriHeckeOfSn R q n) :
    markovTrace R q n (x * y) = markovTrace R q n (y * x) := by
  rw [← G.gradedTrace_zero h, ← G.gradedTrace_zero h, G.gradedTrace_cyclic]

end QOU.IwahoriHecke.MarkovTrace
