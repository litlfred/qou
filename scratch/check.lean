import Mathlib.Tactic
import QOU.QBeta.MarkovZToCkMapping
open QOU.BraidKnot QOU.QBeta
theorem ck_is_constant_on_q 
    (ladder : QBetaPrecisionLadderCoefficients)
    [h : ZToCkMappingClass ladder] 
    (q1 q2 : ℝ) (hq1 : 0 < q1) (hq2 : 0 < q2) (k : ℕ) : 
    ladder.c_k_at_q k q1 = ladder.c_k_at_q k q2 := by
  have h1 := h.f_map_bridges_to_ck q1 hq1
  have h2 := h.f_map_bridges_to_ck q2 hq2
  rw [Function.funext_iff] at h1 h2
  rw [←h1 k, ←h2 k]
