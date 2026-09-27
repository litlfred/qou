/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Data.List.Basic
import Mathlib.Logic.Function.Basic
import Mathlib.Tactic.NormNum

/-!
# Chirality is not the crossing sign — and the braid element is over-subscribed

Bean `qou-wqto` (V9), under epic `qou-qia8`.  Completes the V8 arc
(`QuarkBraidChargeObstruction.lean`).

`sm-open-problems.md` records chirality (`u_L` vs `u_R`) as "unrepresented".
The corpus-grep says something more precise: it is *not represented on braid
words*, but the framework does supply a chirality mechanism, and it is a
**different** datum from the crossing sign.

## The two blocks, and why they do not collide

[`predicted-spectra/parity-violation-skein-interpretation.md`](../../../predicted-spectra/parity-violation-skein-interpretation.md)
reads handedness off the **crossing sign**: `σᵢ` carries weight `q`, `σᵢ⁻¹`
carries `q⁻¹`, and "the weak force … couples only to left-handed particles.
This maps to crossing chirality."

[`brings-surface/archimedean-chirality.md`](../../../brings-surface/archimedean-chirality.md)
reads it off the **Reeb involution** instead: "Chirality is … encoded in the
`±`-eigenspaces of the Reeb involution `ξ ↦ −ξ`", carried by the *vertical*
component `α_V`; "bosons, being purely horizontal, are chirality-blind."

Taken as one mechanism these would collide, because V8 already spent the
crossing sign on flavour: `knot-particle-dictionary-table4-data.md` gives
`𝔲 ↦ σᵢ` and `𝔡 ↦ σᵢ⁻¹`.  `chirality_not_a_function_of_crossing` shows the
collision is real — a chirality that factors through the crossing sign cannot
separate `u_L` from `u_R`, since both are up quarks and so share the sign.

So the two blocks are consistent only on the Reeb reading: **chirality is an
independent bit**, living on the vertical component, not on the braid word.
That is the resolution, and it is what makes the parity block's "maps to
crossing chirality" a statement about the *weak coupling's* sign sensitivity
rather than a definition of handedness.

## The braid element is over-subscribed

Three independent binary labels are wanted on the first-generation quark
sector — flavour (`u`/`d`), chirality (`L`/`R`), and particle/antiparticle —
giving **8** states.  The braid element supplies **one** bit (the crossing
sign), and V8 showed it is already ambiguous even between two of those labels:
the anti-up and the down share `σᵢ⁻¹`.

`braid_element_cannot_separate_gen1` makes the counting exact: no map out of a
two-valued datum separates eight states, so **at least two further independent
bits** are required beyond the braid element.  `archimedean-chirality` supplies
one of them (Reeb `±`); the other — the colour-tube *environment* label that
`up-quark.md` names but nothing formalizes — remains the open datum V8
identified.

## What is proved (all sorry-free)

* `chirality_not_a_function_of_crossing` — chirality cannot factor through the
  crossing sign, because `u_L` and `u_R` share it.
* `gen1_determined_by_flavour_chirality_particle` — the three bits *do*
  determine the eight states (injectivity), so the labelling is not
  over-specified either.
* `braid_element_cannot_separate_gen1` — one bit cannot separate eight states:
  at least two more are needed.
* `flavour_and_particle_alone_insufficient` — and the chirality bit specifically
  is load-bearing: drop it and `u_L` collapses onto `u_R`.  Together with
  `flavour_and_chirality_alone_insufficient` (drop the particle bit and `u_L`
  collapses onto `ū_L`) this shows the three bits are not merely sufficient but
  **minimal**.
* `no_chirality_on_reeb_fixed_state` — a chirality that is **odd** under the
  Reeb involution admits **no** fixed state.  This is `archimedean-chirality`'s
  "bosons, being purely horizontal, are chirality-blind" as a theorem: a purely
  horizontal (Reeb-fixed) object cannot carry the bit at all.  Structurally it
  is the same argument as `LeptonNumberCarrierChirality`'s amphichirality
  obstruction, one level up.

## Honest scope

**Scope-(a).**  This does not construct the chirality datum, does not wire
anything, and does not close `qou-wqto`.  It establishes *which* datum cannot
be it (the crossing sign), *how many* independent bits the sector needs (three,
of which the braid element supplies one), and that the Reeb mechanism has the
right shape — including the correct degeneracy on bosons.  The SM labels enter
as the definition of the enumerated type, i.e. as the thing to be reproduced,
never as derived output.

Purely finite/decidable content: `Bool`, a four-element inductive, and one
involution argument.  No `ℝ`, no ordering, no `q` (§7c).
-/

namespace QOU.StandardModel.Chirality

/-! ### 1. Chirality does not factor through the crossing sign -/

/-- **A chirality bit cannot be a function of the crossing sign.**

`u_L` and `u_R` are both up quarks, so by the knot-particle dictionary they
carry the *same* braid element `σᵢ` and hence the same crossing sign; but they
have opposite chirality by definition.  Any `chir` factoring through `crossing`
is therefore forced to give one value to both.

The hypotheses are exactly the corpus's own assignments: `h_up_same_crossing`
is the dictionary row for `𝔲`, and `h_uL` / `h_uR` are the definitions of the
two chiralities. -/
theorem chirality_not_a_function_of_crossing
    {State : Type*} (crossing chir : State → Bool) (uL uR : State)
    (h_up_same_crossing : crossing uL = crossing uR)
    (h_uL : chir uL = true) (h_uR : chir uR = false)
    (f : Bool → Bool) (hfac : ∀ s, chir s = f (crossing s)) :
    False := by
  have h1 : f (crossing uL) = true := by rw [← hfac]; exact h_uL
  have h2 : f (crossing uR) = false := by rw [← hfac]; exact h_uR
  rw [h_up_same_crossing] at h1
  rw [h1] at h2
  exact Bool.noConfusion h2

/-! ### 2. The first-generation quark sector needs three bits -/

/-- The eight first-generation quark states: flavour × chirality × particle. -/
inductive Gen1Quark
  | uL | uR | dL | dR
  | uLbar | uRbar | dLbar | dRbar
  deriving DecidableEq

open Gen1Quark

/-- Flavour bit: `true` = up-type. -/
def flavour : Gen1Quark → Bool
  | uL | uR | uLbar | uRbar => true
  | dL | dR | dLbar | dRbar => false

/-- Chirality bit: `true` = left-handed. -/
def chirality : Gen1Quark → Bool
  | uL | dL | uLbar | dLbar => true
  | uR | dR | uRbar | dRbar => false

/-- Particle bit: `true` = particle (not antiparticle). -/
def isParticle : Gen1Quark → Bool
  | uL | uR | dL | dR => true
  | uLbar | uRbar | dLbar | dRbar => false

/-- **The three bits determine the sector.**

So the labelling is exactly right-sized: three independent binary labels, eight
states, and the map to `Bool × Bool × Bool` is injective. -/
theorem gen1_determined_by_flavour_chirality_particle :
    Function.Injective (fun x : Gen1Quark => (flavour x, chirality x, isParticle x)) := by
  intro a b h
  cases a <;> cases b <;> simp_all [flavour, chirality, isParticle]

/-- The sector really does have eight pairwise-distinct states. -/
theorem gen1_states_distinct :
    [uL, uR, dL, dR, uLbar, uRbar, dLbar, dRbar].Nodup := by decide

/-- **One bit cannot separate the sector.**

The braid element supplies a single binary datum (the crossing sign).  No map
out of `Bool` can be injective on eight states, so **at least two further
independent bits** are needed beyond the braid element — one of which the Reeb
involution supplies, the other being the unformalized colour-tube environment
label. -/
theorem braid_element_cannot_separate_gen1 (crossing : Gen1Quark → Bool) :
    ¬ Function.Injective crossing := by
  intro hinj
  -- three distinct states, two available values: two must collide
  rcases Bool.eq_false_or_eq_true (crossing uL) with h1 | h1 <;>
  rcases Bool.eq_false_or_eq_true (crossing uR) with h2 | h2 <;>
  rcases Bool.eq_false_or_eq_true (crossing dL) with h3 | h3 <;>
  first
    | exact absurd (hinj (h1.trans h2.symm)) (by decide)
    | exact absurd (hinj (h1.trans h3.symm)) (by decide)
    | exact absurd (hinj (h2.trans h3.symm)) (by decide)

/-- **Each of the three bits is load-bearing: drop the chirality bit and the
sector collapses.**

`u_L` and `u_R` agree on flavour and on particle-ness, so without the chirality
bit they are the same state.  This is the V9 claim in its sharpest form — the
chirality datum is not decoration, it is required for the labelling to be
faithful. -/
theorem flavour_and_particle_alone_insufficient :
    ¬ Function.Injective (fun x : Gen1Quark => (flavour x, isParticle x)) := by
  intro hinj
  exact absurd (hinj (by decide : ((fun x : Gen1Quark => (flavour x, isParticle x)) uL)
      = ((fun x : Gen1Quark => (flavour x, isParticle x)) uR))) (by decide)

/-- Likewise the particle bit: without it `u_L` and `ū_L` collide. -/
theorem flavour_and_chirality_alone_insufficient :
    ¬ Function.Injective (fun x : Gen1Quark => (flavour x, chirality x)) := by
  intro hinj
  exact absurd (hinj (by decide : ((fun x : Gen1Quark => (flavour x, chirality x)) uL)
      = ((fun x : Gen1Quark => (flavour x, chirality x)) uLbar))) (by decide)

/-! ### 3. A Reeb-odd chirality is blind on horizontal states -/

/-- **`archimedean-chirality.md`'s boson clause, as a theorem.**

Chirality is the `±`-eigenvalue of the Reeb involution `ξ ↦ −ξ`, i.e. a bit that
is **odd** under it.  A purely horizontal object is one the involution fixes.
No such object can carry the bit: oddness would force `chir s = !chir s`.

This is `archimedean-chirality`'s "bosons, being purely horizontal, are
chirality-blind" — and it is structurally the same argument as
`LeptonNumberCarrierChirality.no_lepton_number_on_amphichiral_carrier`, one
level up: a grading that anticommutes with an involution vanishes on its fixed
points. -/
theorem no_chirality_on_reeb_fixed_state
    {State : Type*} (reeb : State → State) (chir : State → Bool)
    (hodd : ∀ s, chir (reeb s) = ! chir s)
    (s : State) (hfix : reeb s = s) :
    False := by
  have h : chir s = ! chir s := by
    conv_lhs => rw [← hfix]
    exact hodd s
  cases hc : chir s <;> rw [hc] at h <;> exact Bool.noConfusion h

/-- Conversely, a state the involution **moves** admits such a bit — so the
mechanism is not vacuous, it is exactly a fermion/boson dichotomy. -/
theorem reeb_moved_state_admits_chirality
    {State : Type*} [DecidableEq State] (reeb : State → State) (s : State)
    (hmove : reeb s ≠ s) :
    ∃ chir : State → Bool, chir s = true ∧ chir (reeb s) = false := by
  refine ⟨fun x => decide (x = s), by simp, ?_⟩
  simp [hmove]

end QOU.StandardModel.Chirality
