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

end QOU.Mass.QuantumSl2
