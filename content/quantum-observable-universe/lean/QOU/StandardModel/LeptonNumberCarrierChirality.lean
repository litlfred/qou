/-
Copyright (c) 2026 QOU contributors. All rights reserved.

# Lepton number needs a chiral carrier: the neutrino cannot be the unknot

Companion to `LeptonNumberGradingObstruction.lean`.  That file showed the
*stated* bridge from transition-count to state-function (a `ℤ`-grading on the
Skein module) cannot exist.  This file shows something stronger and more
useful: **no function of the unframed knot type can reproduce the corpus's
own lepton-number table**, and it identifies exactly what extra data is
needed.

## The inconsistency

`lepton-number-categorical-properties.md` assigns

| particle | carrier | `L` |
|---|---|---|
| `e⁻` | `T(2,3)` (trefoil) | `+1` |
| `e⁺` | `T(2,3)^σ` (mirror trefoil) | `-1` |
| `νₑ` | `K_{0₁}` (unknot) | `+1` |
| `ν̄ₑ` | `K_{0₁}^σ` (mirror unknot) | `-1` |

The charged rows are fine: the trefoil is **chiral**, so `T(2,3)` and its
mirror are genuinely different knots and may carry different `L`.

The neutral rows are not.  The unknot is **amphichiral** — it bounds a disk,
so its mirror is itself, `K_{0₁}^σ = K_{0₁}`.  The table therefore assigns
`+1` and `-1` to *the same knot*.  No function of the knot type can do that.

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

## Consequence: what `L` must actually be

Two repairs are available, and they are the only two:

1. **Give the neutrino a chiral carrier.** The unknot cannot work; the
   carrier must be a knot that its mirror does not fix.
2. **Let `L` see more than the knot type.** The natural candidate is the
   *framing*: a framed unknot with framing `+n` and one with framing `-n` are
   distinct framed objects even though the underlying knot is amphichiral, so
   the mirror acts freely there.  This is the same per-strand framing datum
   `T(t)` (`def:strand-twist-datum`) that the eightfold-way chapter carries
   for hypercharge.

Route 2 is the more interesting one, because it would put `L` and the
hypercharge framing datum in the same structure.  Neither route is pursued
here.

## Honest scope

**Scope-(b)** with the invariant cited (amphichirality of the unknot: it
bounds a disk, so it is isotopic to its mirror).  It excludes exactly one
thing — `L` as a function of the *unframed* knot type, given the corpus's own
carrier assignment.  It does **not** refute lepton number, the `Y = B - L`
reduction, `μ̄₁₂₃`, or route 2 above; `chiral_carrier_admits_lepton_number`
makes precise that the obstruction vanishes the moment the carrier is chiral.

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

Applied to the corpus table with `x = K_{0₁}` the unknot (amphichiral, so
`mirror x = x`), this refutes the neutrino / antineutrino rows. -/
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
