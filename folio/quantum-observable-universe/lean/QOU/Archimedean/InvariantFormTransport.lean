/-
# Gauge covariance of the τ-intertwiner scale — the sign of `c` is frame-free

Epic `qou-6ufi` continuation, **re-scoped after convergence** (parallel-work
rule: converge on landing). A sibling landed the transport + assembly first —
`TauS5EquivarianceReduction.invariantForm_pullback` (invariant forms pull back
along an intertwiner, no invertibility needed) and
`tauImage_proportional_hodge` (equivariance + scalar commutant ⟹
`Pᵀ·G_M·P = c • G_H`) — which supersede this branch's independently-derived
duplicates (dropped, cited). What survives here is the **complement** neither
landed file states:

* `invariantForm_pullback_smul` — **gauge covariance of the pulled-back
  form.** Schur fixes the intertwiner `P` only up to a scalar; rescaling
  `P ↦ μ • P` rescales the pulled-back Markov Gram `Pᵀ·G_M·P` by `μ²`. Hence
  the Schur scale `c` in `tauImage_proportional_hodge` is well-defined only
  modulo `μ²` — the *magnitude* of `c` is intertwiner-gauge-dependent.
* `sq_pos_of_gauge` (over `ℝ`) — but `μ² > 0` for every admissible real gauge
  `μ ≠ 0`, so the **sign** of `c` is gauge-independent: "is `c > 0`?" is a
  well-posed, frame-free question. With the Markov Gram positive at `q₀`
  (positivity bonus, `alpha-em-b2-tau-id-c-pin` witness) and the Hodge form
  positive, the identification *requires* `c > 0` — the honest frame-free
  consistency test, and the precise reason the Option-C probe declined to
  report any frame-dependent entrywise ratio as `c`.

STRICT (§"Axiomatization is NOT a Proof", 2026-07-19 ruling): nothing here
constructs the intertwiner or evaluates `c`; no `TauRhoHodgeLift` /
`TauStdIntertwiner` instance is registered for the actual τ. `1/(8π)` stays a
phase-4 identification; nothing is wired.

-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-- Ref: [serre1977] Linear Representations of Finite Groups (Schur's lemma)
-/
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Real.Basic

namespace QOU.Archimedean.InvariantFormTransport

open Matrix

variable {n : Type*} [Fintype n] {k : Type*} [Field k]

/-- **Gauge covariance of the pulled-back form.** Rescaling the intertwiner
`P ↦ μ • P` (the Schur gauge freedom) rescales the pulled-back form
`Pᵀ * M * P` by `μ²`. Hence the proportionality scale `c` of
`TauS5EquivarianceReduction.tauImage_proportional_hodge` is well-defined only
modulo squares of the intertwiner gauge. -/
theorem invariantForm_pullback_smul (μ : k) (P M : Matrix n n k) :
    (μ • P)ᵀ * M * (μ • P) = (μ ^ 2) • (Pᵀ * M * P) := by
  rw [Matrix.transpose_smul, Matrix.smul_mul, Matrix.mul_smul, Matrix.smul_mul,
    smul_smul, sq]

/-- **The sign of the Schur scale is gauge-invariant (over `ℝ`).** Every
admissible real intertwiner gauge `μ ≠ 0` rescales the pulled-back Gram by
`μ² > 0` — so whether the τ-image of the Markov Gram is a *positive* multiple
of the Hodge Gram is a frame-independent question: the honest frame-free
consistency test of the τ-identification (positivity of the Markov Gram at
`q₀` + positivity of the Hodge form ⟹ the identification requires `c > 0`). -/
theorem sq_pos_of_gauge {μ : ℝ} (hμ : μ ≠ 0) : 0 < μ ^ 2 :=
  lt_of_le_of_ne (sq_nonneg μ) (Ne.symm (pow_ne_zero 2 hμ))

end QOU.Archimedean.InvariantFormTransport
