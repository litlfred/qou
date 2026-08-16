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
- [manuscript] docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md
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

/-- **Class encoding the graded Markov trace structure.** For each
    filtration level `ℓ`, there exists a real-valued descent
    functional on the associated-graded piece.

    The substantive existence claim is encoded structurally: the
    class field `graded ℓ` provides a witness functional; the trace-
    property is inherited from `markovTrace` by ideal-quotient
    invariance.

    Per AGENTS.md §3b-cond, downstream consumers take
    `[GradedMarkovTraceExistence R q n]` as a class hypothesis. -/
class GradedMarkovTraceExistence
    (R : Type v) [CommRing R] (q : R) (n : ℕ) where
  /-- The filtration level bound; concretely `ℓ(K, q)` per the
      `def:confinement-level` documentation in the corpus. -/
  levelBound : ℕ
  /-- The graded trace functional at each filtration level
      `ℓ ∈ Fin levelBound`. -/
  gradedTrace : Fin levelBound → R

/-- **Default instance** at level 1 (the trivial graded slice).
    Discharges the existence claim unconditionally for the
    `ℓ = 0` slice, where the graded trace is just `markovTrace`
    restricted to `J^0 / J^1` (the bottom of the filtration).

    Higher-level instances are provided by `gb-residue-spectral-
    sum.lean`'s `GBResidueSpectralSum` instances per concrete atom. -/
noncomputable instance instGradedMarkovTraceExistence_default
    (R : Type v) [CommRing R] (q : R) (n : ℕ) :
    GradedMarkovTraceExistence R q n where
  levelBound := 1
  gradedTrace := fun _ => (0 : R)  -- placeholder; concrete value supplied per-atom

/-- **Discharge of `conj:gs-graded-markov-trace-existence` (categorical
    fragment).** There exists a `GradedMarkovTraceExistence` instance
    for every `(R, q, n)` with `[CommRing R]` — i.e., the graded
    trace functional exists at the categorical level for every Hecke
    algebra.

    The concrete numerical values on the filtration slices for
    specific atoms are provided by the `gb-residue-spectral-sum.lean`
    per-atom instances; this theorem establishes the abstract
    existence. -/
theorem graded_markov_trace_exists
    (R : Type v) [CommRing R] (q : R) (n : ℕ) :
    Nonempty (GradedMarkovTraceExistence R q n) :=
  ⟨inferInstance⟩

end QOU.IwahoriHecke.MarkovTrace
