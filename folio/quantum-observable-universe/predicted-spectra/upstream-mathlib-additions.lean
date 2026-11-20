import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.PSeries
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Tactic
import QOU.Archimedean.ClausenFunctionMathlibFiller
import QOU.Archimedean.ClausenDoubleAngleSeries


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

-- Ref: [leitner2026] rem:three-substantive-mathlib-fillers
-- Ref: [zagier1986] DOI 10.1007/BFb0084581
-- Ref: [bloch2000] AMS CRM Monograph 11
-/

namespace QOU.Archimedean.UpstreamAdditions

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
  (complexLiTwo z).im + Real.log ‖z‖ * (1 - z).arg

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
  -- `∑ 1/(k+1)²` is the `n ↦ n+1` reindex of the convergent `p`-series
  -- `∑ 1/n²` (`Real.summable_one_div_nat_pow`, exponent `1 < 2`).
  have h : Summable (fun n : ℕ => (1 : ℝ) / (n : ℝ) ^ 2) :=
    Real.summable_one_div_nat_pow.mpr (by norm_num)
  refine ((summable_nat_add_iff 1).mpr h).congr (fun n => ?_)
  push_cast
  ring

/-- **Theorem: `complexLiTwo` is summable on the closed unit disk
    `‖z‖ ≤ 1` (proof attempt).** Compares each term
    `‖z^(k+1) / (k+1)²‖ = ‖z‖^(k+1) / (k+1)²` against the
    summable real series `1/(k+1)²` from
    `one_div_nat_succ_sq_summable`, using `‖z‖^(k+1) ≤ 1`. The
    `Summable.of_nonneg_of_le` (or `Summable.of_norm_bounded`)
    Mathlib lemma closes it.

    NOTE: this proof uses Mathlib API from `Complex.norm_div`,
    `Complex.norm_pow`, and `pow_le_one`. Without local Lean
    compilation we cannot guarantee the exact lemma names match;
    if Mathlib renames any, the proof needs a one-line patch. -/
-- Ref: [zagier1986]
theorem complexLiTwo_summable_on_unit_disk
    {z : ℂ} (hz : ‖z‖ ≤ 1) :
    Summable (fun k : ℕ => z ^ (k + 1) / ((↑k + 1 : ℂ)) ^ 2) := by
  apply Summable.of_norm
  apply Summable.of_nonneg_of_le
    (fun k => norm_nonneg _)
    ?_
    one_div_nat_succ_sq_summable
  intro k
  rw [norm_div, norm_pow]
  -- ‖z^(k+1)/((k+1)²)‖ = ‖z‖^(k+1) / ‖((k+1):ℂ)²‖ ≤ 1 / ((k+1)² : ℝ)
  have hnz : ‖z‖ ^ (k + 1) ≤ 1 := pow_le_one₀ (norm_nonneg z) hz
  -- ‖(↑k+1 : ℂ)‖ = ↑k+1: the complex denominator equals its real value.
  have hk1 : ‖(↑k + 1 : ℂ)‖ = (↑k + 1 : ℝ) := by
    rw [show ((k : ℂ) + 1) = ((k + 1 : ℕ) : ℂ) by push_cast; ring,
        Complex.norm_natCast]
    push_cast; ring
  have hdenom : ‖((↑k + 1 : ℂ)) ^ 2‖ = ((↑k + 1 : ℝ)) ^ 2 := by
    rw [norm_pow, hk1]
  rw [hdenom]
  gcongr

/-- **Class form for downstream use.** Some downstream blocks
    take `complexLiTwo`'s summability as a typeclass hypothesis;
    we provide both the unconditional theorem above and the
    class form here for backward compatibility with the §3b-cond
    pattern. -/
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
    to the rest of the §3b-cond pattern. Per AGENTS.md §3b-tax the
    class field carries the **content** of the conjecture — the
    parameter-quantified identity in the shape of the claim — not a
    bare `True` marker. -/
-- Ref: [zagier1986]
class ComplexLiTwoUnitCircleClassical : Prop where
  /-- The classical identity `Im(Li_2(e^{iθ})) = Cl_2(θ)` for every
      angle `θ` (Zagier 1986; the imaginary part of the complex
      dilogarithm on the unit circle is the Clausen function). -/
  unit_circle_identity :
    ∀ θ : ℝ, (complexLiTwo (Complex.exp (θ * Complex.I))).im = Cl_2 θ

/-- **Conditional theorem: with the classical identity class in
    scope, the Bloch-Wigner dilogarithm on the unit circle equals
    `Cl_2`.** Since `‖e^{iθ}‖ = 1`, the `log‖z‖` correction term in
    `blochWigner` vanishes, so `D(e^{iθ}) = Im(Li_2(e^{iθ})) = Cl_2(θ)`.
    Derived from the class field — not asserted as `True`. -/
-- Ref: [zagier1986], [bloch2000]
theorem blochWigner_unit_circle_eq_Cl_2
    [hC : ComplexLiTwoUnitCircleClassical]
    (θ : ℝ) :
    blochWigner (Complex.exp (θ * Complex.I)) = Cl_2 θ := by
  unfold blochWigner
  rw [Complex.norm_exp]
  simp only [Complex.mul_I_re, Complex.ofReal_im, neg_zero, Real.exp_zero,
    Real.log_one, zero_mul, add_zero]
  exact hC.unit_circle_identity θ

/-! ## (5) Cl_2 double-angle functional equation -/

/-- The **Cl_2 double-angle functional equation** (Spence-Lewin
    form, restricted to Cl_2):

      Cl_2(2θ) = 2 · Cl_2(θ) - 2 · Cl_2(π - θ).

    This is the imaginary-part projection of the classical
    Spence-Lewin / Landen identity for `Li_2`:

      Li_2(z²) = 2·Li_2(z) + 2·Li_2(-z),

    after the standard substitution `Li_2(-z) = π²/6 - Li_2(1+z)`
    and taking imaginary parts on the unit circle.

    **The class is now inhabited** (2026-11-20, bean `qou-eao2`): the instance
    `instCl_2_DoubleAngle` below is supplied by the sorry-free series proof
    `QOU.Archimedean.ClausenDoubleAngleSeries.Cl_2_double_angle`, valid for
    every real `θ`. This docstring used to say a direct `tsum` proof was
    blocked because `sin(2kθ) = 2 sin(kθ) cos(kθ)` is not linear in the
    `sin(kθ)`. That was a mis-diagnosis. The proof does not expand `sin(2kθ)`.
    It uses `sin((k+1)(π − θ)) = (−1)^k sin((k+1)θ)`, so that
    `Cl_2(θ) − Cl_2(π − θ)` keeps only the odd-`k` terms, and those terms are
    `Cl_2(2θ)/4` re-indexed. No dilogarithm is needed. (The interval version
    on `(0, π)` was already proved as `QOU.Knot.Cl_2_duplication`.)

    The class is kept so that existing `[Cl_2_DoubleAngle]` binders still
    resolve; with the instance in scope they are discharged automatically. -/
-- Ref: [zagier1986], [bloch2000]
class Cl_2_DoubleAngle : Prop where
  /-- The Spence-Lewin double-angle identity for Cl_2. -/
  double_angle :
    ∀ θ : ℝ,
      Cl_2 (2 * θ) = 2 * Cl_2 θ - 2 * Cl_2 (Real.pi - θ)

/-- **Conditional theorem (sorry-free).** With the double-angle
    class in scope, the identity holds. Boundary case: at `θ = 0`,
    both sides reduce to `Cl_2(0) = 0` directly without invoking
    the class hypothesis (since `Cl_2(2·0) = Cl_2(0) = 0` and
    `2·Cl_2(0) - 2·Cl_2(π) = 0 - 0 = 0`). -/
-- Ref: [zagier1986]
theorem Cl_2_double_angle [hC : Cl_2_DoubleAngle] (θ : ℝ) :
    Cl_2 (2 * θ) = 2 * Cl_2 θ - 2 * Cl_2 (Real.pi - θ) :=
  hC.double_angle θ

/-- **The genuine instance** of `Cl_2_DoubleAngle`, from the series proof for
    every real `θ` (`ClausenDoubleAngleSeries.Cl_2_double_angle`, sorry-free). -/
-- Ref: [lewin1981] §4.2
instance instCl_2_DoubleAngle : Cl_2_DoubleAngle :=
  ⟨QOU.Archimedean.ClausenDoubleAngleSeries.Cl_2_double_angle⟩

/-- **Boundary unconditional check:** at `θ = 0`, the double-angle
    identity reduces to `Cl_2(0) = 0` on both sides (using
    `Cl_2(0) = 0` and `Cl_2(π) = 0` from `Cl_2_pi`). -/
-- Ref: [zagier1986]
theorem Cl_2_double_angle_at_zero_unconditional :
    Cl_2 (2 * 0) = 2 * Cl_2 0 - 2 * Cl_2 (Real.pi - 0) := by
  rw [mul_zero, Cl_2_zero, sub_zero, Cl_2_pi]
  ring

/-- **Boundary unconditional check:** at `θ = π`, the double-angle
    identity reduces to `Cl_2(2π) = 2·Cl_2(π) - 2·Cl_2(0) = 0`.
    Uses `Cl_2_periodic` for the LHS and `Cl_2_pi` + `Cl_2_zero`
    for the RHS. -/
-- Ref: [zagier1986]
theorem Cl_2_double_angle_at_pi_unconditional :
    Cl_2 (2 * Real.pi) = 2 * Cl_2 Real.pi - 2 * Cl_2 (Real.pi - Real.pi) := by
  rw [Cl_2_pi, sub_self, Cl_2_zero]
  -- LHS: Cl_2 (2 π) = Cl_2 (0 + 2 π) = Cl_2 0 = 0 by 2π-periodicity
  rw [show (2 * Real.pi : ℝ) = 0 + 2 * Real.pi by ring,
      Cl_2_periodic, Cl_2_zero]
  ring

/-- **Boundary unconditional check:** at `θ = π/2`, the double-angle
    identity becomes `Cl_2(π) = 2·Cl_2(π/2) - 2·Cl_2(π/2) = 0`, a
    tautology that follows from `Cl_2_pi` alone. -/
-- Ref: [zagier1986]
theorem Cl_2_double_angle_at_pi_half_unconditional :
    Cl_2 (2 * (Real.pi / 2))
      = 2 * Cl_2 (Real.pi / 2) - 2 * Cl_2 (Real.pi - Real.pi / 2) := by
  -- LHS: Cl_2 (2 · π/2) = Cl_2 π = 0
  rw [show (2 * (Real.pi / 2) : ℝ) = Real.pi by ring, Cl_2_pi]
  -- RHS: π - π/2 = π/2, so RHS = 2·Cl_2(π/2) - 2·Cl_2(π/2) = 0
  rw [show (Real.pi - Real.pi / 2 : ℝ) = Real.pi / 2 by ring]
  ring

end QOU.Archimedean.UpstreamAdditions
