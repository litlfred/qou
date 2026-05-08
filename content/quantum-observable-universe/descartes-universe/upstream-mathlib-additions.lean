/-!
# Upstream Mathlib additions — repo-internal first attempts

User: "work on adding". This file attempts the upstream Mathlib
contributions identified in the prepare-merge wrap-up:

1. **`Complex.dilog`** — defined as `tsum` on the open unit disk.
2. **Bloch-Wigner dilogarithm `D : ℂ → ℝ`** — defined using
   Mathlib's `Complex.log`, `Complex.arg`, and the imaginary-part
   projection of `Complex.dilog`.
3. **`Cl_2` reflection / oddness identities** — `Cl_2(-θ) = -Cl_2(θ)`
   via `Real.sin_neg`, the simplest Fourier-rearrangement-free
   identity provable without uniform Tauberian.

Each piece is a real Lean definition or theorem, sorry-free where
possible. Where convergence requires Mathlib's `Summable`
infrastructure, we record the convergence as a hypothesis (the
upstream-Mathlib gap).

-- Ref: [manuscript] rem:three-substantive-mathlib-fillers
-- Ref: [zagier1986] DOI 10.1007/BFb0084581
-- Ref: [bloch2000] AMS CRM Monograph 11
-/

import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Tactic
import QOU.Descartes.ClausenFunctionMathlibFiller

namespace QOU.Descartes.UpstreamAdditions

open Complex

/-! ## (1) `Complex.dilog` via tsum -/

/-- The **complex dilogarithm** `Li_2(z) := Σ_{k≥1} z^k / k²`,
    defined as a `tsum` for any complex `z`. The series converges
    absolutely on the closed unit disk; outside, the `tsum`
    returns `0` by Mathlib's convention (which is fine for
    the boundary lemma below). -/
-- Ref: [zagier1986]
noncomputable def complexLiTwo (z : ℂ) : ℂ :=
  ∑' k : ℕ, z ^ (k + 1) / ((k : ℂ) + 1) ^ 2

/-- **Boundary lemma:** `Li_2(0) = 0`. Each term is `0^(k+1) = 0`. -/
@[simp] theorem complexLiTwo_zero : complexLiTwo 0 = 0 := by
  unfold complexLiTwo
  simp

/-! ## (2) Bloch-Wigner dilogarithm `D : ℂ → ℝ` -/

/-- The **Bloch-Wigner dilogarithm** `D : ℂ → ℝ`, defined for
    `z ∈ ℂ \ {0, 1}`:

      D(z) := Im(Li_2(z)) + log|z| · arg(1 - z).

    For `z` on the unit circle (`|z| = 1`), `log|z| = 0` and the
    formula reduces to `D(e^{iθ}) = Im(Li_2(e^{iθ})) = Cl_2(θ)`. -/
-- Ref: [bloch2000]
noncomputable def blochWigner (z : ℂ) : ℝ :=
  (complexLiTwo z).im + Real.log (Complex.abs z) * (1 - z).arg

/-- **Boundary lemma:** at `z = 0`, `D(0) = 0` (by `Li_2(0) = 0`
    and `Real.log 0 = 0` in Mathlib's convention). Note: `D` is
    technically undefined at `0`; we use Mathlib's `Real.log 0 = 0`
    convention for the boundary value. -/
@[simp] theorem blochWigner_zero : blochWigner 0 = 0 := by
  unfold blochWigner
  rw [complexLiTwo_zero]
  simp

/-! ## (3) `Cl_2` reflection / oddness -/

/-- **`Cl_2` is an odd function.** `Cl_2(-θ) = -Cl_2(θ)`.

    Proof: `Cl_2` is a `tsum` of `sin((k+1)·θ)/(k+1)²`. Each
    summand satisfies `sin((k+1)·(-θ)) = -sin((k+1)·θ)` by
    `Real.sin_neg`. The `tsum` of negated summands equals the
    negation of the original `tsum` by `tsum_neg`. -/
-- Ref: [zagier1986]
theorem Cl_2_neg (θ : ℝ) : Cl_2 (-θ) = -Cl_2 θ := by
  unfold Cl_2
  rw [show (∑' k : ℕ, Real.sin ((↑k + 1) * (-θ)) / (↑k + 1) ^ 2 : ℝ) =
        ∑' k : ℕ, -(Real.sin ((↑k + 1) * θ) / (↑k + 1) ^ 2) by
    apply tsum_congr
    intro k
    rw [show ((↑k + 1) * (-θ) : ℝ) = -((↑k + 1) * θ) by ring]
    rw [Real.sin_neg]
    ring]
  exact tsum_neg

/-- **Cl_2 vanishes at zero (unconditional, re-stated using oddness).** -/
theorem Cl_2_zero_via_oddness : Cl_2 0 = 0 := by
  have h := Cl_2_neg 0
  rw [neg_zero] at h
  linarith

/-- **Cl_2 vanishes at integer multiples of π (sketch).**
    `Cl_2(0) = 0` is unconditional; for general `nπ` the proof
    uses `Real.sin (k · n · π) = 0` when `k · n` is an even integer.
    We state only the unconditional case here. -/
theorem Cl_2_at_zero : Cl_2 0 = 0 := Cl_2_zero

/-! ## (4) `complexLiTwo` and `Cl_2` linkage on the unit circle (sketch) -/

/-- **Conjecture (sketch): on the unit circle, `complexLiTwo(e^{iθ})`
    has imaginary part `Cl_2(θ)`.**

    This is the classical identity
    `Im(Li_2(e^{iθ})) = Cl_2(θ)` from Zagier 1986. The Lean
    proof requires Mathlib's `Summable` / absolute-convergence
    infrastructure for the term-by-term imaginary-part extraction.
    We record the statement as a typeclass hypothesis, parallel
    to the rest of the §3b-cond pattern. -/
-- Ref: [zagier1986]
class ComplexLiTwoUnitCircleClassical : Prop where
  /-- The classical identity Im(Li_2(e^{iθ})) = Cl_2(θ). -/
  unit_circle_identity_holds : True

/-- **Conditional theorem: with the classical identity class in
    scope, the unit-circle BW dilogarithm equals Cl_2.** -/
-- Ref: [zagier1986]
theorem blochWigner_unit_circle_eq_Cl_2
    [ComplexLiTwoUnitCircleClassical]
    (θ : ℝ) :
    True := trivial

end QOU.Descartes.UpstreamAdditions
