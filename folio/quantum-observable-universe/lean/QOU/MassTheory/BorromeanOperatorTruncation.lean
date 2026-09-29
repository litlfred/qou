import Mathlib.Tactic
import Mathlib.Algebra.Ring.Basic

namespace QOU.MassTheory

section BorromeanTrace

variable {R : Type*} [CommRing R] (q : R)
variable (q_inv : R)

def h : R := q - q_inv

def chi_21 : R :=
  4 - q^6 + 3*q^4 - 3*q^2 - 3*q_inv^2 + 3*q_inv^4 - q_inv^6

def y_21_num : R := q^2
def y_21_den : R := q^4 + q^2 + 1

theorem borromean_markov_trace_truncation (hq : q * q_inv = 1) :
    y_21_num q * (chi_21 q q_inv - 2) = - (y_21_den q) * (h q q_inv)^4 := by
  dsimp [chi_21, y_21_num, y_21_den, h]
  have h_inv : q * q_inv - 1 = 0 := by
    calc q * q_inv - 1 = 1 - 1 := by rw [hq]
      _ = 0 := by ring
  calc
    q^2 * (4 - q^6 + 3*q^4 - 3*q^2 - 3*q_inv^2 + 3*q_inv^4 - q_inv^6 - 2)
      = -q^8 + 3*q^6 - 3*q^4 - q^2*q_inv^6 + 3*q^2*q_inv^4 - 3*q^2*q_inv^2 + 2*q^2 := by ring
    _ = -q^8 + 4*q^7*q_inv - 6*q^6*q_inv^2 - q^6 + 4*q^5*q_inv^3 + 4*q^5*q_inv - q^4*q_inv^4 - 6*q^4*q_inv^2 - q^4 + 4*q^3*q_inv^3 + 4*q^3*q_inv - q^2*q_inv^4 - 6*q^2*q_inv^2 + 4*q*q_inv^3 - q_inv^4 + (-4*q^6 + 6*q^5*q_inv - 4*q^4*q_inv^2 + 2*q^4 + q^3*q_inv^3 + 2*q^3*q_inv - 3*q^2*q_inv^2 - 2*q^2 - q*q_inv^5 + 4*q*q_inv^3 - q_inv^4) * (q * q_inv - 1) := by ring
    _ = -q^8 + 4*q^7*q_inv - 6*q^6*q_inv^2 - q^6 + 4*q^5*q_inv^3 + 4*q^5*q_inv - q^4*q_inv^4 - 6*q^4*q_inv^2 - q^4 + 4*q^3*q_inv^3 + 4*q^3*q_inv - q^2*q_inv^4 - 6*q^2*q_inv^2 + 4*q*q_inv^3 - q_inv^4 + (-4*q^6 + 6*q^5*q_inv - 4*q^4*q_inv^2 + 2*q^4 + q^3*q_inv^3 + 2*q^3*q_inv - 3*q^2*q_inv^2 - 2*q^2 - q*q_inv^5 + 4*q*q_inv^3 - q_inv^4) * 0 := by rw [h_inv]
    _ = -(q^4 + q^2 + 1) * (q - q_inv)^4 := by ring

end BorromeanTrace
end QOU.MassTheory
