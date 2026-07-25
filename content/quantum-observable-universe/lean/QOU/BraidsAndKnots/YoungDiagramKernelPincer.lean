import QOU.BraidsAndKnots.YoungDiagramKernel
import QOU.BraidsAndKnots.YoungDiagramTransposeBridge
import QOU.BraidsAndKnots.YoungDiagramKernelDimPos
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# QOU.BraidsAndKnots.YoungDiagramKernelPincer — the two-leg pincer scaffold for the kernel sign

The covariance kernel `covariance_kernel_conjecture` (`kernelValue k ≤ 0`, OPEN) has exactly one
live full-proof route after the recorded eliminations (holonomic, FKG, peeling, transpose-parity,
genus, complete monotonicity): the **tilt-interpolation pincer**. Tilt the Plancherel-squared
weight `(f^λ)²` by `exp(θ·ln f^λ)` and set `g(θ) := E_{2+θ}[ω₃]`; then `g(0) = 0` exactly, the
kernel sign is `g(1) ≤ 0`, and the pincer closes it from two legs:

* **[A2]** `g′(0) = Cov₂(ln f^λ, ω₃) ≤ 0` (the log-dimension/content-spread anti-correlation), and
* **[A3]** the interpolation remainder is dominated: `|g(1) − Cov₂(ln f, ω₃)| ≤ −Cov₂(ln f, ω₃)`.

This file **formalizes the scaffold** (formalize-first): the tilted objects as finite real sums
over the `partsOf` enumeration, the explicit finite-sum covariance `covLnF`, the pure-arithmetic
pincer lemma, and the conditional derivation

    `KernelPincerLegs k`  (mean-zero + A2 + A3, a §3b-cond content-bearing class, NO instance)
      ⟹  `tiltedMean k 1 ≤ 0`  ⟹  `kernelValue k ≤ 0`

so the two legs become the pinned Lean targets. All theorems here are sorry-free; the open
content is carried honestly by the *instance-less* class (§3b-tax: fields are the conjecture's
**inputs**; the kernel bound is genuinely **derived** from them through the positivity/cast
bridge — not a self-assuming projection).

## What is and is not asserted

* The identification `g′(0) = covLnF k` (real differentiation of the finite tilted sums) is the
  next analytic tranche and is **not** asserted here; [A3] is therefore stated directly as the
  remainder-vs-`covLnF` bound, which is the exact inequality the pincer consumes. Arithmetic
  makes [A2] a consequence of [A3] (`pincer_arith_forces_A2`); both are kept as named fields
  because the attack proves them separately (A2 via the hook/Frullani reduction, A3 via uniform
  mixed-cumulant bounds).
* `mean_zero` (`E₂[ω₃] = 0`) is an **exact identity** (regular-character orthogonality),
  `decide`-verified `k ≤ 7` in ℤ-form (`secondMomentKernel_eq_zero_of_le_seven`); its general
  real-form proof rides the same character bridge and is kept as a field until that lands.
* The dimension-positivity hypothesis `∀ l ∈ partsOf k, 0 < sytDim l` is true (`f^λ = #SYT ≥ 1`)
  but its list-level proof needs the HLF divisibility bridge (`hookProd ∣ (sum l)!`); it is taken
  as an explicit hypothesis on the bridge theorems and discharged when that bridge lands.

Base ring (§7c): genuinely archimedean (`Real.exp`, `Real.log`), so `ℝ`. Standalone library file
(no `.ts`/`.md` sibling), verified per-file by `lean`-direct, like its parents.

-- Ref: [manuscript] docs/audits/2026-07-18-deltalambda-covariance-kernel-frontier.md
-/

namespace QOU.BraidsAndKnots.YoungDiagramKernelPincer

open QOU.BraidsAndKnots.YoungDiagramKernel
open QOU.BraidsAndKnots.YoungDiagramTransposeBridge

/-! ## The tilted objects -/

/-- The tilted weight `f² · exp(θ·ln f)` — at `θ = 0` this is the Plancherel-squared weight `f²`;
at `θ = 1` (for `f > 0`) it is `f³`, the kernel's weight. -/
noncomputable def tilt (θ : ℝ) (f : ℕ) : ℝ := (f : ℝ) ^ 2 * Real.exp (θ * Real.log f)

/-- Tilted partition function `Z(θ) = Σ_{λ⊢k} f^{2+θ}`. -/
noncomputable def tiltNorm (k : ℕ) (θ : ℝ) : ℝ :=
  ((partsOf k).map (fun l => tilt θ (sytDim l))).sum

/-- Tilted `ω₃`-sum `W(θ) = Σ_{λ⊢k} f^{2+θ}·ω₃(λ)`. -/
noncomputable def tiltOmega (k : ℕ) (θ : ℝ) : ℝ :=
  ((partsOf k).map (fun l => tilt θ (sytDim l) * (omega3 k l : ℝ))).sum

/-- The tilted mean `g(θ) = E_{2+θ}[ω₃] = W(θ)/Z(θ)` — the pincer's interpolating function.
`g(0) = 0` exactly; the kernel sign is `g(1) ≤ 0`. -/
noncomputable def tiltedMean (k : ℕ) (θ : ℝ) : ℝ := tiltOmega k θ / tiltNorm k θ

/-- First mixed moment `E₂[ln f · ω₃]`. -/
noncomputable def lnDimOmegaMoment (k : ℕ) : ℝ :=
  ((partsOf k).map (fun l =>
    tilt 0 (sytDim l) * Real.log (sytDim l) * (omega3 k l : ℝ))).sum / tiltNorm k 0

/-- First log-dimension moment `E₂[ln f]`. -/
noncomputable def lnDimMoment (k : ℕ) : ℝ :=
  ((partsOf k).map (fun l => tilt 0 (sytDim l) * Real.log (sytDim l))).sum / tiltNorm k 0

/-- **The [A2] quantity**: the finite-sum covariance
`Cov₂(ln f, ω₃) = E₂[ln f·ω₃] − E₂[ln f]·E₂[ω₃]` — the first-order response of the tilted mean,
whose nonpositivity is the log-dimension/content-spread anti-correlation leg. -/
noncomputable def covLnF (k : ℕ) : ℝ :=
  lnDimOmegaMoment k - lnDimMoment k * tiltedMean k 0

/-! ## The pure-arithmetic pincer -/

/-- **The pincer, as bare arithmetic**: if the interpolation error of `g1` against the
first-order value `d` is dominated by `−d`, then `g1 ≤ 0`. -/
theorem pincer_arith {g1 d : ℝ} (hR : |g1 - d| ≤ -d) : g1 ≤ 0 := by
  have h := (abs_le.mp hR).2
  linarith

/-- The remainder domination *forces* leg [A2] arithmetically (`|·| ≥ 0` ⇒ `d ≤ 0`) — recorded so
the two legs' logical relationship is explicit: [A3] as stated subsumes [A2]; they remain
separate targets because the attack proves them by different routes. -/
theorem pincer_arith_forces_A2 {g1 d : ℝ} (hR : |g1 - d| ≤ -d) : d ≤ 0 := by
  have h := abs_nonneg (g1 - d)
  linarith

/-! ## The conditional legs (§3b-cond, content-bearing, NO instance — the open targets) -/

/-- **The two pincer legs + the exact tilt-mean-zero identity** for level `k`. Content-bearing
`Prop` class with **no instance** — providing an instance for all `k` IS closing the covariance
kernel. Fields:

* `mean_zero` — `g(0) = E₂[ω₃] = 0`: exact (regular-character orthogonality); ℤ-form
  `decide`-verified `k ≤ 7` in `YoungDiagramKernel.secondMomentKernel_eq_zero_of_le_seven`.
* `leg_A2` — `Cov₂(ln f, ω₃) ≤ 0`: the anti-correlation leg (hook/Frullani route).
* `leg_A3` — `|g(1) − Cov₂(ln f, ω₃)| ≤ −Cov₂(ln f, ω₃)`: the remainder-domination leg (uniform
  mixed-cumulant route; its *interpretation* as a second-order Taylor bound rides the separate
  `g′(0) = covLnF` identification, not asserted in this file). -/
class KernelPincerLegs (k : ℕ) : Prop where
  mean_zero : tiltedMean k 0 = 0
  leg_A2 : covLnF k ≤ 0
  leg_A3 : |tiltedMean k 1 - covLnF k| ≤ -(covLnF k)

/-- **Conditional kernel sign at the tilted-mean level**: the legs force `g(1) ≤ 0`. -/
theorem tiltedMean_one_nonpos (k : ℕ) [h : KernelPincerLegs k] : tiltedMean k 1 ≤ 0 :=
  pincer_arith h.leg_A3

/-! ## Bridging `g(1) ≤ 0` back to `kernelValue k ≤ 0` -/

/-- The single-row partition `[k]` is enumerated: `partsOf k` is nonempty for `k ≥ 1`. -/
theorem singleRow_mem_partsOf (k : ℕ) (hk : 1 ≤ k) : [k] ∈ partsOf k := by
  apply mem_partsFuel [k] k k k
  · simp
  · intro x hx
    simp only [List.mem_singleton] at hx
    omega
  · intro x hx
    simp only [List.mem_singleton] at hx
    omega
  · exact List.sorted_singleton k
  · simpa using hk

/-- The tilted weight is positive at positive dimension. -/
theorem tilt_pos {f : ℕ} (θ : ℝ) (hf : 0 < f) : 0 < tilt θ f := by
  unfold tilt
  have hfR : (0 : ℝ) < (f : ℝ) := by exact_mod_cast hf
  exact mul_pos (pow_pos hfR 2) (Real.exp_pos _)

/-- The tilted partition function is positive (given the dimension positivity, which is true —
`f^λ = #SYT ≥ 1` — and discharged list-level when the HLF divisibility bridge lands). -/
theorem tiltNorm_pos (k : ℕ) (θ : ℝ) (hk : 1 ≤ k)
    (hf : ∀ l ∈ partsOf k, 0 < sytDim l) : 0 < tiltNorm k θ := by
  unfold tiltNorm
  apply List.sum_pos
  · intro x hx
    obtain ⟨l, hl, rfl⟩ := List.mem_map.mp hx
    exact tilt_pos θ (hf l hl)
  · simp only [ne_eq, List.map_eq_nil_iff]
    exact List.ne_nil_of_mem (singleRow_mem_partsOf k hk)

/-- **At `θ = 1` the tilted `ω₃`-sum IS the kernel**: `W(1) = kernelValue k` (cast to `ℝ`), since
`f²·exp(ln f) = f³` at positive dimension. -/
theorem tiltOmega_one_eq_kernelValue (k : ℕ)
    (hf : ∀ l ∈ partsOf k, 0 < sytDim l) :
    tiltOmega k 1 = (kernelValue k : ℝ) := by
  have hcast : ((kernelValue k : ℤ) : ℝ)
      = ((partsOf k).map (fun l => ((sytDim l : ℝ)) ^ 3 * (omega3 k l : ℝ))).sum := by
    unfold kernelValue
    rw [Int.cast_list_sum, List.map_map]
    refine congrArg List.sum (List.map_congr_left fun l _ => ?_)
    simp only [Function.comp_apply, omega3]
    push_cast
    ring
  rw [hcast]
  unfold tiltOmega
  refine congrArg List.sum (List.map_congr_left fun l hl => ?_)
  have hfl : (0 : ℝ) < (sytDim l : ℝ) := by exact_mod_cast hf l hl
  unfold tilt
  rw [one_mul, Real.exp_log hfl]
  ring

/-- **The conditional kernel bound (capstone, hypothesis-free)**: the two pincer legs close the
covariance-kernel conjecture at level `k` — `kernelValue k ≤ 0` is *derived* from
`KernelPincerLegs k` through the positivity of the tilted partition function (dimension
positivity now *proved*, `YoungDiagramKernelDimPos.sytDim_pos_of_mem_partsOf`) and the `θ = 1`
bridge. Providing the (currently absent) instance for all `k` is exactly the open problem. -/
theorem kernelValue_nonpos_of_legs (k : ℕ) [KernelPincerLegs k] (hk : 1 ≤ k) :
    kernelValue k ≤ 0 := by
  have hf := YoungDiagramKernelDimPos.sytDim_pos_of_mem_partsOf k
  have hZ := tiltNorm_pos k 1 hk hf
  have hg := tiltedMean_one_nonpos k
  have hW : tiltOmega k 1 ≤ 0 := by
    have h2 : tiltOmega k 1 = tiltedMean k 1 * tiltNorm k 1 := by
      unfold tiltedMean
      rw [div_mul_cancel₀ _ (ne_of_gt hZ)]
    rw [h2]
    have h3 := mul_le_mul_of_nonneg_right hg (le_of_lt hZ)
    simpa using h3
  rw [tiltOmega_one_eq_kernelValue k hf] at hW
  exact_mod_cast hW

end QOU.BraidsAndKnots.YoungDiagramKernelPincer
