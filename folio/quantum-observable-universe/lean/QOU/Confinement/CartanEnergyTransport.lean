import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.Algebra.Module.Basic
import Mathlib.Tactic

/-!
# Energies from `U_q(gl₂)` outside `H_n`: what separates `n` from `p`

Bean `qou-99qc`. Companion of `computations/probes/qbeta_uq_energy/`.

Every result is over a generic field `R` (§7c); nothing archimedean is used.

* **Eigenvalue transport.** An operator that commutes with `T⁺` (a twist, a Casimir, any central
  element, any `H₃` operator) takes the same eigenvalue on `v` and on `T⁺v ≠ 0`
  (`eigen_eq_of_commute`). A Cartan-type operator with `K T⁺ = c • T⁺ K` multiplies the
  eigenvalue by `c` (`eigen_mul_of_qcommute`).
* **`Ad_K`.** With `K X = c • X K` and `K K⁻¹ = 1`, `K X K⁻¹ − X = (c − 1) • X`
  (`adK_sub_self`); for the doublet `c = q²`, so the derived amplitude `(q² − 1)·T⁺` is
  `Ad_K(T⁺) − T⁺`.
* **Grouplike charge.** For Kronecker products the `q`-commutation charges multiply
  (`kron_qcommute`). So the charged-current exchange `E ⊗ F` has charge `q²·q⁻² = 1`: it commutes
  with `K ⊗ K` (`EF_commutes_KK`), and the exchange never changes the four-strand `K`-weight
  (`exchange_preserves_weight`).
* **Linear Cartan energy is a conserved charge.** If the energy is `a·H` on quark strands and
  `b·H` on the lepton strand, the energy released in `n ν → p e⁻` is `2(b − a)`
  (`linear_cartan_released`), zero when one coefficient serves all strands.
* **E₀ is not a doublet `K`-gap.** `(q − q⁻¹) = q(q − 1)` only on `(q−1)(q²−q−1) = 0`
  (`h_eq_E0gap_iff`).
-/

namespace QOU.QuarkState.CartanEnergyTransport

open Matrix

variable {R : Type*} [Field R]

/-! ## Eigenvalue transport (generic module) -/

section Transport

variable {M : Type*} [AddCommGroup M] [Module R M]

/-- A commuting operator has equal eigenvalues on `v` and on `E v ≠ 0`. -/
theorem eigen_eq_of_commute (C E : M →ₗ[R] M) (hCE : C ∘ₗ E = E ∘ₗ C) (v : M) (a b : R)
    (hv : C v = a • v) (hEv : C (E v) = b • E v) (hne : E v ≠ 0) : a = b := by
  have h1 : C (E v) = a • E v := by
    have := congrArg (fun f => f v) hCE
    simp only [LinearMap.comp_apply] at this
    rw [this, hv, map_smul]
  have h2 : (a - b) • E v = 0 := by rw [sub_smul, ← h1, ← hEv, sub_self]
  rcases smul_eq_zero.mp h2 with h | h
  · exact sub_eq_zero.mp h
  · exact absurd h hne

/-- A `c`-commuting operator multiplies the eigenvalue by `c`. -/
theorem eigen_mul_of_qcommute (K E : M →ₗ[R] M) (c : R) (hKE : K ∘ₗ E = c • (E ∘ₗ K))
    (v : M) (a : R) (hv : K v = a • v) : K (E v) = (c * a) • E v := by
  have := congrArg (fun f => f v) hKE
  simp only [LinearMap.comp_apply, LinearMap.smul_apply] at this
  rw [this, hv, map_smul, smul_smul]

end Transport

/-! ## The doublet: `K`, `E`, `F` -/

/-- `K = diag(q, q⁻¹)` on the doublet (u = e₀, d = e₁). -/
def Kd (q : R) : Matrix (Fin 2) (Fin 2) R := !![q, 0; 0, q⁻¹]
/-- `E = e₀₁` (d → u). -/
def Ed : Matrix (Fin 2) (Fin 2) R := !![0, 1; 0, 0]
/-- `F = e₁₀` (u → d). -/
def Fd : Matrix (Fin 2) (Fin 2) R := !![0, 0; 1, 0]

theorem K_E (q : R) (hq : q ≠ 0) : Kd q * Ed = (q ^ 2) • (Ed * Kd q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [Kd, Ed, Matrix.mul_apply, Fin.sum_univ_two]; try field_simp)

theorem K_F (q : R) (hq : q ≠ 0) : Kd q * Fd = (q⁻¹ ^ 2) • (Fd * Kd q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [Kd, Fd, Matrix.mul_apply, Fin.sum_univ_two]; try field_simp)

/-- `K ⁻¹`. -/
def Kinv (q : R) : Matrix (Fin 2) (Fin 2) R := !![q⁻¹, 0; 0, q]

theorem K_Kinv (q : R) (hq : q ≠ 0) : Kd q * Kinv q = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Kd, Kinv, Matrix.mul_apply, Fin.sum_univ_two, hq]

/-! ## `Ad_K` -/

/-- `K X K⁻¹ − X = (c − 1) • X` when `K X = c • X K` and `K K⁻¹ = 1`. -/
theorem adK_sub_self {n : Type*} [Fintype n] [DecidableEq n] (K Ki X : Matrix n n R) (c : R)
    (hKX : K * X = c • (X * K)) (hK : K * Ki = 1) : K * X * Ki - X = (c - 1) • X := by
  rw [hKX, Matrix.smul_mul, Matrix.mul_assoc, hK, Matrix.mul_one, sub_smul, one_smul]

/-- On the doublet: `Ad_K(E) − E = (q² − 1) • E`. -/
theorem adK_E (q : R) (hq : q ≠ 0) : Kd q * Ed * Kinv q - Ed = (q ^ 2 - 1) • Ed :=
  adK_sub_self _ _ _ _ (K_E q hq) (K_Kinv q hq)

/-! ## Grouplike charges multiply under `⊗` -/

theorem kron_qcommute {m n : Type*} (K₁ X₁ : Matrix m m R) (K₂ X₂ : Matrix n n R) (c₁ c₂ : R)
    [Fintype m] [Fintype n]
    (h₁ : K₁ * X₁ = c₁ • (X₁ * K₁)) (h₂ : K₂ * X₂ = c₂ • (X₂ * K₂)) :
    kroneckerMap (· * ·) K₁ K₂ * kroneckerMap (· * ·) X₁ X₂ =
      (c₁ * c₂) • (kroneckerMap (· * ·) X₁ X₂ * kroneckerMap (· * ·) K₁ K₂) := by
  rw [← Matrix.mul_kronecker_mul, ← Matrix.mul_kronecker_mul, h₁, h₂,
    Matrix.smul_kronecker, Matrix.kronecker_smul, smul_smul]

/-- helper: `K` has charge 1 against itself. -/
private theorem K_K (q : R) : Kd q * Kd q = (1 : R) • (Kd q * Kd q) := by rw [one_smul]

/-- The charged-current exchange `E ⊗ F` commutes with `K ⊗ K`: total charge `q²·q⁻² = 1`. -/
theorem EF_commutes_KK (q : R) (hq : q ≠ 0) :
    kroneckerMap (· * ·) (Kd q) (Kd q) * kroneckerMap (· * ·) Ed Fd =
      kroneckerMap (· * ·) Ed Fd * kroneckerMap (· * ·) (Kd q) (Kd q) := by
  rw [kron_qcommute _ _ _ _ _ _ (K_E q hq) (K_F q hq)]
  have : q ^ 2 * q⁻¹ ^ 2 = 1 := by field_simp
  rw [this, one_smul]

/-- A three-strand summand `E ⊗ K ⊗ K` of `Δ²(E)` carries charge `q²` under `K ⊗ K ⊗ K`. -/
theorem EKK_charge (q : R) (hq : q ≠ 0) :
    kroneckerMap (· * ·) (kroneckerMap (· * ·) (Kd q) (Kd q)) (Kd q) *
        kroneckerMap (· * ·) (kroneckerMap (· * ·) Ed (Kd q)) (Kd q) =
      (q ^ 2) • (kroneckerMap (· * ·) (kroneckerMap (· * ·) Ed (Kd q)) (Kd q) *
        kroneckerMap (· * ·) (kroneckerMap (· * ·) (Kd q) (Kd q)) (Kd q)) := by
  have h := kron_qcommute _ _ _ _ _ _
    (kron_qcommute _ _ _ _ _ _ (K_E q hq) (K_K q)) (K_K q)
  rw [h, mul_one, mul_one]

/-! ## Linear Cartan energy is conserved -/

/-- Weights: n = udd has `H = −1`, p = uud `H = +1`; ν = u `H = +1`, e⁻ = d `H = −1`.
Energy `a·H` on quark strands, `b·H` on the lepton strand. Released energy
`E(n) + E(ν) − E(p) − E(e⁻) = 2(b − a)`. -/
theorem linear_cartan_released (a b : R) :
    (a * (-1) + b * 1) - (a * 1 + b * (-1)) = 2 * (b - a) := by ring

theorem linear_cartan_released_zero_iff (a b : R) (h2 : (2 : R) ≠ 0) :
    (a * (-1) + b * 1) - (a * 1 + b * (-1)) = 0 ↔ a = b := by
  rw [linear_cartan_released]
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h | h
    · exact absurd h h2
    · exact (sub_eq_zero.mp h).symm
  · intro h; rw [h, sub_self, mul_zero]

/-! ## Four strands: the exchange conserves the `K⊗K` eigenvalue -/

/-- If `w` is a `K⊗K`-eigenvector (eigenvalue `a`), so is `(E⊗F) w`, with the same eigenvalue:
`n⊗ν` and its image `p⊗e⁻` are never separated by the four-strand `K`-grading. -/
theorem exchange_preserves_weight (q : R) (hq : q ≠ 0) (w : Fin 2 × Fin 2 → R) (a : R)
    (hw : (kroneckerMap (· * ·) (Kd q) (Kd q)) *ᵥ w = a • w) :
    (kroneckerMap (· * ·) (Kd q) (Kd q)) *ᵥ ((kroneckerMap (· * ·) Ed Fd) *ᵥ w) =
      a • ((kroneckerMap (· * ·) Ed Fd) *ᵥ w) := by
  rw [Matrix.mulVec_mulVec, EF_commutes_KK q hq, ← Matrix.mulVec_mulVec, hw,
    Matrix.mulVec_smul]

/-! ## The lepton strand under the #8586 functional, and E₀ -/

/-- `ε_ℓ = (q⁻¹ − q)/[2]`: the lepton strand's T³ split under `Tr(K ·)/[2]`. -/
def epsLepton (q : R) : R := (q⁻¹ - q) / (q + q⁻¹)

/-- `E₀ = m_e/(q(q−1))` (order zero). -/
def E0 (me q : R) : R := me / (q * (q - 1))

theorem epsLepton_E0 (me q : R) (hq : q ≠ 0) (h1 : q - 1 ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    epsLepton q * E0 me q = -(me * (q + 1) / (q * (q ^ 2 + 1))) := by
  have hq2 : q + q⁻¹ ≠ 0 := by
    intro h; apply h2
    have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [← this, h, mul_zero]
  unfold epsLepton E0
  field_simp
  ring

/-- `h · E₀ = m_e` iff `q = 1` or `q² − q − 1 = 0`: E₀'s gap `q(q−1)` is not the doublet gap `h`. -/
theorem h_eq_E0gap_iff (q : R) (hq : q ≠ 0) :
    q - q⁻¹ = q * (q - 1) ↔ (q - 1) * (q ^ 2 - q - 1) = 0 := by
  constructor
  · intro h
    have : q * (q - q⁻¹) = q * (q * (q - 1)) := by rw [h]
    have e : q * (q - q⁻¹) = q ^ 2 - 1 := by field_simp
    rw [e] at this
    linear_combination -this
  · intro h
    have e : q * (q - q⁻¹ - q * (q - 1)) = -((q - 1) * (q ^ 2 - q - 1)) := by
      field_simp; ring
    rw [h, neg_zero] at e
    rcases mul_eq_zero.mp e with h' | h'
    · exact absurd h' hq
    · exact sub_eq_zero.mp h'

/-- `q² − 1 = q(q−1)` iff `q = 1`. -/
theorem qsq_eq_E0gap_iff (q : R) : q ^ 2 - 1 = q * (q - 1) ↔ q = 1 := by
  constructor
  · intro h; have : q - 1 = 0 := by linear_combination h
    exact sub_eq_zero.mp this
  · intro h; subst h; ring

end QOU.QuarkState.CartanEnergyTransport

