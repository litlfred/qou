import Mathlib.Tactic

/-!
# QOU.BraidKnot.SpinInvolutionLPDualInvariance

**Canonical declaration** for content block at
[`quantum-observable-universe/mass-theory/spin-involution-lp-dual-invariance-proof.ts`](quantum-observable-universe/mass-theory/spin-involution-lp-dual-invariance-proof.ts).

Formalises the manuscript proof that the spin involution `σ` is an isometry
of the Frobenius pairing `⟨a,b⟩ = τ(ab)` and leaves the LP cost functional
invariant (Steps 1 and 3). The apparatus — trace `τ`, anti-multiplicative
involution `σ` with `τ∘σ = τ` and cyclic `τ` — is axiomatised as a context
class (pure algebra over a generic ring; §7c-clean).
-/

namespace QOU.BraidKnot

/-- The spin-involution / Frobenius-trace apparatus.

    A `definition` carrier: a ring `A`, the Markov trace `τ`, the spin
    involution `σ`, and its structural properties — anti-multiplicativity
    `σ(a)σ(b) = σ(ba)`, involutivity `σ∘σ = id`, trace-invariance `τ∘σ = τ`,
    the cyclic (Markov) property `τ(ab) = τ(ba)`, and a `σ`-fixed cost `c`. -/
structure SpinInvolutionLPDualInvariance (A : Type*) [Ring A] where
  /-- The Markov trace `τ : A → ℝ`. -/
  τ : A → ℝ
  /-- The spin involution `σ`. -/
  σ : A → A
  /-- Anti-multiplicativity: `σ(a)·σ(b) = σ(b·a)`. -/
  sigma_antimul : ∀ a b : A, σ a * σ b = σ (b * a)
  /-- `σ` is involutive. -/
  sigma_involutive : ∀ a : A, σ (σ a) = a
  /-- Trace-invariance `τ ∘ σ = τ`. -/
  trace_sigma : ∀ a : A, τ (σ a) = τ a
  /-- Cyclic / Markov property `τ(ab) = τ(ba)`. -/
  tau_cyclic : ∀ a b : A, τ (a * b) = τ (b * a)
  /-- The LP cost element `c`, fixed by `σ`. -/
  c : A
  /-- `σ` fixes the cost: `σ(c) = c`. -/
  sigma_c : σ c = c

namespace SpinInvolutionLPDualInvariance

variable {A : Type*} [Ring A] (S : SpinInvolutionLPDualInvariance A)

/-- The Frobenius pairing `⟨a,b⟩ = τ(ab)`. -/
def pairing (a b : A) : ℝ := S.τ (a * b)

/-- **Step 1.** `σ` is an isometry of the Frobenius pairing:
    `⟨σa, σb⟩ = ⟨a, b⟩`. -/
theorem sigma_isometry (a b : A) : S.pairing (S.σ a) (S.σ b) = S.pairing a b := by
  unfold pairing
  rw [S.sigma_antimul, S.trace_sigma, S.tau_cyclic]

/-- **Step 3.** The cost functional `τ(c · x)` is `σ`-invariant:
    `τ(c · σx) = τ(c · x)`. -/
theorem cost_invariant (x : A) : S.τ (S.c * S.σ x) = S.τ (S.c * x) := by
  calc S.τ (S.c * S.σ x)
      = S.τ (S.σ x * S.c) := S.tau_cyclic _ _
    _ = S.τ (S.σ x * S.σ (S.c)) := by rw [S.sigma_c]
    _ = S.τ (S.σ (S.c * x)) := by rw [S.sigma_antimul]
    _ = S.τ (S.c * x) := S.trace_sigma _

end SpinInvolutionLPDualInvariance

-- Ref: [manuscript] quantum-observable-universe/mass-theory/spin-involution-lp-dual-invariance-proof.ts

end QOU.BraidKnot
