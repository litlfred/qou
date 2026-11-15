import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Data.Real.Sqrt

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
`computations/markov/markov_pipeline_cross_validator.py` —
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

    No physical-atom instance is provided here (the honest open state);
    the numerical cross-pipeline agreement recorded in
    `markov-pipeline-cross-validation.witness.json` is a computation, not
    a Lean premise.

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

/-! ## Proton (`A = 1`) case — no instance here

Until 2026-11-15 this file carried a `protonExample` instance whose
`archimedean_agreement` field was supplied by an `axiom` equating the
real evaluation of an opaque integer polynomial at `√q₀` with the decimal
`2.1225825095` taken from a Python witness.  It was removed on owner
instruction (no empirical or witness-certified numbers in formal
statements).

The proton identity stays an **open conjecture**, carried with no
instance by `QOU.BraidKnot.HabiroResidueSumEquivalence.protonExample.archimedean_agreement`
(`conj:gs-archimedean-agreement-residue`).  The machine-precision
agreement of the two Python pipelines is a numerical observation and is
recorded in the content block's prose, not here. -/

/-- Substrate parameter `q_0 = 1.10997...` (proton pin) used throughout the
    physical-prediction chapters.  Real-valued; `Real.sqrt q_0`
    gives `u_0`. -/
noncomputable def q_0_proton : ℝ := 1.1099785827513808  -- :leanval[q_0]{precision=17}

/-! ## Trivial-zero skeleton instance

A second, **fully Lean-verified** instance using the zero polynomial
and zero gb-mass.  Both sides of `archimedean_agreement` evaluate to
`0`; the equation holds by direct evaluation.  This proves the class
is non-vacuous as a Lean type and provides a typeclass-resolution
discharge target.
-/

/-- Trivial-zero skeleton: every numerical field is `0`. -/
-- Ref: [leitner2026] habiro-residue-sum-equivalence §"Skeleton"
noncomputable instance trivialZero : HabiroResidueSumEquivalence where
  q_0 := 0
  q_0_nonneg := le_refl 0
  habiro_trace := 0
  gb_mass := 0
  archimedean_agreement := by
    -- Both sides evaluate to 0: (0.map _).eval _ = 0 = gb_mass.
    show (Polynomial.map (Int.castRingHom ℝ) 0).eval (Real.sqrt 0) = 0
    simp

/-! ## §3b-cond upgrade — archimedean agreement DERIVED from one algebraic input

The `archimedean_agreement` field above axiomatizes the *whole* real
equality. Per the formalize-first / anti-laundering
discipline that over-axiomatizes: the two constructions are two representations
of one Habiro-ring element, and the residue is a Habiro-completion **projection**
("no analytic continuation", see `full-pole-structure-mass-trace.lean`), so the
identity is finite-algebraic. The single honest open input is the **algebraic
same-element identification**; the numeric agreement is then a ring-hom
consequence.

See `docs/audits/2026-07-18-residue-habiro-tail-algebraic-not-analytic.md`. -/

/-- Bundled data for the §3b-cond agreement: the two polynomial representatives
    and the GB mass, with the GB side's own internal consistency (`gb_mass` is
    the archimedean evaluation of the GB polynomial representative — true by the
    GB residue-sum construction being a Habiro element; *not* the
    cross-identity). -/
structure HabiroGBData where
  q_0 : ℝ
  /-- Habiro cyclotomic polynomial `Σ a_m (u;u)_m`. -/
  habiro_trace : Polynomial ℤ
  /-- GB residue-sum polynomial representative in `Ẑ[q]`. -/
  gb_trace_poly : Polynomial ℤ
  /-- The GB mass value. -/
  gb_mass : ℝ
  /-- GB internal consistency: the mass is the archimedean eval of the GB
      polynomial representative. -/
  gb_mass_is_eval :
    (gb_trace_poly.map (Int.castRingHom ℝ)).eval (Real.sqrt q_0) = gb_mass

/-- **The single open algebraic input (§3b-cond class, no instance).** The Habiro
    cyclotomic construction and the GB residue-spectral construction yield the
    *same* element of `Ẑ[q]` — an equality of polynomial representatives, hence in
    the Habiro ring. This is the GS-filtration ↔ cyclotomic-projection
    identification (`prop:graded-markov-trace-from-gs-filtration` +
    `prop:residue-at-root`), deferred to the algebraic-substrate layer; it is
    **algebraic**, not an analytic continuation. No instance is provided (the
    honest open state). -/
class HabiroGBSameElement (D : HabiroGBData) : Prop where
  same_element : D.habiro_trace = D.gb_trace_poly

/-- **Archimedean agreement — DERIVED, not axiomatized.** Given the algebraic
    same-element identification, the archimedean realization `ρ_∞` (evaluation at
    `u_0 = √q_0`) of the Habiro trace equals the GB mass, because `ρ_∞` is a ring
    hom that commutes with the finite decomposition. Axiomatizes strictly less
    than `HabiroResidueSumEquivalence.archimedean_agreement`: one *algebraic*
    polynomial identity, versus a transcendental real equality. -/
theorem archimedean_agreement_of_sameElement
    (D : HabiroGBData) [h : HabiroGBSameElement D] :
    (D.habiro_trace.map (Int.castRingHom ℝ)).eval (Real.sqrt D.q_0) = D.gb_mass := by
  rw [h.same_element]; exact D.gb_mass_is_eval

end QOU.BraidKnot
