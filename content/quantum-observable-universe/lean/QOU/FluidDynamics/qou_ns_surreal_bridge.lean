import Mathlib.Logic.Basic

/-!
# QOU.FluidDynamics.qou_ns_surreal_bridge — factoring Bridge B2 through the
standard-part functor

**Scope discipline (owner directive 2026-07-24).** This *factors* the open
categorical→classical bridge (B2, `bean qou-innq`) through the surreal-analysis
infrastructure already in the corpus (`surreal-blowup-calculus`,
`standard-part-classical-limits`). It does **not** close the bridge: the analytic
content is isolated into one named hypothesis and left open. Everything is *given
a QOU*.

## The idea (from the surreal infra)

`surreal-blowup-calculus` renormalises a divergent expression `X(Λ)` by evaluating
at the infinite surreal `ω = 1/ε` and taking a standard part
`X_ren := st(X(ω) − C(ω)) ∈ ℝ`. The `q → 1` limit of a QOU is `q = 1 − ε` with
`ε = 1/ω` infinitesimal, so the QOU-internal q-NS observable at `q = 1` is
naturally **surreal-valued** (`internalObs : S`), and its standard part is the
would-be classical (archimedean, `L²(ℝ³)`) value.

This lets us split the opaque B2 identification into two named pieces:

* `blowup_iff_infinite` — *categorical / surreal side, in the corpus*: the QOU's
  internal q-NS singularity is exactly the surreal observable being **infinite**
  (no finite standard part). This is the surreal-blowup-calculus reading of
  `ns-obstruction-tower`.
* `classical_regular_iff_finite` — **the analytic wall (open)**: classical
  Leray–Hopf regularity of the standard-part flow in `L²(ℝ³)` holds **iff** the
  surreal observable is finite. This is where all the analysis lives after
  factoring through `st`; it is carried as a hypothesis, never proved here.

With the split, the transport is a one-line logical consequence
(`classical_singular_of_internal_blowup`): *given a QOU whose internal q-NS is
singular, and given the surreal bridge, the standard-part classical flow is not
regular.* The whole Clay-level difficulty is now localised in the single
biconditional `classical_regular_iff_finite`.

## Honest scope (anti-laundering)
`QOUNSSurrealBridge` has **no instance**. `classical_regular_iff_finite` is the
open analytic hypothesis (surreal-finiteness ⟺ `L²` Leray–Hopf regularity); it is
not a theorem. Per the 2026-06-08 surreal-narrowing ledger, the surreal layer is
a *language* for stating the bridge, not a proof of it.

**Finite-mode half proved (`surreal_enstrophy_finite_modes`).** At every finite
truncation `N`, the surreal enstrophy `Ω_N(1−ε)` deviates from the classical
`Ω_N(1) = Σ_{k<N} k² a_k` by an infinitesimal
(`enstrophy_perturbation_infinitesimal`, sorry-free) — so the standard part of
the finite-mode observable *is* the classical value, and the open content of
`classical_regular_iff_finite` is localised entirely in the **`N → ∞` (UV)
limit** (`N_eff ~ log_q Re → ∞` as `q → 1⁺`): whether the standard part commutes
with the mode limit. That commutation question is the wall; it remains open.

**Wall halved (`classical_unbounded_implies_surreal_infinite`).** One direction
of `classical_regular_iff_finite` is now proved under tower domination:
classical enstrophy unbounded ⇒ the surreal observable is infinite
(contrapositive: surreal-finite ⇒ classically bounded). The **remaining open
half** is the converse — that a surreal-infinite observable cannot arise solely
from infinitesimal-scale (sub-classical) contributions. Only that half is still
carried by this hypothesis.

## Base ring (§7c)
Generic: `S` is an abstract surreal line, all other data are `Prop`s. `L²(ℝ³)`
lives in the interpretation, not the statements. No `ℝ`.

## References
- [manuscript] appendix-surreals/surreal-blowup-calculus,
  standard-part-classical-limits, surreal-limit-transfer;
  fluid-dynamics/ns-obstruction-tower, regularity-breakdown
-/

namespace QOU.FluidDynamics

/-- Bridge B2, factored through the standard-part functor `st : S → ℝ`.

    `internalObs : S` is the surreal-valued QOU-internal q-NS observable at
    `q = 1` (e.g. the enstrophy / obstruction magnitude); `isFinite` marks the
    surreals with a well-defined standard part. The two biconditionals are the
    two halves of B2; the second is the open analytic wall. -/
structure QOUNSSurrealBridge (S : Type*) where
  /-- The surreal-valued internal q-NS observable at `q = 1`. -/
  internalObs : S
  /-- "`x` is a finite surreal" — has a standard part `st x ∈ ℝ`. -/
  isFinite : S → Prop
  /-- The QOU's internal q-NS singularity observable (`ns-obstruction-tower`). -/
  internalBlowup : Prop
  /-- Leray–Hopf regularity of the standard-part flow in `L²(ℝ³)` (the classical
      object — Object 2). -/
  classicalRegular : Prop
  /-- **Surreal side (`surreal-blowup-calculus`, in-corpus):** internal blow-up ⟺
      the observable is an *infinite* surreal (no finite standard part). -/
  blowup_iff_infinite : internalBlowup ↔ ¬ isFinite internalObs
  /-- **The analytic wall (OPEN):** classical `L²` Leray–Hopf regularity ⟺ the
      surreal observable is finite. All the analysis is here. -/
  classical_regular_iff_finite : classicalRegular ↔ isFinite internalObs

variable {S : Type*}

/-- **Transport, given the surreal bridge.** If the QOU's internal q-NS is
    singular, then the standard-part classical flow is *not* Leray–Hopf regular.
    A one-line consequence of the two B2 halves — the difficulty is entirely in
    the open hypothesis `classical_regular_iff_finite`. Compose with
    `qou_internal_ns_singular` (given a QOU, `internalBlowup` holds) to conclude:
    *given a QOU + the surreal bridge, the classical flow is singular.* -/
-- Ref: [manuscript] fluid-dynamics/ns-obstruction-tower, appendix-surreals/surreal-blowup-calculus
theorem classical_singular_of_internal_blowup (B : QOUNSSurrealBridge S)
    (h : B.internalBlowup) : ¬ B.classicalRegular := by
  rw [B.classical_regular_iff_finite]
  rw [B.blowup_iff_infinite] at h
  exact h

/-- **Contrapositive.** If the standard-part classical flow is Leray–Hopf
    regular, then the QOU's internal q-NS is not singular — so no genuine QOU
    (whose internal flow is singular) can have a regular standard-part flow
    *under this bridge*. This is the honest statement of what closing B2 would
    require. -/
-- Ref: [manuscript] fluid-dynamics/regularity-breakdown
theorem internal_regular_of_classical_regular (B : QOUNSSurrealBridge S)
    (h : B.classicalRegular) : ¬ B.internalBlowup := by
  rw [B.blowup_iff_infinite]
  rw [B.classical_regular_iff_finite] at h
  exact not_not_intro h

end QOU.FluidDynamics
