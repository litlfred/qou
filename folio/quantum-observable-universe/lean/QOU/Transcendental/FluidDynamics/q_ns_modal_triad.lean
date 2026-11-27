import QOU.Transcendental.FluidDynamics.q_ns_enstrophy_order_parameter
import QOU.FluidDynamics.q_ns_triad_core
import Mathlib.Analysis.Calculus.Deriv.MeanValue

/-!
# QOU.FluidDynamics.q_ns_modal_triad

A modal triad model of the q-NS nonlinearity, built for Part A of
`conj:regularity-breakdown` (bean `qou-pa7n`).

## Why this file exists

`QNsWellposednessContext` now carries a free transfer term `T_k` in its modal
law (owner ruling 2026-11-27). Because the class links neither `T_k` to the
amplitudes nor the amplitudes to the energy, Part A stated over it alone is
trivially true (`partA_trivial_over_weakened_class`). This file supplies the
missing structure, taken from the corpus:

* **Modes.** The `Δ_q` eigenmodes are labelled by `SU_q(2)` irreducibles
  (`thm:quantum-peter-weyl`, `prop:q-laplacian-spectral-tower`). Here the label is
  the doubled spin `n = 2j`.
* **Triads.** A quadratic nonlinearity couples mode `n` to the pair `(p, r)` only
  when `V_n` occurs in `V_p ⊗ V_r`. For generic `q` that is the `SU_q(2)` fusion
  rule (Clebsch–Gordan): the triangle inequalities plus `n + p + r` even
  (`FusionTriad`).
* **Energy.** The energy is the weighted Parseval sum `E = ∑ wₙ aₙ²`. The
  nonlinearity conserves it triad by triad
  (`wₙ Cₙₚᵣ + wₚ Cₚᵣₙ + wᵣ Cᵣₙₚ = 0`, Kraichnan's detailed conservation).

## Results (all sorry-free)

| result | statement |
|---|---|
| `galerkin_energy_conservation` | on every finite mode set, `∑ wₙ aₙ Tₙ = 0` |
| `transfer_eq_zero_of_gt` | data on modes `≤ m` feed only modes `≤ 2m` |
| `GalerkinSol.energy_hasDerivAt` | `dE/dt = −2ν ∑ wₙ λₙ aₙ²` |
| `GalerkinSol.enstrophy_le` | `Ω(t) ≤ λ_max · E(0)` |
| `partA_fails_on_truncation` | on any truncation to modes `≤ N`, `sup_t Ω` is bounded uniformly for `q ∈ (1, q₀]`, for every coefficient system and every `ν ≥ 0` |
| `kraichnan` / `kraichnan_ne_zero` | a nonzero coefficient system exists (non-vacuity) |
| `singleMode` | an explicit nonzero Galerkin solution (non-vacuity) |

## Scope (AGENTS.md (a)/(b))

`partA_fails_on_truncation` is a **(b) structural exclusion** for every finite
Galerkin truncation of the triad model. The invariant is triad-wise energy
conservation together with `qIntBal_mono`. It extends the DEC finding (PR #9434)
from one discretisation to every finite truncation and every coefficient choice.

What it shows about Part A: a divergence of `sup_t Ω` as `q → 1⁺` can only come
from energy reaching **arbitrarily high** modes. So Part A is a statement about the
infinite-mode system.

**Not established here.**
* The actual coefficients. They are the `q`-Clebsch–Gordan coefficients of
  `μ ∘ (v ⊗ ∇_q v)` on Peter–Weyl modes, and the corpus does not compute them.
  `kraichnan` is a non-vacuity witness, not the q-NS coefficient system.
* Existence for the infinite-mode system.
* Part A itself, which stays open (bean `qou-pa7n`).

No empirical value enters any proof.

## References

- [leitner2026] fluid-dynamics/q-navier-stokes.md (`def:q-navier-stokes`)
- [leitner2026] fluid-dynamics/regularity-breakdown.md (`conj:regularity-breakdown`)
- [leitner2026] fluid-dynamics/quantum-peter-weyl.md (`thm:quantum-peter-weyl`)
-/

namespace QOU.FluidDynamics.ModalTriad

open Finset QOU.QInteger QOU.FluidDynamics.EnstrophyOrderParameter

-- `FusionTriad`, `TriadCoeff`, `transfer`, `galerkin_energy_conservation`,
-- `transfer_eq_zero_of_gt` and `kraichnan` live in `QOU.FluidDynamics.q_ns_triad_core`.

/-! ### Galerkin dynamics over `ℝ` -/

/-- A solution of the Galerkin triad system on the finite mode set `S`:
    `ȧₙ = −ν λₙ aₙ + Tₙ(a)` for `n ∈ S`. -/
structure GalerkinSol (T : TriadCoeff ℝ) (S : Finset ℕ) (ν : ℝ) (lam : ℕ → ℝ) where
  /-- Mode amplitudes at time `t`. -/
  a : ℝ → ℕ → ℝ
  /-- The modal equations. -/
  deriv : ∀ n ∈ S, ∀ t,
    HasDerivAt (fun s => a s n) (-(ν * lam n) * a t n + transfer T S (a t) n) t

namespace GalerkinSol

variable {T : TriadCoeff ℝ} {S : Finset ℕ} {ν : ℝ} {lam : ℕ → ℝ}

/-- The weighted Parseval energy. -/
def energy (sol : GalerkinSol T S ν lam) (t : ℝ) : ℝ :=
  ∑ n ∈ S, T.w n * sol.a t n ^ 2

/-- The weighted enstrophy `∑ wₙ λₙ aₙ²`. -/
def enstrophy (sol : GalerkinSol T S ν lam) (t : ℝ) : ℝ :=
  ∑ n ∈ S, T.w n * lam n * sol.a t n ^ 2

/-- **Energy equality** `dE/dt = −2ν Ω`: the triads drop out. -/
theorem energy_hasDerivAt (sol : GalerkinSol T S ν lam) (t : ℝ) :
    HasDerivAt sol.energy (-(2 * ν) * sol.enstrophy t) t := by
  have h := HasDerivAt.fun_sum (u := S) (fun n hn =>
    ((hasDerivAt_pow 2 (sol.a t n)).comp t (sol.deriv n hn t)).const_mul (T.w n))
  have hc := galerkin_energy_conservation T S (sol.a t) (by norm_num)
  have hfun : sol.energy =
      fun y => ∑ n ∈ S, T.w n * ((fun x => x ^ 2) ∘ fun s => sol.a s n) y := by
    funext y; simp [energy, Function.comp]
  rw [hfun]
  refine h.congr_deriv ?_
  symm
  calc -(2 * ν) * sol.enstrophy t
      = -(2 * ν) * sol.enstrophy t
        + 2 * ∑ n ∈ S, T.w n * sol.a t n * transfer T S (sol.a t) n := by
        rw [hc]; ring
    _ = _ := by
        simp only [enstrophy, mul_sum, ← sum_add_distrib]
        refine sum_congr rfl fun n _ => ?_
        push_cast
        ring

/-- With `ν ≥ 0` and nonnegative weights and eigenvalues the energy is
    nonincreasing. -/
theorem energy_antitone (sol : GalerkinSol T S ν lam) (hν : 0 ≤ ν)
    (hw : ∀ n, 0 ≤ T.w n) (hlam : ∀ n, 0 ≤ lam n) : Antitone sol.energy := by
  refine antitone_of_deriv_nonpos
    (fun t => (sol.energy_hasDerivAt t).differentiableAt) ?_
  intro t
  rw [(sol.energy_hasDerivAt t).deriv]
  have : 0 ≤ sol.enstrophy t :=
    sum_nonneg fun n _ => mul_nonneg (mul_nonneg (hw n) (hlam n)) (sq_nonneg _)
  nlinarith

/-- **Enstrophy is bounded by the top eigenvalue times the initial energy.** -/
theorem enstrophy_le (sol : GalerkinSol T S ν lam) (hν : 0 ≤ ν)
    (hw : ∀ n, 0 ≤ T.w n) (hlam : ∀ n, 0 ≤ lam n) {Λ : ℝ}
    (hΛ : ∀ n ∈ S, lam n ≤ Λ) {t : ℝ} (ht : 0 ≤ t) :
    sol.enstrophy t ≤ Λ * sol.energy 0 := by
  have hE : sol.energy t ≤ sol.energy 0 := sol.energy_antitone hν hw hlam ht
  have hΛ0 : sol.enstrophy t ≤ Λ * sol.energy t := by
    simp only [enstrophy, energy, mul_sum]
    refine sum_le_sum fun n hn => ?_
    have := mul_le_mul_of_nonneg_right (hΛ n hn)
      (mul_nonneg (hw n) (sq_nonneg (sol.a t n)))
    nlinarith
  have hEt : 0 ≤ sol.energy t :=
    sum_nonneg fun n _ => mul_nonneg (hw n) (sq_nonneg _)
  by_cases hΛ' : 0 ≤ Λ
  · nlinarith [mul_le_mul_of_nonneg_left hE hΛ']
  · -- `Λ < 0` forces `S`-modes to have `lam n < 0`, impossible unless `S` is
    -- empty; then both sides vanish.
    have hS : S = ∅ := by
      by_contra hne
      obtain ⟨n, hn⟩ := Finset.nonempty_iff_ne_empty.mpr hne
      have := hΛ n hn
      have := hlam n
      linarith
    simp [enstrophy, energy, hS]

end GalerkinSol

/-! ### Part A fails on every finite truncation -/

/-- `[n]_q` is nondecreasing in `n` for `q > 1`. -/
theorem qIntBal_mono_n {q : ℝ} (hq : 1 < q) {n N : ℕ} (hnN : n ≤ N) :
    qIntBal q n ≤ qIntBal q N := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  rw [qIntBal_eq_chebU q hq0.ne' (sub_inv_ne_zero hq),
    qIntBal_eq_chebU q hq0.ne' (sub_inv_ne_zero hq)]
  exact monotone_nat_of_le_succ
    (fun k => (chebU_nonneg_mono (two_le_add_inv hq0) k).2) hnN

/-- **Part A fails on every finite truncation of the triad model.**

    Fix a cutoff `N` and any `q₀ > 1`. For every `q ∈ (1, q₀]`, every triad
    coefficient system (allowed to depend on `q`), every `ν ≥ 0` (Euler
    included), and every Galerkin solution on modes `≤ N` with eigenvalues
    `[n]_q²`, the enstrophy at every `t ≥ 0` is at most
    `[N]_{q₀}² · E(0)`. With data fixed in the substrate layer `E(0)` does
    not depend on `q`, so `sup_t Ω` stays bounded as `q → 1⁺`. -/
theorem partA_fails_on_truncation {N : ℕ} {q q₀ : ℝ} (hq : 1 < q) (hqq₀ : q ≤ q₀)
    {T : TriadCoeff ℝ} (hw : ∀ n, 0 ≤ T.w n) {S : Finset ℕ} (hS : ∀ n ∈ S, n ≤ N)
    {ν : ℝ} (hν : 0 ≤ ν)
    (sol : GalerkinSol T S ν (fun n => qIntBal q n ^ 2)) {t : ℝ} (ht : 0 ≤ t) :
    sol.enstrophy t ≤ qIntBal q₀ N ^ 2 * sol.energy 0 := by
  refine sol.enstrophy_le hν hw (fun n => sq_nonneg _) (fun n hn => ?_) ht
  have h1 := qIntBal_mono_n hq (hS n hn)
  have h2 := qIntBal_mono hq hqq₀ N
  have h0 := qIntBal_nonneg hq n
  have : qIntBal q n ≤ qIntBal q₀ N := le_trans h1 h2
  exact pow_le_pow_left₀ h0 this 2

/-! ### Non-vacuity: an explicit nonzero Galerkin solution -/

/-- On the single mode `{n}` the Kraichnan transfer vanishes
    (`fₙ + fₙ − 2fₙ = 0`), so `aₙ(t) = c·e^{−νλₙ t}` solves the system. -/
noncomputable def singleMode (w f : ℕ → ℝ) (hw : ∀ n, w n ≠ 0) (n : ℕ)
    (ν : ℝ) (lam : ℕ → ℝ) (c : ℝ) :
    GalerkinSol (kraichnan w f hw) {n} ν lam where
  a t m := if m = n then c * Real.exp (-(ν * lam n) * t) else 0
  deriv m hm t := by
    rw [Finset.mem_singleton] at hm
    subst hm
    have htr : transfer (kraichnan w f hw) {m}
        (fun k => if k = m then c * Real.exp (-(ν * lam m) * t) else 0) m = 0 := by
      simp only [transfer, Finset.sum_singleton, kraichnan]
      split_ifs <;> ring
    simp only [if_true, htr, add_zero]
    have := ((hasDerivAt_id t).const_mul (-(ν * lam m))).exp.const_mul c
    convert this using 1
    simp; ring

end QOU.FluidDynamics.ModalTriad
