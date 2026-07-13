import QOU.Archimedean.HeckeH3
import QOU.Interactions.BorromeanUnique
import QOU.Interactions.BetaReceptivity

open QOU.Interactions QOU.Archimedean Matrix

theorem test1 : q_from_t * q_inv_from_t = (1 : R_t) := by
  exact q_from_t_mul_q_inv_from_t

theorem test2 : (-q_inv_from_t) * (-q_from_t) = (1 : R_t) := by
  calc
    (-q_inv_from_t) * (-q_from_t) = q_inv_from_t * q_from_t := by ring
    _ = q_from_t * q_inv_from_t := by ring
    _ = 1 := q_from_t_mul_q_inv_from_t

theorem test3 : (q_from_t * q_inv_from_t) ^ 3 = (1 : R_t) := by
  rw [q_from_t_mul_q_inv_from_t]
  ring

theorem test4 : ((-q_inv_from_t) * (-q_from_t)) ^ 3 = (1 : R_t) := by
  have h : (-q_inv_from_t) * (-q_from_t) = (1 : R_t) := by
    calc
      (-q_inv_from_t) * (-q_from_t) = q_inv_from_t * q_from_t := by ring
      _ = q_from_t * q_inv_from_t := by ring
      _ = 1 := q_from_t_mul_q_inv_from_t
  rw [h]
  ring
