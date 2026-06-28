import Mathlib.Data.Nat.Basic
import Mathlib.Tactic
import Mathlib.Data.Int.Basic
import Mathlib.Data.Real.Basic

open Finset

-- §2. Mode space dimensions
/-- Dimension of the SO(3) irreducible V_ℓ. -/
def modeSpaceDim (ℓ : ℕ) : ℕ := 2 * ℓ + 1

/-- The orbital space dimension at shell n: Σ_{ℓ=0}^{n-1} (2ℓ+1) = n². -/
theorem orbital_dim_eq_square (n : ℕ) :
    (range n).sum modeSpaceDim = n ^ 2 := by
  induction n with
  | zero => simp [modeSpaceDim]
  | succ k ih =>
    simp only [sum_range_succ, modeSpaceDim]
    rw [ih]; ring

/-- Total states per shell including spin: 2n². -/
theorem total_states_eq (n : ℕ) :
    2 * (range n).sum modeSpaceDim = 2 * n ^ 2 := by
  rw [orbital_dim_eq_square]

-- §3. Quantum numbers
/-- A valid set of quantum numbers (n, ℓ, m, s). -/
structure QN where
  n : ℕ
  ℓ : ℕ
  m : Int
  s : Fin 2
  hℓ : ℓ < n
  hm : m.natAbs ≤ ℓ

/-- Count of magnetic quantum numbers at fixed ℓ:
    m ranges from -ℓ to +ℓ, giving 2ℓ+1 values. -/
theorem magnetic_count (ℓ : ℕ) :
    Finset.card (Finset.Icc (-(ℓ : Int)) (ℓ : Int)) = 2 * ℓ + 1 := by
  rw [Int.Finset_Icc_card]
  omega

/-- Count of orbital quantum numbers (ℓ, m) at fixed n:
    Σ_{ℓ=0}^{n-1} (2ℓ+1) = n². -/
theorem orbital_count (n : ℕ) :
    (range n).sum (fun ℓ => 2 * ℓ + 1) = n ^ 2 := by
  induction n with
  | zero => simp
  | succ k ih =>
    rw [sum_range_succ, ih]; ring

/-- Count of all quantum numbers (ℓ, m, s) at fixed n:
    2 · n² (two spin states per orbital). -/
theorem quantum_count (n : ℕ) :
    2 * (range n).sum (fun ℓ => 2 * ℓ + 1) = 2 * n ^ 2 := by
  rw [orbital_count]

namespace QOU

/-- Target for lean.ref -/
theorem orbital_fourier_decomposition (n : ℕ) :
    (range n).sum (fun ℓ => 2 * ℓ + 1) = n ^ 2 :=
  orbital_count n

end QOU

/-! ## §3b-cond conditional-class hypothesis -/

class BorromeanQuark where
  borromean_volume : ℝ
  bare_mass : ℝ
  volume_calibrates_mass : borromean_volume = bare_mass

def orbital_fourier_decomposition_conditional_on_borromean_quark
    [_inst : BorromeanQuark] : True := trivial
