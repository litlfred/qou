import Mathlib

/-!
# QOU.MassTheory.qGaussianObstructionAtQ0

Lean statement for `prop:q-gaussian-obstruction-at-q0`. At the substrate value
`q₀ > 1` the Touchard moments `T n = Σ_π q₀^cr(π)` (sum over perfect matchings
of `[2n]`) are bounded below by the maximal-crossing term `q₀^(n(n-1)/2)`, hence
diverge — so the Bożejko–Speicher `q`-Gaussian has no representing measure
(positivity holds iff `|q| ≤ 1`). Full proof in `q-gaussian-obstruction-at-q0.md`.

**Authoring note.** The Lean toolchain is network-blocked in the authoring
environment (elan cannot reach `release.lean-lang.org`), so the proof body is a
cited `sorry` pending a Lean-enabled session.
-/

namespace QOU.MassTheory

/-- **q-Gaussian obstruction at the substrate value.** Given the maximal-crossing
    lower bound `q^(m(m-1)/2) ≤ T m` on the Touchard moments (proved
    combinatorially in the `.md`), for `q > 1` the moment sequence is unbounded —
    the super-exponential divergence that rules out a Bożejko–Speicher
    `q`-Gaussian measure at `q₀ > 1`. -/
theorem qGaussianObstructionAtQ0
    (q : ℝ) (hq : 1 < q) (T : ℕ → ℝ)
    (hT : ∀ m, q ^ (m * (m - 1) / 2) ≤ T m) :
    ∀ N : ℝ, ∃ m, N < T m := by
  sorry -- Ref: [bozejko-speicher1991] https://doi.org/10.1007/BF02100489
        -- + q-gaussian-obstruction-at-q0.md (super-exponential divergence)

end QOU.MassTheory
