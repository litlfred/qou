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

It then builds the polynomial part `S = Σ_{n ≤ M} c_n Eⁿ ⊗ Fⁿ` (`Rep.rSum`, for any two
representations), proves `S Δ(x) = Δ'(x) S` for `x = E, F, K^{±1}` (`Rep.rSum_E`, `Rep.rSum_F`,
`Rep.rSum_Kp`, `Rep.rSum_Km`), and assembles `R = Θ S` on `V_{m+1} ⊗ V_{m'+1}` (`rMat`) with the
intertwining property `R Δ(x) = Δ^op(x) R` (`rMat_E`, `rMat_F`, `rMat_Kp`, `rMat_Km`). The only
hypotheses are `s ≠ 0`, `q ≠ q⁻¹` and `[k] ≠ 0` for `1 ≤ k ≤ max m m'`; the last holds at the
Kashaev point `s = e^{πi/N}` for `m, m' < N`.

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

/-- **`Θ (E⊗K⁻¹) = (E⊗1) Θ`.** -/
theorem cartanTheta_E_Km (s : 𝕜) (hs : s ≠ 0) (m m' : ℕ) :
    cartanTheta s m m' * (irrepE (s ^ 2) m ⊗ₖ irrepKm (s ^ 2) m')
      = (irrepE (s ^ 2) m ⊗ₖ (1 : Matrix (Fin (m' + 1)) (Fin (m' + 1)) 𝕜)) * cartanTheta s m m' := by
  ext ⟨⟨p, hp⟩, ⟨r, hr⟩⟩ ⟨⟨p', hp'⟩, ⟨r', hr'⟩⟩
  simp only [cartanTheta, diagonal_mul, mul_diagonal, kroneckerMap_apply, irrepE, irrepKm,
    diagonal_apply, one_apply, Fin.mk.injEq]
  by_cases h1 : p + 1 = p'
  · by_cases h2 : r = r'
    · subst h1 h2
      simp only [if_true, mul_one]
      rw [irrepKm_diag_eq s hs (by omega), mul_left_comm, ← zpow_add₀ hs]
      congr 1; congr 1
      unfold wt; push_cast; ring
    · simp [h2]
  · simp [h1]

/-- **`Θ (K⊗F) = (1⊗F) Θ`.** -/
theorem cartanTheta_Kp_F (s : 𝕜) (hs : s ≠ 0) (m m' : ℕ) :
    cartanTheta s m m' * (irrepKp (s ^ 2) m ⊗ₖ irrepF (s ^ 2) m')
      = ((1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) ⊗ₖ irrepF (s ^ 2) m') * cartanTheta s m m' := by
  ext ⟨⟨p, hp⟩, ⟨r, hr⟩⟩ ⟨⟨p', hp'⟩, ⟨r', hr'⟩⟩
  simp only [cartanTheta, diagonal_mul, mul_diagonal, kroneckerMap_apply, irrepF, irrepKp,
    diagonal_apply, one_apply, Fin.mk.injEq]
  by_cases h1 : p = p'
  · by_cases h2 : r = r' + 1
    · subst h1 h2
      simp only [if_true, one_mul]
      rw [irrepKp_diag_eq s hs (by omega), ← mul_assoc, ← zpow_add₀ hs, mul_comm]
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

/-- `K E = q² E K`. -/
theorem Kp_E (ρ : Rep q ι) : ρ.Kp * ρ.E = q ^ 2 • (ρ.E * ρ.Kp) := by
  have h := congrArg (· * ρ.Kp) ρ.KE
  simp only [mul_assoc, ρ.Km_Kp, mul_one, smul_mul_assoc] at h
  exact h

/-- `E K = q⁻² K E`. -/
theorem E_Kp (hq : q ≠ 0) (ρ : Rep q ι) : ρ.E * ρ.Kp = q⁻¹ ^ 2 • (ρ.Kp * ρ.E) := by
  rw [Kp_E, smul_smul, ← mul_pow, inv_mul_cancel₀ hq, one_pow, one_smul]

/-- `K⁻¹ E = q⁻² E K⁻¹`. -/
theorem Km_E (hq : q ≠ 0) (ρ : Rep q ι) : ρ.Km * ρ.E = q⁻¹ ^ 2 • (ρ.E * ρ.Km) := by
  rw [E_Km, smul_smul, ← mul_pow, inv_mul_cancel₀ hq, one_pow, one_smul]

/-- `K Eⁿ = q^{2n} Eⁿ K`. -/
theorem Kp_E_pow (ρ : Rep q ι) (n : ℕ) :
    ρ.Kp * ρ.E ^ n = (q ^ 2) ^ n • (ρ.E ^ n * ρ.Kp) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, ← mul_assoc, ih, smul_mul_assoc, mul_assoc, Kp_E, mul_smul_comm, smul_smul,
      ← mul_assoc]
    congr 1
    rw [pow_succ (q ^ 2)]

/-- `K⁻¹ Eⁿ = q^{−2n} Eⁿ K⁻¹`. -/
theorem Km_E_pow (hq : q ≠ 0) (ρ : Rep q ι) (n : ℕ) :
    ρ.Km * ρ.E ^ n = (q⁻¹ ^ 2) ^ n • (ρ.E ^ n * ρ.Km) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, ← mul_assoc, ih, smul_mul_assoc, mul_assoc, Km_E hq, mul_smul_comm, smul_smul,
      ← mul_assoc]
    congr 1
    rw [pow_succ (q⁻¹ ^ 2)]

/-- `E D_n = D_{n+2} E`. -/
theorem E_Dk (hq : q ≠ 0) (ρ : Rep q ι) (n : ℕ) : ρ.E * ρ.Dk n = ρ.Dk (n + 2) * ρ.E := by
  unfold Dk
  simp only [mul_smul_comm, smul_mul_assoc, mul_sub, sub_mul, E_Kp hq, E_Km, smul_smul]
  congr 2 <;> congr 1 <;> ring

/-- **`[E^{n+1}, F] = [n+1] D_n Eⁿ`** (Kassel, Lemma VI.1.3). -/
theorem E_pow_F (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) (ρ : Rep q ι) (n : ℕ) :
    ρ.E ^ (n + 1) * ρ.F - ρ.F * ρ.E ^ (n + 1) = qint q (n + 1) • (ρ.Dk n * ρ.E ^ n) := by
  induction n with
  | zero =>
    have h1 : qint q 1 = 1 := by unfold qint; simp [div_self hq2]
    simp only [zero_add, pow_one, pow_zero, mul_one, h1, one_smul, Dk, ρ.EF]
  | succ n ih =>
    have hsplit : ρ.E ^ (n + 1 + 1) * ρ.F - ρ.F * ρ.E ^ (n + 1 + 1)
        = ρ.E * (ρ.E ^ (n + 1) * ρ.F - ρ.F * ρ.E ^ (n + 1))
          + (ρ.E * ρ.F - ρ.F * ρ.E) * ρ.E ^ (n + 1) := by
      rw [pow_succ' ρ.E (n + 1), mul_sub, sub_mul]
      simp only [mul_assoc]
      abel
    have h0 : (q - q⁻¹)⁻¹ • (ρ.Kp - ρ.Km) = ρ.Dk 0 := by simp [Dk]
    rw [hsplit, ih, ρ.EF, h0, mul_smul_comm, ← mul_assoc, E_Dk hq, mul_assoc, ← pow_succ',
      ← smul_mul_assoc, ← add_mul, Dk_comb hq ρ n, smul_mul_assoc]

/-- The termwise identity for `F`: `−c_{k+1}[k+1] D_k Eᵏ = c_k (Eᵏ K⁻¹ − K Eᵏ)`. -/
theorem rcoef_termF (s : 𝕜) (hs : s ≠ 0) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (ρ : Rep (s ^ 2) ι)
    (k : ℕ) (hk : qint (s ^ 2) (k + 1) ≠ 0) :
    rcoef s (k + 1) • -(qint (s ^ 2) (k + 1) • (ρ.Dk k * ρ.E ^ k))
      = rcoef s k • (ρ.E ^ k * ρ.Km - ρ.Kp * ρ.E ^ k) := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hc := rcoef_succ s k hk
  have h4 : s ^ 4 - 1 ≠ 0 := by
    intro h; apply hq2; field_simp; linear_combination h
  rw [smul_neg, smul_smul, hc]
  unfold Dk
  simp only [smul_mul_assoc, sub_mul, Kp_E_pow, Km_E_pow hq]
  match_scalars <;>
  · field_simp
    ring_nf
    rw [mul_assoc, ← mul_pow, mul_inv_cancel₀ hs, one_pow, mul_one]

/-- **`S Δ(F) = Δ'(F) S`** with `Δ(F) = K⁻¹⊗F + F⊗1` and `Δ'(F) = F⊗1 + K⊗F`, whenever
`F^{M+1} = 0` on the second factor and `[k] ≠ 0` for `1 ≤ k ≤ M`. -/
theorem rSum_F (s : 𝕜) (hs : s ≠ 0) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)
    (ρ : Rep (s ^ 2) ι) (σ : Rep (s ^ 2) κ) (M : ℕ) (hF : σ.F ^ (M + 1) = 0)
    (hint : ∀ k < M, qint (s ^ 2) (k + 1) ≠ 0) :
    rSum s ρ σ M * (ρ.Km ⊗ₖ σ.F + ρ.F ⊗ₖ 1)
      = (ρ.F ⊗ₖ 1 + ρ.Kp ⊗ₖ σ.F) * rSum s ρ σ M := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hB : rSum s ρ σ M * (ρ.Km ⊗ₖ σ.F) - (ρ.Kp ⊗ₖ σ.F) * rSum s ρ σ M
      = ∑ k ∈ Finset.range M,
          rcoef s k • ((ρ.E ^ k * ρ.Km - ρ.Kp * ρ.E ^ k) ⊗ₖ (σ.F ^ (k + 1))) := by
    simp only [rSum, Finset.sum_mul, Finset.mul_sum, ← Finset.sum_sub_distrib]
    rw [Finset.sum_range_succ]
    simp only [smul_mul_assoc, mul_smul_comm, ← mul_kronecker_mul, ← pow_succ, ← pow_succ', hF,
      kronecker_zero, smul_zero, sub_self, add_zero]
    refine Finset.sum_congr rfl fun k _ => ?_
    rw [sub_kronecker', smul_sub]
  have hA : (ρ.F ⊗ₖ 1) * rSum s ρ σ M - rSum s ρ σ M * (ρ.F ⊗ₖ 1)
      = ∑ k ∈ Finset.range M,
          rcoef s (k + 1) • ((ρ.F * ρ.E ^ (k + 1) - ρ.E ^ (k + 1) * ρ.F) ⊗ₖ (σ.F ^ (k + 1))) := by
    simp only [rSum, Finset.sum_mul, Finset.mul_sum, ← Finset.sum_sub_distrib]
    rw [Finset.sum_range_succ']
    simp only [smul_mul_assoc, mul_smul_comm, ← mul_kronecker_mul, pow_zero, one_mul, mul_one,
      sub_self, add_zero]
    refine Finset.sum_congr rfl fun k _ => ?_
    rw [sub_kronecker', smul_sub]
  have key : rSum s ρ σ M * (ρ.Km ⊗ₖ σ.F) - (ρ.Kp ⊗ₖ σ.F) * rSum s ρ σ M
      = (ρ.F ⊗ₖ 1) * rSum s ρ σ M - rSum s ρ σ M * (ρ.F ⊗ₖ 1) := by
    rw [hA, hB]
    refine Finset.sum_congr rfl fun k hk => ?_
    rw [← neg_sub (ρ.E ^ (k + 1) * ρ.F), E_pow_F hq hq2, ← smul_kronecker, ← smul_kronecker,
      rcoef_termF s hs hq2 ρ k (hint k (Finset.mem_range.mp hk))]
  rw [mul_add, add_mul]
  exact sub_eq_sub_iff_add_eq_add.mp key

/-- `K Fⁿ = q^{−2n} Fⁿ K`. -/
theorem Kp_F_pow (ρ : Rep q ι) (n : ℕ) :
    ρ.Kp * ρ.F ^ n = (q⁻¹ ^ 2) ^ n • (ρ.F ^ n * ρ.Kp) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, ← mul_assoc, ih, smul_mul_assoc, mul_assoc, Kp_F, mul_smul_comm, smul_smul,
      ← mul_assoc]
    congr 1
    rw [pow_succ (q⁻¹ ^ 2)]

/-- **`S` commutes with `Δ(K) = K⊗K`.** -/
theorem rSum_Kp (s : 𝕜) (hs : s ≠ 0) (ρ : Rep (s ^ 2) ι) (σ : Rep (s ^ 2) κ) (M : ℕ) :
    rSum s ρ σ M * (ρ.Kp ⊗ₖ σ.Kp) = (ρ.Kp ⊗ₖ σ.Kp) * rSum s ρ σ M := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  simp only [rSum, Finset.sum_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl fun n _ => ?_
  rw [smul_mul_assoc, mul_smul_comm, ← mul_kronecker_mul, ← mul_kronecker_mul, Kp_E_pow,
    Kp_F_pow, smul_kronecker, kronecker_smul, smul_smul, smul_smul, mul_assoc, ← mul_pow,
    ← mul_pow, mul_inv_cancel₀ hq, one_pow, one_pow, mul_one]

/-- **`S` commutes with `Δ(K⁻¹) = K⁻¹⊗K⁻¹`.** -/
theorem rSum_Km (s : 𝕜) (hs : s ≠ 0) (ρ : Rep (s ^ 2) ι) (σ : Rep (s ^ 2) κ) (M : ℕ) :
    rSum s ρ σ M * (ρ.Km ⊗ₖ σ.Km) = (ρ.Km ⊗ₖ σ.Km) * rSum s ρ σ M := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  simp only [rSum, Finset.sum_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl fun n _ => ?_
  rw [smul_mul_assoc, mul_smul_comm, ← mul_kronecker_mul, ← mul_kronecker_mul, Km_E_pow hq,
    Km_F_pow hq, smul_kronecker, kronecker_smul, smul_smul, smul_smul, mul_assoc, ← mul_pow,
    ← mul_pow, inv_mul_cancel₀ hq, one_pow, one_pow, mul_one]

end Rep

/-! ### Nilpotency of `E` and `F` on `V_{m+1}` -/

theorem irrepE_pow_apply (q : 𝕜) (m k : ℕ) (i j : Fin (m + 1)) (h : (i : ℕ) + k ≠ j) :
    (irrepE q m ^ k) i j = 0 := by
  induction k generalizing j with
  | zero =>
    rw [pow_zero, Matrix.one_apply, if_neg]
    intro hij; exact h (by simp [hij])
  | succ k ih =>
    rw [pow_succ, Matrix.mul_apply]
    refine Finset.sum_eq_zero fun l _ => ?_
    by_cases hl : (i : ℕ) + k = l
    · have : irrepE q m l j = 0 := by
        simp only [irrepE]; rw [if_neg]; omega
      rw [this, mul_zero]
    · rw [ih l hl, zero_mul]

theorem irrepE_pow_nil (q : 𝕜) (m : ℕ) : irrepE q m ^ (m + 1) = 0 := by
  ext i j
  rw [irrepE_pow_apply q m (m + 1) i j (by omega), Matrix.zero_apply]

theorem irrepF_pow_apply (q : 𝕜) (m k : ℕ) (i j : Fin (m + 1)) (h : (i : ℕ) ≠ j + k) :
    (irrepF q m ^ k) i j = 0 := by
  induction k generalizing j with
  | zero =>
    rw [pow_zero, Matrix.one_apply, if_neg]
    intro hij; exact h (by simp [hij])
  | succ k ih =>
    rw [pow_succ, Matrix.mul_apply]
    refine Finset.sum_eq_zero fun l _ => ?_
    by_cases hl : (l : ℕ) = j + 1
    · rw [ih l (by omega), zero_mul]
    · have : irrepF q m l j = 0 := by
        simp only [irrepF]; rw [if_neg hl]
      rw [this, mul_zero]

theorem irrepF_pow_nil (q : 𝕜) (m : ℕ) : irrepF q m ^ (m + 1) = 0 := by
  ext i j
  rw [irrepF_pow_apply q m (m + 1) i j (by omega), Matrix.zero_apply]


/-! ### The R-matrix `R = Θ S` on `V_{m+1} ⊗ V_{m'+1}` and its intertwining property -/

section RMatrix

variable (s : 𝕜) (hs : s ≠ 0)

/-- The truncation order `M = max m m'`, at which both `E` on `V_{m+1}` and `F` on `V_{m'+1}`
are nilpotent. -/
def rOrder (m m' : ℕ) : ℕ := max m m'

/-- **The `U_q(sl₂)` R-matrix** `R = q^{H⊗H/2} Σ_n c_n Eⁿ ⊗ Fⁿ` on `V_{m+1} ⊗ V_{m'+1}`. -/
def rMat (m m' : ℕ) : Matrix (Fin (m + 1) × Fin (m' + 1)) (Fin (m + 1) × Fin (m' + 1)) 𝕜 :=
  cartanTheta s m m' *
    Rep.rSum s (irrep (pow_ne_zero 2 hs) m) (irrep (pow_ne_zero 2 hs) m') (rOrder m m')

variable (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)

include hs hq2 in
/-- **`R Δ(E) = Δ^op(E) R`.** -/
theorem rMat_E (m m' : ℕ) (hint : ∀ k < rOrder m m', qint (s ^ 2) (k + 1) ≠ 0) :
    rMat s hs m m' * (irrepE (s ^ 2) m ⊗ₖ irrepKp (s ^ 2) m' + 1 ⊗ₖ irrepE (s ^ 2) m')
      = (irrepKp (s ^ 2) m ⊗ₖ irrepE (s ^ 2) m' + irrepE (s ^ 2) m ⊗ₖ 1) * rMat s hs m m' := by
  have hE : (irrep (pow_ne_zero 2 hs) m).E ^ (rOrder m m' + 1) = 0 :=
    pow_eq_zero_of_le (by unfold rOrder; omega) (irrepE_pow_nil (s ^ 2) m)
  have h := Rep.rSum_E s hs hq2 (irrep (pow_ne_zero 2 hs) m) (irrep (pow_ne_zero 2 hs) m')
    (rOrder m m') hE hint
  unfold rMat
  rw [mul_assoc]
  erw [h]
  rw [← mul_assoc, mul_add]
  erw [cartanTheta_one_E s hs, cartanTheta_E_Km s hs]
  rw [← add_mul, mul_assoc]

include hs hq2 in
/-- **`R Δ(F) = Δ^op(F) R`.** -/
theorem rMat_F (m m' : ℕ) (hint : ∀ k < rOrder m m', qint (s ^ 2) (k + 1) ≠ 0) :
    rMat s hs m m' * (irrepKm (s ^ 2) m ⊗ₖ irrepF (s ^ 2) m' + irrepF (s ^ 2) m ⊗ₖ 1)
      = (1 ⊗ₖ irrepF (s ^ 2) m' + irrepF (s ^ 2) m ⊗ₖ irrepKm (s ^ 2) m') * rMat s hs m m' := by
  have hF : (irrep (pow_ne_zero 2 hs) m').F ^ (rOrder m m' + 1) = 0 :=
    pow_eq_zero_of_le (by unfold rOrder; omega) (irrepF_pow_nil (s ^ 2) m')
  have h := Rep.rSum_F s hs hq2 (irrep (pow_ne_zero 2 hs) m) (irrep (pow_ne_zero 2 hs) m')
    (rOrder m m') hF hint
  unfold rMat
  rw [mul_assoc]
  erw [h]
  rw [← mul_assoc, mul_add]
  erw [cartanTheta_F_one s hs, cartanTheta_Kp_F s hs]
  rw [← add_mul, mul_assoc]
  congr 1
  abel

theorem cartanTheta_comm_diag (m m' : ℕ) (d : Fin (m + 1) × Fin (m' + 1) → 𝕜) :
    cartanTheta s m m' * Matrix.diagonal d = Matrix.diagonal d * cartanTheta s m m' := by
  unfold cartanTheta
  rw [diagonal_mul_diagonal, diagonal_mul_diagonal]
  congr 1; funext x; exact mul_comm _ _

include hs in
/-- **`R` commutes with `Δ(K) = K⊗K`.** -/
theorem rMat_Kp (m m' : ℕ) :
    rMat s hs m m' * (irrepKp (s ^ 2) m ⊗ₖ irrepKp (s ^ 2) m')
      = (irrepKp (s ^ 2) m ⊗ₖ irrepKp (s ^ 2) m') * rMat s hs m m' := by
  have h := Rep.rSum_Kp s hs (irrep (pow_ne_zero 2 hs) m) (irrep (pow_ne_zero 2 hs) m')
    (rOrder m m')
  unfold rMat
  rw [mul_assoc]
  erw [h]
  rw [← mul_assoc, ← mul_assoc]
  congr 1
  change cartanTheta s m m' * (irrepKp (s ^ 2) m ⊗ₖ irrepKp (s ^ 2) m')
    = (irrepKp (s ^ 2) m ⊗ₖ irrepKp (s ^ 2) m') * cartanTheta s m m'
  rw [irrepKp, irrepKp, diagonal_kronecker_diagonal, cartanTheta_comm_diag]

include hs in
/-- **`R` commutes with `Δ(K⁻¹) = K⁻¹⊗K⁻¹`.** -/
theorem rMat_Km (m m' : ℕ) :
    rMat s hs m m' * (irrepKm (s ^ 2) m ⊗ₖ irrepKm (s ^ 2) m')
      = (irrepKm (s ^ 2) m ⊗ₖ irrepKm (s ^ 2) m') * rMat s hs m m' := by
  have h := Rep.rSum_Km s hs (irrep (pow_ne_zero 2 hs) m) (irrep (pow_ne_zero 2 hs) m')
    (rOrder m m')
  unfold rMat
  rw [mul_assoc]
  erw [h]
  rw [← mul_assoc, ← mul_assoc]
  congr 1
  change cartanTheta s m m' * (irrepKm (s ^ 2) m ⊗ₖ irrepKm (s ^ 2) m')
    = (irrepKm (s ^ 2) m ⊗ₖ irrepKm (s ^ 2) m') * cartanTheta s m m'
  rw [irrepKm, irrepKm, diagonal_kronecker_diagonal, cartanTheta_comm_diag]

end RMatrix

end QOU.Mass.QuantumSl2
