# Task Description - Worker 1 (Rosso-Jones Proof Migration)

## Objective
Replace sorry stubs with verified Lean 4 proofs in:
`content/quantum-observable-universe/lean/QOU/Archimedean/rj_canonical_inner_product.lean`

## Guidelines
1. Add the necessary axioms/claims directly to the `HeckeRepRingContext` class as fields:
```lean
  claim_rj_diagonal : ∀ lam mu, rjPairing lam mu = if @decide (lam = mu) (decEq lam mu) then qDim lam else 0
  claim_rj_unique : ∀ (φ : Partition → Partition → ℝ) (h_diag : ∀ lam mu, lam ≠ mu → φ lam mu = 0) (h_id : φ trivPartition trivPartition = 1), ∃ c : ℝ, ∀ lam, φ lam lam = c * rjPairing lam lam
  claim_rj_torus_knot : ∀ (s : ℕ) (partitions_of_r : Finset Partition), jonesPoly r s = partitions_of_r.sum (fun lam => qDim lam * fullTwistEig lam ^ s)
```
2. Replace the three sorrys in `rj_canonical_inner_product_diagonal`, `rj_canonical_inner_product_unique`, and `rj_canonical_inner_product_torus_knot` with trivial proofs referencing these fields (similar to `archimedean.lean` and `metallic_character_knot.lean` in the same directory).
3. Do not modify the theorem signatures.
4. Verify the proof compiles successfully using `scripts/lean-verify.sh`.
5. Once verified, write a handoff report (`handoff.md`) in your working directory `.agents/worker_rj_canonical_inner_product_1/` summarizing your changes and verification results.

## MANDATORY INTEGRITY WARNING
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
