import QOU.EightfoldWay.NeutralLeptonFixesCharges
import QOU.StandardModel.ChiralityIndependentOfCrossing

/-!
# QOU.EightfoldWay.StrandSlotSeparatesGen1 — the strand slot is V9's missing label

`ChiralityIndependentOfCrossing.lean` (V9, bean `qou-wqto`) proves that the eight
first-generation quark states need three bits, that the braid element supplies one
(the crossing sign), and that it cannot separate the sector. It leaves one datum
open: a further label, the colour-tube environment, which it names but does not
formalise.

This module supplies that label from the strand picture of
`prop:neutral-lepton-fixes-charges` and `prop:fermi-pair-wedge`. A quark sits in one
of four **slots**: a single colour strand (in `5̄`), or a strand pair of type
colour∧3, colour∧4 or colour∧colour (in `Λ²5`). Each state also carries a **dual
flag**: whether it sits in `5̄ ⊕ Λ²5` or in the conjugate `5 ⊕ Λ²5̄`.

* `slot_dual_injective` — slot and dual flag together separate all eight states.
* `slot_alone_insufficient` — the slot alone does not: `u_L` and `ū_L` share it.
* `dual_eq_helicity` — the dual flag is the helicity: it is set exactly when the
  chirality bit and the particle bit disagree.
* `charge_from_slot` — the charge read off the slot at `α = 1/6`, sign-flipped by
  the dual flag, is the charge of each state (`+2/3` up, `-1/3` down, negated for
  antiquarks).
* `charge_colour_independent` — that charge does not depend on which colour strand.

## Inputs

1. The assignment of the eight states to slots (`slot`, `dual`) is the
   Georgi–Glashow embedding \cite{baez-huerta2010}, stated as a definition. It is not
   derived. The SM labels enter only as the enumerated type of V9.
2. Everything upstream of the charge values: the matter content and one neutral
   lepton (`prop:neutral-lepton-fixes-charges`), and Fermi exchange
   (`prop:fermi-pair-wedge`).

What this does settle: the label V9 left open can be taken to be the strand slot,
which is finite data with no new carrier, and with it no further bit is needed. The
crossing sign is not used.

Base ring `ℚ`; no empirical input.
-/

namespace QOU.EightfoldWay.StrandSlotSeparatesGen1

open QOU.StandardModel.Chirality QOU.StandardModel.Chirality.Gen1Quark
open QOU.EightfoldWay.NeutralLeptonFixesCharges

/-- The four quark slots on `5 = C ⊕ V`. -/
inductive Slot
  | colour   -- one colour strand, in `5̄`
  | colIso3  -- colour ∧ e₃, in `Λ²5`
  | colIso4  -- colour ∧ e₄, in `Λ²5`
  | colCol   -- colour ∧ colour, in `Λ²5`
  deriving DecidableEq

open Slot

/-- The Georgi–Glashow slot of each first-generation quark state (an input). -/
def slot : Gen1Quark → Slot
  | uL | uLbar => colIso3
  | dL | dLbar => colIso4
  | uR | uRbar => colCol
  | dR | dRbar => colour

/-- Dual flag: `true` when the state sits in the conjugate `5 ⊕ Λ²5̄`. -/
def dual : Gen1Quark → Bool
  | uL | dL | uRbar | dRbar => false
  | uLbar | dLbar | uR | dR => true

theorem slot_dual_injective :
    Function.Injective (fun x : Gen1Quark => (slot x, dual x)) := by
  intro a b h
  cases a <;> cases b <;> simp_all [slot, dual]

theorem slot_alone_insufficient : ¬ Function.Injective slot := by
  intro h
  have : uL = uLbar := h (show slot uL = slot uLbar from rfl)
  exact absurd this (by decide)

/-- The dual flag is the helicity: set exactly when chirality and particle bits differ. -/
theorem dual_eq_helicity (x : Gen1Quark) : dual x = !(chirality x == isParticle x) := by
  cases x <;> rfl

/-- Charge of a slot in `5̄ ⊕ Λ²5` at `α = 1/6`, read at colour strand `0`. -/
def slotCharge : Slot → ℚ
  | colour => qWeight5bar (1 / 6) 0
  | colIso3 => qWeight10 (1 / 6) 0 3
  | colIso4 => qWeight10 (1 / 6) 0 4
  | colCol => qWeight10 (1 / 6) 0 1

/-- The Standard Model charge of each state (the labels to be reproduced). -/
def smCharge : Gen1Quark → ℚ
  | uL | uR => 2 / 3
  | dL | dR => -(1 / 3)
  | uLbar | uRbar => -(2 / 3)
  | dLbar | dRbar => 1 / 3

theorem slotCharge_values :
    slotCharge colour = 1 / 3 ∧ slotCharge colIso3 = 2 / 3 ∧
      slotCharge colIso4 = -(1 / 3) ∧ slotCharge colCol = -(2 / 3) := by
  obtain ⟨hc, -, -, hcc, h3, h4, -⟩ := charges_at_one_sixth (K := ℚ)
  exact ⟨hc 0 (by decide), h3 0 (by decide), h4 0 (by decide),
    hcc 0 1 (by decide) (by decide)⟩

/-- **The slot charge, sign-flipped by the dual flag, is each state's charge.** -/
theorem charge_from_slot (x : Gen1Quark) :
    (if dual x then -1 else 1) * slotCharge (slot x) = smCharge x := by
  obtain ⟨h1, h2, h3, h4⟩ := slotCharge_values
  cases x <;> simp [dual, slot, smCharge, h1, h2, h3, h4]

/-- The slot charge does not depend on the colour strand chosen. -/
theorem charge_colour_independent (i j : Fin 5) (hi : i.1 < 3) (hj : j.1 < 3) :
    qWeight5bar (1 / 6 : ℚ) i = slotCharge colour ∧
      qWeight10 (1 / 6 : ℚ) i 3 = slotCharge colIso3 ∧
      qWeight10 (1 / 6 : ℚ) i 4 = slotCharge colIso4 ∧
      qWeight10 (1 / 6 : ℚ) i j = slotCharge colCol := by
  obtain ⟨h1, h2, h3, h4⟩ := slotCharge_values
  obtain ⟨hc, -, -, hcc, k3, k4, -⟩ := charges_at_one_sixth (K := ℚ)
  rw [h1, h2, h3, h4]
  exact ⟨hc i hi, k3 i hi, k4 i hi, hcc i j hi hj⟩

end QOU.EightfoldWay.StrandSlotSeparatesGen1
