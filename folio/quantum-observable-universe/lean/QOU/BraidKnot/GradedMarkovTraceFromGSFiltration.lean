import Mathlib.LinearAlgebra.Quotient.Basic
import Mathlib.Algebra.Module.Submodule.Map
import QOU.BraidKnot.ConfinementLevel

/-!
# Graded Markov trace from the GS filtration

The graded Markov trace at level `ℓ` is the induced trace on the
quotient `J^ℓ / J^{ℓ+1}` of the Gröbner–Shirshov filtration, and is
purely algebraic over a generic commutative ring (no Archimedean
function theory).

## Disposition (derived, sorry-free)

The proposition `prop:graded-markov-trace-from-gs-filtration` asserts
that for each level `ℓ` there is a **uniquely determined** linear trace

  tr_{M,ℓ} : J^ℓ / J^{ℓ+1} → R

characterised by quotient compatibility (`tr_{M,ℓ} ∘ π_ℓ = tr_M|_{J^ℓ}`),
*well-defined because `tr_M` is filtration-respecting*.

This is exactly the universal property of the quotient: given the
filtration data and the filtration-respecting hypothesis (`tr_M`
vanishes on `J^{ℓ+1}`) as the legitimate inputs, the induced trace
exists (`Submodule.liftQ`) and is unique (a linear map out of a
quotient is determined by its values on representatives).  We therefore
**derive** the existence-and-uniqueness statement sorry-free from those
inputs (`gradedTrace_exists_unique`), rather than projecting it from a
class field.

This replaces the previous self-assuming
`class GradedMarkovTraceFromGSFiltration` whose field
`descends_from_markov : gradedTrace 0 = markovValue` *was* the
conclusion, projected by `theorem … := s.descends_from_markov`
(forbidden by AGENTS.md §1a / §3b-cond rule 5).  The carried data here
(`filtration`, `trace`, `filtration_respecting`) are genuine *inputs*;
the descent map and its uniqueness are *produced*, not assumed.

The construction is purely algebraic over `[CommRing R]` (AGENTS.md §7c)
— no analytic continuation, complex evaluation, or roots of unity.  The
upstream fact that `tr_M` *is* filtration-respecting for the GS
filtration (Cartan–Eilenberg + Jones' Markov-trace existence) is the
hypothesis `filtration_respecting`, supplied by the GS-filtration
theorem `prop:gb-spectral-sequence`.

## References

- [leitner2026] `prop:graded-markov-trace-from-gs-filtration`
- [geckpfeiffer2000] Gröbner–Shirshov filtration on `H_n(q)` (two-sided).
- [jones1987] https://doi.org/10.2307/1971403 — Markov-trace existence.
-/

namespace QOU.BraidKnot

universe u

open Submodule

/-- **GS-filtration data for the graded Markov trace.**

    Bundles the genuine *inputs* of `prop:graded-markov-trace-from-gs-filtration`:

    * `M` — the ambient `R`-module (the Hecke algebra `H_n(R, q)`),
    * `filtration ℓ = J^ℓ` — the descending two-sided GS-filtration,
    * `filtration_mono` — `J^{ℓ+1} ⊆ J^ℓ`,
    * `trace = tr_M` — the Markov trace as an `R`-linear functional,
    * `filtration_respecting` — `tr_M` vanishes on `J^{ℓ+1}` (the
      filtration-respecting property the descent needs).

    No field encodes the descent conclusion: the induced trace and its
    uniqueness are *derived* by `gradedTrace_exists_unique` below. -/
structure GradedMarkovTraceFromGSFiltration (R : Type u) [CommRing R] where
  /-- The ambient `R`-module (the Hecke algebra). -/
  M : Type u
  [addCommGroup : AddCommGroup M]
  [module : Module R M]
  /-- The descending GS-filtration `J^ℓ`. -/
  filtration : ℕ → Submodule R M
  /-- `J^{ℓ+1} ⊆ J^ℓ`. -/
  filtration_mono : ∀ ℓ, filtration (ℓ + 1) ≤ filtration ℓ
  /-- The Markov trace `tr_M : H_n(R, q) → R` as a linear functional. -/
  trace : M →ₗ[R] R
  /-- **Filtration-respecting** (the legitimate input, not the
      conclusion): `tr_M` vanishes on `J^{ℓ+1}`. -/
  filtration_respecting : ∀ ℓ, ∀ x ∈ filtration (ℓ + 1), trace x = 0

attribute [instance] GradedMarkovTraceFromGSFiltration.addCommGroup
attribute [instance] GradedMarkovTraceFromGSFiltration.module

namespace GradedMarkovTraceFromGSFiltration

variable {R : Type u} [CommRing R] (s : GradedMarkovTraceFromGSFiltration R)

/-- The submodule `J^{ℓ+1}` viewed inside `J^ℓ` (the kernel along which
    `tr_M|_{J^ℓ}` descends to `J^ℓ / J^{ℓ+1}`). -/
def gradedKer (ℓ : ℕ) : Submodule R (s.filtration ℓ) :=
  (s.filtration (ℓ + 1)).comap (s.filtration ℓ).subtype

/-- **Graded Markov trace from the GS filtration (derived).**

    For each level `ℓ` there is a **unique** `R`-linear trace

      tr_{M,ℓ} : (J^ℓ / J^{ℓ+1}) → R

    such that `tr_{M,ℓ} ∘ π_ℓ = tr_M|_{J^ℓ}` on representatives — i.e.
    `tr_{M,ℓ}(π_ℓ x) = tr_M x` for every `x ∈ J^ℓ`.

    **Existence** is `Submodule.liftQ` of `tr_M|_{J^ℓ}` along the
    filtration-respecting vanishing (`s.filtration_respecting`).
    **Uniqueness** is the universal property of the quotient: a linear
    map out of `J^ℓ / J^{ℓ+1}` is determined by its values on
    representatives.  Both are produced here, not assumed — no `sorry`,
    no axiom, no projected field. -/
-- Ref: [leitner2026] `prop:graded-markov-trace-from-gs-filtration`
theorem gradedTrace_exists_unique (ℓ : ℕ) :
    ∃! g : ((s.filtration ℓ) ⧸ s.gradedKer ℓ) →ₗ[R] R,
        ∀ x : s.filtration ℓ,
          g (Submodule.Quotient.mk x) = s.trace (x : s.M) := by
  refine ⟨(s.gradedKer ℓ).liftQ (s.trace.comp (s.filtration ℓ).subtype) ?_,
          ?_, ?_⟩
  · -- `gradedKer ℓ ≤ ker (tr_M ∘ subtype)` from filtration-respecting.
    intro x hx
    simp only [gradedKer, Submodule.mem_comap] at hx
    exact s.filtration_respecting ℓ _ hx
  · intro x; rfl
  · intro g hg
    ext x
    exact hg x

end GradedMarkovTraceFromGSFiltration

end QOU.BraidKnot
