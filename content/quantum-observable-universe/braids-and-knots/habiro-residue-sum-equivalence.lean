import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Algebra.Polynomial.Eval

/-!
# Habiro completion ≡ Gröbner–Shirshov residue spectral sum

The Markov trace `tr_M(T_w, q) ∈ Ẑ[q]` of a closed braid admits two
distinct constructions in this chapter:

1. **Polynomial-ring (Habiro)**: `prop:full-pole-structure-mass-trace`,
   formalised as `QOU.BraidKnot.HabiroCompletion`.  The trace is a
   polynomial `trace ∈ ℤ[u]` with cyclotomic coefficients
   `coeff m ∈ ℤ[u]` satisfying the Habiro-ideal property
   `tail_in_ideal`.

2. **Residue spectral sum (Gröbner–Shirshov)**:
   `prop:gb-residue-spectral-sum`, formalised as
   `QOU.BraidKnot.GBResidueSpectralSum`.  The mass is a real number
   `descended + Σ_ℓ residueAtRoot ℓ ζ_ℓ q`.

This file states their equivalence as a class `HabiroResidueSumEquivalence`
relating any pair of instances of the two structures over the same
braid: the archimedean evaluation of the Habiro trace polynomial at
`u_0 = q_0^{1/2}` agrees with the GB spectral-sum mass.

Status: the equivalence is an **analytic identity** between the
cyclotomic tail expansion and the residue contributions of the
quantum dilogarithm `Φ_q`.  A formal proof requires the analytic
identification of `gradedMarkovTrace` and `residueAtRoot` (currently
`noncomputable opaque`).  Empirical certification at machine
precision is provided by
`folio-assistant/computations/markov_pipeline_cross_validator.py` —
0.0 (proton) and 2.79e-16 (neutron) relative difference; see the .md
sibling for details.

Ref: [habiro2004] https://doi.org/10.2140/gt.2004.8.1127
Ref: [jones1987] Hecke algebras and knot polynomials
LaTeX label: `prop:habiro-residue-sum-equivalence`
-/

namespace QOU.BraidKnot

open Polynomial

/-- **Equivalence of the two Markov-trace constructions.**

    A `HabiroResidueSumEquivalence` instance records, for one fixed
    braid word `T_w` and one fixed substrate parameter `q_0 ∈ ℝ`,
    the agreement of the polynomial-ring evaluation of the Habiro
    trace polynomial at `u_0 = q_0^{1/2}` with the GB residue-sum
    mass — both viewed in `ℝ` via the archimedean realization
    `ρ_∞ : Ẑ[q] → ℝ`.

    Fields:
    * `q_0`              — the substrate parameter (archimedean evaluation point).
    * `habiro_trace`     — the Habiro polynomial trace, in `ℤ[u]`.
    * `gb_mass`          — the GB residue-sum mass value, in `ℝ`.
    * `archimedean_agreement` — the substantive axiom:
      `eval (q_0^{1/2}) (map (Int.castRingHom ℝ) habiro_trace) = gb_mass`.
      This is an **analytic identity**, currently axiomatized; a
      Lean proof would require formalising the identification of
      `Σ_m a_m(u_0) · (u_0;u_0)_m` with the residue spectral sum
      `descended + Σ_ℓ Res_{q→ζ_ℓ}(Φ_q · tr_{M,ℓ})`.

    Concrete instances supply `archimedean_agreement` as a `sorry`-axiom
    (CLAUDE.md §3b), backed by the empirical witness
    `markov-pipeline-cross-validation.witness.json` (relative
    difference ≤ `1e-9` to machine epsilon for every available atom).

    Ref: [habiro2004], [jones1987]. -/
class HabiroResidueSumEquivalence where
  /-- Archimedean evaluation point. -/
  q_0 : ℝ
  /-- Non-negativity of the substrate parameter (so `q_0^{1/2}` is real). -/
  q_0_nonneg : 0 ≤ q_0
  /-- The Habiro polynomial trace in `ℤ[u]` (matches
      `HabiroCompletion.trace`). -/
  habiro_trace : Polynomial ℤ
  /-- The GB residue-sum mass value in `ℝ` (matches
      `GBResidueSpectralSum.mass`). -/
  gb_mass : ℝ
  /-- **Analytic identity (substrate axiom).**

      The archimedean realization of the Habiro polynomial trace at
      `u_0 = q_0^{1/2}` agrees with the GB residue-sum mass.

      This is the formal counterpart to the cross-pipeline witness
      `markov-pipeline-cross-validation.witness.json`, which checks
      this equality numerically at relative tolerance `1e-9` and
      consistently achieves rel_diff ≤ machine epsilon on every
      available atom.  The Lean proof is open at the level of
      `gb-residue-spectral-sum.lean`'s `noncomputable opaque`
      declarations. -/
  archimedean_agreement :
    (habiro_trace.map (Int.castRingHom ℝ)).eval (Real.sqrt q_0) = gb_mass

end QOU.BraidKnot
