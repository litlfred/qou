import QOU.Mass.QuantumSl2Irrep

/-!
# The `U_q(sl₂)` R-matrix on `V_{m+1} ⊗ V_{m'+1}`: the Cartan factor `q^{H⊗H/2}`

Stage 1b of deriving Zheng's tangle functions. Kassel's universal R-matrix (for the
coproduct of `QuantumSl2Fundamental`, `Δ(E) = E⊗K + 1⊗E`, `Δ(F) = F⊗1 + K⁻¹⊗F`) is

    R = q^{H⊗H/2} · Σ_{n≥0} q^{n(n−1)/2} (q − q⁻¹)ⁿ/[n]! · Eⁿ ⊗ Fⁿ.

On weight vectors `H` acts by `m − 2p`, so `q^{H⊗H/2}` needs half-integer powers of `q`
when `m m'` is odd. We therefore work with `s` and `q = s²` throughout.

This file builds the Cartan factor `Θ = q^{H⊗H/2}` on `V_{m+1} ⊗ V_{m'+1}` and proves the
four conjugation rules that the intertwining proof uses (`cartanTheta_E_one`,
`cartanTheta_one_E`, `cartanTheta_F_one`, `cartanTheta_one_F`):

    Θ (E⊗1) = (E⊗K) Θ,   Θ (1⊗E) = (K⊗E) Θ,
    Θ (F⊗1) = (F⊗K⁻¹) Θ, Θ (1⊗F) = (K⁻¹⊗F) Θ.

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. VII (Thm VII.2.1, §VII.7)
-/

namespace QOU.Mass.QuantumSl2

open Matrix
open scoped Kronecker

variable {𝕜 : Type*} [Field 𝕜]

/-- The weight `m − 2p` of `v_p ∈ V_{m+1}`, as an integer. -/
def wt (m p : ℕ) : ℤ := (m : ℤ) - 2 * p

/-- The `K` eigenvalue `q^{m−2p}`, rewritten as a power of `s` when `q = s²`. -/
theorem irrepKp_diag_eq (s : 𝕜) (hs : s ≠ 0) {m p : ℕ} (hp : p ≤ m) :
    (s ^ 2) ^ (m - p) * (s ^ 2)⁻¹ ^ p = s ^ (2 * wt m p) := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hp
  unfold wt
  rw [Nat.add_sub_cancel_left,
    show (2 : ℤ) * (((p + k : ℕ) : ℤ) - 2 * p) = ((2 * k : ℕ) : ℤ) - ((2 * p : ℕ) : ℤ) by
      push_cast; ring,
    zpow_sub₀ hs, zpow_natCast, zpow_natCast, ← pow_mul, inv_pow, ← pow_mul, div_eq_mul_inv]

/-- The Cartan factor `Θ = q^{H⊗H/2}`: `v_p ⊗ v_r ↦ s^{(m−2p)(m'−2r)} v_p ⊗ v_r`. -/
def cartanTheta (s : 𝕜) (m m' : ℕ) : Matrix (Fin (m + 1) × Fin (m' + 1)) (Fin (m + 1) × Fin (m' + 1)) 𝕜 :=
  Matrix.diagonal fun x => s ^ (wt m x.1 * wt m' x.2)

/-- **`Θ (E⊗1) = (E⊗K) Θ`.** -/
theorem cartanTheta_E_one (s : 𝕜) (hs : s ≠ 0) (m m' : ℕ) :
    cartanTheta s m m' * (irrepE (s ^ 2) m ⊗ₖ (1 : Matrix (Fin (m' + 1)) (Fin (m' + 1)) 𝕜))
      = (irrepE (s ^ 2) m ⊗ₖ irrepKp (s ^ 2) m') * cartanTheta s m m' := by
  ext ⟨⟨p, hp⟩, ⟨r, hr⟩⟩ ⟨⟨p', hp'⟩, ⟨r', hr'⟩⟩
  simp only [cartanTheta, diagonal_mul, mul_diagonal, kroneckerMap_apply, irrepE, irrepKp,
    diagonal_apply, one_apply, Fin.mk.injEq]
  by_cases h1 : p + 1 = p'
  · by_cases h2 : r = r'
    · subst h1 h2
      simp only [if_true, mul_one]
      rw [irrepKp_diag_eq s hs (by omega), mul_assoc, ← zpow_add₀ hs, mul_comm]
      congr 1; congr 1
      unfold wt; push_cast; ring
    · simp [h2]
  · simp [h1]


/-- The `K⁻¹` eigenvalue `q^{−(m−2p)}` as a power of `s`. -/
theorem irrepKm_diag_eq (s : 𝕜) (hs : s ≠ 0) {m p : ℕ} (hp : p ≤ m) :
    (s ^ 2)⁻¹ ^ (m - p) * (s ^ 2) ^ p = s ^ (-(2 * wt m p)) := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hp
  unfold wt
  rw [Nat.add_sub_cancel_left,
    show -((2 : ℤ) * (((p + k : ℕ) : ℤ) - 2 * p)) = ((2 * p : ℕ) : ℤ) - ((2 * k : ℕ) : ℤ) by
      push_cast; ring,
    zpow_sub₀ hs, zpow_natCast, zpow_natCast, ← pow_mul, inv_pow, ← pow_mul, div_eq_mul_inv,
    mul_comm]

/-- **`Θ (1⊗E) = (K⊗E) Θ`.** -/
theorem cartanTheta_one_E (s : 𝕜) (hs : s ≠ 0) (m m' : ℕ) :
    cartanTheta s m m' * ((1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) ⊗ₖ irrepE (s ^ 2) m')
      = (irrepKp (s ^ 2) m ⊗ₖ irrepE (s ^ 2) m') * cartanTheta s m m' := by
  ext ⟨⟨p, hp⟩, ⟨r, hr⟩⟩ ⟨⟨p', hp'⟩, ⟨r', hr'⟩⟩
  simp only [cartanTheta, diagonal_mul, mul_diagonal, kroneckerMap_apply, irrepE, irrepKp,
    diagonal_apply, one_apply, Fin.mk.injEq]
  by_cases h1 : p = p'
  · by_cases h2 : r + 1 = r'
    · subst h1 h2
      simp only [if_true, one_mul]
      rw [irrepKp_diag_eq s hs (by omega), mul_comm (s ^ (2 * wt m p)), mul_assoc,
        ← zpow_add₀ hs, mul_comm]
      congr 1; congr 1
      unfold wt; push_cast; ring
    · simp [h2]
  · simp [h1]

/-- **`Θ (F⊗1) = (F⊗K⁻¹) Θ`.** -/
theorem cartanTheta_F_one (s : 𝕜) (hs : s ≠ 0) (m m' : ℕ) :
    cartanTheta s m m' * (irrepF (s ^ 2) m ⊗ₖ (1 : Matrix (Fin (m' + 1)) (Fin (m' + 1)) 𝕜))
      = (irrepF (s ^ 2) m ⊗ₖ irrepKm (s ^ 2) m') * cartanTheta s m m' := by
  ext ⟨⟨p, hp⟩, ⟨r, hr⟩⟩ ⟨⟨p', hp'⟩, ⟨r', hr'⟩⟩
  simp only [cartanTheta, diagonal_mul, mul_diagonal, kroneckerMap_apply, irrepF, irrepKm,
    diagonal_apply, one_apply, Fin.mk.injEq]
  by_cases h1 : p = p' + 1
  · by_cases h2 : r = r'
    · subst h1 h2
      simp only [if_true, mul_one]
      rw [irrepKm_diag_eq s hs (by omega), mul_assoc, ← zpow_add₀ hs, mul_comm]
      congr 1; congr 1
      unfold wt; push_cast; ring
    · simp [h2]
  · simp [h1]

/-- **`Θ (1⊗F) = (K⁻¹⊗F) Θ`.** -/
theorem cartanTheta_one_F (s : 𝕜) (hs : s ≠ 0) (m m' : ℕ) :
    cartanTheta s m m' * ((1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) ⊗ₖ irrepF (s ^ 2) m')
      = (irrepKm (s ^ 2) m ⊗ₖ irrepF (s ^ 2) m') * cartanTheta s m m' := by
  ext ⟨⟨p, hp⟩, ⟨r, hr⟩⟩ ⟨⟨p', hp'⟩, ⟨r', hr'⟩⟩
  simp only [cartanTheta, diagonal_mul, mul_diagonal, kroneckerMap_apply, irrepF, irrepKm,
    diagonal_apply, one_apply, Fin.mk.injEq]
  by_cases h1 : p = p'
  · by_cases h2 : r = r' + 1
    · subst h1 h2
      simp only [if_true, one_mul]
      rw [irrepKm_diag_eq s hs (by omega), mul_comm (s ^ (-(2 * wt m p))), mul_assoc,
        ← zpow_add₀ hs, mul_comm]
      congr 1; congr 1
      unfold wt; push_cast; ring
    · simp [h2]
  · simp [h1]


/-! ### The polynomial part `S = Σ c_n Eⁿ ⊗ Fⁿ` and its commutation with `Δ(E)` -/

/-- The quantum factorial `[n]! = [1][2]⋯[n]`. -/
def qfact (q : 𝕜) (n : ℕ) : 𝕜 := ∏ k ∈ Finset.range n, qint q (k + 1)

/-- The R-matrix coefficient `c_n = q^{n(n−1)/2} (q − q⁻¹)ⁿ / [n]!`, with `q = s²`. -/
def rcoef (s : 𝕜) (n : ℕ) : 𝕜 := s ^ (n * (n - 1)) * (s ^ 2 - (s ^ 2)⁻¹) ^ n / qfact (s ^ 2) n

/-- `c_{n+1} [n+1] = c_n q^n (q − q⁻¹)`, whenever `[n+1] ≠ 0`. -/
theorem rcoef_succ (s : 𝕜) (n : ℕ) (hn : qint (s ^ 2) (n + 1) ≠ 0) :
    rcoef s (n + 1) * qint (s ^ 2) (n + 1) = rcoef s n * (s ^ 2) ^ n * (s ^ 2 - (s ^ 2)⁻¹) := by
  unfold rcoef qfact
  rw [Finset.prod_range_succ]
  by_cases h0 : ∏ k ∈ Finset.range n, qint (s ^ 2) (k + 1) = 0
  · simp [h0]
  have e : (n + 1) * (n + 1 - 1) = n * (n - 1) + 2 * n := by
    cases n with
    | zero => rfl
    | succ k => simp only [Nat.add_sub_cancel]; ring
  rw [e, pow_add, pow_succ, ← pow_mul]
  field_simp

namespace Rep

variable {q : 𝕜} {ι κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ]

/-- `K⁻¹ Fⁿ = q^{2n} Fⁿ K⁻¹`. -/
theorem Km_F_pow (hq : q ≠ 0) (ρ : Rep q ι) (n : ℕ) :
    ρ.Km * ρ.F ^ n = (q ^ 2) ^ n • (ρ.F ^ n * ρ.Km) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, ← mul_assoc, ih, smul_mul_assoc, mul_assoc, Km_F hq, mul_smul_comm, smul_smul,
      ← mul_assoc]
    congr 1
    rw [pow_succ (q ^ 2)]

/-- The truncated polynomial part `S = Σ_{n ≤ M} c_n Eⁿ ⊗ Fⁿ` on `V ⊗ W`. -/
def rSum (s : 𝕜) (ρ : Rep (s ^ 2) ι) (σ : Rep (s ^ 2) κ) (M : ℕ) :
    Matrix (ι × κ) (ι × κ) 𝕜 :=
  ∑ n ∈ Finset.range (M + 1), rcoef s n • ((ρ.E ^ n) ⊗ₖ (σ.F ^ n))

/-- The termwise identity `c_{k+1} [k+1] Fᵏ D_k = c_k (Fᵏ K − K⁻¹ Fᵏ)`. -/
theorem rcoef_term (s : 𝕜) (hs : s ≠ 0) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (σ : Rep (s ^ 2) κ)
    (k : ℕ) (hk : qint (s ^ 2) (k + 1) ≠ 0) :
    rcoef s (k + 1) • qint (s ^ 2) (k + 1) • (σ.F ^ k * σ.Dk k)
      = rcoef s k • (σ.F ^ k * σ.Kp - σ.Km * σ.F ^ k) := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hc := rcoef_succ s k hk
  rw [Km_F_pow hq, smul_smul, hc]
  unfold Dk
  have h4 : s ^ 4 - 1 ≠ 0 := by
    intro h; apply hq2; field_simp; linear_combination h
  simp only [mul_sub, mul_smul_comm]
  match_scalars
  · field_simp
    rw [mul_assoc, ← mul_pow, mul_one_div_cancel (pow_ne_zero 2 hs), one_pow, mul_one]
  · field_simp
    ring

/-- **`S Δ(E) = Δ'(E) S`** with `Δ(E) = E⊗K + 1⊗E` and `Δ'(E) = 1⊗E + E⊗K⁻¹`, whenever
`E^{M+1} = 0` on the first factor and `[k] ≠ 0` for `1 ≤ k ≤ M`. -/
theorem rSum_E (s : 𝕜) (hs : s ≠ 0) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)
    (ρ : Rep (s ^ 2) ι) (σ : Rep (s ^ 2) κ) (M : ℕ) (hE : ρ.E ^ (M + 1) = 0)
    (hint : ∀ k < M, qint (s ^ 2) (k + 1) ≠ 0) :
    rSum s ρ σ M * (ρ.E ⊗ₖ σ.Kp + 1 ⊗ₖ σ.E)
      = (1 ⊗ₖ σ.E + ρ.E ⊗ₖ σ.Km) * rSum s ρ σ M := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hB : rSum s ρ σ M * (ρ.E ⊗ₖ σ.Kp) - (ρ.E ⊗ₖ σ.Km) * rSum s ρ σ M
      = ∑ k ∈ Finset.range M,
          rcoef s k • ((ρ.E ^ (k + 1)) ⊗ₖ (σ.F ^ k * σ.Kp - σ.Km * σ.F ^ k)) := by
    simp only [rSum, Finset.sum_mul, Finset.mul_sum, ← Finset.sum_sub_distrib]
    rw [Finset.sum_range_succ]
    rw [smul_mul_assoc, mul_smul_comm, ← mul_kronecker_mul, ← mul_kronecker_mul, ← pow_succ,
      ← pow_succ', hE, zero_kronecker, zero_kronecker, smul_zero, sub_self, add_zero]
    refine Finset.sum_congr rfl fun k _ => ?_
    rw [smul_mul_assoc, mul_smul_comm, ← mul_kronecker_mul, ← mul_kronecker_mul, ← pow_succ,
      ← pow_succ', ← smul_sub, kronecker_sub']
  have hA : (1 ⊗ₖ σ.E) * rSum s ρ σ M - rSum s ρ σ M * (1 ⊗ₖ σ.E)
      = ∑ k ∈ Finset.range M,
          rcoef s (k + 1) • ((ρ.E ^ (k + 1)) ⊗ₖ (σ.E * σ.F ^ (k + 1) - σ.F ^ (k + 1) * σ.E)) := by
    simp only [rSum, Finset.sum_mul, Finset.mul_sum, ← Finset.sum_sub_distrib]
    rw [Finset.sum_range_succ']
    simp only [smul_mul_assoc, mul_smul_comm, ← mul_kronecker_mul, pow_zero, one_mul, mul_one,
      sub_self, add_zero]
    refine Finset.sum_congr rfl fun k _ => ?_
    rw [kronecker_sub', smul_sub]
  have key : rSum s ρ σ M * (ρ.E ⊗ₖ σ.Kp) - (ρ.E ⊗ₖ σ.Km) * rSum s ρ σ M
      = (1 ⊗ₖ σ.E) * rSum s ρ σ M - rSum s ρ σ M * (1 ⊗ₖ σ.E) := by
    rw [hA, hB]
    refine Finset.sum_congr rfl fun k hk => ?_
    rw [E_F_pow hq hq2]
    simp only [← kronecker_smul]
    rw [rcoef_term s hs hq2 σ k (hint k (Finset.mem_range.mp hk))]
  rw [mul_add, add_mul]
  exact sub_eq_sub_iff_add_eq_add.mp key

end Rep

end QOU.Mass.QuantumSl2
