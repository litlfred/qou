import Mathlib.Algebra.BigOperators.Finprod
import Mathlib.Data.Real.Basic

/-!
# The Rosso–Jones index set: quantified vs. data

Run:  `LEAN_PATH=<mathlib oleans> lean <this file>`  ->  exit 0.

`QOU/Archimedean/rj_canonical_inner_product.lean` stated the Rosso–Jones
formula `J(τ(r,s)) = Σ_{λ ⊢ r} d_λ ω_λ^s` with the **index set
universally quantified**:

    jonesPoly_eq_eval : ∀ s (partitions_of_r : Finset Partition),
      jonesPoly r s = partitions_of_r.sum (fun lam => …)

The sum is over the partitions *of r* — one specific finite set — so
quantifying over every `Finset` asserts far more than the theorem.
Instantiating at `∅` collapses the whole claim.

Note what did **not** catch this. The class stayed *inhabitable* (take
every scalar zero), so no vacuity check and no `False`-derivation fires;
the defect is collapse, not inconsistency. It was found by
`scripts/unbounded-quantifier-audit.py`, which looks for a bound or
identity asserted over an unconstrained quantified variable.
-/

namespace QOU.Audits.RossoJonesProbe

variable {P : Type}

/-- **The old shape collapses.** With the index set quantified, the empty
    `Finset` forces the Jones polynomial to vanish for every `s` —
    whatever the pairing and eigenvalues are. -/
theorem quantified_index_forces_zero
    (jonesPoly : ℕ → ℕ → ℝ) (rjPairing : P → P → ℝ) (fullTwistEig : P → ℝ)
    (r : ℕ)
    (h : ∀ (s : ℕ) (partitions_of_r : Finset P),
      jonesPoly r s
        = partitions_of_r.sum (fun lam => rjPairing lam lam * fullTwistEig lam ^ s))
    (s : ℕ) : jonesPoly r s = 0 := by
  simpa using h s (∅ : Finset P)

/-- **The fixed shape does not collapse.** With the index set carried as
    data, a model with a non-vanishing Jones polynomial exists — so the
    repair is a genuine correction and not merely a different way to say
    nothing. -/
example : ∃ (jonesPoly : ℕ → ℕ → ℝ) (rjPairing : Unit → Unit → ℝ)
    (fullTwistEig : Unit → ℝ) (partitionsOf : Finset Unit),
    (∀ s : ℕ, jonesPoly 1 s
      = partitionsOf.sum (fun lam => rjPairing lam lam * fullTwistEig lam ^ s))
    ∧ jonesPoly 1 0 ≠ 0 := by
  refine ⟨fun _ _ => 1, fun _ _ => 1, fun _ => 1, {()}, fun s => ?_, by norm_num⟩
  simp

end QOU.Audits.RossoJonesProbe
