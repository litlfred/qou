import Mathlib.Analysis.SpecialFunctions.Complex.Arg
import Mathlib.Data.Complex.BigOperators

/-!
# QOU.MathlibExt.HalfPlaneNonCancellation — an oscillatory sum that cannot cancel

Bean `qou-mlgp` **Gap 5**.

## The asymmetry this addresses

For a sum of complex numbers Mathlib gives the **upper** bound for free —
`norm_sum_le` is the triangle inequality — and nothing at all in the other
direction. That asymmetry is exactly the corpus's blocker. Every volume-conjecture
instance needs

    (2π/N) · log‖⟨K⟩_N‖  →  Vol(K),

the upper half of which follows from `‖Σ zₖ‖ ≤ Σ‖zₖ‖` plus a majorant estimate, and the
lower half of which needs to know the phases did **not** conspire to cancel. The corpus
has the upper halves (`norm_whiteheadLinkKashaev_le`, the `W6` majorant rate) and is
stuck on the lower ones (`WhiteheadLinkLowerRate.lower`,
`VdVWhiteheadLemma4.phase_cost`).

## What is actually provable, cheaply

Full non-cancellation for an arbitrary oscillatory sum is false, and proving it in the
cases that matter is the method of steepest descent — the expensive thing this bean's
Gap 5 is about. But there is a large, elementary special case:

> **terms confined to a half-plane cannot cancel.**

If every term lies in the closed cone of half-angle `α < π/2` about some direction, the
sum keeps at least `cos α` of its mass. No analysis, no asymptotics — one rotation and
the triangle inequality in the other direction (`Re w ≤ ‖w‖`).

Measured on the Whitehead-chain sums at `q = e^{2πi/N}`, the **inner** clasp sum is
exactly phase-free (arc `0.00°`) and at the neighbouring root `e^{2πi/(N+½)}` it spans
`≈ 90°` at the dominant index — comfortably inside a half-plane, giving a clean factor
`1/√2`.

## ⚠ What this lemma does NOT reach, and why — measured 2026-08-31

An earlier revision of this header claimed the lemma "settles the inner sums outright
and isolates the outer one as the real obstruction". **Neither half of that is a gain,
and the file should not advertise one.**

* The inner sums are *already* settled without it. In the corpus's own transcription
  (`QOU/Knot/WhiteheadLinkScaffold.lean`) the inner sum `Σ_k S_{n,k}` is a sum of
  **real positive** terms — `whiteheadTerm_pos`, `whiteheadLink_inner_pos` — so
  `‖Σ‖ = Σ‖·‖` holds on the nose and there is nothing for a `cos α` factor to buy.
* The outer sum is not merely "not confined"; it is confined *nowhere*, and the failure
  gets worse with `N`. The Fresnel phase is
  `θ_n = −n(n+1−N)π/(2N)` (`whiteheadLinkPhase`), whose total sweep over
  `n ∈ [0, N)` is `(N−1)²π/(8N) ≈ Nπ/8` radians — **unbounded**. Measured arc covered
  mod `2π`: `135.0°` at `N = 8`, `303.8°` at `N = 32`, `340.3°` at `N = 128`,
  `349.5°` at `N = 256`, i.e. → `360°`. A half-plane hypothesis here would need
  `α ≳ 175°`, and `cos α < 0` makes the conclusion vacuous.

So the only sum in the corpus whose lower bound is open
(`VdVWhiteheadLemma4` / `WhiteheadLinkLowerRate`) is exactly the one this lemma cannot
touch, and a conditional theorem "phases half-plane-confined ⟹ Lemma 4" was
deliberately **not** written: its hypothesis is measured false, so it would be vacuous
content dressed as progress. What is recorded instead is the measurement, which closes
the elementary route.

The lemma remains correct, upstreamable, and the right tool wherever a genuinely
localised (windowed) sum appears — but it has no consumer in this corpus today, and
saying so is more useful than a forced one.

## Scope

Pure complex analysis — no knots, no Kashaev invariant, no volume. Upstreamable
unchanged.

Archimedean (ℂ).
-/

namespace QOU.MathlibExt

open Finset Complex

variable {ι : Type*}

/-- **No cancellation after a rotation, in terms of real parts.**

If some unit `u` rotates every term so that its real part is at least `c` times its
norm, then the sum keeps at least the fraction `c` of the total mass.

This is the whole content; the arg-based statement below is a repackaging. The proof is
three steps — sum the pointwise bound, pull the rotation out of the sum, and use
`Re w ≤ ‖w‖`, which is the reverse-direction triangle inequality that `norm_sum_le` does
not provide.

`c` is unconstrained: it may be negative, in which case the conclusion is weak but true,
and `c = 0` recovers the trivial bound. -/
theorem norm_sum_ge_of_rotated_re (s : Finset ι) (z : ι → ℂ) (u : ℂ) (hu : ‖u‖ = 1)
    (c : ℝ) (h : ∀ i ∈ s, c * ‖z i‖ ≤ (u * z i).re) :
    c * ∑ i ∈ s, ‖z i‖ ≤ ‖∑ i ∈ s, z i‖ := by
  rw [Finset.mul_sum]
  calc ∑ i ∈ s, c * ‖z i‖
      ≤ ∑ i ∈ s, (u * z i).re := Finset.sum_le_sum h
    _ = (u * ∑ i ∈ s, z i).re := by rw [Finset.mul_sum, Complex.re_sum]
    _ ≤ ‖u * ∑ i ∈ s, z i‖ := Complex.re_le_norm _
    _ = ‖∑ i ∈ s, z i‖ := by rw [norm_mul, hu, one_mul]

/-- **Terms in a half-plane keep a `cos α` share of their mass.**

If, after rotating by `e^{-iθ}`, every term has argument within `α ≤ π/2` of the real
axis — i.e. the terms lie in a closed cone of half-angle `α` about direction `θ` — then

    `cos α · Σ‖zᵢ‖ ≤ ‖Σ zᵢ‖`.

At `α = π/2` this degenerates to `0 ≤ ‖Σ zᵢ‖`, which is the honest boundary: a closed
half-plane permits `1 + (−1) · i·i`-style cancellation only in the limit, and the bound
must vanish there. Strictly inside, the constant is strictly positive and *independent
of the number of terms* — which is what makes it useful against a sum whose length grows
with `N`.

Zero terms are allowed and need no hypothesis: `arg 0 = 0`, so they satisfy the bound
automatically. -/
theorem cos_mul_sum_norm_le_norm_sum (s : Finset ι) (z : ι → ℂ) (θ : ℝ) {α : ℝ}
    (hα0 : 0 ≤ α) (hα : α ≤ Real.pi / 2)
    (h : ∀ i ∈ s, |arg (exp (-(θ : ℂ) * I) * z i)| ≤ α) :
    Real.cos α * ∑ i ∈ s, ‖z i‖ ≤ ‖∑ i ∈ s, z i‖ := by
  refine norm_sum_ge_of_rotated_re s z (exp (-(θ : ℂ) * I)) ?_ _ ?_
  · -- `‖e^{-iθ}‖ = 1`
    rw [show (-(θ : ℂ) * I) = ((-θ : ℝ) : ℂ) * I by push_cast; ring]
    exact Complex.norm_exp_ofReal_mul_I _
  · intro i hi
    set w : ℂ := exp (-(θ : ℂ) * I) * z i with hw
    have hnorm : ‖w‖ = ‖z i‖ := by
      rw [hw, norm_mul,
        show (-(θ : ℂ) * I) = ((-θ : ℝ) : ℂ) * I by push_cast; ring,
        Complex.norm_exp_ofReal_mul_I, one_mul]
    rw [← hnorm]
    rcases eq_or_ne w 0 with hz | hz
    · simp [hz]
    · -- `Re w = ‖w‖ · cos (arg w)` and `cos` is decreasing on `[0, π]`
      -- `arg` is signed, so evenness of `cos` has to come first: the monotonicity
      -- lemma wants a nonnegative left argument, and `|arg w|` is the one we bound.
      have hcos : Real.cos α ≤ Real.cos (arg w) := by
        rw [← Real.cos_abs (arg w)]
        exact Real.cos_le_cos_of_nonneg_of_le_pi (abs_nonneg _)
          (by linarith [Real.pi_pos]) (h i hi)
      have hre : (w.re) = ‖w‖ * Real.cos (arg w) := by
        rw [Complex.cos_arg hz]
        field_simp
      calc Real.cos α * ‖w‖ ≤ Real.cos (arg w) * ‖w‖ := by
            exact mul_le_mul_of_nonneg_right hcos (norm_nonneg _)
        _ = w.re := by rw [hre]; ring

end QOU.MathlibExt
