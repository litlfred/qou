import Mathlib.Data.Complex.Basic
import Mathlib.GroupTheory.Perm.Fin
import Mathlib.Data.Fintype.Card
import Mathlib.Tactic.FinCases

open Equiv

namespace QOU.BraidsKnots

abbrev S3 := Equiv.Perm (Fin 3)

theorem galois_group_order : Fintype.card S3 = 6 := by
  change Nat.factorial 3 = 6; rfl

def cyclic_perm : S3 := swap 0 1 * swap 1 2

noncomputable def resolvent (zeta : ℂ) (i : Fin 3) : ℂ :=
  if i = 0 then 1
  else if i = 1 then zeta⁻¹
  else (zeta⁻¹)^2

theorem resolvent_agreement (zeta : ℂ) (hzeta : zeta ^ 3 = 1) :
    resolvent zeta ∘ cyclic_perm = zeta⁻¹ • resolvent zeta := by
  ext i
  fin_cases i
  · change resolvent zeta 1 = zeta⁻¹ * resolvent zeta 0
    dsimp [resolvent]
    ring
  · change resolvent zeta 2 = zeta⁻¹ * resolvent zeta 1
    dsimp [resolvent]
    ring
  · change resolvent zeta 0 = zeta⁻¹ * resolvent zeta 2
    dsimp [resolvent]
    have h1 : zeta⁻¹ * (zeta⁻¹)^2 = 1 := by
      calc zeta⁻¹ * (zeta⁻¹)^2 = (zeta⁻¹)^3 := by ring
        _ = (zeta^3)⁻¹ := by ring
        _ = 1⁻¹ := by rw [hzeta]
        _ = 1 := inv_one
    exact h1.symm

