import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# The K-weight exponent of the nucleon split is forced, on every level of the tower

Owner, 2026-11-27: *"make sure you work on all strands on the full tower"*, *"dervie k-weight
expoentn"*, *"dont look at leadgin term only"*. Beans `qou-myts`, `qou-99qc`.

The Gibbs map of PR #9475 gives `m_n − m_p = E·log(τ_p/τ_n)`, and every route so far has had
`τ_p/τ_n = q²` from the `K`-weight `K = diag(q, q⁻¹)` of the convention-D trace
`Tr(K^{⊗n} ·)/[2]^n`. This file asks where the exponent `2` comes from and whether anything on
the tower can change it.

## What is proved

1. `markov_forces_K`: on one strand pair, with the corpus braiding `Ř` (the matrices of
   `NucleonWeightSpaceTraces`: `Ř(u⊗u) = q·u⊗u`, `Ř(d⊗d) = q·d⊗d`, `Ř(u⊗d) = d⊗u`,
   `Ř(d⊗u) = u⊗d + h·d⊗u`, `h = q − q⁻¹`), let `K` be **any** `2 × 2` matrix. If the
   `K`-weighted partial trace has the Markov property, `ptr_K(Ř) = z·ptr_K(1)`, then `K` is
   diagonal and `q²·K_dd = K_uu`. Nothing else is assumed: not that `K` is diagonal, not that it
   commutes with `Ř`, not its normalisation.
2. `markov_forces_z`: for `K ≠ 0` the Markov parameter is `z = q³/(q²+1)`, i.e. convention D.
   `markov_K_exists` shows the diagonal solution does satisfy the Markov property, so (1) is not
   vacuous.
3. `mirror_forces_K`: with the mirror braiding (the `h` on the other off-diagonal entry) the
   relation is `q²·K_uu = K_dd`. So the **magnitude** of the exponent is `2` for either
   orientation; the orientation only decides which of `u`, `d` carries the larger weight.
4. `strandWeight_flip`: on `n = a + b + 1` strands, a configuration with one more `u` than
   another has `K^{⊗n}`-eigenvalue `q²` times larger, for every `a, b`. The exponent does not
   depend on the tower level.
5. `spectator_ratio`: spectator strands enter as a tensor factor and cancel from `τ_p/τ_n`.
6. `gibbs_split_full_tower`: hence, whenever `τ_p = q²·τ_n`, the Gibbs split is `2E·log q`.

7. `left_markov_forces_K`, `no_two_sided_markov`: the partial trace over the FIRST strand is
   Markov only for the inverse weight (`q²·K_uu = K_dd`), so no single `K` is Markov on both
   sides unless `q⁴ = 1`. The convention-D trace reduces spectators on the right of a tagged block
   by the Markov conditional expectation and does not reduce spectators on its left.

Consequence for the tower (with `NucleonSplitSingleElement.tauP_eq` / `tauN_eq`: `τ_p = q·t`,
`τ_n = q⁻¹·t` for every element of the 3-strand braid algebra). For a tagged nucleon whose
spectators all lie to its right, the `K`-weighted sum over spectator colourings is the Markov
conditional expectation `E_{n→3}` (item 1: `ptr_K(x·σ_{n−1}·y) = z·x·y`), it lands in `H_3`, and
`τ_p/τ_n = q²` exactly at every `n`, to all orders in `q`. The iteration of item 1 over `n` is
the standard Jones argument and is **not** formalised here for general `n`; the probe checks it
exactly at `n = 6` over `ℤ[q, q⁻¹]` and at `n = 9` at rational `q`. For a tagged nucleon with entangled spectators
on its left, item 7 removes the argument, and the probe finds the ratio is element-dependent.
Spectators that enter as a tensor factor cancel on either side (item 5).

## What is NOT claimed

* Nothing about `E` (the scale) or about distinct elements for the two nucleons (route 2).
* No numerical value enters. Generic `[Field R]` except item 6, which uses `Real.log` (§7c).

-- Ref: [leitner2026] docs/audits/2026-11-27-nucleon-split-full-tower.md
-- Ref: [leitner2026] docs/audits/2026-11-27-nucleon-split-single-element-theorem.md
-/

namespace QOU.Nuclear.NucleonSplitFullTower

open Matrix

section Generic

variable {R : Type*} [Field R]

/-- The corpus braiding `Ř` on `C² ⊗ C²`, index `(strand₁, strand₂)` with `0 = u`, `1 = d`.
Same matrices as `NucleonWeightSpaceTraces` (`σ₁` on the proton weight space). -/
def rCheck (q : R) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R := fun a b =>
  if a = (0, 0) ∧ b = (0, 0) then q
  else if a = (1, 1) ∧ b = (1, 1) then q
  else if a = (1, 0) ∧ b = (0, 1) then 1
  else if a = (0, 1) ∧ b = (1, 0) then 1
  else if a = (1, 0) ∧ b = (1, 0) then q - q⁻¹
  else 0

/-- The mirror braiding: the skein term on the other off-diagonal entry. -/
def rMirror (q : R) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R := fun a b =>
  if a = (0, 0) ∧ b = (0, 0) then q
  else if a = (1, 1) ∧ b = (1, 1) then q
  else if a = (1, 0) ∧ b = (0, 1) then 1
  else if a = (0, 1) ∧ b = (1, 0) then 1
  else if a = (0, 1) ∧ b = (0, 1) then q - q⁻¹
  else 0

/-- `K`-weighted partial trace over the second strand: `(id ⊗ Tr)((1 ⊗ K)·M)`. -/
def ptrK (K : Matrix (Fin 2) (Fin 2) R) (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R) :
    Matrix (Fin 2) (Fin 2) R :=
  fun i j => ∑ k : Fin 2, ∑ m : Fin 2, K k m * M (i, m) (j, k)

theorem ptrK_one (K : Matrix (Fin 2) (Fin 2) R) (i j : Fin 2) :
    ptrK K 1 i j = if i = j then K 0 0 + K 1 1 else 0 := by
  fin_cases i <;> fin_cases j <;>
    simp [ptrK, Fin.sum_univ_two, Matrix.one_apply]

theorem ptrK_rCheck (q : R) (K : Matrix (Fin 2) (Fin 2) R) :
    ptrK K (rCheck q) 0 0 = q * K 0 0 ∧ ptrK K (rCheck q) 0 1 = K 0 1 ∧
    ptrK K (rCheck q) 1 0 = K 1 0 ∧
    ptrK K (rCheck q) 1 1 = (q - q⁻¹) * K 0 0 + q * K 1 1 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> simp [ptrK, rCheck, Fin.sum_univ_two] <;> ring

theorem ptrK_rMirror (q : R) (K : Matrix (Fin 2) (Fin 2) R) :
    ptrK K (rMirror q) 0 0 = q * K 0 0 + (q - q⁻¹) * K 1 1 ∧
    ptrK K (rMirror q) 0 1 = K 0 1 ∧ ptrK K (rMirror q) 1 0 = K 1 0 ∧
    ptrK K (rMirror q) 1 1 = q * K 1 1 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> simp [ptrK, rMirror, Fin.sum_univ_two] <;> ring

/-- **The Markov property forces the `K`-weight.** Any `K` whose weighted partial trace is
Markov for the corpus braiding is diagonal with `q²·K_dd = K_uu`. -/
theorem markov_forces_K (q z : R) (hq : q ≠ 0) (K : Matrix (Fin 2) (Fin 2) R)
    (hM : ∀ i j, ptrK K (rCheck q) i j = z * ptrK K 1 i j) :
    K 0 1 = 0 ∧ K 1 0 = 0 ∧ q ^ 2 * K 1 1 = K 0 0 := by
  obtain ⟨h00, h01, h10, h11⟩ := ptrK_rCheck q K
  have e00 := hM 0 0; have e01 := hM 0 1; have e10 := hM 1 0; have e11 := hM 1 1
  rw [ptrK_one] at e00 e01 e10 e11
  simp at e00 e01 e10 e11
  refine ⟨by rw [← h01, e01], by rw [← h10, e10], ?_⟩
  have key : q * K 0 0 = (q - q⁻¹) * K 0 0 + q * K 1 1 := by rw [← h00, ← h11, e00, e11]
  have : q⁻¹ * K 0 0 = q * K 1 1 := by linear_combination key
  have hq' : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  linear_combination (-q) * this + K 0 0 * hq'

/-- The Markov parameter that goes with it is convention D's `z = q³/(q²+1)`. -/
theorem markov_forces_z (q z : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (K : Matrix (Fin 2) (Fin 2) R) (hK : K 0 0 ≠ 0)
    (hM : ∀ i j, ptrK K (rCheck q) i j = z * ptrK K 1 i j) :
    z = q ^ 3 / (q ^ 2 + 1) := by
  obtain ⟨-, -, hd⟩ := markov_forces_K q z hq K hM
  obtain ⟨h00, -, -, -⟩ := ptrK_rCheck q K
  have e00 := hM 0 0
  rw [ptrK_one, h00] at e00
  simp at e00
  -- q·K00 = z·(K00 + K11), and q²·K11 = K00
  have hsum : q ^ 2 * (K 0 0 + K 1 1) = K 0 0 * (q ^ 2 + 1) := by linear_combination hd
  have hK' : K 0 0 + K 1 1 ≠ 0 := by
    intro h0; rw [h0, mul_zero] at hsum
    exact mul_ne_zero hK hq2 hsum.symm
  rw [eq_div_iff hq2]
  have : q ^ 3 * (K 0 0 + K 1 1) = z * (q ^ 2 + 1) * (K 0 0 + K 1 1) := by
    linear_combination q * hsum + (q ^ 2 + 1) * e00
  exact (mul_right_cancel₀ hK' this).symm

/-- The diagonal weight `diag(a, a/q²)` is Markov with `z = q³/(q²+1)`: the forcing theorem is
not vacuous. -/
theorem markov_K_exists (q a : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    ∀ i j, ptrK (!![a, 0; 0, a / q ^ 2]) (rCheck q) i j =
      q ^ 3 / (q ^ 2 + 1) * ptrK (!![a, 0; 0, a / q ^ 2]) 1 i j := by
  intro i j
  obtain ⟨h00, h01, h10, h11⟩ := ptrK_rCheck q (!![a, 0; 0, a / q ^ 2])
  rw [ptrK_one]
  fin_cases i <;> fin_cases j <;> simp_all <;> field_simp <;> ring

/-- **Mirror orientation**: the same magnitude, with `u` and `d` exchanged. -/
theorem mirror_forces_K (q z : R) (hq : q ≠ 0) (K : Matrix (Fin 2) (Fin 2) R)
    (hM : ∀ i j, ptrK K (rMirror q) i j = z * ptrK K 1 i j) :
    K 0 1 = 0 ∧ K 1 0 = 0 ∧ q ^ 2 * K 0 0 = K 1 1 := by
  obtain ⟨h00, h01, h10, h11⟩ := ptrK_rMirror q K
  have e00 := hM 0 0; have e01 := hM 0 1; have e10 := hM 1 0; have e11 := hM 1 1
  rw [ptrK_one] at e00 e01 e10 e11
  simp at e00 e01 e10 e11
  refine ⟨by rw [← h01, e01], by rw [← h10, e10], ?_⟩
  have key : q * K 0 0 + (q - q⁻¹) * K 1 1 = q * K 1 1 := by rw [← h00, ← h11, e00, e11]
  have : q * K 0 0 = q⁻¹ * K 1 1 := by linear_combination key
  have hq' : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  linear_combination q * this + K 1 1 * hq'

/-- `K`-weighted partial trace over the FIRST strand: `(Tr ⊗ id)((K ⊗ 1)·M)`. -/
def ptrKL (K : Matrix (Fin 2) (Fin 2) R) (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R) :
    Matrix (Fin 2) (Fin 2) R :=
  fun i j => ∑ k : Fin 2, ∑ m : Fin 2, K k m * M (m, i) (k, j)

theorem ptrKL_one (K : Matrix (Fin 2) (Fin 2) R) (i j : Fin 2) :
    ptrKL K 1 i j = if i = j then K 0 0 + K 1 1 else 0 := by
  fin_cases i <;> fin_cases j <;>
    simp [ptrKL, Fin.sum_univ_two, Matrix.one_apply]

/-- **The left partial trace is Markov only for the INVERSE weight.** For the corpus braiding,
a `K` whose first-strand partial trace is Markov has `q²·K_uu = K_dd`: the opposite of
`markov_forces_K`. -/
theorem left_markov_forces_K (q z : R) (hq : q ≠ 0) (K : Matrix (Fin 2) (Fin 2) R)
    (hM : ∀ i j, ptrKL K (rCheck q) i j = z * ptrKL K 1 i j) :
    K 0 1 = 0 ∧ K 1 0 = 0 ∧ q ^ 2 * K 0 0 = K 1 1 := by
  have h00 : ptrKL K (rCheck q) 0 0 = q * K 0 0 + (q - q⁻¹) * K 1 1 := by
    simp [ptrKL, rCheck, Fin.sum_univ_two]; ring
  have h01 : ptrKL K (rCheck q) 0 1 = K 0 1 := by simp [ptrKL, rCheck, Fin.sum_univ_two]
  have h10 : ptrKL K (rCheck q) 1 0 = K 1 0 := by simp [ptrKL, rCheck, Fin.sum_univ_two]
  have h11 : ptrKL K (rCheck q) 1 1 = q * K 1 1 := by
    simp [ptrKL, rCheck, Fin.sum_univ_two]; ring
  have e00 := hM 0 0; have e01 := hM 0 1; have e10 := hM 1 0; have e11 := hM 1 1
  rw [ptrKL_one] at e00 e01 e10 e11
  simp at e00 e01 e10 e11
  refine ⟨by rw [← h01, e01], by rw [← h10, e10], ?_⟩
  have key : q * K 0 0 + (q - q⁻¹) * K 1 1 = q * K 1 1 := by rw [← h00, ← h11, e00, e11]
  have : q * K 0 0 = q⁻¹ * K 1 1 := by linear_combination key
  have hq' : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  linear_combination q * this + K 1 1 * hq'

/-- **No two-sided Markov weight.** One `K` cannot make both partial traces Markov unless
`q⁴ = 1` or `K_uu = 0`. So the convention-D trace `Tr(K^{⊗n}·)` reduces spectators on the RIGHT
of a tagged block by the Markov conditional expectation, and does not reduce spectators on its
LEFT. -/
theorem no_two_sided_markov (q z w : R) (hq : q ≠ 0) (K : Matrix (Fin 2) (Fin 2) R)
    (hR : ∀ i j, ptrK K (rCheck q) i j = z * ptrK K 1 i j)
    (hL : ∀ i j, ptrKL K (rCheck q) i j = w * ptrKL K 1 i j) :
    (q ^ 4 - 1) * K 0 0 = 0 := by
  obtain ⟨-, -, hr⟩ := markov_forces_K q z hq K hR
  obtain ⟨-, -, hl⟩ := left_markov_forces_K q w hq K hL
  linear_combination q ^ 2 * hl + hr

/-- `K^{⊗n}` eigenvalue on a strand configuration with `a` up and `b` down strands. -/
def strandWeight (ku kd : R) (a b : ℕ) : R := ku ^ a * kd ^ b

/-- **Tower independence.** With the forced weight `q²·k_d = k_u`, turning one `d` strand into a
`u` strand multiplies the `K^{⊗n}` eigenvalue by `q²`, for every `a, b` (every `n = a + b + 1`). -/
theorem strandWeight_flip (q ku kd : R) (hd : q ^ 2 * kd = ku) (a b : ℕ) :
    strandWeight ku kd (a + 1) b = q ^ 2 * strandWeight ku kd a (b + 1) := by
  unfold strandWeight; rw [← hd]; ring

/-- Spectator strands enter `τ_p` and `τ_n` as the same tensor factor and cancel from the
ratio. -/
theorem spectator_ratio {m k : Type*} [Fintype m] [Fintype k]
    (Ap An : Matrix m m R) (B : Matrix k k R) (hB : trace B ≠ 0) :
    trace (kroneckerMap (· * ·) Ap B) / trace (kroneckerMap (· * ·) An B) =
      trace Ap / trace An := by
  rw [trace_kronecker, trace_kronecker, mul_div_mul_right _ _ hB]

end Generic

/-- The Gibbs split on any tower level where `τ_p = q²·τ_n`. -/
theorem gibbs_split_full_tower {q E τn : ℝ} (hτ : 0 < τn) :
    E * Real.log (q ^ 2 * τn / τn) = 2 * E * Real.log q := by
  rw [mul_div_assoc, div_self hτ.ne', mul_one, Real.log_pow]; push_cast; ring

end QOU.Nuclear.NucleonSplitFullTower
