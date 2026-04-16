-- Ref: [manuscript] Ch. 7, §ns-regular-qou
-- NS-regular quantum observable universe

/-- An **NS-regular** quantum observable universe is one where the
    NS obstruction class vanishes: NS(A) = 0.

    This implies global regularity of the q-Navier-Stokes equation
    and hence no finite-time blowup. -/
structure NSRegularQOU where
  /-- Substrate parameter q > 1. -/
  q : ℝ
  q_gt_one : 1 < q
  /-- The obstruction vanishes. -/
  regular : True  -- placeholder: actual statement requires H³_loc
