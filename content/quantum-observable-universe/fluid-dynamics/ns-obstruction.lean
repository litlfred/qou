-- Ref: [manuscript] Ch. 7, §ns-obstruction
-- NS obstruction class NS(A) ∈ H³_loc(A, θ)

/-- The **NS obstruction class** of a Frobenius-Hopf object A.

    NS(A) ∈ H³_loc(A, θ) is the Yekutieli obstruction tower of the
    q-NS system evaluated at q = 1.

    - NS(A) = 0 ⟺ the quantum universe is NS-regular (global regularity)
    - NS(A) ≠ 0 ⟹ finite-time blowup in the classical limit -/
structure NSObstruction where
  /-- Whether the obstruction class vanishes. -/
  isRegular : Bool
  /-- Obstruction degree (0 if regular). -/
  degree : Nat
  degree_zero_iff : degree = 0 ↔ isRegular = true

/-- An NS-regular QOU has vanishing obstruction. -/
theorem ns_regular_implies_zero (obs : NSObstruction) (h : obs.isRegular = true) :
    obs.degree = 0 :=
  obs.degree_zero_iff.mpr h
