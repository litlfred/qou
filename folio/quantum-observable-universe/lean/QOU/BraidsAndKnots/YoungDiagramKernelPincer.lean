import QOU.BraidsAndKnots.YoungDiagramKernel
import QOU.BraidsAndKnots.YoungDiagramTransposeBridge
import QOU.BraidsAndKnots.YoungDiagramKernelDimPos
import QOU.BraidKnot.IdentityIContentDecomposition
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.Calculus.Deriv.Slope

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

-- Ref: [leitner2026] docs/audits/2026-07-18-deltalambda-covariance-kernel-frontier.md
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

/-! ### Discharging `mean_zero` on the certified range

`mean_zero` is the one member of `KernelPincerLegs` that is **not** conjectural — it is the exact
identity `k!·E_Planch[ω₃] = 0`. Its ℤ-form `secondMomentKernel k = 0` is `decide`-verified for
`k ≤ 20` (`YoungDiagramKernel.secondMomentKernel_eq_zero_of_le_twenty`). The three lemmas below
build the missing ℝ-side bridge, so that on the certified range the hypothesis is **discharged**
rather than assumed: a `[KernelPincerLegs k]` instance for `3 ≤ k ≤ 20` needs only the two
genuinely open legs `A2` and `A3`.

The general-`k` statement remains open *as Lean* (not as mathematics): the character-orthogonality
proof needs the Jucys–Murphy-eigenvalue ⇒ Plancherel-mean bridge — the identity coefficient of
`Σ_i X_i²` is `#{(i,j) : j < i} = C(k,2)` — which is Sₙ representation-theory infrastructure the
corpus does not yet carry. Recording it as a certified floor keeps a provable premise from sitting
silently beside two open ones (the `conditional-proved ≠ premise-established` discipline). -/

/-- At `θ = 0` the tilt is the plain squared dimension: `tilt 0 f = f²` (no positivity needed —
the exponent `0 · log f` vanishes even at `f = 0`). -/
theorem tilt_zero (f : ℕ) : tilt 0 f = (f : ℝ) ^ 2 := by
  unfold tilt
  rw [zero_mul, Real.exp_zero, mul_one]

/-- **At `θ = 0` the tilted `ω₃`-sum IS the dim²-weighted content-spread total**:
`W(0) = secondMomentKernel k` (cast to `ℝ`). The ℝ-side twin of
`tiltOmega_one_eq_kernelValue`. -/
theorem tiltOmega_zero_eq_secondMomentKernel (k : ℕ) :
    tiltOmega k 0 = (secondMomentKernel k : ℝ) := by
  have hcast : ((secondMomentKernel k : ℤ) : ℝ)
      = ((partsOf k).map (fun l => ((sytDim l : ℝ)) ^ 2 * (omega3 k l : ℝ))).sum := by
    unfold secondMomentKernel
    rw [Int.cast_list_sum, List.map_map]
    refine congrArg List.sum (List.map_congr_left fun l _ => ?_)
    simp only [Function.comp_apply]
    push_cast
    ring
  rw [hcast]
  unfold tiltOmega
  refine congrArg List.sum (List.map_congr_left fun l _ => ?_)
  rw [tilt_zero]

/-- **The mean-zero bridge**: the ℤ-form vanishing `Σ_λ (f^λ)²·ω₃(λ) = 0` gives the scaffold's
`mean_zero` hypothesis `E₂[ω₃] = 0` outright (the quotient's numerator vanishes, so no
non-degeneracy of the normalisation is needed). -/
theorem tiltedMean_zero_of_secondMomentKernel_eq_zero (k : ℕ) (h : secondMomentKernel k = 0) :
    tiltedMean k 0 = 0 := by
  unfold tiltedMean
  rw [tiltOmega_zero_eq_secondMomentKernel, h, Int.cast_zero, zero_div]

/-- **`mean_zero` is discharged for `3 ≤ k ≤ 20`** — not assumed. On this range the pincer's
premise set reduces to the two genuinely open legs. -/
theorem tiltedMean_zero_of_le_twenty (k : ℕ) (hk : 3 ≤ k) (hk' : k ≤ 20) :
    tiltedMean k 0 = 0 :=
  tiltedMean_zero_of_secondMomentKernel_eq_zero k
    (YoungDiagramKernel.secondMomentKernel_eq_zero_of_le_twenty k hk hk')

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

/-! ## The derivative identification: `g′(0) = covLnF`

The remaining analytic content of the scaffold: the [A2] quantity `covLnF` **is** the derivative
of the tilted mean at `θ = 0`, so `leg_A2`/`leg_A3` genuinely are the first-order coefficient and
Taylor remainder of the pincer interpolation — closing the gap flagged in this file's header
("the identification `g′(0) = covLnF k` … is the next analytic tranche"). -/

/-- Derivative of a finite list sum, term by term. -/
theorem hasDerivAt_list_sum {ι : Type*} (L : List ι) (F : ι → ℝ → ℝ) (F' : ι → ℝ) (x : ℝ)
    (h : ∀ i ∈ L, HasDerivAt (F i) (F' i) x) :
    HasDerivAt (fun θ => (L.map (fun i => F i θ)).sum) ((L.map F').sum) x := by
  induction L with
  | nil => simpa using hasDerivAt_const x (0 : ℝ)
  | cons a t ih =>
      simp only [List.map_cons, List.sum_cons]
      exact (h a List.mem_cons_self).add
        (ih fun i hi => h i (List.mem_cons_of_mem a hi))

/-- The tilted weight is differentiable in `θ` with logarithmic derivative `ln f`:
`(d/dθ) f^{2+θ} = f^{2+θ}·ln f`. -/
theorem hasDerivAt_tilt (f : ℕ) (θ₀ : ℝ) :
    HasDerivAt (fun θ => tilt θ f) (tilt θ₀ f * Real.log f) θ₀ := by
  unfold tilt
  have h1 : HasDerivAt (fun θ : ℝ => θ * Real.log f) (Real.log f) θ₀ := by
    simpa using (hasDerivAt_id θ₀).mul_const (Real.log f)
  have h2 := h1.exp
  have h3 := h2.const_mul ((f : ℝ) ^ 2)
  convert h3 using 1
  ring

/-- The tilted partition function differentiates term by term:
`Z′(0) = Σ f²·ln f` (the `lnDimMoment` numerator). -/
theorem hasDerivAt_tiltNorm_zero (k : ℕ) :
    HasDerivAt (fun θ => tiltNorm k θ)
      (((partsOf k).map (fun l => tilt 0 (sytDim l) * Real.log (sytDim l))).sum) 0 := by
  unfold tiltNorm
  exact hasDerivAt_list_sum (partsOf k) _ _ 0 fun l _ => hasDerivAt_tilt (sytDim l) 0

/-- The tilted `ω₃`-sum differentiates term by term:
`W′(0) = Σ f²·ln f·ω₃` (the `lnDimOmegaMoment` numerator). -/
theorem hasDerivAt_tiltOmega_zero (k : ℕ) :
    HasDerivAt (fun θ => tiltOmega k θ)
      (((partsOf k).map (fun l =>
        tilt 0 (sytDim l) * Real.log (sytDim l) * (omega3 k l : ℝ))).sum) 0 := by
  unfold tiltOmega
  exact hasDerivAt_list_sum (partsOf k) _ _ 0 fun l _ =>
    (hasDerivAt_tilt (sytDim l) 0).mul_const ((omega3 k l : ℝ))

/-- **The derivative identification (the analytic leg of the scaffold, now closed)**:
`g′(0) = covLnF k` — the tilted mean has derivative exactly the finite-sum covariance
`Cov₂(ln f, ω₃)` at `θ = 0`. Quotient rule on the term-by-term derivatives, with the tilted
partition function nonvanishing by the (proved) dimension positivity. Hence `leg_A2` is
literally the sign of `g′(0)`, and `leg_A3` is literally the first-order Taylor-remainder
bound: the class fields are the pincer's genuine analytic legs. -/
theorem hasDerivAt_tiltedMean_zero (k : ℕ) (hk : 1 ≤ k) :
    HasDerivAt (tiltedMean k) (covLnF k) 0 := by
  have hf := YoungDiagramKernelDimPos.sytDim_pos_of_mem_partsOf k
  have hZ0 : tiltNorm k 0 ≠ 0 := (tiltNorm_pos k 0 hk hf).ne'
  have hquot := (hasDerivAt_tiltOmega_zero k).div (hasDerivAt_tiltNorm_zero k) hZ0
  have hEq : covLnF k
      = ((((partsOf k).map (fun l =>
            tilt 0 (sytDim l) * Real.log (sytDim l) * (omega3 k l : ℝ))).sum) * tiltNorm k 0
          - tiltOmega k 0 *
            (((partsOf k).map (fun l => tilt 0 (sytDim l) * Real.log (sytDim l))).sum))
        / tiltNorm k 0 ^ 2 := by
    unfold covLnF lnDimOmegaMoment lnDimMoment tiltedMean
    field_simp
  rw [show tiltedMean k = fun θ => tiltOmega k θ / tiltNorm k θ from rfl, hEq]
  exact hquot

/-- The `deriv`-form restatement: `deriv (g k) 0 = Cov₂(ln f, ω₃)`. -/
theorem deriv_tiltedMean_zero (k : ℕ) (hk : 1 ≤ k) :
    deriv (tiltedMean k) 0 = covLnF k :=
  (hasDerivAt_tiltedMean_zero k hk).deriv

/-! ## The hook form of leg [A2]

The FRT quotient turns the log-dimension into log-factorial-minus-log-hooks,
`ln f = ln k! − ln ∏h`, and covariance kills the constant, so

    `covLnF k = − Cov₂(ln ∏h, ω₃)`.

Hence **[A2] ⇔ the hook–spread positive correlation** `Cov₂(ln ∏h, ω₃) ≥ 0` — two "spread"
functionals of the diagram positively correlated under the Plancherel-squared weight. This is the
first *exact* step of the A2 hook/Frullani reduction
(`wlambda-covariance-epic-A2-hook-reduction.witness.json`). **Status of the further Frullani
step (corrected 2026-07-25):** the integral representation
`Cov₂(ln f, ω₃) = ∫₀^∞ (1/s)·Cov₂(Σ_□ e^{−s·h}, ω₃) ds` itself survives, but the once-conjectured
*pointwise* sign of its integrand is **FALSE for `n ≥ 29`** (first failure `max_s ≈ +0.056` at
`s ≈ 0.52`, growing with `n`) — A2 holds by cancellation in `s`, not pointwise; see
`docs/audits/2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md`. The live lead is
the moment-skeleton / even-hook-power route (`a168710a0d`: even hook-power moment positivity
PROVED). -/

/-- Finite list sums subtract termwise. -/
theorem list_sum_map_sub {ι : Type*} (L : List ι) (f g : ι → ℝ) :
    (L.map (fun i => f i - g i)).sum = (L.map f).sum - (L.map g).sum := by
  induction L with
  | nil => simp
  | cons a t ih =>
      simp only [List.map_cons, List.sum_cons, ih]
      ring

/-- Constants scale out of finite list sums. -/
theorem list_sum_map_mul_left {ι : Type*} (L : List ι) (c : ℝ) (f : ι → ℝ) :
    (L.map (fun i => c * f i)).sum = c * (L.map f).sum := by
  induction L with
  | nil => simp
  | cons a t ih =>
      simp only [List.map_cons, List.sum_cons, ih]
      ring

/-- **The FRT log identity** on enumerated partitions: `ln f = ln k! − ln ∏h` — the real form of
`numSYTenum · prodHooks = n!` through the (proved) hook-product bridge and dimension
positivity. -/
theorem log_sytDim_eq (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (hpos : ∀ x ∈ l, 0 < x) :
    Real.log (sytDim l) = Real.log (l.sum).factorial - Real.log (hookProd l) := by
  have hph : 0 < hookProd l := by
    rw [YoungDiagramKernelDimPos.hookProd_eq_prodHooks l hs]
    exact QOU.Mathlib.SYTEnum.prodHooks_pos l hs hpos
  have hmul : sytDim l * hookProd l = (l.sum).factorial := by
    rw [YoungDiagramKernelDimPos.sytDim_eq_numSYTenum l hs hpos,
      YoungDiagramKernelDimPos.hookProd_eq_prodHooks l hs]
    exact QOU.Mathlib.SYTEnum.numSYTenum_mul_prodHooks l hs hpos
  have hcast : (sytDim l : ℝ) = ((l.sum).factorial : ℝ) / (hookProd l : ℝ) := by
    have hphR : (hookProd l : ℝ) ≠ 0 := by exact_mod_cast hph.ne'
    field_simp
    exact_mod_cast hmul
  rw [hcast, Real.log_div (by
      exact_mod_cast (Nat.factorial_pos (l.sum)).ne') (by exact_mod_cast hph.ne')]

/-- First log-hook moment `E₂[ln ∏h]`. -/
noncomputable def lnHookMoment (k : ℕ) : ℝ :=
  ((partsOf k).map (fun l => tilt 0 (sytDim l) * Real.log (hookProd l))).sum / tiltNorm k 0

/-- First mixed log-hook moment `E₂[ln ∏h · ω₃]`. -/
noncomputable def lnHookOmegaMoment (k : ℕ) : ℝ :=
  ((partsOf k).map (fun l =>
    tilt 0 (sytDim l) * Real.log (hookProd l) * (omega3 k l : ℝ))).sum / tiltNorm k 0

/-- **The hook–spread covariance** `Cov₂(ln ∏h, ω₃)` — the [A2] quantity in hook form. -/
noncomputable def covLnHooks (k : ℕ) : ℝ :=
  lnHookOmegaMoment k - lnHookMoment k * tiltedMean k 0

/-- **The exact hook reduction of leg [A2]**: `Cov₂(ln f, ω₃) = −Cov₂(ln ∏h, ω₃)`. The
log-factorial is constant on `partsOf k` (every enumerated partition sums to `k`), and covariance
kills constants. -/
theorem covLnF_eq_neg_covLnHooks (k : ℕ) : covLnF k = -covLnHooks k := by
  have hlog : ∀ l ∈ partsOf k,
      tilt 0 (sytDim l) * Real.log (sytDim l)
        = tilt 0 (sytDim l) * Real.log (k.factorial)
          - tilt 0 (sytDim l) * Real.log (hookProd l) := by
    intro l hl
    obtain ⟨hsum, hpos, hsort⟩ := partsOf_facts k l hl
    rw [log_sytDim_eq l hsort hpos, hsum]
    ring
  have hlogω : ∀ l ∈ partsOf k,
      tilt 0 (sytDim l) * Real.log (sytDim l) * (omega3 k l : ℝ)
        = Real.log (k.factorial) * (tilt 0 (sytDim l) * (omega3 k l : ℝ))
          - tilt 0 (sytDim l) * Real.log (hookProd l) * (omega3 k l : ℝ) := by
    intro l hl
    obtain ⟨hsum, hpos, hsort⟩ := partsOf_facts k l hl
    rw [log_sytDim_eq l hsort hpos, hsum]
    ring
  have hnum1 : ((partsOf k).map (fun l => tilt 0 (sytDim l) * Real.log (sytDim l))).sum
      = Real.log (k.factorial) * tiltNorm k 0
        - ((partsOf k).map (fun l => tilt 0 (sytDim l) * Real.log (hookProd l))).sum := by
    rw [List.map_congr_left hlog, list_sum_map_sub]
    congr 1
    unfold tiltNorm
    rw [show (fun l => tilt 0 (sytDim l) * Real.log (k.factorial))
          = (fun l => Real.log (k.factorial) * tilt 0 (sytDim l)) from
        funext fun l => mul_comm _ _, list_sum_map_mul_left]
  have hnum2 : ((partsOf k).map (fun l =>
        tilt 0 (sytDim l) * Real.log (sytDim l) * (omega3 k l : ℝ))).sum
      = Real.log (k.factorial) * tiltOmega k 0
        - ((partsOf k).map (fun l =>
            tilt 0 (sytDim l) * Real.log (hookProd l) * (omega3 k l : ℝ))).sum := by
    rw [List.map_congr_left hlogω, list_sum_map_sub]
    congr 1
    unfold tiltOmega
    rw [list_sum_map_mul_left]
  unfold covLnF lnDimOmegaMoment lnDimMoment covLnHooks lnHookOmegaMoment lnHookMoment
    tiltedMean
  rw [hnum1, hnum2]
  rcases eq_or_ne (tiltNorm k 0) 0 with hZ | hZ
  · simp [hZ]
  · field_simp
    ring

/-- **Leg [A2] in hook form**: `Cov₂(ln f, ω₃) ≤ 0 ↔ 0 ≤ Cov₂(ln ∏h, ω₃)` — the anti-correlation
of dimension with spread is exactly the *positive* correlation of total log-hook with spread. The
open [A2] target, restated on the hook statistic. (The pointwise-in-`s` Frullani attack on it is
refuted for `n ≥ 29`; the surviving routes are integral-level cancellation and the
moment-skeleton / even-hook-power lead.) -/
theorem covLnF_nonpos_iff (k : ℕ) : covLnF k ≤ 0 ↔ 0 ≤ covLnHooks k := by
  rw [covLnF_eq_neg_covLnHooks]
  constructor <;> intro h <;> linarith

/-! ## The second-moment anchor: `Cov₂(Σ_□h², ω₃) = Var₂(ω₃) ≥ 0`

The surviving A2 lead (the moment skeleton) constrains the hook-spectrum covariances
`ν_v = Cov₂(N_v, ω₃)` by exact moments; its second moment is `Σ_v v²·ν_v = Cov₂(Σ_□h², ω₃)`.
The classical identity `Σ_□h² = Σ_□c² + n²` (proved outright in the corpus,
`IdentityI.sumSqHooks_eq_sumSqContents_add_sq`) makes the hook-square statistic a *constant
shift* of `ω₃` on `partsOf k` — so this covariance **is** the variance of `ω₃`, hence
nonnegative. Lean-locks the anchor `Σ_v v²·ν_v = Var₂(ω₃) ≥ 0` of the ν-system. -/

/-- Finite list sums add termwise. -/
theorem list_sum_map_add {ι : Type*} (L : List ι) (f g : ι → ℝ) :
    (L.map (fun i => f i + g i)).sum = (L.map f).sum + (L.map g).sum := by
  induction L with
  | nil => simp
  | cons a t ih =>
      simp only [List.map_cons, List.sum_cons, ih]
      ring

/-- `IdentityI.sumSqContents` is the kernel's `contentSq` (two formalizations of the same
nested sum). -/
theorem sumSqContents_eq_contentSq (l : List ℕ) :
    QOU.BraidKnot.IdentityI.sumSqContents l = contentSq l := by
  unfold QOU.BraidKnot.IdentityI.sumSqContents
  rw [contentSq_eq_finset_sum, list_sum_map_range]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [list_sum_map_range]

/-- **The hook-square statistic is a constant shift of `ω₃`** on enumerated partitions:
`Σ_□h² = ω₃ + C(k,2) + k²` — the corpus identity `Σh² = Σc² + n²` plus `Σc² = ω₃ + C(k,2)`,
with both shift terms constant across `partsOf k`. -/
theorem sumSqHooks_eq_omega3_add (k : ℕ) (l : List ℕ) (hl : l ∈ partsOf k) :
    QOU.BraidKnot.IdentityI.sumSqHooks l
      = omega3 k l + ((k * (k - 1) / 2 : ℕ) : ℤ) + (k : ℤ) ^ 2 := by
  obtain ⟨hsum, _, hsort⟩ := partsOf_facts k l hl
  have h1 := QOU.BraidKnot.IdentityI.sumSqHooks_eq_sumSqContents_add_sq l hsort
  have hsz : QOU.BraidKnot.IdentityI.sz l = k := hsum
  rw [h1, sumSqContents_eq_contentSq, hsz]
  unfold omega3
  ring

/-- Second moment `E₂[ω₃²]`. -/
noncomputable def omegaSqMoment (k : ℕ) : ℝ :=
  ((partsOf k).map (fun l => tilt 0 (sytDim l) * (omega3 k l : ℝ) ^ 2)).sum / tiltNorm k 0

/-- **The variance `Var₂(ω₃)`** under the Plancherel-squared weight. -/
noncomputable def omegaVar (k : ℕ) : ℝ := omegaSqMoment k - tiltedMean k 0 ^ 2

/-- First hook-square moment `E₂[Σh²]`. -/
noncomputable def hookSqMoment (k : ℕ) : ℝ :=
  ((partsOf k).map (fun l =>
    tilt 0 (sytDim l) * (QOU.BraidKnot.IdentityI.sumSqHooks l : ℝ))).sum / tiltNorm k 0

/-- Mixed hook-square moment `E₂[Σh²·ω₃]`. -/
noncomputable def hookSqOmegaMoment (k : ℕ) : ℝ :=
  ((partsOf k).map (fun l =>
    tilt 0 (sytDim l) * (QOU.BraidKnot.IdentityI.sumSqHooks l : ℝ)
      * (omega3 k l : ℝ))).sum / tiltNorm k 0

/-- **The second moment of the ν-system**: `Cov₂(Σ_□h², ω₃)`. -/
noncomputable def covHookSq (k : ℕ) : ℝ :=
  hookSqOmegaMoment k - hookSqMoment k * tiltedMean k 0

/-- **`Cov₂(Σ_□h², ω₃) = Var₂(ω₃)`** — the constant shift drops from the covariance. -/
theorem covHookSq_eq_omegaVar (k : ℕ) : covHookSq k = omegaVar k := by
  set c : ℝ := ((((k * (k - 1) / 2 : ℕ) : ℤ) + (k : ℤ) ^ 2 : ℤ) : ℝ) with hc
  have hshift : ∀ l ∈ partsOf k,
      (QOU.BraidKnot.IdentityI.sumSqHooks l : ℝ) = (omega3 k l : ℝ) + c := by
    intro l hl
    rw [hc]
    exact_mod_cast congrArg (fun z : ℤ => (z : ℝ))
      (by rw [sumSqHooks_eq_omega3_add k l hl]; ring :
        QOU.BraidKnot.IdentityI.sumSqHooks l
          = omega3 k l + (((k * (k - 1) / 2 : ℕ) : ℤ) + (k : ℤ) ^ 2))
  have hnum1 : ((partsOf k).map (fun l =>
        tilt 0 (sytDim l) * (QOU.BraidKnot.IdentityI.sumSqHooks l : ℝ))).sum
      = tiltOmega k 0 + c * tiltNorm k 0 := by
    rw [List.map_congr_left (fun l hl => by rw [hshift l hl]; ring :
      ∀ l ∈ partsOf k, tilt 0 (sytDim l) * (QOU.BraidKnot.IdentityI.sumSqHooks l : ℝ)
        = tilt 0 (sytDim l) * (omega3 k l : ℝ) + c * tilt 0 (sytDim l))]
    rw [list_sum_map_add, list_sum_map_mul_left]
    rfl
  have hnum2 : ((partsOf k).map (fun l =>
        tilt 0 (sytDim l) * (QOU.BraidKnot.IdentityI.sumSqHooks l : ℝ)
          * (omega3 k l : ℝ))).sum
      = ((partsOf k).map (fun l =>
          tilt 0 (sytDim l) * (omega3 k l : ℝ) ^ 2)).sum + c * tiltOmega k 0 := by
    rw [List.map_congr_left (fun l hl => by rw [hshift l hl]; ring :
      ∀ l ∈ partsOf k, tilt 0 (sytDim l) * (QOU.BraidKnot.IdentityI.sumSqHooks l : ℝ)
          * (omega3 k l : ℝ)
        = tilt 0 (sytDim l) * (omega3 k l : ℝ) ^ 2
            + c * (tilt 0 (sytDim l) * (omega3 k l : ℝ)))]
    rw [list_sum_map_add, list_sum_map_mul_left]
    rfl
  unfold covHookSq hookSqOmegaMoment hookSqMoment omegaVar omegaSqMoment tiltedMean
  rw [hnum1, hnum2]
  rcases eq_or_ne (tiltNorm k 0) 0 with hZ | hZ
  · simp [hZ]
  · field_simp
    ring

/-- The tilted weight is nonnegative (with no positivity hypothesis). -/
theorem tilt_nonneg (θ : ℝ) (f : ℕ) : 0 ≤ tilt θ f :=
  mul_nonneg (sq_nonneg _) (Real.exp_pos _).le

/-- The variance in centered form: `Var₂(ω₃) = E₂[(ω₃ − E₂[ω₃])²]`. -/
theorem omegaVar_eq_centered (k : ℕ) :
    omegaVar k = ((partsOf k).map (fun l =>
      tilt 0 (sytDim l) * ((omega3 k l : ℝ) - tiltedMean k 0) ^ 2)).sum / tiltNorm k 0 := by
  have hexp : ∀ l ∈ partsOf k,
      tilt 0 (sytDim l) * ((omega3 k l : ℝ) - tiltedMean k 0) ^ 2
        = tilt 0 (sytDim l) * (omega3 k l : ℝ) ^ 2
            + ((-(2 * tiltedMean k 0)) * (tilt 0 (sytDim l) * (omega3 k l : ℝ))
              + tiltedMean k 0 ^ 2 * tilt 0 (sytDim l)) := by
    intro l _
    ring
  rw [List.map_congr_left hexp, list_sum_map_add, list_sum_map_add,
    list_sum_map_mul_left, list_sum_map_mul_left]
  have hW : ((partsOf k).map (fun l => tilt 0 (sytDim l) * (omega3 k l : ℝ))).sum
      = tiltOmega k 0 := rfl
  have hZr : ((partsOf k).map (fun l => tilt 0 (sytDim l))).sum = tiltNorm k 0 := rfl
  rw [hW, hZr]
  unfold omegaVar omegaSqMoment tiltedMean
  rcases eq_or_ne (tiltNorm k 0) 0 with hZ | hZ
  · simp [hZ]
  · field_simp
    ring

/-- **The second-moment anchor, Lean-locked**: `0 ≤ Cov₂(Σ_□h², ω₃)` — the ν-system's second
moment `Σ_v v²·ν_v` is a variance, hence nonnegative, at every level `k`. (Contrast with the
*zeroth* moment `Σ_v ν_v = 0` and the refuted pointwise sign: the moment skeleton's exact
constraints survive and this one is now machine-checked.) -/
theorem covHookSq_nonneg (k : ℕ) : 0 ≤ covHookSq k := by
  rw [covHookSq_eq_omegaVar, omegaVar_eq_centered]
  apply div_nonneg
  · apply List.sum_nonneg
    intro x hx
    obtain ⟨l, _, rfl⟩ := List.mem_map.mp hx
    exact mul_nonneg (tilt_nonneg 0 _) (sq_nonneg _)
  · unfold tiltNorm
    apply List.sum_nonneg
    intro x hx
    obtain ⟨l, _, rfl⟩ := List.mem_map.mp hx
    exact tilt_nonneg 0 _

/-! ## The hook spectrum and the ν-system

The surviving A2 lead works with the **hook spectrum** `N_v(λ) = #{□ ∈ λ : h(□) = v}` and the
signed measure `ν_v = Cov₂(N_v, ω₃)`; A2 is its log-moment sign (`Σ_v ln(v)·ν_v ≥ 0`, cf.
`covLnF_nonpos_iff`), its second moment is the proved `Cov₂(Σh², ω₃) = Var₂(ω₃) ≥ 0`, and its
zeroth moment vanishes. This section defines the spectrum and ν in Lean, proves the **spectral
decomposition** `Σ_v φ(v)·N_v = Σ_□ φ(h(□))` for every `φ` (fiberwise over the cell set), and
locks the **zeroth-moment constraint** `Σ_v ν_v = 0`. Bookkeeping note: sums run over
`v < 2k + 1` via the cheap hook bound `h ≤ λ_i + λ'_j ≤ 2k`; the classical tight bound is
`h ≤ k`, but any range containing all hooks gives the same constraints (empty fibers contribute
`ν_v = 0`). -/

/-- The hook length of a cell, in the kernel's per-cell form `λ_i + λ'_j − j − i − 1`. -/
def hookLen (l : List ℕ) (p : ℕ × ℕ) : ℕ :=
  l.getD p.1 0 + (conj l).getD p.2 0 - p.2 - p.1 - 1

/-- **The hook spectrum** `N_v(λ)`: the number of cells with hook length `v`. -/
noncomputable def hookCount (l : List ℕ) (v : ℕ) : ℕ :=
  ((cells l).filter (fun p => hookLen l p = v)).card

/-- Any single part is at most the size. -/
theorem getD_le_sum (l : List ℕ) (i : ℕ) : l.getD i 0 ≤ l.sum := by
  induction l generalizing i with
  | nil => simp
  | cons a t ih =>
      cases i with
      | zero =>
          rw [List.getD_cons_zero, List.sum_cons]
          exact Nat.le_add_right a t.sum
      | succ i' =>
          rw [List.getD_cons_succ, List.sum_cons]
          exact le_trans (ih i') (Nat.le_add_left _ _)

/-- The cheap hook bound on enumerated partitions: `h(□) ≤ λ_i + λ'_j ≤ 2k`. -/
theorem hookLen_lt_of_mem (k : ℕ) (l : List ℕ) (hl : l ∈ partsOf k) (p : ℕ × ℕ)
    (_ : p ∈ cells l) : hookLen l p < 2 * k + 1 := by
  obtain ⟨hsum, hpos, hsort⟩ := partsOf_facts k l hl
  have h1 : l.getD p.1 0 ≤ k := hsum ▸ getD_le_sum l p.1
  have h2 : (conj l).getD p.2 0 ≤ k := by
    rw [conj_getD l hsort]
    exact le_trans List.countP_le_length (hsum ▸ length_le_sum l hpos)
  unfold hookLen
  omega

/-- **The spectral decomposition of hook statistics**: for every `φ`,
`Σ_v φ(v)·N_v(λ) = Σ_□ φ(h(□))` — fiberwise summation of the cell set over hook values. This is
the exact mechanism by which the ν-system's moments realize the scaffold's hook covariances
(`φ = ln` ↦ `covLnHooks`, `φ = (·)²` ↦ `covHookSq`, `φ = 1` ↦ the zeroth moment below). -/
theorem hookSpectrum_sum (k : ℕ) (l : List ℕ) (hl : l ∈ partsOf k) (φ : ℕ → ℝ) :
    ∑ v ∈ Finset.range (2 * k + 1), φ v * (hookCount l v : ℝ)
      = ∑ p ∈ cells l, φ (hookLen l p) := by
  have h1 : ∀ v ∈ Finset.range (2 * k + 1),
      φ v * (hookCount l v : ℝ)
        = ∑ p ∈ (cells l).filter (fun p => hookLen l p = v), φ (hookLen l p) := by
    intro v _
    rw [Finset.sum_congr rfl (fun p hp => by rw [(Finset.mem_filter.mp hp).2]),
      Finset.sum_const, nsmul_eq_mul]
    unfold hookCount
    ring
  rw [Finset.sum_congr rfl h1]
  exact Finset.sum_fiberwise_of_maps_to
    (fun p hp => Finset.mem_range.mpr (hookLen_lt_of_mem k l hl p hp)) _

/-- Mixed spectrum moment `E₂[N_v·ω₃]`. -/
noncomputable def nuMixedMoment (k v : ℕ) : ℝ :=
  ((partsOf k).map (fun l =>
    tilt 0 (sytDim l) * (hookCount l v : ℝ) * (omega3 k l : ℝ))).sum / tiltNorm k 0

/-- Spectrum mean `E₂[N_v]`. -/
noncomputable def nuMean (k v : ℕ) : ℝ :=
  ((partsOf k).map (fun l => tilt 0 (sytDim l) * (hookCount l v : ℝ))).sum / tiltNorm k 0

/-- **The ν-system**: `ν_v = Cov₂(N_v, ω₃)` — the hook-spectrum/content-spread covariances whose
log-moment sign is leg [A2]. -/
noncomputable def nuV (k v : ℕ) : ℝ := nuMixedMoment k v - nuMean k v * tiltedMean k 0

/-- A `Finset`-indexed family of list sums swaps with the list sum. -/
theorem finset_sum_list_map_sum {ι : Type*} (s : Finset ℕ) (L : List ι) (f : ℕ → ι → ℝ) :
    ∑ v ∈ s, (L.map (f v)).sum = (L.map (fun l => ∑ v ∈ s, f v l)).sum := by
  induction L with
  | nil => simp
  | cons a t ih =>
      simp only [List.map_cons, List.sum_cons, Finset.sum_add_distrib, ih]

/-- The spectrum totals to the size: `Σ_v N_v(λ) = k` (φ = 1 in the spectral decomposition,
plus `|cells| = k`). -/
theorem sum_hookCount (k : ℕ) (l : List ℕ) (hl : l ∈ partsOf k) :
    ∑ v ∈ Finset.range (2 * k + 1), (hookCount l v : ℝ) = (k : ℝ) := by
  have h := hookSpectrum_sum k l hl (fun _ => 1)
  simp only [one_mul] at h
  rw [h, Finset.sum_const, nsmul_eq_mul, mul_one, card_cells l,
    (partsOf_facts k l hl).1]

/-- **The zeroth-moment constraint, Lean-locked**: `Σ_v ν_v = 0` — the spectrum totals to the
constant `k`, and covariance against a constant vanishes. Together with the second moment
(`Σ_v v²·ν_v = Var₂(ω₃) ≥ 0`, via `covHookSq_nonneg`) and the [A2] target
(`Σ_v ln(v)·ν_v ≥ 0 ⇔` leg [A2], via `covLnF_nonpos_iff`), this pins the surviving moment
skeleton's exact shape: a mean-zero signed measure with positive second moment whose log-moment
sign is the open leg. -/
theorem sum_nuV_eq_zero (k : ℕ) : ∑ v ∈ Finset.range (2 * k + 1), nuV k v = 0 := by
  unfold nuV nuMixedMoment nuMean
  rw [Finset.sum_sub_distrib]
  rw [← Finset.sum_div, ← Finset.sum_mul, ← Finset.sum_div]
  rw [finset_sum_list_map_sum, finset_sum_list_map_sum]
  have hω : ((partsOf k).map (fun l => ∑ v ∈ Finset.range (2 * k + 1),
      tilt 0 (sytDim l) * (hookCount l v : ℝ) * (omega3 k l : ℝ))).sum
      = (k : ℝ) * tiltOmega k 0 := by
    rw [List.map_congr_left (fun l hl => by
      rw [show (fun v => tilt 0 (sytDim l) * (hookCount l v : ℝ) * (omega3 k l : ℝ))
            = (fun v => (tilt 0 (sytDim l) * (omega3 k l : ℝ)) * (hookCount l v : ℝ)) from
          funext fun v => by ring, ← Finset.mul_sum, sum_hookCount k l hl] :
      ∀ l ∈ partsOf k, (∑ v ∈ Finset.range (2 * k + 1),
          tilt 0 (sytDim l) * (hookCount l v : ℝ) * (omega3 k l : ℝ))
        = tilt 0 (sytDim l) * (omega3 k l : ℝ) * (k : ℝ))]
    rw [show (fun l => tilt 0 (sytDim l) * (omega3 k l : ℝ) * (k : ℝ))
          = (fun l => (k : ℝ) * (tilt 0 (sytDim l) * (omega3 k l : ℝ))) from
        funext fun l => by ring, list_sum_map_mul_left]
    rfl
  have hZ : ((partsOf k).map (fun l => ∑ v ∈ Finset.range (2 * k + 1),
      tilt 0 (sytDim l) * (hookCount l v : ℝ))).sum
      = (k : ℝ) * tiltNorm k 0 := by
    rw [List.map_congr_left (fun l hl => by
      rw [← Finset.mul_sum, sum_hookCount k l hl] :
      ∀ l ∈ partsOf k, (∑ v ∈ Finset.range (2 * k + 1),
          tilt 0 (sytDim l) * (hookCount l v : ℝ))
        = tilt 0 (sytDim l) * (k : ℝ))]
    rw [show (fun l => tilt 0 (sytDim l) * (k : ℝ))
          = (fun l => (k : ℝ) * tilt 0 (sytDim l)) from funext fun l => by ring,
      list_sum_map_mul_left]
    rfl
  rw [hω, hZ]
  unfold tiltedMean
  rcases eq_or_ne (tiltNorm k 0) 0 with hZ0 | hZ0
  · simp [hZ0]
  · field_simp
    ring

/-! ## The spectral links: `Σ v²·ν_v = Cov₂(Σh², ω₃)` and `Σ ln(v)·ν_v = Cov₂(ln ∏h, ω₃)`

The two remaining exact links of the skeleton: instantiating the spectral decomposition at
`φ = (·)²` and `φ = ln` identifies the ν-system's second and log moments with the scaffold's
already-analyzed hook covariances. With them, every constraint and the target itself are
statements **about ν alone**: `Σν_v = 0`, `Σv²ν_v = Var₂(ω₃) ≥ 0`, and [A2] ⇔ `Σln(v)·ν_v ≥ 0`. -/

/-- Hooks are positive on genuine cells (cell bound + its staircase mirror). -/
theorem hookLen_pos (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (p : ℕ × ℕ) (hp : p ∈ cells l) :
    0 < hookLen l p := by
  rw [mem_cells] at hp
  have hstair : p.1 < l.countP (fun x => decide (p.2 < x)) :=
    (lt_countP_iff l hs p.2 p.1).mpr hp
  unfold hookLen
  rw [conj_getD l hs]
  omega

/-- **The hook is contained in the diagram**: a cell's hook length is at most the size
`n = Σλᵢ`. The hook of `(i,j)` is the disjoint union of its arm `{(i,j′) : j ≤ j′ < λᵢ}` and
its strict leg `{(i′,j) : i < i′ < λ′ⱼ}`, both inside the cell set; counting the union gives
`h(i,j) = (λᵢ − j) + (λ′ⱼ − i − 1) ≤ |cells λ| = n`. This is the first brick of the (TAIL)
carrier method: the extreme case `h = n` forces the hook to *exhaust* the diagram, confining
the carriers of `ν_n` to the hook shapes `(a, 1^{n−a})` — the containment proved here is the
inequality whose equality analysis is that carrier lemma. -/
theorem hookLen_le_sum (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (p : ℕ × ℕ)
    (hp : p ∈ cells l) : hookLen l p ≤ l.sum := by
  obtain ⟨i, j⟩ := p
  rw [mem_cells] at hp
  have hcol : i < (conj l).getD j 0 := by
    rw [conj_getD l hs]
    exact (lt_countP_iff l hs j i).mpr hp
  have hinj1 : Function.Injective (fun j' : ℕ => (i, j')) := fun a b h => by
    simpa using congrArg Prod.snd h
  have hinj2 : Function.Injective (fun i' : ℕ => (i', j)) := fun a b h => by
    simpa using congrArg Prod.fst h
  have harm : (Finset.Ico j (l.getD i 0)).image (fun j' => (i, j')) ⊆ cells l := by
    intro q hq
    obtain ⟨j', hj', rfl⟩ := Finset.mem_image.mp hq
    rw [mem_cells]
    exact (Finset.mem_Ico.mp hj').2
  have hleg : (Finset.Ioo i ((conj l).getD j 0)).image (fun i' => (i', j)) ⊆ cells l := by
    intro q hq
    obtain ⟨i', hi', rfl⟩ := Finset.mem_image.mp hq
    rw [mem_cells]
    refine (lt_countP_iff l hs j i').mp ?_
    have h2 := (Finset.mem_Ioo.mp hi').2
    rwa [conj_getD l hs] at h2
  have hdisj : Disjoint ((Finset.Ico j (l.getD i 0)).image (fun j' => (i, j')))
      ((Finset.Ioo i ((conj l).getD j 0)).image (fun i' => (i', j))) := by
    rw [Finset.disjoint_left]
    intro q hqa hql
    obtain ⟨j', _, rfl⟩ := Finset.mem_image.mp hqa
    obtain ⟨i', hi', h'⟩ := Finset.mem_image.mp hql
    simp only [Prod.mk.injEq] at h'
    have h1 := (Finset.mem_Ioo.mp hi').1
    omega
  have hcard := Finset.card_le_card (Finset.union_subset harm hleg)
  rw [Finset.card_union_of_disjoint hdisj, card_cells,
      Finset.card_image_of_injective _ hinj1, Finset.card_image_of_injective _ hinj2,
      Nat.card_Ico, Nat.card_Ioo] at hcard
  unfold hookLen
  dsimp only
  omega

/-- The tight hook bound on enumerated partitions: `h(□) ≤ k` (sharpening the cheap `2k`
range bound `hookLen_lt_of_mem`; the classical bound, now proved rather than assumed). -/
theorem hookLen_le_of_mem (k : ℕ) (l : List ℕ) (hl : l ∈ partsOf k) (p : ℕ × ℕ)
    (hp : p ∈ cells l) : hookLen l p ≤ k := by
  obtain ⟨hsum, _, hsort⟩ := partsOf_facts k l hl
  exact hsum ▸ hookLen_le_sum l hsort p hp

/-- **The carrier lemma (equality analysis)**: a hook of maximal length `n = Σλᵢ` forces the
carrier cell to be the corner `(0,0)` and the diagram to be a **hook shape** (every row past the
first has at most one cell, i.e. `λ = (a, 1^c)`). Equality in `hookLen_le_sum`'s containment
means the arm ∪ strict-leg union *is* the cell set; testing the corner against the union pins
`p = (0,0)`, and testing any cell `(i′,1)` with `i′ ≥ 1` (off row 0 and column 0) kills any
non-hook row. This confines the carriers of the top hook statistic `N_n` to the `n` hook shapes
— the Lean form of step 1 of the derived `ν_n` closed form (the (TAIL) first instance). -/
theorem hookShape_of_hookLen_eq_sum (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (p : ℕ × ℕ)
    (hp : p ∈ cells l) (heq : hookLen l p = l.sum) :
    p = (0, 0) ∧ ∀ i', 1 ≤ i' → l.getD i' 0 ≤ 1 := by
  obtain ⟨i, j⟩ := p
  rw [mem_cells] at hp
  dsimp only at hp
  have hcol : i < (conj l).getD j 0 := by
    rw [conj_getD l hs]
    exact (lt_countP_iff l hs j i).mpr hp
  have hinj1 : Function.Injective (fun j' : ℕ => (i, j')) := fun a b h => by
    simpa using congrArg Prod.snd h
  have hinj2 : Function.Injective (fun i' : ℕ => (i', j)) := fun a b h => by
    simpa using congrArg Prod.fst h
  set armF := (Finset.Ico j (l.getD i 0)).image (fun j' => (i, j')) with harmF
  set legF := (Finset.Ioo i ((conj l).getD j 0)).image (fun i' => (i', j)) with hlegF
  have harm : armF ⊆ cells l := by
    intro q hq
    obtain ⟨j', hj', rfl⟩ := Finset.mem_image.mp hq
    rw [mem_cells]
    exact (Finset.mem_Ico.mp hj').2
  have hleg : legF ⊆ cells l := by
    intro q hq
    obtain ⟨i', hi', rfl⟩ := Finset.mem_image.mp hq
    rw [mem_cells]
    refine (lt_countP_iff l hs j i').mp ?_
    have h2 := (Finset.mem_Ioo.mp hi').2
    rwa [conj_getD l hs] at h2
  have hdisj : Disjoint armF legF := by
    rw [Finset.disjoint_left]
    intro q hqa hql
    obtain ⟨j', _, rfl⟩ := Finset.mem_image.mp hqa
    obtain ⟨i', hi', h'⟩ := Finset.mem_image.mp hql
    simp only [Prod.mk.injEq] at h'
    have h1 := (Finset.mem_Ioo.mp hi').1
    omega
  have hcardU : (armF ∪ legF).card = hookLen l (i, j) := by
    rw [Finset.card_union_of_disjoint hdisj, harmF, hlegF,
        Finset.card_image_of_injective _ hinj1, Finset.card_image_of_injective _ hinj2,
        Nat.card_Ico, Nat.card_Ioo]
    unfold hookLen
    dsimp only
    omega
  have hunion : armF ∪ legF = cells l := by
    refine Finset.eq_of_subset_of_card_le (Finset.union_subset harm hleg) ?_
    rw [hcardU, heq, card_cells]
  have hmem : ∀ a b : ℕ, (a, b) ∈ cells l → (a = i ∧ j ≤ b) ∨ (b = j ∧ i < a) := by
    intro a b hq
    rw [← hunion] at hq
    rcases Finset.mem_union.mp hq with hqa | hql
    · obtain ⟨j', hj', hEq⟩ := Finset.mem_image.mp hqa
      simp only [Prod.mk.injEq] at hEq
      have hlo := (Finset.mem_Ico.mp hj').1
      left; omega
    · obtain ⟨i', hi', hEq⟩ := Finset.mem_image.mp hql
      simp only [Prod.mk.injEq] at hEq
      have hlo := (Finset.mem_Ioo.mp hi').1
      right; omega
  have hilen : i < l.length := by
    by_contra hcon
    rw [List.getD_eq_default _ _ (le_of_not_gt hcon)] at hp
    exact Nat.not_lt_zero j hp
  have hhead : l.getD i 0 ≤ l.getD 0 0 := by
    rw [getD_zero_eq_headD]
    refine mem_le_headD l hs _ ?_
    rw [List.getD_eq_getElem _ _ hilen]
    exact List.getElem_mem hilen
  have h00 : ((0 : ℕ), (0 : ℕ)) ∈ cells l := by
    rw [mem_cells]
    dsimp only
    omega
  have hij0 : i = 0 ∧ j = 0 := by
    rcases hmem 0 0 h00 with ⟨h1, h2⟩ | ⟨h1, h2⟩ <;> omega
  obtain ⟨hi0, hj0⟩ := hij0
  refine ⟨by simp only [Prod.mk.injEq]; exact ⟨hi0, hj0⟩, ?_⟩
  intro i' hi'
  by_contra hcon
  push_neg at hcon
  have hc : (i', 1) ∈ cells l := by
    rw [mem_cells]
    exact hcon
  rcases hmem i' 1 hc with ⟨h1, _⟩ | ⟨h1, _⟩ <;> omega

/-- **Converse of the carrier lemma**: on a hook shape (positive parts, at most one cell per row
past the first) the corner's hook exhausts the diagram — `h(0,0) = a + λ′₀ − 1 = a + c = n`.
Together with `hookShape_of_hookLen_eq_sum` this characterizes the carriers of the top hook
statistic `N_n`: they are exactly the corner cells of the `n` hook shapes `(a, 1^{n−a})`. -/
theorem hookLen_corner_of_hookShape (l : List ℕ) (hs : l.Sorted (· ≥ ·))
    (hpos : ∀ x ∈ l, 0 < x) (hne : l ≠ [])
    (hhook : ∀ i', 1 ≤ i' → l.getD i' 0 ≤ 1) :
    hookLen l (0, 0) = l.sum := by
  have hcount : l.countP (fun x => decide (0 < x)) = l.length :=
    List.countP_eq_length.mpr fun x hx => by simpa using hpos x hx
  have hones : ∀ (t : List ℕ), (∀ x ∈ t, x = 1) → t.sum = t.length := by
    intro t
    induction t with
    | nil => intro _; rfl
    | cons b s ih =>
        intro h
        rw [List.sum_cons, List.length_cons, h b List.mem_cons_self,
            ih (fun x hx => h x (List.mem_cons_of_mem b hx))]
        omega
  obtain ⟨a, t, rfl⟩ : ∃ a t, l = a :: t := by
    cases l with
    | nil => exact absurd rfl hne
    | cons a t => exact ⟨a, t, rfl⟩
  have ht1 : ∀ x ∈ t, x = 1 := by
    intro x hx
    obtain ⟨k, hk, rfl⟩ := List.mem_iff_getElem.mp hx
    have h1 : (a :: t).getD (k + 1) 0 ≤ 1 := hhook (k + 1) (Nat.le_add_left 1 k)
    rw [List.getD_cons_succ, List.getD_eq_getElem _ _ hk] at h1
    have h2 : 0 < t[k] := hpos _ (List.mem_cons_of_mem a hx)
    omega
  unfold hookLen
  dsimp only
  rw [conj_getD _ hs, hcount, List.getD_cons_zero, List.sum_cons, List.length_cons,
      hones t ht1]
  omega

/-- **Carrier confinement, count form (hook shape)**: on a hook shape the top hook statistic is
exactly `N_n = 1` — the corner is the *unique* cell of hook length `n` (existence by
`hookLen_corner_of_hookShape`, uniqueness by the carrier lemma
`hookShape_of_hookLen_eq_sum`). -/
theorem hookCount_sum_of_hookShape (l : List ℕ) (hs : l.Sorted (· ≥ ·))
    (hpos : ∀ x ∈ l, 0 < x) (hne : l ≠ [])
    (hhook : ∀ i', 1 ≤ i' → l.getD i' 0 ≤ 1) :
    hookCount l l.sum = 1 := by
  have h00cell : ((0 : ℕ), (0 : ℕ)) ∈ cells l := by
    rw [mem_cells]
    dsimp only
    cases l with
    | nil => exact absurd rfl hne
    | cons a t => simpa using hpos a List.mem_cons_self
  unfold hookCount
  rw [Finset.card_eq_one]
  refine ⟨((0 : ℕ), (0 : ℕ)), ?_⟩
  rw [Finset.eq_singleton_iff_unique_mem]
  constructor
  · rw [Finset.mem_filter]
    exact ⟨h00cell, hookLen_corner_of_hookShape l hs hpos hne hhook⟩
  · intro p hp
    rw [Finset.mem_filter] at hp
    exact (hookShape_of_hookLen_eq_sum l hs p hp.1 hp.2).1

/-- **Carrier confinement, count form (non-hook shape)**: off the hook shapes the top hook
statistic vanishes, `N_n = 0` — a cell of hook length `n` would force the hook shape by the
carrier lemma. -/
theorem hookCount_sum_of_not_hookShape (l : List ℕ) (hs : l.Sorted (· ≥ ·))
    (hnot : ¬ ∀ i', 1 ≤ i' → l.getD i' 0 ≤ 1) :
    hookCount l l.sum = 0 := by
  unfold hookCount
  rw [Finset.card_eq_zero, Finset.eq_empty_iff_forall_notMem]
  intro p hp
  rw [Finset.mem_filter] at hp
  exact hnot (hookShape_of_hookLen_eq_sum l hs p hp.1 hp.2).2

/-- `getD` on a replicate list, in range. -/
theorem getD_replicate_of_lt (x d : ℕ) : ∀ n i, i < n → (List.replicate n x).getD i d = x := by
  intro n
  induction n with
  | zero => intro i h; exact absurd h (Nat.not_lt_zero i)
  | succ n ih =>
      intro i h
      cases i with
      | zero => rw [List.replicate_succ, List.getD_cons_zero]
      | succ i' =>
          rw [List.replicate_succ, List.getD_cons_succ]
          exact ih i' (Nat.lt_of_succ_lt_succ h)

/-- **Content square of a hook shape** `(a, 1^c)`: row 0 contributes the squares of the arm
contents `0, …, a−1`; the column cells `(i,0)`, `1 ≤ i ≤ c`, contribute `(−i)² = i²`. This is
step 2 of the (TAIL) first-instance derivation (`ω₃ = Q(a−1) + Q(c) − C(n,2)` after subtracting
the center term). -/
theorem contentSq_hookShape (a c : ℕ) :
    contentSq (a :: List.replicate c 1)
      = (∑ j ∈ Finset.range a, ((j : ℤ)) ^ 2) + ∑ i ∈ Finset.range c, ((i : ℤ) + 1) ^ 2 := by
  rw [contentSq_eq_finset_sum]
  have hlen : (a :: List.replicate c 1).length = c + 1 := by
    rw [List.length_cons, List.length_replicate]
  rw [hlen, Finset.sum_range_succ']
  rw [add_comm (∑ j ∈ Finset.range a, ((j : ℤ)) ^ 2)]
  congr 1
  refine Finset.sum_congr rfl fun i hi => ?_
  have hgd : (a :: List.replicate c 1).getD (i + 1) 0 = 1 := by
    rw [List.getD_cons_succ]
    exact getD_replicate_of_lt 1 0 c i (Finset.mem_range.mp hi)
  rw [hgd, Finset.sum_range_one]
  push_cast
  ring

/-- Division-free sum of squares: `6·Σ_{j<m} j² = (m−1)·m·(2m−1)` in `ℤ` — the polynomial
evaluation of the hook-shape content data (`Q(m) = Σ_{t≤m} t²` in the audit's notation is
`Σ_{j<m+1} j²` here). -/
theorem six_mul_sum_range_sq (m : ℕ) :
    6 * ∑ j ∈ Finset.range m, ((j : ℤ)) ^ 2 = ((m : ℤ) - 1) * m * (2 * m - 1) := by
  induction m with
  | zero => simp
  | succ m ih =>
      rw [Finset.sum_range_succ, mul_add, ih]
      push_cast
      ring

/-- Hook shapes are weakly decreasing. -/
theorem sorted_hookShape (a c : ℕ) (ha : 1 ≤ a) :
    (a :: List.replicate c 1).Sorted (· ≥ ·) := by
  rw [List.sorted_cons]
  refine ⟨fun b hb => le_trans (le_of_eq (List.eq_of_mem_replicate hb)) ha, ?_⟩
  induction c with
  | zero => exact List.sorted_nil
  | succ c ih =>
      rw [List.replicate_succ, List.sorted_cons]
      exact ⟨fun b hb => le_of_eq (List.eq_of_mem_replicate hb), ih⟩

/-- The size of a hook shape is `a + c`. -/
theorem sum_replicate_one : ∀ c : ℕ, (List.replicate c 1).sum = c := by
  intro c
  induction c with
  | zero => rfl
  | succ c ih =>
      rw [List.replicate_succ, List.sum_cons, ih]
      omega

/-- Descending-factor product: `∏_{j<m} (m − j) = m!`. -/
theorem prod_range_sub_eq_factorial : ∀ m : ℕ, (∏ j ∈ Finset.range m, (m - j)) = m.factorial := by
  intro m
  induction m with
  | zero => rfl
  | succ m ih =>
      rw [Finset.prod_range_succ']
      have hshift : (∏ j ∈ Finset.range m, (m + 1 - (j + 1))) = ∏ j ∈ Finset.range m, (m - j) :=
        Finset.prod_congr rfl fun j _ => by omega
      rw [hshift, ih, Nat.factorial_succ, Nat.sub_zero, Nat.mul_comm]

/-- `hookProd` as a nested `Finset.range` product (row-structured form). -/
theorem hookProd_eq_finset_prod (l : List ℕ) :
    hookProd l = ∏ i ∈ Finset.range l.length, ∏ j ∈ Finset.range (l.getD i 0),
      (l.getD i 0 + (conj l).getD j 0 - j - i - 1) := by
  unfold hookProd
  rw [list_prod_map_range]
  exact Finset.prod_congr rfl fun i _ => list_prod_map_range _ _

/-- **Hook product of a hook shape** `(a, 1^c)`: the corner hook is `a + c = n`, the arm hooks
descend `a−1, …, 1`, the leg hooks descend `c, …, 1` — so `∏h = n·(a−1)!·c!`. Step 2 of the
(TAIL) first-instance derivation. -/
theorem hookProd_hookShape (a c : ℕ) (ha : 1 ≤ a) :
    hookProd (a :: List.replicate c 1) = (a + c) * (a - 1).factorial * c.factorial := by
  obtain ⟨b, rfl⟩ : ∃ b, a = b + 1 := ⟨a - 1, by omega⟩
  simp only [Nat.add_sub_cancel]
  have hsorted : ((b + 1) :: List.replicate c 1).Sorted (· ≥ ·) :=
    sorted_hookShape (b + 1) c (Nat.succ_le_succ (Nat.zero_le b))
  have hcj0 : (conj ((b + 1) :: List.replicate c 1)).getD 0 0 = c + 1 := by
    rw [conj_getD _ hsorted]
    have hall : ∀ x ∈ (b + 1) :: List.replicate c 1, (fun x => decide (0 < x)) x = true := by
      intro x hx
      rcases List.mem_cons.mp hx with rfl | hxr
      · simp
      · rw [List.eq_of_mem_replicate hxr]; decide
    rw [List.countP_eq_length.mpr hall, List.length_cons, List.length_replicate]
  have hcjj : ∀ j, 1 ≤ j → j < b + 1 →
      (conj ((b + 1) :: List.replicate c 1)).getD j 0 = 1 := by
    intro j hj1 hjb
    rw [conj_getD _ hsorted, List.countP_cons]
    have hz : (List.replicate c 1).countP (fun x => decide (j < x)) = 0 := by
      rw [List.countP_eq_zero]
      intro x hx
      rw [List.eq_of_mem_replicate hx]
      simp only [decide_eq_true_eq]
      omega
    rw [hz]
    simp [hjb]
  rw [hookProd_eq_finset_prod, List.length_cons, List.length_replicate,
      Finset.prod_range_succ']
  have hrows : ∀ i ∈ Finset.range c,
      (∏ j ∈ Finset.range (((b + 1) :: List.replicate c 1).getD (i + 1) 0),
        (((b + 1) :: List.replicate c 1).getD (i + 1) 0
          + (conj ((b + 1) :: List.replicate c 1)).getD j 0 - j - (i + 1) - 1))
      = c - i := by
    intro i hi
    have hgd : ((b + 1) :: List.replicate c 1).getD (i + 1) 0 = 1 := by
      rw [List.getD_cons_succ]
      exact getD_replicate_of_lt 1 0 c i (Finset.mem_range.mp hi)
    rw [hgd, Finset.prod_range_one, hcj0]
    omega
  rw [Finset.prod_congr rfl hrows, prod_range_sub_eq_factorial]
  have hrow0 :
      (∏ j ∈ Finset.range (((b + 1) :: List.replicate c 1).getD 0 0),
        (((b + 1) :: List.replicate c 1).getD 0 0
          + (conj ((b + 1) :: List.replicate c 1)).getD j 0 - j - 0 - 1))
      = (b + 1 + c) * b.factorial := by
    rw [List.getD_cons_zero, Finset.prod_range_succ']
    have hgj : ∀ j ∈ Finset.range b,
        (b + 1 + (conj ((b + 1) :: List.replicate c 1)).getD (j + 1) 0 - (j + 1) - 0 - 1)
        = b - j := by
      intro j hj
      rw [hcjj (j + 1) (Nat.le_add_left 1 j) (Nat.succ_lt_succ (Finset.mem_range.mp hj))]
      omega
    rw [Finset.prod_congr rfl hgj, prod_range_sub_eq_factorial, hcj0]
    have hg0 : b + 1 + (c + 1) - 0 - 0 - 1 = b + 1 + c := by omega
    rw [hg0, Nat.mul_comm]
  rw [hrow0]
  ring

/-! ### The hook-shape family inside `partsOf`

Step 3 of the (TAIL) first-instance derivation: the carrier confinement is a statement about
*individual* diagrams (`hookCount_sum_of_hookShape` / `_of_not_hookShape`); to turn it into a
statement about the Plancherel sum one needs the hook shapes as an explicit, nodup sub-family of
the enumerator `partsOf k`, plus the converse structural fact that a sorted positive list whose
rows past the first are all `≤ 1` **is** one of them. -/

/-- The `k` hook shapes of size `k`, enumerated by arm length `a = i + 1`. -/
def hookShapes (k : ℕ) : List (List ℕ) :=
  (List.range k).map (fun i => (i + 1) :: List.replicate (k - 1 - i) 1)

/-- Each enumerated hook shape has size `k`. -/
theorem hookShape_sum (k i : ℕ) (hi : i < k) :
    ((i + 1) :: List.replicate (k - 1 - i) 1).sum = k := by
  rw [List.sum_cons, sum_replicate_one]
  omega

/-- Every hook shape is a genuine member of the partition enumerator. -/
theorem hookShape_mem_partsOf (k i : ℕ) (hi : i < k) :
    ((i + 1) :: List.replicate (k - 1 - i) 1) ∈ partsOf k := by
  apply mem_partsFuel _ k k k (hookShape_sum k i hi)
  · intro x hx
    rcases List.mem_cons.mp hx with rfl | hxr
    · omega
    · rw [List.eq_of_mem_replicate hxr]; omega
  · intro x hx
    rcases List.mem_cons.mp hx with rfl | hxr
    · omega
    · rw [List.eq_of_mem_replicate hxr]; omega
  · exact sorted_hookShape (i + 1) (k - 1 - i) (Nat.succ_le_succ (Nat.zero_le i))
  · rw [List.length_cons, List.length_replicate]; omega

/-- The hook-shape enumeration has no duplicates (the arm length is the head). -/
theorem hookShapes_nodup (k : ℕ) : (hookShapes k).Nodup := by
  unfold hookShapes
  refine List.Nodup.map ?_ (List.nodup_range)
  intro a b hab
  simp only [List.cons.injEq] at hab
  omega

/-- **Converse structural fact**: a nonempty list all of whose rows past the first are `≤ 1`, with
positive entries, *is* the hook shape `(head, 1^{len−1})`. Together with the carrier lemma this
makes "is a hook shape" (a `getD` condition) and "belongs to `hookShapes`" (an enumeration
condition) interchangeable. -/
theorem eq_hookShape_of_rows_le_one (l : List ℕ) (hpos : ∀ x ∈ l, 0 < x) (hne : l ≠ [])
    (hhook : ∀ i', 1 ≤ i' → l.getD i' 0 ≤ 1) :
    l = l.headD 0 :: List.replicate (l.length - 1) 1 := by
  obtain ⟨a, t, rfl⟩ : ∃ a t, l = a :: t := by
    cases l with
    | nil => exact absurd rfl hne
    | cons a t => exact ⟨a, t, rfl⟩
  have ht : t = List.replicate t.length 1 := by
    refine (List.eq_replicate_iff.mpr ⟨rfl, fun b hb => ?_⟩)
    obtain ⟨j, hj, rfl⟩ := List.mem_iff_getElem.mp hb
    have h1 : (a :: t).getD (j + 1) 0 ≤ 1 := hhook (j + 1) (Nat.le_add_left 1 j)
    rw [List.getD_cons_succ, List.getD_eq_getElem _ _ hj] at h1
    have h2 : 0 < t[j] := hpos _ (List.mem_cons_of_mem a hb)
    omega
  simp only [List.headD_cons, List.length_cons, Nat.add_sub_cancel]
  exact congrArg (fun s => a :: s) ht

/-- A hook-shaped member of `partsOf k` is in the enumeration `hookShapes k`. -/
theorem mem_hookShapes_of_rows_le_one (k : ℕ) (l : List ℕ) (hl : l ∈ partsOf k) (hk : 1 ≤ k)
    (hhook : ∀ i', 1 ≤ i' → l.getD i' 0 ≤ 1) : l ∈ hookShapes k := by
  obtain ⟨hsum, hpos, _⟩ := partsOf_facts k l hl
  have hne : l ≠ [] := by
    intro h
    rw [h, List.sum_nil] at hsum
    omega
  have heq := eq_hookShape_of_rows_le_one l hpos hne hhook
  have hlen : 1 ≤ l.length := by
    cases l with
    | nil => exact absurd rfl hne
    | cons _ _ => simp
  have hhd : l.headD 0 + (l.length - 1) = k := by
    have := congrArg List.sum heq
    rw [List.sum_cons, sum_replicate_one] at this
    omega
  have hpos' : 0 < l.headD 0 := by
    cases l with
    | nil => exact absurd rfl hne
    | cons a t => exact hpos a List.mem_cons_self
  unfold hookShapes
  refine List.mem_map.mpr ⟨l.headD 0 - 1, List.mem_range.mpr (by omega), ?_⟩
  have h1 : l.headD 0 - 1 + 1 = l.headD 0 := by omega
  have h2 : k - 1 - (l.headD 0 - 1) = l.length - 1 := by omega
  rw [h1, h2]
  exact heq.symm

/-- **SYT dimension of a hook shape**: `f^{(a,1^c)} = C(n−1, a−1)` with `n = a + c` — the
hook-length formula evaluated on the hook-shape data. Step 2 of the (TAIL) first-instance
derivation, feeding the binomial-square sums. -/
theorem sytDim_hookShape (a c : ℕ) (ha : 1 ≤ a) :
    sytDim (a :: List.replicate c 1) = Nat.choose (a + c - 1) (a - 1) := by
  obtain ⟨b, rfl⟩ : ∃ b, a = b + 1 := ⟨a - 1, by omega⟩
  simp only [Nat.add_sub_cancel]
  have h1 : b + 1 + c - 1 = b + c := by omega
  rw [h1]
  unfold sytDim
  rw [List.sum_cons, sum_replicate_one,
      hookProd_hookShape (b + 1) c (Nat.succ_le_succ (Nat.zero_le b))]
  simp only [Nat.add_sub_cancel]
  rw [Nat.choose_eq_factorial_div_factorial (by omega : b ≤ b + c)]
  have h2 : b + c - b = c := by omega
  rw [h2]
  have h3 : b + 1 + c = (b + c) + 1 := by omega
  rw [h3, Nat.factorial_succ, Nat.mul_assoc]
  exact Nat.mul_div_mul_left _ _ (Nat.succ_pos _)

/-- **Step 3 (the Plancherel restriction)**: a weight vanishing off the hook shapes may be summed
over the explicit `k`-element family `hookShapes k` instead of the whole enumerator `partsOf k`.
Both lists are nodup (`partsFuel_nodup`, `hookShapes_nodup`) and the family embeds
(`hookShape_mem_partsOf`), so this is `Finset.sum_subset` transported along `List.sum_toFinset`. -/
theorem sum_partsOf_eq_sum_hookShapes (k : ℕ) (g : List ℕ → ℝ)
    (hg : ∀ l ∈ partsOf k, l ∉ hookShapes k → g l = 0) :
    ((partsOf k).map g).sum = ((hookShapes k).map g).sum := by
  have hnd : (partsOf k).Nodup := partsFuel_nodup k k k
  rw [← List.sum_toFinset g hnd, ← List.sum_toFinset g (hookShapes_nodup k)]
  refine (Finset.sum_subset ?_ ?_).symm
  · intro x hx
    rw [List.mem_toFinset] at hx ⊢
    obtain ⟨i, hi, rfl⟩ := List.mem_map.mp hx
    exact hookShape_mem_partsOf k i (List.mem_range.mp hi)
  · intro x hx hnx
    rw [List.mem_toFinset] at hx
    rw [List.mem_toFinset] at hnx
    exact hg x hx hnx

/-- The top hook statistic vanishes off the hook shapes, *as members of the enumerator*: the
`getD`-level carrier lemma transported to the enumeration via `mem_hookShapes_of_rows_le_one`. -/
theorem hookCount_top_eq_zero_of_not_mem (k : ℕ) (hk : 1 ≤ k) (l : List ℕ) (hl : l ∈ partsOf k)
    (hnm : l ∉ hookShapes k) : hookCount l k = 0 := by
  obtain ⟨hsum, _, hsort⟩ := partsOf_facts k l hl
  have hnot : ¬ ∀ i', 1 ≤ i' → l.getD i' 0 ≤ 1 := fun h =>
    hnm (mem_hookShapes_of_rows_le_one k l hl hk h)
  have := hookCount_sum_of_not_hookShape l hsort hnot
  rwa [hsum] at this

/-- The top hook statistic is `1` on every enumerated hook shape. -/
theorem hookCount_top_eq_one_mem (k i : ℕ) (hi : i < k) :
    hookCount ((i + 1) :: List.replicate (k - 1 - i) 1) k = 1 := by
  have hsorted := sorted_hookShape (i + 1) (k - 1 - i) (Nat.succ_le_succ (Nat.zero_le i))
  have hpos : ∀ x ∈ (i + 1) :: List.replicate (k - 1 - i) 1, 0 < x := by
    intro x hx
    rcases List.mem_cons.mp hx with rfl | hxr
    · omega
    · rw [List.eq_of_mem_replicate hxr]; omega
  have hhook : ∀ i', 1 ≤ i' →
      ((i + 1) :: List.replicate (k - 1 - i) 1).getD i' 0 ≤ 1 := by
    intro i' hi'
    obtain ⟨j, rfl⟩ : ∃ j, i' = j + 1 := ⟨i' - 1, by omega⟩
    rw [List.getD_cons_succ]
    by_cases hj : j < k - 1 - i
    · rw [getD_replicate_of_lt 1 0 (k - 1 - i) j hj]
    · rw [List.getD_eq_default _ _ (by rw [List.length_replicate]; omega)]
      omega
  have := hookCount_sum_of_hookShape _ hsorted hpos (by simp) hhook
  rwa [hookShape_sum k i hi] at this

/-- **The top mixed moment restricts to the hook shapes.** Combining the carrier confinement
(`N_k = 1` on hook shapes, `0` elsewhere) with the enumeration transfer: the `v = k` numerator of
the ν-system is a sum over the `k` hook shapes alone. This is the wiring step that turns the
per-diagram carrier lemma into the classical single-index sum of the (TAIL) first instance. -/
theorem top_mixedMoment_eq_hookShapes_sum (k : ℕ) (hk : 1 ≤ k) :
    ((partsOf k).map
        (fun l => tilt 0 (sytDim l) * (hookCount l k : ℝ) * (omega3 k l : ℝ))).sum
      = ((hookShapes k).map (fun l => tilt 0 (sytDim l) * (omega3 k l : ℝ))).sum := by
  rw [sum_partsOf_eq_sum_hookShapes k _ (fun l hl hnm => by
    rw [hookCount_top_eq_zero_of_not_mem k hk l hl hnm]
    push_cast
    ring)]
  unfold hookShapes
  rw [List.map_map, List.map_map]
  refine congrArg List.sum (List.map_congr_left fun i hi => ?_)
  simp only [Function.comp_apply]
  rw [hookCount_top_eq_one_mem k i (List.mem_range.mp hi)]
  push_cast
  ring

/-- Index shift for the column contents: `Σ_{t<c} (t+1)² = Σ_{j<c+1} j²`. -/
theorem sum_range_succ_shift (c : ℕ) :
    ∑ i ∈ Finset.range c, ((i : ℤ) + 1) ^ 2 = ∑ j ∈ Finset.range (c + 1), ((j : ℤ)) ^ 2 := by
  rw [Finset.sum_range_succ']
  simp

/-- `2·C(k,2) = k(k−1)` — the `ℕ`-division in `omega3`'s centre term is exact. -/
theorem two_mul_choose_two (k : ℕ) : 2 * (k * (k - 1) / 2) = k * (k - 1) := by
  cases k with
  | zero => rfl
  | succ r =>
      simp only [Nat.add_sub_cancel]
      rw [Nat.mul_comm (r + 1) r]
      exact Nat.mul_div_cancel' (Even.two_dvd (Nat.even_mul_succ_self r))

/-- **The bracket-arithmetic hinge**: on the hook shape with arm `a = i+1` and leg `c = k−1−i`,
six times the 3-cycle eigenvalue is the quadratic the collapse consumes,

`6·ω₃ = 2k·(3i² − 3(k−1)i + (k−1)(k−2))`.

The cubic terms of the arm and leg content sums cancel identically — this is the cancellation
recorded in `BinomialSquareSums`, here proved at the level of the diagram data
(`contentSq_hookShape` + `six_mul_sum_range_sq`). -/
theorem six_mul_omega3_hookShape (k i : ℕ) (hi : i < k) :
    6 * (omega3 k ((i + 1) :: List.replicate (k - 1 - i) 1) : ℤ)
      = 2 * (k : ℤ) * (3 * (i : ℤ) ^ 2 - 3 * ((k : ℤ) - 1) * (i : ℤ)
          + ((k : ℤ) - 1) * ((k : ℤ) - 2)) := by
  have harm : 6 * ∑ j ∈ Finset.range (i + 1), ((j : ℤ)) ^ 2
      = (i : ℤ) * ((i : ℤ) + 1) * (2 * (i : ℤ) + 1) := by
    rw [six_mul_sum_range_sq (i + 1)]
    push_cast
    ring
  have hleg : 6 * ∑ t ∈ Finset.range (k - 1 - i), ((t : ℤ) + 1) ^ 2
      = ((k : ℤ) - 1 - (i : ℤ)) * ((k : ℤ) - (i : ℤ)) * (2 * ((k : ℤ) - 1 - (i : ℤ)) + 1) := by
    rw [sum_range_succ_shift, six_mul_sum_range_sq (k - 1 - i + 1)]
    have hc : ((k - 1 - i : ℕ) : ℤ) = (k : ℤ) - 1 - (i : ℤ) := by
      have : i + 1 ≤ k := hi
      push_cast [Nat.cast_sub (by omega : i ≤ k - 1), Nat.cast_sub (by omega : 1 ≤ k)]
      ring
    push_cast [hc]
    ring
  have hcentre : ((k * (k - 1) / 2 : ℕ) : ℤ) * 2 = (k : ℤ) * ((k : ℤ) - 1) := by
    cases k with
    | zero => simp
    | succ r =>
        have h2 := two_mul_choose_two (r + 1)
        simp only [Nat.add_sub_cancel] at h2
        have hZ : (2 : ℤ) * (((r + 1) * r / 2 : ℕ) : ℤ) = ((r : ℤ) + 1) * (r : ℤ) := by
          exact_mod_cast congrArg (fun n : ℕ => (n : ℤ)) h2
        simp only [Nat.add_sub_cancel]
        push_cast
        linarith
  unfold omega3
  rw [contentSq_hookShape (i + 1) (k - 1 - i)]
  have hexp : (6 : ℤ) * ((∑ j ∈ Finset.range (i + 1), ((j : ℤ)) ^ 2)
        + ∑ t ∈ Finset.range (k - 1 - i), ((t : ℤ) + 1) ^ 2
        - ((k * (k - 1) / 2 : ℕ) : ℤ))
      = (6 * ∑ j ∈ Finset.range (i + 1), ((j : ℤ)) ^ 2)
        + (6 * ∑ t ∈ Finset.range (k - 1 - i), ((t : ℤ) + 1) ^ 2)
        - 3 * (((k * (k - 1) / 2 : ℕ) : ℤ) * 2) := by ring
  rw [hexp, harm, hleg, hcentre]
  have hik : (i : ℤ) + 1 ≤ (k : ℤ) := by exact_mod_cast hi
  ring

/-- `IdentityI.sumSqHooks` as a cell-set sum of the kernel-form hook (the two per-cell
ℕ-subtraction forms agree on genuine cells, as in `hookProd_eq_prodHooks`). -/
theorem sumSqHooks_eq_sum_cells (l : List ℕ) (hs : l.Sorted (· ≥ ·)) :
    QOU.BraidKnot.IdentityI.sumSqHooks l = ∑ p ∈ cells l, (hookLen l p : ℤ) ^ 2 := by
  have hcells : (∑ p ∈ cells l, (hookLen l p : ℤ) ^ 2)
      = ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0),
          (hookLen l (i, j) : ℤ) ^ 2 := by
    unfold cells
    rw [Finset.sum_biUnion (fun x _ y _ hxy => Finset.disjoint_left.mpr (by
        rintro p hp hq
        obtain ⟨j, _, rfl⟩ := Finset.mem_map.mp hp
        obtain ⟨j', _, h'⟩ := Finset.mem_map.mp hq
        exact hxy (by simpa using (congrArg Prod.fst h').symm)))]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Finset.sum_map]
    simp only [Function.Embedding.coeFn_mk]
  rw [hcells]
  unfold QOU.BraidKnot.IdentityI.sumSqHooks
  rw [list_sum_map_range]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [list_sum_map_range]
  refine Finset.sum_congr rfl fun j hj => ?_
  rw [Finset.mem_range] at hj
  have hstair : i < l.countP (fun x => decide (j < x)) := (lt_countP_iff l hs j i).mpr hj
  have hcell : (l.getD i 0 - j) + (QOU.BraidKnot.IdentityI.colLen l j - i) - 1
      = hookLen l (i, j) := by
    show (l.getD i 0 - j) + (QOU.BraidKnot.IdentityI.colLen l j - i) - 1
        = l.getD i 0 + (conj l).getD j 0 - j - i - 1
    rw [YoungDiagramKernelDimPos.colLen_eq_countP l j, conj_getD l hs j]
    omega
  rw [hcell]

/-- `ln ∏h` as a cell-set sum of hook logs (`hookProd_eq_prod_cells` + `Real.log_prod`). -/
theorem log_hookProd_eq_sum_cells (l : List ℕ) (hs : l.Sorted (· ≥ ·)) :
    Real.log (hookProd l) = ∑ p ∈ cells l, Real.log (hookLen l p) := by
  rw [hookProd_eq_prod_cells l]
  show Real.log ((∏ p ∈ cells l, hookLen l p : ℕ) : ℝ) = _
  rw [Nat.cast_prod]
  exact Real.log_prod _ _ fun p hp => by
    exact_mod_cast (hookLen_pos l hs p hp).ne'

/-- Spectral instance `φ = (·)²`: `Σ_v v²·N_v = Σ_□h²` per diagram. -/
theorem spectral_sq (k : ℕ) (l : List ℕ) (hl : l ∈ partsOf k) :
    ∑ v ∈ Finset.range (2 * k + 1), ((v : ℝ)) ^ 2 * (hookCount l v : ℝ)
      = (QOU.BraidKnot.IdentityI.sumSqHooks l : ℝ) := by
  have hsort := (partsOf_facts k l hl).2.2
  rw [hookSpectrum_sum k l hl (fun v => ((v : ℝ)) ^ 2),
    sumSqHooks_eq_sum_cells l hsort]
  push_cast
  rfl

/-- Spectral instance `φ = ln`: `Σ_v ln(v)·N_v = ln ∏h` per diagram. -/
theorem spectral_log (k : ℕ) (l : List ℕ) (hl : l ∈ partsOf k) :
    ∑ v ∈ Finset.range (2 * k + 1), Real.log v * (hookCount l v : ℝ)
      = Real.log (hookProd l) := by
  have hsort := (partsOf_facts k l hl).2.2
  rw [hookSpectrum_sum k l hl (fun v => Real.log v),
    log_hookProd_eq_sum_cells l hsort]

/-- Generic diagram-statistic covariance `Cov₂(S, ω₃)` (the shape shared by `covHookSq`,
`covLnHooks`, and the ν-moment sums). -/
noncomputable def covStat (k : ℕ) (S : List ℕ → ℝ) : ℝ :=
  ((partsOf k).map (fun l => tilt 0 (sytDim l) * S l * (omega3 k l : ℝ))).sum / tiltNorm k 0
    - ((partsOf k).map (fun l => tilt 0 (sytDim l) * S l)).sum / tiltNorm k 0
      * tiltedMean k 0

/-- `covStat` respects member-wise equality of statistics. -/
theorem covStat_congr (k : ℕ) {S1 S2 : List ℕ → ℝ}
    (h : ∀ l ∈ partsOf k, S1 l = S2 l) : covStat k S1 = covStat k S2 := by
  unfold covStat
  rw [List.map_congr_left (fun l hl => by rw [h l hl] :
        ∀ l ∈ partsOf k, tilt 0 (sytDim l) * S1 l * (omega3 k l : ℝ)
          = tilt 0 (sytDim l) * S2 l * (omega3 k l : ℝ)),
      List.map_congr_left (fun l hl => by rw [h l hl] :
        ∀ l ∈ partsOf k, tilt 0 (sytDim l) * S1 l = tilt 0 (sytDim l) * S2 l)]

/-- **Weighted ν-sums are statistic covariances**: for every weight `φ`,
`Σ_v φ(v)·ν_v = Cov₂(Σ_v φ(v)·N_v, ω₃)` — covariance is linear in the statistic, and the
`v`-sum assembles the diagram statistic `Σ_v φ(v)·N_v(λ)`. -/
theorem sum_weighted_nuV (k : ℕ) (φ : ℕ → ℝ) :
    ∑ v ∈ Finset.range (2 * k + 1), φ v * nuV k v
      = covStat k (fun l => ∑ v ∈ Finset.range (2 * k + 1), φ v * (hookCount l v : ℝ)) := by
  unfold nuV nuMixedMoment nuMean covStat
  rw [Finset.sum_congr rfl (fun v _ => by ring :
      ∀ v ∈ Finset.range (2 * k + 1),
        φ v * (((partsOf k).map (fun l =>
            tilt 0 (sytDim l) * (hookCount l v : ℝ) * (omega3 k l : ℝ))).sum / tiltNorm k 0
          - ((partsOf k).map (fun l =>
              tilt 0 (sytDim l) * (hookCount l v : ℝ))).sum / tiltNorm k 0
            * tiltedMean k 0)
        = (φ v * ((partsOf k).map (fun l =>
            tilt 0 (sytDim l) * (hookCount l v : ℝ) * (omega3 k l : ℝ))).sum) / tiltNorm k 0
          - (φ v * ((partsOf k).map (fun l =>
              tilt 0 (sytDim l) * (hookCount l v : ℝ))).sum) / tiltNorm k 0
            * tiltedMean k 0),
    Finset.sum_sub_distrib, ← Finset.sum_div, ← Finset.sum_mul, ← Finset.sum_div]
  rw [show (fun v => φ v * ((partsOf k).map (fun l =>
        tilt 0 (sytDim l) * (hookCount l v : ℝ) * (omega3 k l : ℝ))).sum)
      = (fun v => ((partsOf k).map (fun l =>
          φ v * (tilt 0 (sytDim l) * (hookCount l v : ℝ) * (omega3 k l : ℝ)))).sum) from
    funext fun v => (list_sum_map_mul_left _ _ _).symm]
  rw [show (fun v => φ v * ((partsOf k).map (fun l =>
        tilt 0 (sytDim l) * (hookCount l v : ℝ))).sum)
      = (fun v => ((partsOf k).map (fun l =>
          φ v * (tilt 0 (sytDim l) * (hookCount l v : ℝ)))).sum) from
    funext fun v => (list_sum_map_mul_left _ _ _).symm]
  rw [finset_sum_list_map_sum, finset_sum_list_map_sum]
  rw [List.map_congr_left (fun l _ => by
      rw [show (fun v => φ v * (tilt 0 (sytDim l) * (hookCount l v : ℝ) * (omega3 k l : ℝ)))
            = (fun v => (tilt 0 (sytDim l) * (omega3 k l : ℝ))
                * (φ v * (hookCount l v : ℝ))) from funext fun v => by ring,
        ← Finset.mul_sum]
      ring :
    ∀ l ∈ partsOf k, (∑ v ∈ Finset.range (2 * k + 1),
        φ v * (tilt 0 (sytDim l) * (hookCount l v : ℝ) * (omega3 k l : ℝ)))
      = tilt 0 (sytDim l) * (∑ v ∈ Finset.range (2 * k + 1),
          φ v * (hookCount l v : ℝ)) * (omega3 k l : ℝ))]
  rw [List.map_congr_left (fun l _ => by
      rw [show (fun v => φ v * (tilt 0 (sytDim l) * (hookCount l v : ℝ)))
            = (fun v => tilt 0 (sytDim l) * (φ v * (hookCount l v : ℝ))) from
          funext fun v => by ring,
        ← Finset.mul_sum] :
    ∀ l ∈ partsOf k, (∑ v ∈ Finset.range (2 * k + 1),
        φ v * (tilt 0 (sytDim l) * (hookCount l v : ℝ)))
      = tilt 0 (sytDim l) * (∑ v ∈ Finset.range (2 * k + 1), φ v * (hookCount l v : ℝ)))]

/-- **The ν-system's second moment is the proved variance**:
`Σ_v v²·ν_v = Cov₂(Σh², ω₃) (= Var₂(ω₃))`. -/
theorem sum_sq_nuV (k : ℕ) :
    ∑ v ∈ Finset.range (2 * k + 1), ((v : ℝ)) ^ 2 * nuV k v = covHookSq k := by
  rw [sum_weighted_nuV k (fun v => ((v : ℝ)) ^ 2),
    covStat_congr k (fun l hl => spectral_sq k l hl)]
  rfl

/-- `Σ_v v²·ν_v ≥ 0` — the positive-second-moment constraint in pure ν-form. -/
theorem sum_sq_nuV_nonneg (k : ℕ) :
    0 ≤ ∑ v ∈ Finset.range (2 * k + 1), ((v : ℝ)) ^ 2 * nuV k v := by
  rw [sum_sq_nuV]
  exact covHookSq_nonneg k

/-- **The ν-system's log moment is the [A2] hook covariance**:
`Σ_v ln(v)·ν_v = Cov₂(ln ∏h, ω₃)`. -/
theorem sum_log_nuV (k : ℕ) :
    ∑ v ∈ Finset.range (2 * k + 1), Real.log v * nuV k v = covLnHooks k := by
  rw [sum_weighted_nuV k (fun v => Real.log v),
    covStat_congr k (fun l hl => spectral_log k l hl)]
  rfl

/-- **Leg [A2] in pure ν-form (capstone)**: `Cov₂(ln f, ω₃) ≤ 0 ↔ Σ_v ln(v)·ν_v ≥ 0`. The open
kernel leg is exactly: *the mean-zero (`sum_nuV_eq_zero`), positive-second-moment
(`sum_sq_nuV_nonneg`) signed measure `ν` has nonnegative log moment.* -/
theorem covLnF_nonpos_iff_nu_log (k : ℕ) :
    covLnF k ≤ 0 ↔ 0 ≤ ∑ v ∈ Finset.range (2 * k + 1), Real.log v * nuV k v := by
  rw [sum_log_nuV]
  exact covLnF_nonpos_iff k

/-! ## The fractional-moment family and the FMP ⇒ [A2] bridge

The fractional-moment family `M_α = Σ_v v^α·ν_v` interpolates the proved even anchors
(`α = 2, 4, 6`: even hook-power moment positivity) and has [A2] as its `α → 0⁺` boundary: since
`M(0) = Σν_v = 0` (proved, `sum_nuV_eq_zero`) and `M′(0) = Σ ln(v)·ν_v` (proved below), positivity
of `M` on any right neighborhood of `0` forces the log moment — i.e. leg [A2] — to be
nonnegative. **FMP** (`M_α ≥ 0` for all `α > 0`) is the new instance-less target *above*
`KernelPincerLegs.leg_A2`; exact-`Fraction` verified `n ≤ 30`, `α ∈ [0.02, 6]`, with the minimum
always at the [A2] boundary
(`wlambda-covariance-epic-A2-fractional-moment-family.witness.json`). -/

/-- No hooks of length zero: the `v = 0` fiber of the spectrum is empty. -/
theorem hookCount_zero (l : List ℕ) (hs : l.Sorted (· ≥ ·)) : hookCount l 0 = 0 := by
  unfold hookCount
  rw [Finset.card_eq_zero]
  exact Finset.filter_eq_empty_iff.mpr fun p hp => (hookLen_pos l hs p hp).ne'

/-- The ν-system vanishes at `v = 0`. -/
theorem nuV_zero (k : ℕ) : nuV k 0 = 0 := by
  unfold nuV nuMixedMoment nuMean
  rw [List.map_congr_left (fun l hl => by
      rw [hookCount_zero l (partsOf_facts k l hl).2.2]
      push_cast
      ring :
    ∀ l ∈ partsOf k, tilt 0 (sytDim l) * (hookCount l 0 : ℝ) * (omega3 k l : ℝ) = 0)]
  rw [List.map_congr_left (fun l hl => by
      rw [hookCount_zero l (partsOf_facts k l hl).2.2]
      push_cast
      ring :
    ∀ l ∈ partsOf k, tilt 0 (sytDim l) * (hookCount l 0 : ℝ) = 0)]
  simp

/-- **The fractional-moment family** `M_α = Σ_v v^α·ν_v`, in `exp(α·ln v)` form (the `v = 0` term
is the constant `exp(α·ln 0) = exp(0) = 1` under Lean's `Real.log 0 = 0`, and is annihilated by
`nuV_zero`, so the convention is harmless). -/
noncomputable def fracMoment (k : ℕ) (α : ℝ) : ℝ :=
  ∑ v ∈ Finset.range (2 * k + 1), Real.exp (α * Real.log v) * nuV k v

/-- `M(0) = Σ_v ν_v = 0` — the zeroth-moment constraint. -/
theorem fracMoment_zero (k : ℕ) : fracMoment k 0 = 0 := by
  unfold fracMoment
  simp only [zero_mul, Real.exp_zero, one_mul]
  exact sum_nuV_eq_zero k

/-- **`M′(0) = Σ ln(v)·ν_v`** — the fractional-moment family's derivative at the boundary is
exactly the [A2] log moment (term-by-term `exp` differentiation). -/
theorem hasDerivAt_fracMoment_zero (k : ℕ) :
    HasDerivAt (fracMoment k)
      (∑ v ∈ Finset.range (2 * k + 1), Real.log v * nuV k v) 0 := by
  have h : ∀ v ∈ Finset.range (2 * k + 1),
      HasDerivAt (fun α : ℝ => Real.exp (α * Real.log v) * nuV k v)
        (Real.log v * nuV k v) 0 := by
    intro v _
    have h1 : HasDerivAt (fun α : ℝ => α * Real.log v) (Real.log v) 0 := by
      simpa using (hasDerivAt_id (0 : ℝ)).mul_const (Real.log v)
    have h2 := (h1.exp).mul_const (nuV k v)
    convert h2 using 1
    simp [Real.exp_zero]
  have h2 := HasDerivAt.sum h
  have hfun : (∑ i ∈ Finset.range (2 * k + 1), fun α : ℝ =>
      Real.exp (α * Real.log i) * nuV k i) = fracMoment k := by
    funext α
    rw [Finset.sum_apply]
    rfl
  rwa [hfun] at h2

/-- **The FMP ⇒ [A2] bridge**: if the fractional-moment family is nonnegative on any right
neighborhood `(0, ε)` of the boundary, the log moment is nonnegative — `0 = M(0) ≤ M(α)` near `0`
forces the one-sided derivative, which IS the [A2] quantity, to be `≥ 0`. -/
theorem nu_log_nonneg_of_fracMoment_nonneg (k : ℕ) {ε : ℝ} (hε : 0 < ε)
    (hFMP : ∀ α ∈ Set.Ioo (0 : ℝ) ε, 0 ≤ fracMoment k α) :
    0 ≤ ∑ v ∈ Finset.range (2 * k + 1), Real.log v * nuV k v := by
  have hD := (hasDerivAt_fracMoment_zero k).hasDerivWithinAt (s := Set.Ioi (0 : ℝ))
  rw [hasDerivWithinAt_iff_tendsto_slope,
    show Set.Ioi (0 : ℝ) \ {0} = Set.Ioi 0 from
      Set.diff_singleton_eq_self (by simp)] at hD
  refine ge_of_tendsto hD (Filter.eventually_of_mem (Ioo_mem_nhdsGT hε) ?_)
  intro α hα
  have hslope : slope (fracMoment k) 0 α = fracMoment k α / α := by
    rw [slope_def_field, fracMoment_zero, sub_zero, sub_zero]
  rw [hslope]
  exact div_nonneg (hFMP α hα) (le_of_lt hα.1)

/-- **Fractional-moment positivity (FMP)** — the new instance-less target *above* leg [A2]: the
family `M_α` is nonnegative on some right neighborhood of the boundary. Exact-`Fraction` verified
`n ≤ 30` on `α ∈ [0.02, 6]` (with the minimum always at the [A2] boundary `α → 0⁺` and survival
past the `n ≥ 29` pointwise falsification — the failing bounded weights lie outside the power
family). Providing this instance for all `k` closes leg [A2] via the bridge below. NO instance is
provided — that is the open problem, one level sharper than [A2] itself. -/
class FractionalMomentPositivity (k : ℕ) : Prop where
  pos : ∃ ε > 0, ∀ α ∈ Set.Ioo (0 : ℝ) ε, 0 ≤ fracMoment k α

/-- **FMP ⇒ leg [A2] (machine-checked)**: fractional-moment positivity near the boundary forces
`Cov₂(ln f, ω₃) ≤ 0`. -/
theorem covLnF_nonpos_of_FMP (k : ℕ) [h : FractionalMomentPositivity k] :
    covLnF k ≤ 0 := by
  obtain ⟨ε, hε, hpos⟩ := h.pos
  exact (covLnF_nonpos_iff_nu_log k).mpr (nu_log_nonneg_of_fracMoment_nonneg k hε hpos)

end QOU.BraidsAndKnots.YoungDiagramKernelPincer
