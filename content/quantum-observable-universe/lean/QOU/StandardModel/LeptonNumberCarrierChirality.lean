/-
Copyright (c) 2026 QOU contributors. All rights reserved.

# Lepton number cannot factor through the unframed knot type

Companion to `LeptonNumberGradingObstruction.lean`.  That file showed the
*stated* bridge from transition-count to state-function (a `ℤ`-grading on the
Skein module) cannot exist.  This file locates the *level* at which `L` can live: **it cannot factor
through the unframed knot type**, because the mirror must move the carrier
and the unknot is amphichiral.  The corpus already works one level down
(braid words, framing), so this is a constraint that its model satisfies —
not a defect in it.

## What this does and does not say (corrected 2026-08-10)

`lepton-number-categorical-properties.md` assigns

| particle | carrier | `L` |
|---|---|---|
| `e⁻` | `T(2,3)` (trefoil) | `+1` |
| `e⁺` | `T(2,3)^σ` (mirror trefoil) | `-1` |
| `νₑ` | `K_{0₁}` (unknot) | `+1` |
| `ν̄ₑ` | `K_{0₁}^σ` (mirror unknot) | `-1` |

Read as *topological knot types*, the neutral rows are inconsistent: the
unknot is amphichiral (it bounds a disk, so it is isotopic to its mirror),
and the rows would assign `+1` and `-1` to the same knot.

**That reading is wrong, and this file does not assert it.**  The corpus's own
antiparticle operation
(`QOU/Torsion/antiparticle_crossing_reversal.lean`,
`AntiparticleCrossingReversalContext`) is `mirror : Braid → Braid`, the
involution `σᵢ ↦ σᵢ⁻¹` on **braid words**, and it explicitly records
`impl_topological_mass_invariance` — *"the mirror preserves the knot type"*.
What separates particle from antiparticle there is the **crossing energy**
under the bar involution `q ↔ q⁻¹` (`E_anti = -E_bar`) and the Coulomb
charge, both valued in the coefficient ring `R` — not the knot type.

So `K_{0₁}` and `K_{0₁}^σ` are braid-level (framed) objects, and the label
"unknot" is a *projection* that discards precisely the writhe / framing data
distinguishing them.  On that reading the mirror moves the carrier and the
obstruction below does not fire.

What the theorems therefore establish is a **positive constraint**, not a
refutation: any `L` separating particle from antiparticle by mirroring must
be defined at a level where the mirror acts freely — braid word, framing, or
the `q`-side — and *cannot* factor through the unframed knot type.  The
corpus already works at that level; this file pins down why it must.

## What is proved

* `no_lepton_number_on_amphichiral_carrier` — if the mirror fixes a carrier,
  no `ℤ`-valued function of the carrier can give it `+1` on the particle and
  `-1` on its mirror.  Instantiated at the unknot, this refutes the table's
  neutral rows.
* `mirror_must_move_the_carrier` — the contrapositive, and the *actionable*
  form: any `L` separating a particle from its antiparticle by mirroring
  forces `mirror x ≠ x`.  The carrier must be chiral.
* `chiral_carrier_admits_lepton_number` — the obstruction is exactly
  amphichirality and nothing more: as soon as `mirror x ≠ x`, an `L` with the
  required values exists.  So this is a sharp characterisation, not merely a
  necessary condition.

## Consequence: which level `L` lives on

`L` must be defined where the mirror acts freely.  Two such levels exist, and
the corpus already uses both:

1. **The braid word.** `mirror : Braid → Braid` is `σᵢ ↦ σᵢ⁻¹`; distinct
   braid words can present the same knot, and the mirror moves them.
2. **The framing / writhe.** A framed unknot with framing `+n` and one with
   `-n` are distinct framed objects even though the underlying knot is
   amphichiral.  This is the per-strand framing datum `T(t)`
   (`def:strand-twist-datum`) the eightfold-way chapter carries for
   hypercharge.

Level 2 carries a tension worth stating: if `L` requires framing while the
chapter's hypercharge programme requires a *framing-independent* second
invariant, the two cannot be the same datum.  Not resolved here.

## Honest scope

**Scope-(a)** — a statement about which *level* `L` can live on, with the
invariant cited (amphichirality of the unknot: it bounds a disk, so it is
isotopic to its mirror).  It excludes one thing: `L` as a function of the
**unframed knot type**.  It does **not** refute lepton number, the corpus
table (whose carriers are braid-level, see above), the `Y = B - L` reduction,
or `μ̄₁₂₃`.  `chiral_carrier_admits_lepton_number` makes the limit precise —
the obstruction vanishes the moment the mirror moves the carrier, which at
braid/framing level it does.

Amphichirality of the unknot is taken as a **hypothesis** here
(`hamphi : mirror x = x`), not asserted as a Lean fact about a knot type —
the corpus has no `Knot` type to state it over.  It is standard and stated in
the audit; the theorems are about any carrier the mirror fixes.

Base ring / setting: a bare type with an involution and a `ℤ`-valued
function (§7c) — no ordering, no `Real`, no algebraic structure assumed.
-/

import Mathlib.Data.Int.Basic
import Mathlib.Logic.Function.Basic

namespace QOU.StandardModel

variable {K : Type*}

/-- **The obstruction.**

If the mirror involution fixes a carrier `x`, no `ℤ`-valued function of the
carrier can assign `+1` to the particle and `-1` to its mirror image.

Applied to a carrier the mirror fixes — e.g. the unknot read as a bare knot
type — this shows `L` cannot be a function of that carrier alone.  It is not
a statement about the corpus table, whose carriers are braid-level; see the
module docstring. -/
theorem no_lepton_number_on_amphichiral_carrier
    (mirror : K → K) (L : K → ℤ) (x : K)
    (hamphi : mirror x = x)
    (hparticle : L x = 1)
    (hanti : L (mirror x) = -1) :
    False := by
  rw [hamphi, hparticle] at hanti
  exact absurd hanti (by decide)

/-- **The actionable form: the carrier must be chiral.**

Any `L` that separates a particle from its antiparticle by mirroring forces
the carrier to be moved by the mirror.  The unknot is not such a carrier. -/
theorem mirror_must_move_the_carrier
    (mirror : K → K) (L : K → ℤ) (x : K)
    (hparticle : L x = 1)
    (hanti : L (mirror x) = -1) :
    mirror x ≠ x := by
  intro hfix
  exact no_lepton_number_on_amphichiral_carrier mirror L x hfix hparticle hanti

/-- **The obstruction is exactly amphichirality — nothing more.**

As soon as the mirror moves the carrier, a lepton-number function with the
required values exists.  So chirality of the carrier is *sufficient* as well
as necessary, and the negative above is sharp: it rules out the unknot, not
the idea. -/
theorem chiral_carrier_admits_lepton_number
    [DecidableEq K] (mirror : K → K) (x : K) (hchiral : mirror x ≠ x) :
    ∃ L : K → ℤ, L x = 1 ∧ L (mirror x) = -1 := by
  refine ⟨fun y => if y = x then 1 else -1, ?_, ?_⟩
  · simp
  · simp [hchiral]

end QOU.StandardModel
