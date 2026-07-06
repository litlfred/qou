import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecificLimits.Basic

/-!
# QOU.MassTheory.qGaussianObstructionAtQ0

Lean statement for `prop:q-gaussian-obstruction-at-q0`. For `q > 1` the Touchard
moments `T n = Σ_π q^cr(π)` (sum over perfect matchings of `[2n]`) are bounded
below by the maximal-crossing term `q^(n(n-1)/2)`, hence diverge; with the
Bożejko–Speicher positivity bound (a positive Fock representation exists iff
`|q| ≤ 1`) this rules out a representing measure. At the substrate `q₀ ≈ 1.11 > 1`
this is the obstruction. Full proof in `q-gaussian-obstruction-at-q0.md`.

**Authoring note.** The Lean toolchain is network-blocked in the authoring
environment (elan cannot reach `release.lean-lang.org`), so the proof body is a
cited `sorry` pending a Lean-enabled session.
-/

namespace QOU.MassTheory

/-- **q-Gaussian obstruction.** Given the maximal-crossing lower bound
    `q^(m(m-1)/2) ≤ T m` on the Touchard moments (proved combinatorially in the
    `.md`), for `q > 1` the moment sequence is unbounded — the super-exponential
    divergence that witnesses the Bożejko–Speicher obstruction (a positive Fock
    representation exists iff `|q| ≤ 1`) for `q > 1`. -/
theorem qGaussianObstructionAtQ0
    (q : ℝ) (hq : 1 < q) (T : ℕ → ℝ)
    (hT : ∀ m, q ^ (m * (m - 1) / 2) ≤ T m) :
    ∀ N : ℝ, ∃ m, N < T m := by
  -- Ref: [bozejko-speicher1991] https://doi.org/10.1007/BF02100489
  --      + q-gaussian-obstruction-at-q0.md (super-exponential divergence)
  intro N
  -- `q > 1` is archimedean: some power `q ^ n` exceeds any `N`.
  obtain ⟨n, hn⟩ := pow_unbounded_of_one_lt N hq
  refine ⟨n + 1, ?_⟩
  -- the triangular exponent at `m = n+1` dominates `n`, so `q ^ n ≤ q ^ (exp)`.
  have hexp : n ≤ (n + 1) * ((n + 1) - 1) / 2 := by
    simp only [Nat.add_sub_cancel]
    rw [Nat.le_div_iff_mul_le (by norm_num)]
    nlinarith [Nat.le_mul_of_pos_left n (Nat.succ_pos n)]
  calc N < q ^ n := hn
    _ ≤ q ^ ((n + 1) * ((n + 1) - 1) / 2) := pow_le_pow_right₀ (le_of_lt hq) hexp
    _ ≤ T (n + 1) := hT (n + 1)

end QOU.MassTheory
