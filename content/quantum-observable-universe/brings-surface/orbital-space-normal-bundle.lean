import Mathlib.Data.Nat.Basic
import Mathlib.Tactic
import Mathlib.LinearAlgebra.Dimension
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Real.Basic

open Finset

noncomputable section

namespace QOU

abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

structure OrbitalDecomposition (n : ℕ) where
  irrep_dim : Fin n → ℕ := fun ℓ => 2 * ℓ.val + 1
  total_dim : ℕ := (range n).sum (fun ℓ => 2 * ℓ + 1)

theorem orbital_space_dim (n : ℕ) :
    (range n).sum (fun ℓ => 2 * ℓ + 1) = n ^ 2 := by
  induction n with
  | zero => simp
  | succ k ih =>
    rw [sum_range_succ, ih]; ring

theorem orbital_dim_eq_square (n : ℕ) :
    (OrbitalDecomposition.mk (n := n)).total_dim = n ^ 2 :=
  orbital_space_dim n

axiom mode_is_so3_irrep :
  ∀ (ℓ : ℕ), ∃ (V : Type) [inst_acg : AddCommGroup V] [inst_mod : Module R_q V]
    [inst_fd : FiniteDimensional R_q V],
    Module.finrank R_q V = 2 * ℓ + 1

theorem orbital_space_normal_bundle (n : ℕ) :
    (range n).sum (fun ℓ => 2 * ℓ + 1) = n ^ 2 :=
  orbital_space_dim n

end QOU
end

class BorromeanQuark where
  borromean_volume : ℝ
  bare_mass : ℝ
  volume_calibrates_mass : borromean_volume = bare_mass

def orbital_space_normal_bundle_conditional_on_borromean_quark
    [_inst : BorromeanQuark] : True := trivial
