import QOU.KnotTheory
import QOU.KnotTheory.JonesPolynomial
import QOU.AlgebraicSubstrate.MetallicHierarchy
import QOU.MassDerivation
import Mathlib.Data.Real.Basic
import Mathlib.Order.Interval.Set.Basic

/-!
# QOU.KnotTheory.MetallicPiecewise — sharpened metallic-piecewise conjectures

The owner's structural conjecture (2026-06-09): on the metallic ladder
`δ_n = (n + √(n²+4))/2`, certain SDP-feasibility / character-sign
observables of the Hecke algebra are **piecewise constant** on each
interval `(δ_{n-1}, δ_n)`, with **jumps** exactly at the metallic
ratios `q = δ_n`.

Three empirical probes have tested this so far (Wenzl weights, Jones
polynomials, per-block characters at n=3) and **all returned null** —
sign-flip bifurcation is not at metallic ratios for those observables.
The structure of the conjecture must therefore live at one of:

  (M1) **Higher-strand q-characters** χ^λ(β) for n ≥ 4 — the n=3
       characters are too simple (3 partitions, mostly q-monotonic).
       Counter-examples to monotonicity start to appear at n=4 (5
       partitions) or higher.

  (M2) **Catalog-blind SDP enumeration** N(q) := |{nuclide configurations
       feasible at q under the parameterised SDP-uniqueness theorem}|.
       The 252 number is currently observational (hardcoded NNDC list);
       no one has run the blind count.

  (M3) **Δ_λ piecewise structure**, which would explain the option-e
       v1-v7 failures: a single closure formula across (1, ∞) cannot
       fit something that's genuinely piecewise on the metallic ladder.

Each of (M1), (M2), (M3) is stated below as a §3b-cond conjectural class.
The conjectures are **sharpened** versions of the owner's original
"piecewise on metallic ratios" claim, incorporating the three null
results from the probes:

  - The Wenzl/Jones-polynomial level is **excluded** as the boundary
    locus by the empirical probes.
  - The conjecture is **narrowed** to (M1), (M2), (M3) — three concrete
    falsifiable forms.

-- Ref: [leitner2026] QOU.AlgebraicSubstrate.MetallicHierarchy
-- Ref: [leitner2026] docs/audits/2026-06-08-metallic-q-hierarchy-proof.md
-- Ref: [leitner2026] computations/metallic_q_wenzl_sign_sweep.py
-- Ref: [leitner2026] computations/metallic_q_jones_sign_sweep.py
-- Ref: [leitner2026] computations/metallic_q_quark_bifurcation.py
-/

namespace QOU.KnotTheory.MetallicPiecewise

open QOU.AlgebraicSubstrate

/-! ## (M1) Sharpened conjecture: higher-strand character bifurcation

For some strand count `n ≥ 4`, some braid word `β ∈ B_n`, and some
partition `λ ⊢ n`, the q-character `χ^λ(β)` has a sign change in the
open interval `(δ_{n-1}, δ_n)` if and only if the interval **contains
a metallic ratio**.  Equivalently, the locus of `χ^λ(β) = 0` in `(1, ∞)`
is the set of metallic ratios `{δ_n : n ∈ ℕ⁺}`.

This refines the original "N(q) piecewise" claim into a falsifiable
algebraic statement: it predicts that the roots of higher q-characters
are exactly the algebraic numbers `δ_n`, not "near" them. -/

/-- Conjectural witness for (M1). -/
class HigherStrandCharacterBifurcation where
  /-- There exists a strand count, partition, and braid word whose
      q-character has a root at every metallic ratio. -/
  exists_witness : Prop

/-! ## (M2) Sharpened conjecture: catalog-blind SDP-count is piecewise

Let `N(q)` denote the count of distinct categorical-mass-formula
configurations admitting an SDP-feasible solution at parameter q,
**without** reference to any experimental catalog.  Then `N` is a
piecewise-constant function of `q` on `(1, ∞)`, with discontinuities
exactly at the metallic ratios `{δ_n}`.

Furthermore, `N(q₀) = 252` (the experimental count) under the
**substrate** evaluation, which would convert the observational 252
into a substrate-derived prediction. -/

/-- Catalog-blind SDP-feasibility count, declared opaque pending the
    parametric-SDP enumeration infrastructure (sib. infra to
    `nucleus_real_sdp.py` but not pinned to a fixed character witness). -/
opaque blindSDPCount : ℝ → ℕ

/-- Conjectural witness for (M2). -/
class CatalogBlindSDPCount where
  /-- `blindSDPCount` is constant on each open metallic interval. -/
  piecewise_constant : ∀ n : ℕ, ∀ q₁ q₂ : ℝ,
    metallic n < q₁ → q₁ < q₂ → q₂ < metallic (n + 1) →
    blindSDPCount q₁ = blindSDPCount q₂
  /-- `blindSDPCount` jumps at every metallic ratio. -/
  jumps_at_metallic : ∀ n : ℕ, ∃ ε > 0,
    blindSDPCount (metallic n - ε) ≠ blindSDPCount (metallic n + ε)
  /-- At the substrate value `q₀ ≈ 1.1097`
      (`QOU.MassDerivation.substrate_q`), the count equals 252. -/
  count_at_substrate : blindSDPCount QOU.MassDerivation.substrate_q = 252

/-! ## (M3) Sharpened conjecture: Δ_λ closure is piecewise

The Δ_λ closure (option-e target) has different functional forms on
the metallic intervals `(δ_{n-1}, δ_n)`.  The option-e v1-v7 failures
are explained by attempting a single global closure where a piecewise
one is required. -/

/-- Conjectural witness for (M3).

    **Fixed 2026-09-12 (`prop-universe-field`).** The field was typed bare
    `: Prop` — the *universe* of propositions, not a proposition — so an instance
    supplied a proposition rather than a proof of one and `instance := ⟨True⟩`
    discharged the class. A carrier in that state cannot serve as a §3b
    conjectural witness either: it asserts nothing *even as a conjecture*. The
    statement is now a **parameter**, so assuming the conjecture costs a proof of
    it rather than costing nothing.

    Note the contrast with `MetallicSDPJumps` directly above, whose fields are
    genuine propositions (`blindSDPCount (metallic n - ε) ≠ blindSDPCount (metallic
    n + ε)`, `count_at_substrate : … = 252`) — the defect was local to this
    carrier, not a habit of the file.

    Proved for the shape in
    `QOU.ProofHygiene.SelfAssumingContexts.propUniverse_inhabited`. The conjecture
    is untouched and still open; no instance is supplied. -/
class DeltaLambdaPiecewise (PiecewiseClosureExists : Prop) : Prop where
  /-- There exist distinct closed-form expressions on `(1, φ)` vs
      `(φ, δ_silver)` that each match the deuteron Δ_λ to within
      Wenzl-positivity bounds on their respective intervals. -/
  piecewise_closure_exists : PiecewiseClosureExists

end QOU.KnotTheory.MetallicPiecewise
