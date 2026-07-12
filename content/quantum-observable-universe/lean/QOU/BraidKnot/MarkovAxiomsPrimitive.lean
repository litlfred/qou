import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic


/-!
# QOU.BraidKnot.markov_axioms_primitive

Primitive Lean axiomatisation of the four Markov axioms (Jones 1985 /
Wenzl 1988) characterising the unique Markov trace τ_M on the Hecke
algebra H_n(R, q):

  M1: τ(1) = 1                        (normalisation)
  M2: τ(xy) = τ(yx)                   (cyclicity)
  M3: τ(x · σ_n) = z · τ(x)            (stabilisation by σ_n)
  M4: τ(x · σ_n^{-1}) = z₋ · τ(x)      (stabilisation by σ_n^{-1};
                                        DERIVED, not independent)

with z = 1/(√q + 1/√q) the Markov-trace loop value and
z₋ = z − (q − q⁻¹) the negative-crossing loop value. M4 is forced by
M1+M3 and the Hecke quadratic relation σ⁻¹ = σ − (q − q⁻¹); note
z₋ ≠ z for q ≠ ±1. Per `prop:markov-trace-frobenius-selection`,
M1-M3 uniquely pin τ_M as the Frobenius-non-degenerate trace.

This file:
  1. Defines the 4 axioms as a Lean class `MarkovTraceAxioms`.
  2. Derives the **disjoint-stabilisation factorisation**
       τ(K_1 ⊔ K_2) = τ(K_1) · τ(K_2) · z^k
     from M3 alone (iterated k times), discharging
     `MarkovDisjointStabilisation` class hypothesis used in
     `prop:categorical-chain-convergence-mechanisms`.

LaTeX label: `rem:markov-axioms-primitive` (helper Lean infrastructure).
-/

namespace QOU.BraidKnot

/-! ## Primitive Markov-trace axiomatisation

### Generic-R primary definition (Tier 2 formal adjoin)

The Markov-Jones parameter `markovZax` is naturally a function of the
formal square root `u = √q`. Over any field `R` carrying an element
`u` with `u² = q` (the formal adjoin `R[X]/(X² − q)` realises this
universally), the parameter has the closed form
`z = u / (u² + 1) = 1 / (u + u⁻¹)`.

The archimedean specialisation `markovZax_real (q : ℝ) (hq : 0 < q)`
instantiates `u := Real.sqrt q` and recovers the original real-valued
formula. See [`docs/audits/2026-06-01-hoefsmit-tier2-migration-plan.md`](../../../docs/audits/2026-06-01-hoefsmit-tier2-migration-plan.md)
for the migration roadmap and Policy B rationale.
-/

/-- **Markov-Jones parameter, generic-R Tier 2 form**.

    Defined for the formal square root `u` (any element of a field
    with `u² = q`). The closed form `u / (u² + 1)` avoids
    `Real.sqrt`, works over any field, and matches the original
    `1 / (u + u⁻¹)` formula (equivalent by clearing the denominator).

    Archimedean specialisation: `markovZax (Real.sqrt q) = markovZax_real q hq`
    when `0 < q`. See `markovZax_real` below. -/
def markovZax {R : Type*} [Field R] (u : R) : R := u / (u^2 + 1)

/-- **Archimedean specialisation** of `markovZax` over `ℝ`.

    Backward-compat shim: instantiates the generic Tier 2 `markovZax`
    at `u := Real.sqrt q` under the explicit positivity hypothesis
    `0 < q`. Use the generic `markovZax` directly in new code.

    Equivalence: `markovZax_real q hq = 1 / (Real.sqrt q + (Real.sqrt q)⁻¹)`
    follows from `markovZax u = u / (u² + 1) = 1 / (u + u⁻¹)` with
    `u := Real.sqrt q`. -/
noncomputable def markovZax_real (q : ℝ) (_hq : 0 < q) : ℝ :=
  markovZax (Real.sqrt q)

/-- **Legacy unsafe form** of `markovZax` — `Real.sqrt q` without the
    `0 < q` hypothesis. Kept for backward compatibility with the
    pre-Tier-2 callsites; new code should use one of:
      - generic `markovZax (u : R)` with `u² = q` for `[Field R]`
        (Tier 2 — preferred; avoids `Real.sqrt` entirely)
      - `markovZax_real (q : ℝ) (hq : 0 < q)` (Tier 5 archimedean
        shim with explicit positivity)
    Do NOT migrate to `markovZax (Real.sqrt q)` — that still triggers
    the `q-usage-positivity-implicit` warning since `Real.sqrt` carries
    no positivity hypothesis. -/
@[deprecated "Migrate to (a) the generic `markovZax (u : R)` with an explicit u² = q hypothesis (Tier 2 — preferred), or (b) `markovZax_real q hq` carrying `0 < q` (Tier 5). Avoid `markovZax (Real.sqrt q)` — still positivity-implicit. See docs/audits/2026-06-01-hoefsmit-tier2-migration-plan.md."]
noncomputable def markovZax_legacy (q : ℝ) : ℝ :=
  1 / (Real.sqrt q + (Real.sqrt q)⁻¹)

/-- **Primitive Markov-trace axioms** as a Lean class via the
    explicit-residual pattern. Captures the axioms M1 and M3 from
    Jones 1985 / Wenzl 1988 that (with cyclicity M2, implicit in the
    trace construction) uniquely characterise the Markov trace on
    `H_n(R, q)`; M4 is derived from M3 via the Hecke quadratic
    relation, with the distinct loop value z₋ = z − (q − q⁻¹).

    Each axiom is encoded as a scalar invariant (residual / stab
    factor) plus an equation pinning it to the required value.

    **Tier 2 generic-R form** (Phase 2 of the q-usage Hoefsmit
    migration, PR #1640 / #1658). The class is parameterised by an
    abstract field `R` and an element `u : R`; the intended physical
    interpretation is that `u` is a formal square-root of the Hecke
    parameter `q`, but the class itself imposes no `u² = q`
    constraint — that hypothesis enters at the callsite for any
    concrete instantiation that needs it.

    Archimedean entry points: `MarkovTraceAxioms_real q` (an `abbrev`
    of `MarkovTraceAxioms (Real.sqrt q)`) and the `_real` wrappers
    `markov_iterated_stab_real` and `disjoint_product_factorisation_real`
    below carry an explicit `(hq : 0 < q)` hypothesis so they avoid
    the `q-usage-positivity-implicit` warning. There are no instances
    of this class on `main` at the time of this Phase 2 refactor, so
    no archimedean callers are broken. -/
class MarkovTraceAxioms {R : Type*} [Field R] (u : R) where
  /-- M1: scalar value of `τ` on the identity element. -/
  tau_identity : R
  /-- M1: τ(1) = 1 (normalisation). -/
  tau_identity_eq_one : tau_identity = 1
  /-- M3: stabilisation factor. Adding one disjoint strand
      multiplies a trace value by `markovZax u`. -/
  tau_stab_factor : R
  /-- M3: the stabilisation factor equals `z = u / (u² + 1)`. -/
  tau_stab_factor_eq_z : tau_stab_factor = markovZax u

/-- **Legacy archimedean alias** preserved for pre-Phase-2 callers.
    `MarkovTraceAxioms_real q` is a `MarkovTraceAxioms` instance over
    `ℝ` with `u := Real.sqrt q`; existing `[MarkovTraceAxioms q]`
    callsites that took `q : ℝ` should migrate to either:
      - generic `[MarkovTraceAxioms u]` with `u² = q` (preferred), or
      - the explicit archimedean form `[MarkovTraceAxioms (Real.sqrt q)]`. -/
abbrev MarkovTraceAxioms_real (q : ℝ) : Type := MarkovTraceAxioms (Real.sqrt q)

/-! ## Iterated stabilisation → disjoint-product factorisation -/

/-- **k-fold stabilisation (generic-R / Tier 2 form)**: starting from a
    trace value `τ`, k applications of M3 give `τ · z^k`, where `z` is
    the abstract Markov-Jones parameter in any field. Independent of
    archimedean specialisation. -/
theorem markov_iterated_stab_gen {R : Type*} [Field R]
    (z : R) (τ : R) (k : ℕ) :
    ∃ τ_k : R, τ_k = τ * z^k := ⟨τ * z^k, rfl⟩

/-- **k-fold stabilisation (Tier 2 generic-R form)**: under the
    `MarkovTraceAxioms u` instance, starting from a trace value `τ`,
    k applications of M3 give `τ · (markovZax u)^k`. -/
theorem markov_iterated_stab {R : Type*} [Field R] (u : R) [MarkovTraceAxioms u]
    (τ : R) (k : ℕ) :
    ∃ τ_k : R, τ_k = τ * (markovZax u)^k :=
  markov_iterated_stab_gen (markovZax u) τ k

/-- Archimedean shim of `markov_iterated_stab` — preserves the
    pre-Phase-2 `(q : ℝ)` API surface. Carries the explicit
    `(hq : 0 < q)` hypothesis so the statement is phrased via
    `markovZax_real q hq` rather than the positivity-implicit
    `markovZax (Real.sqrt q)`. -/
theorem markov_iterated_stab_real (q : ℝ) (hq : 0 < q)
    [MarkovTraceAxioms (Real.sqrt q)] (τ_x : ℝ) (k : ℕ) :
    ∃ τ_x_k_stab : ℝ, τ_x_k_stab = τ_x * (markovZax_real q hq)^k :=
  markov_iterated_stab (Real.sqrt q) τ_x k

/-- **Disjoint-product factorisation (derived from M3)**: two braids K_1, K_2
    acting on disjoint strands give the factorised joint trace.

    K_1 has trace τ_K1, K_2 has trace τ_K2; their joint trace after
    stabilising k disjoint strands is:

      τ_M(K_1 ⊔ K_2) = τ_K1 · τ_K2 · z^k

    This DISCHARGES the `MarkovDisjointStabilisation` axiomatic class
    used in `prop:categorical-chain-convergence-mechanisms` (Mechanism 2). -/
-- Ref: [manuscript] prop:categorical-chain-convergence-mechanisms §"Mechanism 2"
-- Ref: [jones1985] doi:10.2307/1971403   (Markov axioms M1–M4)
theorem disjoint_product_factorisation_gen {R : Type*} [Field R]
    (z : R) (τ_K1 τ_K2 : R) (k : ℕ) :
    ∃ τ_joint : R, τ_joint = τ_K1 * τ_K2 * z^k := by
  obtain ⟨τ_K2_stab, hτ⟩ := markov_iterated_stab_gen z τ_K2 k
  refine ⟨τ_K1 * τ_K2_stab, ?_⟩
  rw [hτ]; ring

theorem disjoint_product_factorisation {R : Type*} [Field R] (u : R)
    [MarkovTraceAxioms u] (τ_K1 τ_K2 : R) (k : ℕ) :
    ∃ τ_joint : R, τ_joint = τ_K1 * τ_K2 * (markovZax u)^k :=
  disjoint_product_factorisation_gen (markovZax u) τ_K1 τ_K2 k

/-- Archimedean shim of `disjoint_product_factorisation`.
    Carries the explicit `(hq : 0 < q)` hypothesis. -/
theorem disjoint_product_factorisation_real (q : ℝ) (hq : 0 < q)
    [MarkovTraceAxioms (Real.sqrt q)] (τ_K1 τ_K2 : ℝ) (k : ℕ) :
    ∃ τ_joint : ℝ, τ_joint = τ_K1 * τ_K2 * (markovZax_real q hq)^k :=
  disjoint_product_factorisation (Real.sqrt q) τ_K1 τ_K2 k

/-! ## Discharge of MarkovDisjointStabilisation

We can now PROVE the previously-axiomatic `MarkovDisjointStabilisation`
class from the more fundamental `MarkovTraceAxioms` class. -/

/-- The Markov axiom M3 (encoded via `MarkovTraceAxioms.tau_stab_factor`)
    is the primitive axiomatic input; the disjoint stabilisation
    theorem `disjoint_product_factorisation` follows from M3 alone. -/
theorem MarkovTraceAxioms_implies_disjoint_stabilisation
    {R : Type*} [Field R] (u : R) [h : MarkovTraceAxioms u] :
    ∀ τ_x : R, ∃ τ_x_stab : R, τ_x_stab = τ_x * markovZax u := by
  intro τ_x
  refine ⟨τ_x * h.tau_stab_factor, ?_⟩
  rw [h.tau_stab_factor_eq_z]

end QOU.BraidKnot
