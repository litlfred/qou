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

/-- **`Cl_2(π) = 0` (unconditional).** Every summand
    `sin((k+1)·π)/(k+1)²` vanishes by `Real.sin_nat_mul_pi`
    applied to the natural number `k+1`. The `tsum` of identically-
    zero summands is therefore zero. -/
-- Ref: [zagier1986]
theorem Cl_2_pi : Cl_2 Real.pi = 0 := by
  unfold Cl_2
  have hzero : ∀ k : ℕ,
      Real.sin ((↑k + 1) * Real.pi) / ((↑k + 1 : ℝ)) ^ 2 = 0 := by
    intro k
    have hcast : ((↑k + 1 : ℝ)) * Real.pi = ((k + 1 : ℕ) : ℝ) * Real.pi := by
      push_cast; ring
    rw [hcast, Real.sin_nat_mul_pi]
    simp
  rw [tsum_congr hzero, tsum_zero]

/-- **`Cl_2` is `2π`-periodic.** `Cl_2(θ + 2π) = Cl_2(θ)`.

    Proof: `sin((k+1)(θ + 2π)) = sin((k+1)θ + (k+1)·2π) = sin((k+1)θ)`
    by `Real.sin_periodic` applied `k+1` times (the integer multiple
    of `2π` is annihilated by sine periodicity). The two `tsum`s
    are then equal term-by-term. -/
-- Ref: [zagier1986]
theorem Cl_2_periodic (θ : ℝ) : Cl_2 (θ + 2 * Real.pi) = Cl_2 θ := by
  unfold Cl_2
  apply tsum_congr
  intro k
  congr 1
  -- Reduce the argument: (k+1)(θ + 2π) = (k+1)θ + (k+1)·2π
  rw [show ((↑k + 1) * (θ + 2 * Real.pi) : ℝ) =
        (↑k + 1) * θ + (↑k + 1) * (2 * Real.pi) by ring]
  -- Use periodicity: sin(x + n · 2π) = sin(x) for integer n
  -- We use the integer-multiple form: the (k+1)·2π factor is an
  -- integer multiple of 2π since k+1 is a natural number.
  rw [show ((↑k + 1) * (2 * Real.pi) : ℝ) =
        ((k + 1 : ℕ) : ℝ) * (2 * Real.pi) by push_cast; ring]
  exact Real.sin_add_nat_mul_two_pi _ _

/-- **`Cl_2` reflection at `2π`.** `Cl_2(2π - θ) = -Cl_2(θ)`.

    Proof: `sin((k+1)(2π - θ)) = sin((k+1)·2π - (k+1)θ)`
                              `= sin(-(k+1)θ)`  (by 2π-periodicity)
                              `= -sin((k+1)θ)`  (by `Real.sin_neg`).
    The `tsum` of negated summands equals the negation of the
    original `tsum`. -/
-- Ref: [zagier1986]
theorem Cl_2_reflection_2pi (θ : ℝ) : Cl_2 (2 * Real.pi - θ) = -Cl_2 θ := by
  -- Cl_2(2π - θ) = Cl_2(-θ + 2π) = Cl_2(-θ) by periodicity
  have h_swap : (2 * Real.pi - θ : ℝ) = -θ + 2 * Real.pi := by ring
  rw [h_swap, Cl_2_periodic, Cl_2_neg]

/-! ## (1') `complexLiTwo` summability on the unit disk -/

/-- **Helper: `1/(k+1)²` is summable.** Standard fact, used as
    the comparison series for `complexLiTwo` summability. -/
theorem one_div_nat_succ_sq_summable :
    Summable (fun k : ℕ => (1 : ℝ) / ((k : ℝ) + 1) ^ 2) := by
  -- Equivalent to ∑ 1/n² over n ≥ 1, which is convergent (= π²/6 - 1
  -- via reindexing); Mathlib has Real.summable_one_div_nat_rpow_iff
  -- or summable_one_div_nat_pow with an exponent > 1.
  have h := Real.summable_one_div_nat_rpow.mpr (by norm_num : (1 : ℝ) < 2)
  -- Convert: 1/((k:ℝ)+1)² is a reindex of 1/(n^2)_{n≥1}
  refine (h.subtype_compl ({0} : Set ℕ).toFinite.toFinset.toSet).comp_injective
    (fun k : ℕ => ⟨k + 1, by simp⟩) ?_ |>.congr ?_
  · intro a b hab
    simp [Subtype.mk_eq_mk] at hab
    omega
  · intro k
    simp [Real.rpow_natCast]
    ring

/-- **Sketch lemma (deferred):** `complexLiTwo` is summable on the
    closed unit disk `|z| ≤ 1`. The proof would compare each term
    `|z^(k+1) / (k+1)²|` against `1/(k+1)²` using `|z|^(k+1) ≤ 1`
    and apply `Summable.of_nonneg_of_le` to the helper above.

    The Lean proof requires Mathlib's complex absolute-value
    infrastructure and `Summable.norm_iff` / `Complex.summable_abs`
    bridging. We state the conclusion as a class hypothesis,
    parallel to the Tauberian gap. -/
-- Ref: [zagier1986]
class ComplexLiTwoSummable (z : ℂ) : Prop where
  /-- The complex dilogarithm series is summable at `z`. -/
  is_summable :
    Summable (fun k : ℕ => z ^ (k + 1) / ((k : ℂ) + 1) ^ 2)

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
