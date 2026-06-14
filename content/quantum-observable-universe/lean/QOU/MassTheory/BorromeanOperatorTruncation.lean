import Mathlib.Tactic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Field.Basic

namespace QOU.MassTheory

/-- 
  The scalar algebraic identities proving the Borromean rings operator trace
  truncates EXACTLY at N=2 in the bar-even sector.
-/

section BorromeanTrace

variable {R : Type*} [CommRing R] (q : R)
-- Assume q is invertible, so we can work with q and q_inv
variable (q_inv : R)
variable (hq : q * q_inv = 1)

-- Define h = q - 1/q
def h : R := q - q_inv

-- The exact Markov trace M_net for the Borromean rings in the bar-even sector.
-- From exact extraction, M_net = -h^4.
-- We prove that the trace expression simplifies to -h^4.

-- The trace of (s_0 s_1^{-1})^3 in the (2,1) Wedderburn block is:
def chi_21 : R :=
  4 - q^6 + 3*q^4 - 3*q^2 - 3*q_inv^2 + 3*q_inv^4 - q_inv^6

-- The Wenzl weight y_{(2,1)} is q^2 / (q^4 + q^2 + 1).
-- We work with the numerator and denominator to avoid division in generic rings.
def y_21_num : R := q^2
def y_21_den : R := q^4 + q^2 + 1

-- The unnormalized Markov trace of net(T_w) is y_21_num * (chi_21 - 2).
-- We prove that this equals - y_21_den * h^4.
theorem borromean_markov_trace_truncation :
    y_21_num q * (chi_21 q q_inv - 2) = - (y_21_den q) * (h q q_inv)^4 := by
  dsimp [chi_21, y_21_num, y_21_den, h]
  -- We just need to show the polynomial identity in q, q_inv given q * q_inv = 1.
  -- We can do this by substituting q_inv = 1/q or multiplying by q^6.
  -- Actually, nlinarith or ring might struggle with the relation q * q_inv = 1 directly
  -- unless we use linear_combination.
  have h_inv : q * q_inv - 1 = 0 := by
    calc q * q_inv - 1 = 1 - 1 := by rw [hq]
      _ = 0 := by ring
  linear_combination (
    -4*q^6 + 6*q^5*q_inv - 4*q^4*q_inv^2 + 2*q^4 + q^3*q_inv^3 + 2*q^3*q_inv - 3*q^2*q_inv^2 - 2*q^2 - q*q_inv^5 + 4*q*q_inv^3 - q_inv^4
  ) * h_inv

end BorromeanTrace

end QOU.MassTheory
