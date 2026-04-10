/-!
# Atomic Braid Mass Formula

Formalizes the atomic braid H_{A+Z}(q) and the three-invariant
Wedderburn mass formula.

-- Ref: [manuscript] Chapter 11 §8, Atomic braid and Wedderburn mass formula
-/

import Mathlib.Algebra.Group.Basic
import Mathlib.Data.Real.Basic

namespace QOU.AtomicBraid

/-- Crossing type in the atomic braid. -/
inductive CrossingType
  | pp   -- proton-proton: σ (strong repulsion)
  | nn   -- neutron-neutron: σ⁻¹ (strong inverse)
  | pn   -- proton-neutron: ½(σ+σ⁻¹) (strong mixed)
  | pe   -- proton-electron: σ⁻¹ (EM attraction)
  | ne   -- neutron-electron: identity (no interaction)
  | ee   -- electron-electron: σ (EM repulsion)

/-- Strand type in the atomic braid. -/
inductive StrandType
  | proton
  | neutron
  | electron

/-- An atomic braid ordering is a list of strand types. -/
def AtomicOrdering := List StrandType

/-- The crossing type between two strand types. -/
def crossingType : StrandType → StrandType → CrossingType
  | .proton,   .proton   => .pp
  | .neutron,  .neutron  => .nn
  | .proton,   .neutron  => .pn
  | .neutron,  .proton   => .pn
  | .proton,   .electron => .pe
  | .electron, .proton   => .pe
  | .neutron,  .electron => .ne
  | .electron, .neutron  => .ne
  | .electron, .electron => .ee

/-- A neutral atom has Z protons, N neutrons, Z electrons. -/
structure NeutralAtom where
  Z : ℕ
  N : ℕ
  ordering : AtomicOrdering
  proton_count : ordering.count .proton = Z
  neutron_count : ordering.count .neutron = N
  electron_count : ordering.count .electron = Z

/-- The three Wedderburn invariants of a transfer matrix chain. -/
structure WedderburnInvariants where
  Φ₁ : ℝ  -- Σ ln|V̂_i| (standard trace)
  Φ₂ : ℝ  -- Σ ln|det(M_i)| (sym × alt determinant)
  Φ₃ : ℝ  -- Σ ln|sym_i/alt_i| (chirality)

/-- The Wedderburn mass formula. The three invariants are complete:
    no fourth independent invariant exists for H_n(q). -/
-- Ref: [manuscript] Theorem thm:wedderburn-mass-formula
class WedderburnMassFormula (q : ℝ) (m_e : ℝ) where
  /-- Proton mass from Picard-Lefschetz thimble. -/
  m_p : ℝ
  /-- Neutron mass from quark crossing change. -/
  m_n : ℝ
  /-- Binding scale α = m_e × Vol(B₃). -/
  α : ℝ
  /-- Hecke parameter. -/
  HA : ℝ := q - q⁻¹
  /-- Quantum 3-integer. -/
  q3 : ℝ := (q^3 - q⁻¹^3) / (q - q⁻¹)
  /-- Degree-2 weight. -/
  β₂ : ℝ := -2 * q3
  /-- Degree-3 weight. -/
  β₃ : ℝ := HA^2
  /-- The mass formula. -/
  mass (atom : NeutralAtom) (inv : WedderburnInvariants) : ℝ :=
    atom.Z * m_p + atom.N * m_n + atom.Z * m_e +
    α * (inv.Φ₁ + β₂ * inv.Φ₂ + β₃ * inv.Φ₃)

end QOU.AtomicBraid
