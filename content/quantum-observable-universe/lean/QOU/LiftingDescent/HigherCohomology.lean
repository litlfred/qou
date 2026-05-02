/-!
# QOU.LiftingDescent.HigherCohomology — magic shell requires higher-cohomological knot operator

The SDP optimum at substrate `q_0` decomposes via the spectral
sequence `E_r^{p, q}(n)` of `conj:homological-shell-condensation`.
The conjecture below claims: at magic `n`, the optimum has
non-trivial contribution in `E_∞^{p, q ≥ 1}` (higher cohomology,
non-Hopf-decomposable, brane-tower-derived); at non-magic `n`, the
optimum is purely in `E_∞^{0, *}` (Hopf-decomposable, descended
Markov trace).

LaTeX label: `conj:magic-requires-higher-cohomology`

## References

- [yekutieli2010] https://doi.org/10.1142/9789814322188
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [mathas1999] https://doi.org/10.1090/ulect/015
- [manuscript] lifting-and-descent / magic-requires-higher-cohomology
-/

import QOU.LiftingDescent.HomologicalCondensation

namespace QOU.LiftingDescent.HigherCohomology

open QOU.LiftingDescent.HomologicalCondensation

/-! ## §1  Surrogate predicates -/

/-- The SDP optimum at strand count `n` and substrate `q` has
    *non-trivial contribution* in cohomological degrees `p` and
    `q ≥ 1`. Concrete instances will tie this to spectral-sequence
    decomposition. -/
opaque OptimumHasHigherCohomologyContribution (n : ℕ) (q : ℝ) : Prop

/-- The SDP optimum at `(n, q)` lies *entirely* in `E_∞^{0, *}`
    (purely descended / Markov-trace piece, Hopf-decomposable). -/
opaque OptimumPurelyDescended (n : ℕ) (q : ℝ) : Prop

/-! ## §2  The higher-cohomology conjecture -/

/-- **Conjecture (Proposition 8).** At substrate `q = q_0`, the
    magic predicate equates with non-trivial higher-cohomological
    contribution to the SDP optimum:

      n magic at q_0  ↔  OptimumHasHigherCohomologyContribution n q_0

    Equivalently:

      n non-magic at q_0  ↔  OptimumPurelyDescended n q_0

    The two predicates partition the integers (modulo the trivial
    `n ≤ 0` and degenerate `n = 1`). -/
-- Ref: [manuscript] conj:magic-requires-higher-cohomology
class MagicRequiresHigherCohomology where
  q_0_value : ℝ
  q_0_pos : 1 < q_0_value
  /-- Magic ↔ higher-cohomology contribution. -/
  magic_iff_higher_cohom :
    ∀ (n : ℕ),
      n ∈ magicLadder ↔ OptimumHasHigherCohomologyContribution n q_0_value
  /-- Non-magic ↔ purely descended. -/
  nonmagic_iff_descended :
    ∀ (n : ℕ),
      n ∉ magicLadder ↔ OptimumPurelyDescended n q_0_value

/-- Re-export forward direction. -/
-- Ref: [manuscript] conj:magic-requires-higher-cohomology
theorem higher_cohom_at_magic
    [C : MagicRequiresHigherCohomology]
    {n : ℕ} (hn : n ∈ magicLadder) :
    OptimumHasHigherCohomologyContribution n C.q_0_value :=
  (C.magic_iff_higher_cohom n).mp hn

/-- Re-export reverse direction. -/
-- Ref: [manuscript] conj:magic-requires-higher-cohomology
theorem magic_of_higher_cohom
    [C : MagicRequiresHigherCohomology]
    {n : ℕ}
    (h : OptimumHasHigherCohomologyContribution n C.q_0_value) :
    n ∈ magicLadder :=
  (C.magic_iff_higher_cohom n).mpr h

/-- Re-export: at non-magic `n`, the optimum is purely descended
    (Hopf-decomposable). -/
-- Ref: [manuscript] conj:magic-requires-higher-cohomology
theorem descended_at_nonmagic
    [C : MagicRequiresHigherCohomology]
    {n : ℕ} (hn : n ∉ magicLadder) :
    OptimumPurelyDescended n C.q_0_value :=
  (C.nonmagic_iff_descended n).mp hn

/-! ## §3  Per-n typeclass decomposition + structural reduction -/

/-- Per-n assertion: `n` is *known* to have a higher-cohomology
    SDP-optimum contribution at `q`. -/
class IsKnownHigherCohom (n : ℕ) (q : ℝ) : Prop where
  has_higher : OptimumHasHigherCohomologyContribution n q

/-- Per-n assertion: `n` is *known* to have a purely-descended
    SDP optimum at `q`. -/
class IsKnownPurelyDescended (n : ℕ) (q : ℝ) : Prop where
  is_descended : OptimumPurelyDescended n q

/-- **Assembly theorem.** If at substrate `q` (with `q > 1`) we have
    per-n axioms

      IsKnownHigherCohom n q  for every n ∈ magicLadder,
      IsKnownPurelyDescended n q  for every n ≥ 2 with n ∉ magicLadder,

    plus a *partition* axiom (no n satisfies both), then the
    `MagicRequiresHigherCohomology` conjecture holds at `q`.

    The `n ≥ 2` restriction handles n = 0 (vacuum, no operator) and
    n = 1 (single strand, trivially descended). -/
-- Ref: [manuscript] conj:magic-requires-higher-cohomology
theorem magicRequiresHigherCohom_iff_perN_axioms_at
    {q : ℝ} (h_q : 1 < q)
    (h_in : ∀ n, n ∈ magicLadder → IsKnownHigherCohom n q)
    (h_out : ∀ n, 2 ≤ n → n ∉ magicLadder → IsKnownPurelyDescended n q)
    -- Partition axiom: no n is simultaneously higher-cohom and purely descended.
    (h_partition :
      ∀ n,
        ¬ (OptimumHasHigherCohomologyContribution n q
          ∧ OptimumPurelyDescended n q)) :
    ∀ n, 2 ≤ n →
      (n ∈ magicLadder ↔ OptimumHasHigherCohomologyContribution n q) := by
  intro n hn
  constructor
  · intro h_in_ladder
    exact (h_in n h_in_ladder).has_higher
  · intro h_higher
    by_contra h_not_in
    have h_desc := (h_out n hn h_not_in).is_descended
    exact h_partition n ⟨h_higher, h_desc⟩

end QOU.LiftingDescent.HigherCohomology
