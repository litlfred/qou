/-
Copyright (c) 2026 QOU contributors. All rights reserved.

# Information content of the hypercharge battery

`content/quantum-observable-universe/eightfold-way/eightfold-open-problems.md`
item 2 records hypercharge `Y` as **open**: the writhe map is falsified as a
`Y` assignment (proton and neutron share `Y = +1` while their writhes
differ), so a second crossing invariant independent of the writhe is
required.  `flavor-charge-assignments.md` states two batteries a candidate
must pass:

* **B1** Gell-Mann--Nishijima `Q = I₃ + Y/2` on the nucleon doublet;
* **B2** the first-generation spectrum, `Y` of `(u, d, e⁻, νₑ)` equal to
  `{+1/3, +1/3, -1, -1}` left-handed and `{+4/3, -2/3, -2, 0}` right-handed.

This file measures what those batteries *constrain*.  It proves nothing
about any candidate invariant and derives no hypercharge; it is the
forward, formalize-first prune of AGENTS.md §"Formalize-first probe
discipline" -- narrow the target before searching for an object to hit it.

## Results

* `hypercharge_determined_of_isospin_zero` -- on a weak singlet (`I₃ = 0`)
  the GMN relation pins `Y` **uniquely** from `Q`.  Hence the right-handed
  half of B2 is *entailed* by the framework's already-derived `Q`: it can
  separate no two candidates, exactly the vacuity established for
  Gell-Mann--Okubo in `GellMannOkuboIdentity.lean`.
* `lh_hypercharge_eq_baryon_sub_lepton` -- the left-handed half of B2 is
  termwise `Y = B - L`.
* `nucleon_hypercharge_eq_baryon_number` -- on the nucleon doublet `L = 0`,
  so B1 is the `L = 0` restriction `Y = B`.

**Honest scope (AGENTS.md anti-laundering).** `Y = B - L` on the left-handed
sector is a *standard Standard-Model identity*, not a QOU derivation, and
nothing here derives `B`, `L`, or `Y` from the substrate.  The content is
the **reduction**: B2 imposes one independent condition, not two, and B1 is
its `L = 0` restriction.  A candidate supplying `B` alone therefore closes
B1 and the quark rows of B2-LH while leaving the lepton-number half open.
This is a scope-(a) statement about the battery, not a scope-(b) exclusion
of any invariant.

Base ring is a generic `Field K` (§7c): no ordering, no `Real`, no
archimedean construct is used.
-/

import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace QOU.StandardModel

/-- The Gell-Mann--Nishijima relation `Q = I₃ + Y/2`. -/
def GellMannNishijima {K : Type*} [Field K] (Q I₃ Y : K) : Prop :=
  Q = I₃ + Y / 2

/-- **The right-handed battery is an identity, not a test.**

On a weak singlet (`I₃ = 0`) the Gell-Mann--Nishijima relation determines
`Y` uniquely from `Q`.  So two candidate hypercharge assignments that both
satisfy GMN against the *same* derived charge agree on every right-handed
row: the right-handed half of B2 has no discriminating power.

Characteristic zero is *required*, not decorative: in characteristic `2`
the element `2` is `0`, division by it is junk, and the statement is false. -/
theorem hypercharge_determined_of_isospin_zero {K : Type*} [Field K]
    [CharZero K] (Q Y₁ Y₂ : K)
    (h₁ : GellMannNishijima Q 0 Y₁)
    (h₂ : GellMannNishijima Q 0 Y₂) :
    Y₁ = Y₂ := by
  unfold GellMannNishijima at h₁ h₂
  rw [zero_add] at h₁ h₂
  have h : Y₁ / 2 = Y₂ / 2 := by rw [← h₁, ← h₂]
  have h2 : (2 : K) ≠ 0 := by norm_num
  field_simp at h
  exact h

/-- The right-handed hypercharge forced by GMN at `I₃ = 0` is `2Q`. -/
theorem rh_hypercharge_eq_two_mul_charge {K : Type*} [Field K] [CharZero K]
    (Q Y : K) (h : GellMannNishijima Q 0 Y) :
    Y = 2 * Q := by
  unfold GellMannNishijima at h
  rw [zero_add] at h
  subst h
  have h2 : (2 : K) ≠ 0 := by norm_num
  field_simp

/-- First-generation quantum numbers: electric charge, left-handed weak
isospin, baryon number, lepton number. -/
structure FermionCharges (K : Type*) [Field K] where
  Q : K
  I₃ : K
  B : K
  L : K

namespace FermionCharges

variable {K : Type*} [Field K]

/-- Hypercharge forced by GMN: `Y = 2(Q - I₃)`. -/
def hypercharge (f : FermionCharges K) : K := 2 * (f.Q - f.I₃)

/-- The anomaly-free combination `B - L`. -/
def baryonMinusLepton (f : FermionCharges K) : K := f.B - f.L

end FermionCharges

open FermionCharges

/-- Left-handed up quark: `Q = 2/3`, `I₃ = 1/2`, `B = 1/3`, `L = 0`. -/
def upL (K : Type*) [Field K] : FermionCharges K :=
  ⟨2 / 3, 1 / 2, 1 / 3, 0⟩

/-- Left-handed down quark: `Q = -1/3`, `I₃ = -1/2`, `B = 1/3`, `L = 0`. -/
def downL (K : Type*) [Field K] : FermionCharges K :=
  ⟨-(1 / 3), -(1 / 2), 1 / 3, 0⟩

/-- Left-handed electron neutrino: `Q = 0`, `I₃ = 1/2`, `B = 0`, `L = 1`. -/
def nuEL (K : Type*) [Field K] : FermionCharges K :=
  ⟨0, 1 / 2, 0, 1⟩

/-- Left-handed electron: `Q = -1`, `I₃ = -1/2`, `B = 0`, `L = 1`. -/
def electronL (K : Type*) [Field K] : FermionCharges K :=
  ⟨-1, -(1 / 2), 0, 1⟩

/-- **The left-handed battery is exactly `B - L`.**

For each of the four first-generation left-handed fermions, the hypercharge
forced by Gell-Mann--Nishijima equals baryon number minus lepton number.
Stated over a generic field of characteristic zero (needed only so that
`1/2`, `1/3` are the intended elements). -/
theorem lh_hypercharge_eq_baryon_sub_lepton {K : Type*} [Field K]
    [CharZero K] :
    (upL K).hypercharge = (upL K).baryonMinusLepton ∧
    (downL K).hypercharge = (downL K).baryonMinusLepton ∧
    (nuEL K).hypercharge = (nuEL K).baryonMinusLepton ∧
    (electronL K).hypercharge = (electronL K).baryonMinusLepton := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    simp only [FermionCharges.hypercharge, FermionCharges.baryonMinusLepton,
      upL, downL, nuEL, electronL] <;>
    norm_num

/-- Proton: `Q = 1`, `I₃ = 1/2`, `B = 1`, `L = 0`. -/
def proton (K : Type*) [Field K] : FermionCharges K := ⟨1, 1 / 2, 1, 0⟩

/-- Neutron: `Q = 0`, `I₃ = -1/2`, `B = 1`, `L = 0`. -/
def neutron (K : Type*) [Field K] : FermionCharges K :=
  ⟨0, -(1 / 2), 1, 0⟩

/-- **B1 is the `L = 0` restriction of B2-LH.**

On the nucleon doublet lepton number vanishes, so the GMN-forced hypercharge
equals the baryon number -- and equals `+1` for *both* the proton and the
neutron.  This is the same degeneracy the chapter records as falsifying the
writhe map: `Y` does not separate `p` from `n`, while the writhe does. -/
theorem nucleon_hypercharge_eq_baryon_number {K : Type*} [Field K]
    [CharZero K] :
    (proton K).hypercharge = (proton K).B ∧
    (neutron K).hypercharge = (neutron K).B ∧
    (proton K).hypercharge = (neutron K).hypercharge := by
  refine ⟨?_, ?_, ?_⟩ <;>
    simp only [FermionCharges.hypercharge, proton, neutron] <;>
    norm_num

end QOU.StandardModel
