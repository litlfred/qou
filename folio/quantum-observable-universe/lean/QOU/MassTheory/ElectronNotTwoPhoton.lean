/-
  The electron `σ₀σ₁σ₀` is not a two-photon product (audit
  2026-11-21-proton-q3-kl-coordinate, Rounds 8–9).

  Photon (owner ruling 2026-11-20): `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹`.

  Setting. `H₃(q)` at generic `q` is semisimple with three irreducible blocks: the trivial
  character (`σᵢ ↦ q`), the sign character (`σᵢ ↦ -q⁻¹`) and the two-dimensional
  representation `S0, S1` below. An identity `γ·γ' = λ·σ₀σ₁σ₀` in `H₃(q)` holds iff it
  holds in each block. **That Wedderburn bridge is not formalised here**: the theorem takes
  the three block identities as hypotheses.

  Results (field `R`, `q ≠ 0`, `q² + 1 ≠ 0`, `q² ± q + 1 ≠ 0`).
  * `S0`, `S1` satisfy the Hecke relation and the braid relation (`hecke_S0`, `hecke_S1`,
    `braid_S`), and `S1inv` is the inverse of `S1`.
  * `vertex_cube`: on the two-dimensional block `V = S0·S1⁻¹` obeys
    `V³ = 1 + h²(V - V²)`, `h = q - q⁻¹`. On the two one-dimensional blocks `V ↦ 1`, where
    the same identity is `1 = 1`.
  * `electron_not_two_photon`: if the three block identities hold for
    `γ(a, b, c)·γ(a', b', c') = λ·σ₀σ₁σ₀`, then `λ = 0`. The proof is an explicit algebraic
    certificate: `λ·det γ` and `det γ·det γ' + λ²` are combinations of the block equations,
    so `λ³ = 0`.

  -- Ref: [leitner2026] def:photon; audit Rounds 8–9
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases

namespace QOU.MassTheory.ElectronNotTwoPhoton

open Matrix

variable {R : Type*} [Field R]

/-- `σ₀` in the two-dimensional block. -/
def S0 (q : R) : Matrix (Fin 2) (Fin 2) R := !![q, 0; 1, -1 / q]
/-- `σ₁` in the two-dimensional block. -/
def S1 (q : R) : Matrix (Fin 2) (Fin 2) R := !![-1 / q, 1; 0, q]
/-- `σ₁⁻¹` in the two-dimensional block. -/
def S1inv (q : R) : Matrix (Fin 2) (Fin 2) R := !![-q, 1; 0, 1 / q]

/-- The photon `1 + a·σ₀ + b·σ₁ + c·σ₀σ₁⁻¹` in the two-dimensional block. -/
def photonMat (q a b c : R) : Matrix (Fin 2) (Fin 2) R :=
  1 + a • S0 q + b • S1 q + c • (S0 q * S1inv q)

/-- The electron `σ₀σ₁σ₀` in the two-dimensional block. -/
def electronMat (q : R) : Matrix (Fin 2) (Fin 2) R := S0 q * S1 q * S0 q

/-- A photon under the trivial character `σᵢ ↦ q` (the vertex maps to `q·q⁻¹ = 1`). -/
def trivPhoton (q a b c : R) : R := 1 + q * (a + b) + c
/-- A photon under the sign character `σᵢ ↦ -q⁻¹` (the vertex maps to `1`). -/
def signPhoton (q a b c : R) : R := 1 - (a + b) / q + c

theorem S1_mul_S1inv (q : R) (hq : q ≠ 0) : S1 q * S1inv q = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [S1, S1inv, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

theorem hecke_S0 (q : R) (hq : q ≠ 0) :
    S0 q * S0 q = (q - q⁻¹) • S0 q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [S0, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

theorem hecke_S1 (q : R) (hq : q ≠ 0) :
    S1 q * S1 q = (q - q⁻¹) • S1 q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [S1, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

theorem braid_S (q : R) (hq : q ≠ 0) :
    S0 q * S1 q * S0 q = S1 q * S0 q * S1 q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [S0, S1, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

/-- `V³ = 1 + h²(V - V²)` for the chiral vertex `V = σ₀σ₁⁻¹` on the two-dimensional block. -/
theorem vertex_cube (q : R) (hq : q ≠ 0) :
    let V := S0 q * S1inv q
    V * V * V = 1 + (q - q⁻¹) ^ 2 • (V - V * V) := by
  intro V
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [V, S0, S1inv, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring


/-- Entries of a photon in the two-dimensional block. -/
theorem photonMat_eq (q a b c : R) (hq : q ≠ 0) :
    photonMat q a b c = !![a * q - b / q - c * q ^ 2 + 1, b + c * q;
      a - c * q, -a / q + b * q + c - c / q ^ 2 + 1] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [photonMat, S0, S1, S1inv] <;> field_simp <;> ring

/-- The electron `σ₀σ₁σ₀` in the two-dimensional block is the antidiagonal `-1`. -/
theorem electronMat_eq (q : R) (hq : q ≠ 0) : electronMat q = !![0, -1; -1, 0] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [electronMat, S0, S1, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;>
    first | ring1 | simp

set_option maxHeartbeats 1000000 in
/-- **The electron is not a two-photon product.** If
`γ(a,b,c)·γ(a',b',c') = λ·σ₀σ₁σ₀` holds on the two-dimensional block and under the trivial
and sign characters (where `σ₀σ₁σ₀ ↦ q³` and `↦ -q⁻³`), then `λ = 0`. -/
theorem electron_not_two_photon (q a b c a' b' c' l : R) (hq : q ≠ 0)
    (h1 : q ^ 2 + 1 ≠ 0) (h2 : q ^ 2 - q + 1 ≠ 0) (h3 : q ^ 2 + q + 1 ≠ 0)
    (h : photonMat q a b c * photonMat q a' b' c' = l • electronMat q)
    (ht : trivPhoton q a b c * trivPhoton q a' b' c' = l * q ^ 3)
    (hs : signPhoton q a b c * signPhoton q a' b' c' = -l / q ^ 3) :
    l = 0 := by
  rw [photonMat_eq q a b c hq, photonMat_eq q a' b' c' hq, electronMat_eq q hq,
    Matrix.mul_fin_two, Matrix.smul_of] at h
  have h00 := congrFun (congrFun h 0) 0
  have h01 := congrFun (congrFun h 0) 1
  have h10 := congrFun (congrFun h 1) 0
  have h11 := congrFun (congrFun h 1) 1
  simp only [Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.head_cons, Matrix.head_fin_const,
    Pi.smul_apply, smul_eq_mul] at h00 h01 h10 h11
  simp only [trivPhoton, signPhoton] at ht hs
  have H00 : a*a'*q^4 - a*b'*q^2 - a*c'*q^5 + a*q^3 - a'*c*q^5 + a'*c*q^3 + a'*q^3 + b*b' - b*q + b'*c*q^3 - b'*q + c*c'*q^6 - c*c'*q^4 - c*q^4 - c'*q^4 + q^2 = 0 := by
    linear_combination (norm := skip) q ^ 2 * h00
    field_simp
    ring
  have H01 : a*b'*q^3 + a*c'*q^4 - a'*b*q - a'*c*q^2 + b*b'*q^3 - b*b'*q - b*c' + b*q^2 + b'*q^2 - c*c'*q^5 + c*c'*q^3 - c*c'*q + c*q^3 + c'*q^3 + l*q^2 = 0 := by
    linear_combination (norm := skip) q ^ 2 * h01
    field_simp
    ring
  have H10 : a*a'*q^3 - a*a'*q - a*b'*q - a*c'*q^4 + a*c'*q^2 + a*q^2 + a'*b*q^3 - a'*c*q^4 + a'*c*q^2 - a'*c + a'*q^2 - b*c'*q^4 + b'*c*q^2 + c*c'*q^5 - c*c'*q^3 + c*c'*q - c*q^3 - c'*q^3 + l*q^2 = 0 := by
    linear_combination (norm := skip) q ^ 2 * h10
    field_simp
    ring
  have H11 : a*a'*q^2 + a*c'*q^5 - a*c'*q^3 + a*c'*q - a*q^3 - a'*b*q^4 - a'*c*q^3 + a'*c*q - a'*q^3 + b*b'*q^6 + b*c'*q^5 - b*c'*q^3 + b*q^5 - b'*c*q^3 + b'*q^5 - c*c'*q^6 + c*c'*q^4 - 2*c*c'*q^2 + c*c' + c*q^4 - c*q^2 + c'*q^4 - c'*q^2 + q^4 = 0 := by
    linear_combination (norm := skip) q ^ 4 * h11
    field_simp
    ring
  have HT : a*a'*q^2 + a*b'*q^2 + a*c'*q + a*q + a'*b*q^2 + a'*c*q + a'*q + b*b'*q^2 + b*c'*q + b*q + b'*c*q + b'*q + c*c' + c + c' - l*q^3 + 1 = 0 := by
    linear_combination (norm := skip) q ^ 0 * ht
    field_simp
    ring
  have HS : a*a'*q + a*b'*q - a*c'*q^2 - a*q^2 + a'*b*q - a'*c*q^2 - a'*q^2 + b*b'*q - b*c'*q^2 - b*q^2 - b'*c*q^2 - b'*q^2 + c*c'*q^3 + c*q^3 + c'*q^3 + l + q^3 = 0 := by
    linear_combination (norm := skip) q ^ 3 * hs
    field_simp
    ring
  have hD : q ^ 3 * ((q ^ 2 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1)) ≠ 0 :=
    mul_ne_zero (pow_ne_zero _ hq) (mul_ne_zero (mul_ne_zero h1 h2) h3)
  have hDld : q ^ 3 * ((q ^ 2 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1)) *
      (l * (-a^2*q^3 + a*b*q^5 - a*b*q^3 + a*b*q + a*c*q^4 - a*c*q^2 + a*q^4 - a*q^2 - b^2*q^3 - b*c*q^6 + b*c*q^4 - b*c*q^2 + b*c + b*q^4 - b*q^2 + c^2*q^3 - c*q^5 + c*q^3 - c*q + q^3)) = 0 := by
    linear_combination (-a^3*b*q^9 + a^3*b*q^5 + a^3*c*q^8 + a^3*c*q^6 - a^3*q^8 - a^3*q^6 + a^2*b^2*q^11 - 3*a^2*b^2*q^9 + 3*a^2*b^2*q^5 - a^2*b^2*q^3 + a^2*b*c*q^10 + a^2*b*c*q^8 + 3*a^2*b*q^10 - 3*a^2*b*q^8 - 3*a^2*b*q^6 + 3*a^2*b*q^4 - 2*a^2*c^2*q^9 - a^2*c^2*q^7 + a^2*c^2*q^5 + a^2*c*q^7 + a^2*c*q^5 + 2*a^2*q^9 - 2*a^2*q^5 + 2*a*b^3*q^11 - 3*a*b^3*q^9 - a*b^3*q^7 + 3*a*b^3*q^5 - a*b^3*q^3 - 2*a*b^2*c*q^12 + 3*a*b^2*c*q^10 - a*b^2*c*q^8 - a*b^2*c*q^6 + 3*a*b^2*c*q^4 - 2*a*b^2*c*q^2 - a*b^2*q^12 + 7*a*b^2*q^10 - 3*a*b^2*q^8 - 5*a*b^2*q^6 + 5*a*b^2*q^4 - a*b^2*q^2 + a*b*c^2*q^11 - a*b*c^2*q^9 - 2*a*b*c^2*q^3 - 4*a*b*c*q^11 + 2*a*b*c*q^9 - 3*a*b*c*q^5 + 3*a*b*c*q^3 - 2*a*b*q^11 + 7*a*b*q^9 + 2*a*b*q^7 - 5*a*b*q^5 + 2*a*b*q^3 + a*c^3*q^10 - a*c^3*q^8 - 2*a*c^3*q^6 + 2*a*c^2*q^10 - a*c^2*q^8 - a*c^2*q^6 + 2*a*c^2*q^4 - 2*a*c*q^10 - a*c*q^8 - a*c*q^6 - 2*a*c*q^4 - a*q^10 + 2*a*q^8 + 2*a*q^6 - a*q^4 + b^4*q^11 - b^4*q^9 - b^4*q^7 + b^4*q^5 - 2*b^3*c*q^12 + 2*b^3*c*q^10 - b^3*c*q^8 - b^3*c*q^6 + 3*b^3*c*q^4 - b^3*c*q^2 - b^3*q^12 + 4*b^3*q^10 - b^3*q^8 - 4*b^3*q^6 + 2*b^3*q^4 + b^2*c^2*q^13 + b^2*c^2*q^9 + b^2*c^2*q^3 - b^2*c^2*q + b^2*c*q^13 - 6*b^2*c*q^11 + 2*b^2*c*q^9 - 2*b^2*c*q^7 - 5*b^2*c*q^5 + 5*b^2*c*q^3 - b^2*c*q - 3*b^2*q^11 + 5*b^2*q^9 + 2*b^2*q^7 - 5*b^2*q^5 + b^2*q^3 - b*c^3*q^12 - b*c^3*q^8 + b*c^3*q^4 - b*c^3*q^2 + b*c^2*q^12 + b*c^2*q^10 + b*c^2*q^8 + b*c^2*q^6 + b*c^2*q^4 + b*c^2*q^2 + 2*b*c*q^12 - 4*b*c*q^10 + b*c*q^8 - 5*b*c*q^4 + 2*b*c*q^2 - 3*b*q^10 + 2*b*q^8 + 3*b*q^6 - 2*b*q^4 + c^4*q^9 + c^4*q^7 - c^3*q^11 + c^3*q^9 - c^3*q^5 + c^3*q^3 + c^2*q^9 - c^2*q^5 + c*q^11 + c*q^7 + c*q^5 - c*q^3 - q^9 + q^5) * H00 + (-a^3*b*q^8 + a^3*b*q^4 + a^3*c*q^7 + a^3*c*q^5 - a^3*q^7 - a^3*q^5 + a^2*b^2*q^10 - 2*a^2*b^2*q^8 + 2*a^2*b^2*q^4 - a^2*b^2*q^2 + a^2*b*c*q^9 - a^2*b*c*q^7 - a^2*b*c*q^5 + a^2*b*c*q^3 + 3*a^2*b*q^9 - 2*a^2*b*q^7 - 2*a^2*b*q^5 + 3*a^2*b*q^3 - 2*a^2*c^2*q^8 + 2*a^2*c^2*q^4 + a^2*q^8 - a^2*q^6 - 2*a^2*q^4 + 2*a*b^3*q^10 - 2*a*b^3*q^8 - a*b^3*q^6 + 2*a*b^3*q^4 - a*b^3*q^2 - a*b^2*c*q^11 + 2*a*b^2*c*q^9 - 3*a*b^2*c*q^7 - a*b^2*c*q^5 + 3*a*b^2*c*q^3 - 2*a*b^2*c*q - a*b^2*q^11 + 6*a*b^2*q^9 - 2*a*b^2*q^7 - 4*a*b^2*q^5 + 4*a*b^2*q^3 - a*b^2*q - a*b*c^2*q^4 - a*b*c^2*q^2 - 2*a*b*c*q^10 + 4*a*b*c*q^8 - 2*a*b*c*q^6 - 4*a*b*c*q^4 + 4*a*b*c*q^2 - a*b*q^10 + 6*a*b*q^8 + a*b*q^6 - 4*a*b*q^4 + 2*a*b*q^2 + a*c^3*q^9 - 2*a*c^3*q^7 - 2*a*c^3*q^5 + a*c^3*q^3 + a*c^2*q^9 - 2*a*c^2*q^7 - a*c^2*q^5 + 2*a*c^2*q^3 + a*c*q^7 - a*c*q^5 - 2*a*c*q^3 + 2*a*q^7 + a*q^5 - a*q^3 + b^4*q^10 - b^4*q^8 - b^4*q^6 + b^4*q^4 - b^3*c*q^11 + b^3*c*q^9 - 2*b^3*c*q^7 + 3*b^3*c*q^3 - b^3*c*q - b^3*q^11 + 3*b^3*q^9 - 2*b^3*q^7 - 4*b^3*q^5 + 2*b^3*q^3 - b^2*c^2*q^10 + b^2*c^2*q^8 + b^2*c^2*q^6 + b^2*c^2*q^4 + b^2*c^2*q^2 - b^2*c^2 - 4*b^2*c*q^10 + 2*b^2*c*q^8 - 3*b^2*c*q^6 - 3*b^2*c*q^4 + 5*b^2*c*q^2 - b^2*c - 2*b^2*q^10 + 4*b^2*q^8 - 5*b^2*q^4 + b^2*q^2 + b*c^3*q^9 + b*c^3*q^7 + b*c^3*q^5 - b*c^3*q - b*c^2*q^9 + b*c^2*q^7 + b*c^2*q^5 + b*c^2*q - 3*b*c*q^9 + 2*b*c*q^7 - b*c*q^5 - 4*b*c*q^3 + 2*b*c*q - b*q^9 + 3*b*q^7 + 2*b*q^5 - 2*b*q^3 + c^4*q^8 - c^4*q^4 + 2*c^3*q^8 - c^3*q^4 + c^3*q^2 + c^2*q^8 - c^2*q^4 + c*q^6 - c*q^2 + q^6 + q^4) * H01 + (a^3*b*q^10 - a^3*b*q^6 - a^3*c*q^9 - a^3*c*q^7 + a^3*q^9 + a^3*q^7 - a^2*b^2*q^12 + 2*a^2*b^2*q^10 - 2*a^2*b^2*q^6 + a^2*b^2*q^4 - a^2*b*c*q^11 + a^2*b*c*q^7 - 3*a^2*b*q^11 + 2*a^2*b*q^9 + 2*a^2*b*q^7 - 3*a^2*b*q^5 + 2*a^2*c^2*q^10 + a^2*c^2*q^8 - a^2*c^2*q^6 - a^2*c*q^8 - a^2*c*q^6 - 2*a^2*q^10 - a^2*q^8 + a^2*q^6 - a*b^3*q^12 + a*b^3*q^10 - a*b^3*q^6 + a*b^3*q^4 + 2*a*b^2*c*q^13 - 3*a*b^2*c*q^11 + a*b^2*c*q^9 + 3*a*b^2*c*q^7 - 2*a*b^2*c*q^5 + a*b^2*c*q^3 + a*b^2*q^13 - 4*a*b^2*q^11 + 2*a*b^2*q^9 + 2*a*b^2*q^7 - 4*a*b^2*q^5 + a*b^2*q^3 - a*b*c^2*q^12 + a*b*c^2*q^4 + 4*a*b*c*q^12 - 3*a*b*c*q^10 - 2*a*b*c*q^8 + 4*a*b*c*q^6 - a*b*c*q^4 + 2*a*b*q^12 - 4*a*b*q^10 - a*b*q^8 + 4*a*b*q^6 - a*b*q^4 - a*c^3*q^11 + a*c^3*q^9 + 2*a*c^3*q^7 - 2*a*c^2*q^11 + a*c^2*q^9 + 2*a*c^2*q^7 - a*c^2*q^5 + 2*a*c*q^11 + a*c*q^9 - a*c*q^7 + a*q^11 - a*q^9 - 2*a*q^7 + b^3*c*q^13 - 2*b^3*c*q^11 + 2*b^3*c*q^7 - b^3*c*q^5 - b^3*q^11 + b^3*q^9 + 2*b^3*q^7 - b^2*c^2*q^14 + b^2*c^2*q^12 + b^2*c^2*q^8 + b^2*c^2*q^6 - 2*b^2*c^2*q^4 - b^2*c*q^14 + 5*b^2*c*q^12 - 2*b^2*c*q^10 - b^2*c*q^8 + 4*b^2*c*q^6 - 3*b^2*c*q^4 + b^2*q^12 - 3*b^2*q^10 - 2*b^2*q^8 + 2*b^2*q^6 + b*c^3*q^13 - b*c^3*q^7 - 2*b*c^3*q^5 - b*c^2*q^13 - b*c^2*q^9 - b*c^2*q^7 + b*c^2*q^5 - 2*b*c*q^13 + 4*b*c*q^11 - 2*b*c*q^7 + 4*b*c*q^5 + 2*b*q^11 - b*q^9 - 3*b*q^7 - c^4*q^10 - c^4*q^8 + c^3*q^12 - c^3*q^10 + 2*c^3*q^6 - c^2*q^10 + c^2*q^6 - c*q^12 - c*q^6 + q^10 + q^8) * H10 + (-a^2*b^2*q^7 + a^2*b^2*q^3 - a^2*b*c*q^8 + a^2*b*c*q^6 + 2*a^2*b*c*q^4 - a^2*b*q^6 - a^2*b*q^4 + a^2*c^2*q^7 + a^2*c^2*q^5 - a^2*c*q^7 - a^2*c*q^5 - 2*a*b^3*q^7 + a*b^3*q^5 + 2*a*b^3*q^3 - a*b^3*q - a*b^2*c*q^8 + 2*a*b^2*c*q^6 + 2*a*b^2*c*q^4 - a*b^2*c*q^2 + a*b^2*q^8 - 3*a*b^2*q^6 - a*b^2*q^4 + 3*a*b^2*q^2 + a*b*c^2*q^9 + a*b*c^2*q^3 + a*b*c*q^9 - 3*a*b*c*q^7 + 4*a*b*c*q^3 - 2*a*b*q^5 - 2*a*b*q^3 - a*c^3*q^8 + a*c^3*q^4 + a*c^2*q^6 + a*c^2*q^4 - 2*a*c*q^6 - 2*a*c*q^4 - b^4*q^7 + b^4*q^5 + b^4*q^3 - b^4*q + b^3*c*q^6 + b^3*c*q^4 - b^3*c*q^2 - b^3*c + b^3*q^8 - 2*b^3*q^6 + b^3*q^4 + 3*b^3*q^2 - b^3 + b^2*c^2*q^9 - b^2*c^2*q^3 - 2*b^2*c^2*q + b^2*c*q^9 + 2*b^2*c*q^5 + 3*b^2*c*q^3 + b^2*q^7 - 2*b^2*q^5 - b^2*q^3 + 2*b^2*q - b*c^3*q^6 - 2*b*c^3*q^4 - b*c^3*q^2 + 2*b*c^2*q^8 + 2*b*c^2*q^2 + b*c*q^8 - 2*b*c*q^6 - b*c*q^4 + 2*b*c*q^2 - b*q^4 - b*q^2 - c^4*q^7 - c^4*q^5 - c^3*q^7 + c^3*q^3 - c*q^5 - c*q^3) * H11 + (a^3*b*q^9 - a^3*b*q^7 - a^3*c*q^8 + a^3*q^8 - a^2*b^2*q^11 + 3*a^2*b^2*q^9 - 4*a^2*b^2*q^7 + 2*a^2*b^2*q^5 - a^2*b*c*q^10 + a^2*b*c*q^8 + a^2*b*c*q^6 - 3*a^2*b*q^10 + 5*a^2*b*q^8 - 4*a^2*b*q^6 + 2*a^2*c^2*q^9 - a^2*c^2*q^7 - a^2*c*q^7 - a^2*q^9 + 2*a^2*q^7 - a*b^3*q^11 + 4*a*b^3*q^9 - 5*a*b^3*q^7 + 3*a*b^3*q^5 - a*b^3*q^3 + 2*a*b^2*c*q^12 - 4*a*b^2*c*q^10 + 4*a*b^2*c*q^8 - 4*a*b^2*c*q^6 + a*b^2*c*q^4 + a*b^2*q^12 - 5*a*b^2*q^10 + 11*a*b^2*q^8 - 8*a*b^2*q^6 + 3*a*b^2*q^4 - a*b*c^2*q^11 - 2*a*b*c^2*q^7 + 2*a*b*c^2*q^5 + 4*a*b*c*q^11 - 5*a*b*c*q^9 + 4*a*b*c*q^7 - 2*a*b*c*q^5 + a*b*q^11 - 6*a*b*q^9 + 7*a*b*q^7 - 3*a*b*q^5 - a*c^3*q^10 + 2*a*c^3*q^8 - 2*a*c^2*q^10 + 2*a*c^2*q^8 - 2*a*c^2*q^6 + a*c*q^10 + a*c*q^6 - 2*a*q^8 + a*q^6 + b^4*q^9 - 2*b^4*q^7 + b^4*q^5 + b^3*c*q^12 - 4*b^3*c*q^10 + 4*b^3*c*q^8 - 3*b^3*c*q^6 + 3*b^3*c*q^4 - b^3*c*q^2 - 2*b^3*q^10 + 5*b^3*q^8 - 5*b^3*q^6 + b^3*q^4 - b^2*c^2*q^13 + b^2*c^2*q^11 + 2*b^2*c^2*q^7 - b^2*c^2*q^3 - b^2*c*q^13 + 5*b^2*c*q^11 - 9*b^2*c*q^9 + 7*b^2*c*q^7 - 6*b^2*c*q^5 + 3*b^2*c*q^3 + b^2*q^11 - 4*b^2*q^9 + 7*b^2*q^7 - 3*b^2*q^5 + b*c^3*q^12 + b*c^3*q^8 - 2*b*c^3*q^6 - b*c^2*q^12 + 2*b*c^2*q^4 - b*c*q^12 + 5*b*c*q^10 - 5*b*c*q^8 + 3*b*c*q^6 - 3*b*c*q^4 + b*q^10 - 3*b*q^8 + 3*b*q^6 - c^4*q^9 + c^3*q^11 - c^3*q^9 + 2*c^3*q^7 - 2*c^2*q^9 - c^2*q^5 + c*q^9 + c*q^5 - q^7) * HT + (a^3*b*q^8 - a^3*b*q^6 - a^3*c*q^7 + a^3*q^7 - 2*a^2*b^2*q^10 + 4*a^2*b^2*q^8 - 3*a^2*b^2*q^6 + a^2*b^2*q^4 + a^2*b*c*q^9 + a^2*b*c*q^7 - a^2*b*c*q^5 - 4*a^2*b*q^9 + 5*a^2*b*q^7 - 3*a^2*b*q^5 + a^2*c^2*q^8 - 2*a^2*c^2*q^6 + a^2*c*q^8 - 2*a^2*q^8 + a^2*q^6 + a*b^3*q^12 - 3*a*b^3*q^10 + 5*a*b^3*q^8 - 4*a*b^3*q^6 + a*b^3*q^4 + a*b^2*c*q^11 - 4*a*b^2*c*q^9 + 4*a*b^2*c*q^7 - 4*a*b^2*c*q^5 + 2*a*b^2*c*q^3 + 3*a*b^2*q^11 - 8*a*b^2*q^9 + 11*a*b^2*q^7 - 5*a*b^2*q^5 + a*b^2*q^3 - 2*a*b*c^2*q^10 + 2*a*b*c^2*q^8 + a*b*c^2*q^4 + 2*a*b*c*q^10 - 4*a*b*c*q^8 + 5*a*b*c*q^6 - 4*a*b*c*q^4 + 3*a*b*q^10 - 7*a*b*q^8 + 6*a*b*q^6 - a*b*q^4 + 2*a*c^3*q^7 - a*c^3*q^5 - 2*a*c^2*q^9 + 2*a*c^2*q^7 - 2*a*c^2*q^5 + a*c*q^9 + a*c*q^5 + a*q^9 - 2*a*q^7 - b^4*q^10 + 2*b^4*q^8 - b^4*q^6 - b^3*c*q^13 + 3*b^3*c*q^11 - 3*b^3*c*q^9 + 4*b^3*c*q^7 - 4*b^3*c*q^5 + b^3*c*q^3 + b^3*q^11 - 5*b^3*q^9 + 5*b^3*q^7 - 2*b^3*q^5 + b^2*c^2*q^12 - 2*b^2*c^2*q^8 - b^2*c^2*q^4 + b^2*c^2*q^2 - 3*b^2*c*q^12 + 6*b^2*c*q^10 - 7*b^2*c*q^8 + 9*b^2*c*q^6 - 5*b^2*c*q^4 + b^2*c*q^2 + 3*b^2*q^10 - 7*b^2*q^8 + 4*b^2*q^6 - b^2*q^4 - 2*b*c^3*q^9 + b*c^3*q^7 + b*c^3*q^3 + 2*b*c^2*q^11 - b*c^2*q^3 - 3*b*c*q^11 + 3*b*c*q^9 - 5*b*c*q^7 + 5*b*c*q^5 - b*c*q^3 + 3*b*q^9 - 3*b*q^7 + b*q^5 + c^4*q^6 - 2*c^3*q^8 + c^3*q^6 - c^3*q^4 + c^2*q^10 + 2*c^2*q^6 - c*q^10 - c*q^6 + q^8) * HS
  have hld : l * (-a^2*q^3 + a*b*q^5 - a*b*q^3 + a*b*q + a*c*q^4 - a*c*q^2 + a*q^4 - a*q^2 - b^2*q^3 - b*c*q^6 + b*c*q^4 - b*c*q^2 + b*c + b*q^4 - b*q^2 + c^2*q^3 - c*q^5 + c*q^3 - c*q + q^3) = 0 := (mul_eq_zero.mp hDld).resolve_left hD
  have hdd : q ^ 0 * ((-a^2*q^3 + a*b*q^5 - a*b*q^3 + a*b*q + a*c*q^4 - a*c*q^2 + a*q^4 - a*q^2 - b^2*q^3 - b*c*q^6 + b*c*q^4 - b*c*q^2 + b*c + b*q^4 - b*q^2 + c^2*q^3 - c*q^5 + c*q^3 - c*q + q^3) * (-a'^2*q^3 + a'*b'*q^5 - a'*b'*q^3 + a'*b'*q + a'*c'*q^4 - a'*c'*q^2 + a'*q^4 - a'*q^2 - b'^2*q^3 - b'*c'*q^6 + b'*c'*q^4 - b'*c'*q^2 + b'*c' + b'*q^4 - b'*q^2 + c'^2*q^3 - c'*q^5 + c'*q^3 - c'*q + q^3) + q ^ 6 * l ^ 2) = 0 := by
    linear_combination (a*a'*q^2 + a*c'*q^5 - a*c'*q^3 + a*c'*q - a*q^3 - a'*b*q^4 - a'*c*q^3 + a'*c*q - a'*q^3 + b*b'*q^6 + b*c'*q^5 - b*c'*q^3 + b*q^5 - b'*c*q^3 + b'*q^5 - c*c'*q^6 + c*c'*q^4 - 2*c*c'*q^2 + c*c' + c*q^4 - c*q^2 + c'*q^4 - c'*q^2 + q^4) * H00 + (-a*a'*q^5 + a*a'*q^3 + a*b'*q^3 + a*c'*q^6 - a*c'*q^4 - a*q^4 - a'*b*q^5 + a'*c*q^6 - a'*c*q^4 + a'*c*q^2 - a'*q^4 + b*c'*q^6 - b'*c*q^4 - c*c'*q^7 + c*c'*q^5 - c*c'*q^3 + c*q^5 + c'*q^5) * H01 + (l*q^4) * H10 + (0) * H11
  have hdd' : (-a^2*q^3 + a*b*q^5 - a*b*q^3 + a*b*q + a*c*q^4 - a*c*q^2 + a*q^4 - a*q^2 - b^2*q^3 - b*c*q^6 + b*c*q^4 - b*c*q^2 + b*c + b*q^4 - b*q^2 + c^2*q^3 - c*q^5 + c*q^3 - c*q + q^3) * (-a'^2*q^3 + a'*b'*q^5 - a'*b'*q^3 + a'*b'*q + a'*c'*q^4 - a'*c'*q^2 + a'*q^4 - a'*q^2 - b'^2*q^3 - b'*c'*q^6 + b'*c'*q^4 - b'*c'*q^2 + b'*c' + b'*q^4 - b'*q^2 + c'^2*q^3 - c'*q^5 + c'*q^3 - c'*q + q^3) + q ^ 6 * l ^ 2 = 0 :=
    (mul_eq_zero.mp hdd).resolve_left (pow_ne_zero _ hq)
  have hl3 : q ^ 6 * l ^ 3 = 0 := by
    linear_combination l * hdd' - (-a'^2*q^3 + a'*b'*q^5 - a'*b'*q^3 + a'*b'*q + a'*c'*q^4 - a'*c'*q^2 + a'*q^4 - a'*q^2 - b'^2*q^3 - b'*c'*q^6 + b'*c'*q^4 - b'*c'*q^2 + b'*c' + b'*q^4 - b'*q^2 + c'^2*q^3 - c'*q^5 + c'*q^3 - c'*q + q^3) * hld
  have hl3' : l ^ 3 = 0 := (mul_eq_zero.mp hl3).resolve_left (pow_ne_zero _ hq)
  exact pow_eq_zero_iff (by norm_num) |>.mp hl3'

end QOU.MassTheory.ElectronNotTwoPhoton
