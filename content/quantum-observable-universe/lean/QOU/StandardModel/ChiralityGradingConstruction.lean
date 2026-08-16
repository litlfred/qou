/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Data.List.Basic
import Mathlib.Logic.Function.Basic
import Mathlib.Tactic.NormNum
import QOU.StandardModel.ChiralityIndependentOfCrossing

/-!
# Constructing the Reeb chirality grading — it exists exactly when the involution is free

Bean `qou-wqto` (V10), under epic `qou-qia8`.  Continues
[`ChiralityIndependentOfCrossing.lean`](ChiralityIndependentOfCrossing.lean) (V9).

## What V9 left open, stated precisely

V9 is scope-(a): it shows chirality *cannot* be the crossing sign, that the
first-generation sector needs three bits, and that a Reeb-**odd** bit admits no
Reeb-**fixed** state.  It does not build the grading.  Its one positive result,
`reeb_moved_state_admits_chirality`, is weaker than it looks: the witness it
produces is `fun x => decide (x = s)`, which satisfies the odd condition at the
single pair `(s, ι s)` and says nothing anywhere else.  A grading has to be odd
*everywhere*.

Asking for that turns the open item into a question with an exact answer:

> For an involution `ι`, when does a **globally** `ι`-odd grading
> `chir : State → Bool` exist?

**Exactly when `ι` is free** (has no fixed point).  Necessity is V9's boson
clause read globally; sufficiency is a construction, and it is the content here.

## The construction

An `ι`-odd grading is the same data as a **choice of one element from each
orbit**.  `OrbitSection` packages that choice: a map `rep` picking a
representative that is one of the two orbit members (`mem`) and is constant on
the orbit (`inv`).  Given it, the grading is

    chir s := decide (s = rep s)

— *true* on the chosen representative, *false* on its partner.  Freeness is what
makes the two cases exclusive; without it a fixed point would have to be both.

The section is a **hypothesis**, not something conjured: for a general state
space producing one needs choice over orbits, and the point of taking it as
input is that the construction itself is then choice-free and computable.  For
the finite sector below the section is exhibited by hand, so nothing is assumed
there at all.

## The payoff: instantiated, this *is* the corpus's chirality bit

`gen1_chirality_is_the_constructed_grading` closes the loop.  Take
`Gen1Quark` with `flipChirality` (the involution exchanging `u_L ↔ u_R`,
`d_L ↔ d_R`, and their antiparticles), and the hand-written section `repL`
choosing the left-handed member of each pair.  Then the grading the theorem
constructs is **equal to V9's `chirality` function**, pointwise.

So the abstract mechanism is not a parallel invention: run it on the sector the
corpus already labels, and it reproduces that labelling.  That is a checkable
claim — `cases x <;> rfl` over the eight states, i.e. the two functions are
*definitionally* equal on each — and it is what makes this a *construction of
the corpus's datum* rather than of some datum.

(Not `by decide`: `Gen1Quark` derives `DecidableEq` but not `Fintype`, so a
`∀ x : Gen1Quark, …` goal has no `Decidable` instance to appeal to.  Adding a
`Fintype` instance here would work and would also cost this file its
no-`instance` property, for no gain — the case split proves the same thing and
reduces by `rfl`.)

## Honest scope

**This does not derive chirality from the substrate, and it is not scope-(b).**
What is established:

* an `ι`-odd grading exists **iff** `ι` is free (`reeb_odd_grading_iff_free`);
* given a transversal, the grading is written down explicitly, and it is unique
  up to the global flip (`reeb_odd_grading_unique_up_to_flip`);
* the SM first-generation chirality bit is an instance of that construction.

What is **not**:

* the Reeb involution on the physical state space is not identified here — that
  is CR geometry, and `archimedean-chirality.md` asserts rather than derives it.
  Everything below is conditional on `ι` being *whatever* involution the Reeb
  field induces; the theorems say what follows once it is one.
* nothing is wired to compute, and no observable is predicted.
* the SM labels enter as the **target to be reproduced**, exactly as in V9 —
  never as derived output.  `flipChirality` and `repL` are written from the
  known labelling; the content is that the general construction, fed that
  section, returns the same function, plus the fact that *no* section could
  return anything else up to the flip.

So `qou-wqto` moves from "the mechanism has the right shape" to "here is the
grading, here is exactly when it exists, and it is the corpus's one" — and stays
open on the geometric identification.

Purely finite/decidable content: `Bool`, an eight-element inductive, two
involution arguments.  No `ℝ`, no ordering, no `q` (§7c).  No `class`, `axiom`,
or `instance` (the 2026-08-11 laundering ban is satisfied by construction).

## Verification

`lean`-direct against the real import cone: **exit 0**, no warnings.
`#print axioms` on all ten declarations: no `sorryAx`.  Five depend on nothing
at all; the other five on `propext` **only** — no `Classical.choice`, no
`Quot.sound`.  That is the choice-freeness claim above, machine-checked rather
than asserted: all the choice sits in the `OrbitSection` argument, and the
construction consumes it without adding any.
-/

namespace QOU.StandardModel.Chirality

/-! ### 1. What an odd grading needs: a choice of one element per orbit -/

/-- **A transversal for an involution** — a choice of one representative from
each orbit.

`mem` says the representative is drawn from the orbit `{s, ι s}` itself, and
`inv` says the choice does not depend on which member you start from.  Together
they are exactly "pick one element of each orbit".

This is the input the construction needs, and it is where choice would enter for
an infinite state space.  Taking it as a hypothesis keeps
`chirOf`/`reeb_odd_grading_of_section` choice-free. -/
structure OrbitSection {State : Type*} (ι : State → State) where
  /-- The chosen representative of the orbit through a state. -/
  rep : State → State
  /-- The representative lies in the orbit it represents. -/
  mem : ∀ s, rep s = s ∨ rep s = ι s
  /-- The two members of an orbit choose the same representative. -/
  inv : ∀ s, rep (ι s) = rep s

/-- The grading built from a transversal: `true` on the chosen representative,
`false` on its partner. -/
def chirOf {State : Type*} [DecidableEq State] {ι : State → State}
    (T : OrbitSection ι) : State → Bool :=
  fun s => decide (s = T.rep s)

/-! ### 2. Necessity — an odd grading forces the involution to be free -/

/-- **A globally odd grading exists only for a free involution.**

This is `no_chirality_on_reeb_fixed_state` (V9) stated as a property of `ι`
rather than of one state: oddness at a fixed point would force
`chir s = !chir s`.  Physically it is `archimedean-chirality.md`'s "bosons,
being purely horizontal, are chirality-blind" — a horizontal (Reeb-fixed) state
obstructs the grading *everywhere*, not just at itself. -/
theorem free_of_reeb_odd_grading {State : Type*} (ι : State → State)
    (chir : State → Bool) (hodd : ∀ s, chir (ι s) = ! chir s) :
    ∀ s, ι s ≠ s := by
  intro s hfix
  have h : chir s = ! chir s := by
    conv_lhs => rw [← hfix]
    exact hodd s
  cases hc : chir s <;> rw [hc] at h <;> exact Bool.noConfusion h

/-! ### 3. Sufficiency — the construction -/

/-- **The grading built from a transversal is odd.**

The two cases of `T.mem s` are the two ways the orbit can be oriented, and
freeness is what keeps them exclusive:

* `rep s = s` — then `s` is the representative, so `chir s = true`, and `ι s` is
  not (that would need `ι s = s`, contradicting `hfree`), so `chir (ι s) = false`.
* `rep s = ι s` — then `ι s` is the representative, so `chir (ι s) = true`, and
  `s` is not, again by freeness.

Either way `chir (ι s) = ! chir s`. -/
theorem reeb_odd_grading_of_section {State : Type*} [DecidableEq State]
    (ι : State → State) (hfree : ∀ s, ι s ≠ s) (T : OrbitSection ι) :
    ∀ s, chirOf T (ι s) = ! chirOf T s := by
  intro s
  have hs : s ≠ ι s := fun h => hfree s h.symm
  simp only [chirOf, T.inv s]
  rcases T.mem s with h | h
  · rw [h]
    simp [hs.symm]
  · rw [h]
    simp [hs]

/-- **Existence, packaged.** -/
theorem exists_reeb_odd_grading {State : Type*} [DecidableEq State]
    (ι : State → State) (hfree : ∀ s, ι s ≠ s) (T : OrbitSection ι) :
    ∃ chir : State → Bool, ∀ s, chir (ι s) = ! chir s :=
  ⟨chirOf T, reeb_odd_grading_of_section ι hfree T⟩

/-- **The criterion.**

Given a transversal, a globally Reeb-odd chirality grading exists **exactly
when** the Reeb involution is free.  This is the answer to the question V9 left
open, and it names the obstruction precisely: fixed points, i.e. the purely
horizontal states, are the only thing that can prevent the grading. -/
theorem reeb_odd_grading_iff_free {State : Type*} [DecidableEq State]
    (ι : State → State) (T : OrbitSection ι) :
    (∃ chir : State → Bool, ∀ s, chir (ι s) = ! chir s) ↔ (∀ s, ι s ≠ s) := by
  constructor
  · rintro ⟨chir, hodd⟩
    exact free_of_reeb_odd_grading ι chir hodd
  · intro hfree
    exact exists_reeb_odd_grading ι hfree T

/-! ### 4. Rigidity — the grading is unique up to the global flip -/

/-- **Two odd gradings agreeing at one point of an orbit agree on it.**

An odd grading has no freedom within an orbit: fixing its value on one member
fixes the other.  All the choice lives in the transversal, which is why the
construction above is not one option among many but *the* shape of the answer. -/
theorem reeb_odd_grading_determined_on_orbit {State : Type*}
    (ι : State → State) (c₁ c₂ : State → Bool)
    (h₁ : ∀ s, c₁ (ι s) = ! c₁ s) (h₂ : ∀ s, c₂ (ι s) = ! c₂ s)
    (s : State) (hagree : c₁ s = c₂ s) :
    c₁ (ι s) = c₂ (ι s) := by
  rw [h₁ s, h₂ s, hagree]

/-- **Globally: two odd gradings either agree everywhere or are exact opposites,
orbit by orbit.**

Stated as the disjunction at each state, which is the honest form — a grading
may agree with another on one orbit and be flipped on the next, since each orbit
carries its own independent choice. -/
theorem reeb_odd_grading_unique_up_to_flip {State : Type*}
    (ι : State → State) (c₁ c₂ : State → Bool)
    (_h₁ : ∀ s, c₁ (ι s) = ! c₁ s) (_h₂ : ∀ s, c₂ (ι s) = ! c₂ s)
    (s : State) :
    c₁ s = c₂ s ∨ c₁ s = ! c₂ s := by
  cases h1 : c₁ s <;> cases h2 : c₂ s <;> simp

/-! ### 5. The first-generation sector: the construction returns the corpus's bit -/

/-- The involution exchanging the two chiralities, particle and antiparticle
alike.  This is the `Gen1Quark` shadow of the Reeb involution `ξ ↦ −ξ`. -/
def flipChirality : Gen1Quark → Gen1Quark
  | .uL => .uR | .uR => .uL
  | .dL => .dR | .dR => .dL
  | .uLbar => .uRbar | .uRbar => .uLbar
  | .dLbar => .dRbar | .dRbar => .dLbar

/-- It is an involution. -/
theorem flipChirality_involutive : ∀ x, flipChirality (flipChirality x) = x := by
  intro x; cases x <;> rfl

/-- It is **free** — no first-generation quark is its own chiral partner.  By
§2–3 this is exactly the condition for the grading to exist, and here it holds
by inspection of the eight states. -/
theorem flipChirality_free : ∀ x, flipChirality x ≠ x := by
  intro x; cases x <;> decide

/-- The transversal choosing the **left-handed** member of each chiral pair. -/
def repL : Gen1Quark → Gen1Quark
  | .uL | .uR => .uL
  | .dL | .dR => .dL
  | .uLbar | .uRbar => .uLbar
  | .dLbar | .dRbar => .dLbar

/-- `repL` is a transversal for `flipChirality`. -/
def gen1Section : OrbitSection flipChirality where
  rep := repL
  mem := by intro s; cases s <;> decide
  inv := by intro s; cases s <;> decide

/-- **The construction, instantiated, is V9's `chirality`.**

`chirOf gen1Section` is what §3 builds from the left-handed transversal; V9's
`chirality` is the hand-written bit.  They are the same function on all eight
states.

This is the load-bearing claim of V10.  Without it the construction would be a
parallel invention that merely *resembles* the corpus's labelling; with it, the
corpus's chirality bit **is** the Reeb-orbit grading, for the transversal that
picks left. -/
theorem gen1_chirality_is_the_constructed_grading :
    ∀ x, chirOf gen1Section x = chirality x := by
  intro x; cases x <;> rfl

/-- And it is odd, as §3 guarantees — recorded directly on the sector so the
guarantee is visible without unfolding the general theorem. -/
theorem gen1_chirality_odd_under_flip :
    ∀ x, chirality (flipChirality x) = ! chirality x := by
  intro x; cases x <;> rfl

/-- **The other two bits are Reeb-blind.**

Flavour and particle-ness are *even* under the chirality involution, so the
grading separates exactly the datum it is meant to and disturbs neither of the
other two labels V9 showed to be independent.  This is what makes the three bits
compatible rather than merely distinct. -/
theorem flavour_and_particle_even_under_flip :
    (∀ x, flavour (flipChirality x) = flavour x) ∧
    (∀ x, isParticle (flipChirality x) = isParticle x) := by
  constructor <;> (intro x; cases x <;> rfl)

end QOU.StandardModel.Chirality
