/-
Copyright (c) 2026 QOU contributors. All rights reserved.

# Information content of the hypercharge battery

`content/quantum-observable-universe/eightfold-way/eightfold-open-problems.md`
item 2 records hypercharge `Y` as **open**: the writhe map is falsified as a
`Y` assignment (proton and neutron share `Y = +1` while their writhes
differ), so a second crossing invariant independent of the writhe is
required.  `flavor-charge-assignments.md` states two batteries a candidate
must pass:

* **B1** Gell-Mann--Nishijima on the nucleon doublet;
* **B2** the first-generation spectrum, `Y` of `(u, d, e⁻, νₑ)` equal to
  `{+1/3, +1/3, -1, -1}` left-handed and `{+4/3, -2/3, -2, 0}` right-handed.

This file measures what those batteries *constrain*.  It proves nothing
about any candidate invariant and derives no hypercharge; it is the
forward, formalize-first prune of AGENTS.md §"Formalize-first probe
discipline" -- narrow the target before searching for an object to hit it.

## Division-free formulation

Gell-Mann--Nishijima is usually written `Q = I₃ + Y/2`.  That form needs `2`
to be invertible -- a hypothesis about the base ring with no physical
content, and one that is easy to state too strongly (`CharZero` is far more
than is needed; `2 ≠ 0` would be enough).  We avoid the question entirely by
using the **cleared** form throughout:

  `2Q = 2I₃ + Y`

equivalent to the familiar form whenever `2 ≠ 0`, and better behaved when it
is not.  Every result below then holds over an arbitrary `CommRing R` with
**no characteristic hypothesis at all**: in the cleared form `Y` is
*subtracted* out, never *divided* out.

The physical charges are thirds and halves, so the concrete tables store
**six times** each quantum number (`sixQ = 6Q`, and so on).  Every entry is
then an integer and the whole battery is integer arithmetic, closed by
`decide`.

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

Base ring is a generic `CommRing R` (§7c): no field, no ordering, no
`Real`, no division, no archimedean construct.
-/

import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Int.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum

namespace QOU.StandardModel

/-- The Gell-Mann--Nishijima relation in **cleared (division-free)** form,
`2Q = 2I₃ + Y`.

Equivalent to the familiar `Q = I₃ + Y/2` whenever `2` is invertible, but
stated so that it makes sense -- and the results below hold -- over an
arbitrary commutative ring, with no characteristic hypothesis. -/
def GellMannNishijima {R : Type*} [CommRing R] (Q I₃ Y : R) : Prop :=
  2 * Q = 2 * I₃ + Y

/-- **The right-handed battery is an identity, not a test.**

On a weak singlet (`I₃ = 0`) the Gell-Mann--Nishijima relation determines
`Y` outright from `Q`.  So two candidate hypercharge assignments that both
satisfy GMN against the *same* derived charge agree on every right-handed
row: the right-handed half of B2 has no discriminating power.

No characteristic hypothesis is needed -- in the cleared form `Y` is
subtracted out, never divided out. -/
theorem hypercharge_determined_of_isospin_zero {R : Type*} [CommRing R]
    (Q Y₁ Y₂ : R)
    (h₁ : GellMannNishijima Q 0 Y₁)
    (h₂ : GellMannNishijima Q 0 Y₂) :
    Y₁ = Y₂ := by
  unfold GellMannNishijima at h₁ h₂
  linear_combination h₂ - h₁

/-- The right-handed hypercharge forced by GMN at `I₃ = 0` is `2Q`. -/
theorem rh_hypercharge_eq_two_mul_charge {R : Type*} [CommRing R]
    (Q Y : R) (h : GellMannNishijima Q 0 Y) :
    Y = 2 * Q := by
  unfold GellMannNishijima at h
  linear_combination -h

/-- First-generation quantum numbers, stored as **six times** the physical
value so every entry is an integer and no division ever occurs:
`sixQ = 6Q`, `sixI₃ = 6I₃`, `sixB = 6B`, `sixL = 6L`. -/
structure FermionCharges where
  sixQ : ℤ
  sixI₃ : ℤ
  sixB : ℤ
  sixL : ℤ
  deriving DecidableEq

namespace FermionCharges

/-- Six times the hypercharge forced by GMN: from `2Q = 2I₃ + Y` we get
`Y = 2Q - 2I₃`, hence `6Y = 2·(6Q) - 2·(6I₃)`. -/
def sixHypercharge (f : FermionCharges) : ℤ := 2 * f.sixQ - 2 * f.sixI₃

/-- Six times the anomaly-free combination `B - L`. -/
def sixBaryonMinusLepton (f : FermionCharges) : ℤ := f.sixB - f.sixL

/-- `sixHypercharge` is not an independent stipulation: it is exactly what
the cleared Gell-Mann--Nishijima relation forces from `sixQ` and `sixI₃`. -/
theorem gmn_sixHypercharge (f : FermionCharges) :
    GellMannNishijima f.sixQ f.sixI₃ f.sixHypercharge := by
  unfold GellMannNishijima sixHypercharge
  ring

end FermionCharges

open FermionCharges

/-- Left-handed up quark: `Q = 2/3`, `I₃ = 1/2`, `B = 1/3`, `L = 0`. -/
def upL : FermionCharges := ⟨4, 3, 2, 0⟩

/-- Left-handed down quark: `Q = -1/3`, `I₃ = -1/2`, `B = 1/3`, `L = 0`. -/
def downL : FermionCharges := ⟨-2, -3, 2, 0⟩

/-- Left-handed electron neutrino: `Q = 0`, `I₃ = 1/2`, `B = 0`, `L = 1`. -/
def nuEL : FermionCharges := ⟨0, 3, 0, 6⟩

/-- Left-handed electron: `Q = -1`, `I₃ = -1/2`, `B = 0`, `L = 1`. -/
def electronL : FermionCharges := ⟨-6, -3, 0, 6⟩

/-- **The left-handed battery is exactly `B - L`.**

For each of the four first-generation left-handed fermions, the hypercharge
forced by Gell-Mann--Nishijima equals baryon number minus lepton number.
Pure integer arithmetic in the `6×` normalisation. -/
theorem lh_hypercharge_eq_baryon_sub_lepton :
    upL.sixHypercharge = upL.sixBaryonMinusLepton ∧
    downL.sixHypercharge = downL.sixBaryonMinusLepton ∧
    nuEL.sixHypercharge = nuEL.sixBaryonMinusLepton ∧
    electronL.sixHypercharge = electronL.sixBaryonMinusLepton := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> decide

/-- The B2-LH targets, in the `6×` normalisation: `6Y = {2, 2, -6, -6}`,
i.e. `Y = {+1/3, +1/3, -1, -1}` for `(u, d, νₑ, e⁻)`. -/
theorem lh_hypercharge_values :
    upL.sixHypercharge = 2 ∧ downL.sixHypercharge = 2 ∧
    nuEL.sixHypercharge = -6 ∧ electronL.sixHypercharge = -6 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> decide

/-- Proton: `Q = 1`, `I₃ = 1/2`, `B = 1`, `L = 0`. -/
def proton : FermionCharges := ⟨6, 3, 6, 0⟩

/-- Neutron: `Q = 0`, `I₃ = -1/2`, `B = 1`, `L = 0`. -/
def neutron : FermionCharges := ⟨0, -3, 6, 0⟩

/-- **B1 is the `L = 0` restriction of B2-LH.**

On the nucleon doublet lepton number vanishes, so the GMN-forced hypercharge
equals the baryon number -- and equals `+1` for *both* the proton and the
neutron.  This is the same degeneracy the chapter records as falsifying the
writhe map: `Y` does not separate `p` from `n`, while the writhe does. -/
theorem nucleon_hypercharge_eq_baryon_number :
    proton.sixHypercharge = proton.sixB ∧
    neutron.sixHypercharge = neutron.sixB ∧
    proton.sixHypercharge = neutron.sixHypercharge := by
  refine ⟨?_, ?_, ?_⟩ <;> decide

/-- The nucleon hypercharge is `+1` (i.e. `6Y = 6`) for both. -/
theorem nucleon_hypercharge_eq_one :
    proton.sixHypercharge = 6 ∧ neutron.sixHypercharge = 6 := by
  refine ⟨?_, ?_⟩ <;> decide

end QOU.StandardModel
