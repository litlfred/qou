-- Classical limit: recovery of the symmetric path integral
-- See QOU/FeynmanPathIntegrals.lean §3 for the full formalization
--
-- Ref: [chari1994guide] Chari & Pressley, "A Guide to Quantum Groups," CUP 1994
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.

import QOU.FeynmanPathIntegrals

/-!
The q → 1 degeneration of the categorical trace to standard
quantum mechanics:

1. H_n(q) → k[S_n]  (Hecke → symmetric group)
2. tr_M → flat character trace on S_n
3. S_q(K) → S_1(K) = classical action
4. dim_q(V_λ) → 2j+1  (quantum → ordinary dimension)
5. J_K(1) = 1 for all K  (knot discrimination lost)

Lean declarations:
  - `QOU.FeynmanPathIntegrals.ClassicalLimitDegeneration`
  - `QOU.FeynmanPathIntegrals.hecke_degeneration_symmetric`
  - `QOU.FeynmanPathIntegrals.planck_at_one`
  - `QOU.FeynmanPathIntegrals.jones_trace_generator_at_one`
  - `QOU.FeynmanPathIntegrals.q_energy_classical_limit`
  - `QOU.FeynmanPathIntegrals.quantumDim_at_one`
-/


/-! ## §3b-cond conditional-class hypothesis -/

namespace QOU.FeynmanClassicalLimit.ConditionalAudit

/-- **§3b-cond hypothesis class** for `conj:classical-limit-stpart`.

    The classical-limit functor is the standard-part of evaluation at
    `q = 1 + ε`; in that limit the categorical trace degenerates so that
    the Jones polynomial loses all knot-discrimination — `J_K(1) = 1`
    for every knot `K` (clause 4 of `prop:feynman-classical-limit`).

    Content: for a given knot-indexed Jones evaluator `jones K q`, the
    value at `q = 1` is `1` for every knot. The evaluator is a parameter,
    so the class constrains it rather than asserting that some constant
    function exists. (Before 2026-11-16 the field read
    `∃ jonesAtOne : ℕ → ℝ, ∀ K, jonesAtOne K = 1`, which
    `⟨fun _ => 1, fun _ => rfl⟩` proves outright: a carrier that asserted
    nothing.) The full categorical degeneration is in
    `QOU.FeynmanPathIntegrals.ClassicalLimitDegeneration`. -/
-- Ref: [leitner2026] conj:classical-limit-stpart
class ClassicalLimitStpart (jones : ℕ → ℝ → ℝ) : Prop where
  /-- In the `q → 1` limit every knot's Jones value collapses to `1`. -/
  jones_trivial_at_one : ∀ K : ℕ, jones K 1 = 1

/-- **Conditional on `conj:classical-limit-stpart`.** At `q = 1` the
    Jones evaluator cannot distinguish two knots. Derived from the class
    hypothesis (both values equal `1`), not assumed. -/
theorem feynman_classical_limit_g3_conditional (jones : ℕ → ℝ → ℝ)
    [inst : ClassicalLimitStpart jones] :
    ∀ K₁ K₂ : ℕ, jones K₁ 1 = jones K₂ 1 := fun K₁ K₂ => by
  rw [inst.jones_trivial_at_one K₁, inst.jones_trivial_at_one K₂]

/-- The class is not trivially inhabited: an evaluator with
    `jones 0 1 = 0` admits no instance. -/
theorem classicalLimitStpart_not_trivial :
    ¬ ClassicalLimitStpart (fun _ _ => (0 : ℝ)) := fun h => by
  have := h.jones_trivial_at_one 0
  norm_num at this

end QOU.FeynmanClassicalLimit.ConditionalAudit
