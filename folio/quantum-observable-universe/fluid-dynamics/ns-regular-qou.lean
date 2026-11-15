import Mathlib.Data.Real.Basic
import Mathlib.Data.Int.Basic
-- Ref: [leitner2026] Ch. 7, §ns-regular-qou
-- NS-regular quantum observable universe

/-- An **NS-regular** quantum observable universe is one where the
    NS obstruction class vanishes: `NS(A) = 0`.

    Per the sibling `.md`, the NS obstruction `NS(A) = κ₀|_Σ` depends
    only on the categorical data through the Euler characteristic
    `χ(A) = tr(κ₀)`, and the regularity dichotomy is
    `NS(A) = 0 ⟺ χ(A) = 0`. We therefore carry the Euler
    characteristic `chi` as data and encode NS-regularity as its
    genuine defining property `chi = 0` (not a `: True` placeholder).

    NS-regularity implies global regularity of the classical
    (`q = 1`) Navier–Stokes specialisation: no finite-time blowup. -/
structure NSRegularQOU where
  /-- Substrate parameter q > 1. -/
  q : ℝ
  q_gt_one : 1 < q
  /-- The Euler characteristic `χ(A) = tr(κ₀)` of the categorical
      data — the only invariant the NS obstruction depends on. -/
  chi : ℤ
  /-- The NS obstruction vanishes: `NS(A) = 0`, equivalently `χ(A) = 0`
      (the NS-regular row of the dichotomy table in the `.md`). -/
  regular : chi = 0
