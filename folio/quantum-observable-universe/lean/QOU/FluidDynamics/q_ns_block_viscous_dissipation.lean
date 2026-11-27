import CompactQuantumMetrics.OqSU2BudgetLittleQJacobi
import CompactQuantumMetrics.OqSU2BudgetSign

/-!
# QOU.FluidDynamics.q_ns_block_viscous_dissipation — the pair budget term is the
# viscous dissipation rate on the Cartan block

Bean `qou-q3dc` (q-NS Part A, `conj:regularity-breakdown`), point 1 of the coordinator's
split of 2026-11-27: identify the budget integrands with terms of the q-NS energy budget.

`def:q-navier-stokes` carries the viscous term `ν_q Δ_q v`. On the torus-invariant block
`K[ζ]`, `ζ = βγ`, of `O_q(SU(2))`, `CompactQuantumMetrics.OqSU2BudgetLittleQJacobi`
(#9666) computes `L = X₊ ∘ X₋` and shows the off-diagonal budget is
`h(X₊a · X₋b) = −q⁻² h(a · L b)`. This file takes the linear flow `u̇ = −ν L u` on the
block, the flow `q_ns_block_heat_loss` treats mode by mode, and proves, over the algebra:

* `lap_ev_mem`: `L` maps `K[ζ]` into itself.
* `block_viscous_energy_rate`: the Haar energy rate of that flow is
  `h(u̇ · u) + h(u · u̇) = 2 ν q² · h(X₊u · X₋u)`.
  So the X₊X₋ pair term of the budget **is** the energy rate of the flow `u̇ = −νLu`,
  up to the factor `2νq²`. That is the identification point 1 asked for, on this block.
* `compactStar_ev`: every element of `K[ζ]` is self-adjoint (`ζ* = ζ`).
* `haarState_block_lap_nonneg`: `h(u · L u) ≥ 0` on the block, for `0 < q`, `q ≠ 1`.
  So `L` is a nonnegative operator for the Haar form and `−L` has the sign of a Laplacian.
* `block_viscous_dissipates`: for `ν ≥ 0` the energy rate is `≤ 0`.
* `block_eigenmode_energy_rate`: on an eigenpolynomial `L u = λ u` the rate is
  `−2νλ h(u·u)`, which is the modal law `e(t) = e(0) exp(−2νλt)` that
  `q_ns_block_heat_loss` takes as its definition.

Hypotheses: `hs : s ^ 2 = q⁻¹` for some `s : Kˣ` is the twist hypothesis of
`haarState_plusMinus_nonpos`; it is carried, not derived.

## Not established

* That `−L` on `K[ζ]` is the restriction of the corpus's `Δ_q = d_qδ_q + δ_qd_q` from
  `def:q-navier-stokes`. The corpus does not define `d_q`, `δ_q` or `∇_q` on `O_q(SU(2))`
  (see the docstring of `q_ns_twisted_transport`). This file identifies the pair term with
  the energy rate of the flow `u̇ = −νLu`; it does not identify that flow with q-NS.
* The value of `ν` (the corpus's `ν_q = (1 − q⁻¹)/2`); here `ν` is any nonnegative scalar.
* The other weight blocks, the nonlinear term, and Part A.

Everything is algebraic (ordered field, no limits), so the file stays out of
`QOU/Transcendental/`. No empirical value enters any proof.

-- Ref: [woronowicz1987-twisted-su2] (the star structure and Haar state on `S_μU(2)`)
-- Ref: [leitner2026] (`def:q-navier-stokes`, viscous term)
-/

namespace QOU.FluidDynamics.BlockViscous

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2

section Field

variable {K : Type*} [Field K] (q : Kˣ)

/-- `L` maps the block `K[ζ]` into itself. -/
theorem lap_ev_mem (P : Polynomial K) : ∃ Q : Polynomial K, lap q (ev q P) = ev q Q := by
  induction P using Polynomial.induction_on' with
  | add P₁ P₂ h₁ h₂ =>
    obtain ⟨Q₁, e₁⟩ := h₁
    obtain ⟨Q₂, e₂⟩ := h₂
    exact ⟨Q₁ + Q₂, by rw [map_add, map_add, e₁, e₂, map_add]⟩
  | monomial n c =>
    rcases n with _ | k
    · refine ⟨0, ?_⟩
      rw [ev_monomial, pow_zero, map_smul, lap_one, smul_zero, map_zero]
    · refine ⟨Polynomial.monomial k (c * (jk ((((q⁻¹ : Kˣ) : K)) * (((q⁻¹ : Kˣ) : K))) (k + 1) *
          ((q : K) * jk ((q : K) * q) (k + 1)))) +
        Polynomial.monomial (k + 1) (c * (jk ((((q⁻¹ : Kˣ) : K)) * (((q⁻¹ : Kˣ) : K))) (k + 1) *
          jk ((q : K) * q) (k + 2))), ?_⟩
      rw [ev_monomial, map_smul, lap_zeta_pow, map_add, ev_monomial, ev_monomial,
        smul_add, smul_smul, smul_smul]

/-- **The pair budget term is the energy rate of the linear block flow.**
For `u = ev P` and `u̇ = −ν L u`, `h(u̇ u) + h(u u̇) = 2νq² h(X₊u · X₋u)`. -/
theorem block_viscous_energy_rate (hq : ∀ n, qSqNum q n ≠ 0) (ν : K) (P : Polynomial K) :
    haarState q ((-ν) • lap q (ev q P) * ev q P) +
        haarState q (ev q P * ((-ν) • lap q (ev q P))) =
      (2 * ν * ((q : K) * q)) *
        haarState q (fieldPlus q (ev q P) * fieldMinus q (ev q P)) := by
  obtain ⟨Q, hQ⟩ := lap_ev_mem q P
  have hcomm : lap q (ev q P) * ev q P = ev q P * lap q (ev q P) := by
    rw [hQ, ev_comm]
  have hb := haarState_budget_poly q hq P P
  have h0 : (q : K) ≠ 0 := q.ne_zero
  rw [smul_mul_assoc, mul_smul_comm, hcomm, map_smul, smul_eq_mul, hb]
  field_simp
  ring

/-- On an eigenpolynomial `L u = λ u` the energy rate of `u̇ = −νLu` is `−2νλ h(u·u)`. -/
theorem block_eigenmode_energy_rate (ν l : K) (P : Polynomial K)
    (hP : lap q (ev q P) = l • ev q P) :
    haarState q ((-ν) • lap q (ev q P) * ev q P) +
        haarState q (ev q P * ((-ν) • lap q (ev q P))) =
      -(2 * ν * l) * haarState q (ev q P * ev q P) := by
  rw [hP, smul_smul, smul_mul_assoc, mul_smul_comm, map_smul, smul_eq_mul]
  ring

/-- `ζ` is self-adjoint: `(βγ)* = γ*β* = (−q⁻¹β)(−qγ) = βγ`. -/
theorem compactStar_zeta : compactStar q (zetaB (R := K) q) = zetaB q := by
  rw [zetaB, compactStar_mul, compactStar_beta, compactStar_gamma, smul_mul_smul_comm,
    neg_mul_neg, Units.inv_mul, one_smul]

theorem compactStar_one' : compactStar q (1 : OqSU2 K q) = 1 := by
  simp [compactStar]

theorem compactStar_pow (x : OqSU2 K q) (n : ℕ) :
    compactStar q (x ^ n) = compactStar q x ^ n := by
  induction n with
  | zero => rw [pow_zero, pow_zero, compactStar_one']
  | succ n ih => rw [pow_succ, compactStar_mul, ih, ← pow_succ']

/-- Every element of the block `K[ζ]` is self-adjoint. -/
theorem compactStar_ev (P : Polynomial K) : compactStar q (ev q P) = ev q P := by
  induction P using Polynomial.induction_on' with
  | add P₁ P₂ h₁ h₂ => rw [map_add, map_add, h₁, h₂]
  | monomial n c => rw [ev_monomial, map_smul, compactStar_pow, compactStar_zeta]

end Field

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] (q : Kˣ)

theorem jk_pos {x : K} (hx : 0 ≤ x) (n : ℕ) : 0 < jk x (n + 1) := by
  induction n with
  | zero => rw [jk_succ', show (0 : ℕ) = 0 from rfl]; simp [jk]
  | succ n ih => rw [jk_succ']; nlinarith

theorem qSqNum_ne_zero (n : ℕ) : qSqNum q n ≠ 0 := by
  rw [qSqNum_eq_jk]
  exact (jk_pos (mul_self_nonneg (q : K)) n).ne'

/-- **`L` is nonnegative for the Haar form on the block.** -/
theorem haarState_block_lap_nonneg (hq0 : 0 < (q : K)) (hq1 : (q : K) ≠ 1) (s : Kˣ)
    (hs : s ^ 2 = q⁻¹) (P : Polynomial K) :
    0 ≤ haarState q (ev q P * lap q (ev q P)) := by
  have hb := haarState_budget_poly q (qSqNum_ne_zero q) P P
  have hn := haarState_plusMinus_nonpos q hq0 hq1 s hs (ev q P) (compactStar_ev q P)
  rw [hb] at hn
  have hpos : 0 < (q : K)⁻¹ * (q : K)⁻¹ := by positivity
  nlinarith

/-- **The linear block flow dissipates.** For `ν ≥ 0`, the Haar energy rate of
`u̇ = −νLu` on `K[ζ]` is `≤ 0`. -/
theorem block_viscous_dissipates (hq0 : 0 < (q : K)) (hq1 : (q : K) ≠ 1) (s : Kˣ)
    (hs : s ^ 2 = q⁻¹) (ν : K) (hν : 0 ≤ ν) (P : Polynomial K) :
    haarState q ((-ν) • lap q (ev q P) * ev q P) +
        haarState q (ev q P * ((-ν) • lap q (ev q P))) ≤ 0 := by
  rw [block_viscous_energy_rate q (qSqNum_ne_zero q) ν P]
  exact mul_nonpos_of_nonneg_of_nonpos (by positivity)
    (haarState_plusMinus_nonpos q hq0 hq1 s hs (ev q P) (compactStar_ev q P))

end Ordered

end QOU.FluidDynamics.BlockViscous
