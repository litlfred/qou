## 2026-06-23T20:18:12-04:00
You are worker_batch6_m3_fourier. Your working directory is `/Users/litlfred/space_cats/qou/.agents/worker_batch6_m3_fourier/`.
Your task is to replace the `sorry` statement in `content/quantum-observable-universe/lean/QOU/orbital_fourier_decomposition.lean` with a valid Lean proof.
Math info:
This is a class context proof. The theorem is `orbital_fourier_decomposition`.
The context class has:
  claim_orbital_fourier_decomposition : k = 2 * (n - 1 : ℤ) ∧ ℓ < n ∧ -(ℓ : ℤ) ≤ m ∧ m ≤ (ℓ : ℤ) ∧ (s = 1/2 ∨ s = -(1/2))
So the proof is simply:
  ctx.claim_orbital_fourier_decomposition
Ensure you insert `import Mathlib` at the top of the file since it uses `ℝ`, `ℕ`, and `ℤ`.
Verify your proof compiles successfully by running `scripts/lean-verify.sh content/quantum-observable-universe/lean/QOU/orbital_fourier_decomposition.lean`.
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
Write a handoff report in your working directory and send a completion message to the parent (conversation ID: 837fa052-e939-4f89-aa75-7a97078c29a4).
