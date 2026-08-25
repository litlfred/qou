/-
Copyright (c) 2026 QOU contributors. All rights reserved.

# The writhe is Markov-I invariant but not Markov-II invariant

Bean `qou-ap47`.  This is a statement about `Q` and `I₃`, which are wired to
production, not only about lepton number.

## The two claims that collide

`braids-and-knots/markov-moves-brane-tower.md`:

> Conjugation `β ↦ γβγ⁻¹` is the horizontal direction. It represents gauge
> transformations within a single fibre at a fixed level `n`. […] Markov's
> theorem dictates that **horizontal and vertical moves exhaust the gauge
> freedom.**

`appendix-standard-model/sm-lagrangian-selection-rules.md`:

> Conserved quantities are functions on states **constant on gauge orbits**.
> The framework currently exhibits two such invariants without fitted
> parameters: the Coulomb charge `Q = w/2` […] and the writhe-to-isospin
> assignment `w ↦ I₃`.

Horizontal is Markov I (conjugation).  Vertical is Markov II (stabilisation),
`β ∈ B_n ↦ βσ_n^{±1} ∈ B_{n+1}`, which presents the *same link* and changes the
writhe by `±1`.  So a writhe-derived quantity cannot be constant on gauge orbits
if the orbits include vertical moves.

## What is proved

* `writhe_append`, `writhe_inv` — the writhe is additive and inverts on the
  inverse word.
* `writhe_conj` — **Markov I is safe**: `writhe (γ ++ β ++ γ⁻¹) = writhe β`.
  Conjugation, the horizontal/fixed-`n` direction, preserves the writhe, so `Q`
  and `I₃` *are* invariant there.
* `writhe_stabilize`, `writhe_stabilize_neg` — **Markov II is not**:
  stabilisation shifts the writhe by exactly `±1`.
* `coulombCharge_not_stabilization_invariant` — hence `Q = w/2` shifts by
  `±1/2` under a move that does not change the link.

## Consequence

The corpus's two claims are inconsistent as written.  Exactly one of these must
be given up, and the choice is the framework's to make:

1. **Gauge freedom is horizontal only** (fixed strand number `n`).  Then `Q` and
   `I₃` are genuinely gauge-invariant, but "horizontal *and vertical* moves
   exhaust the gauge freedom" is wrong, and states are *not* links — they are
   braid words modulo conjugation, or Gröbner–Shirshov normal forms
   (`mba-step02-gs-reduction.md`: "every downstream algorithm consumes `NF(w)`,
   not the raw braid").
2. **Gauge freedom includes vertical moves.**  Then states are links, and `Q`
   and `I₃` are **not** conserved quantities — they are not functions on states
   at all.

**🟧 OWNER RULING (2026-08-10): reading 1 — Gröbner–Shirshov normal forms are
the states.** Reading 2 is kept open but is not the working convention.

The owner supplied the sharper principle that makes this work: *"the observable
at a point is the trace on the lowest part of the substrate tower."*  That is
not a quotient by the vertical move — it is a **canonical section** of it.  One
destabilises down the tower (`tr_M(x T_n) = z · tr_M(x)`,
`appendix-surreals/collatz-three-forms.md`) to the minimal level and evaluates
there.

This resolves the inconsistency without giving up `Q` or `I₃`:

* the minimal level is the **braid index**, itself a link invariant;
* at the minimal level the surviving moves are conjugation (and exchange), which
  `writhe_conj` shows preserve the writhe;
* so the writhe *evaluated at the bottom of the tower* is well-defined, and `Q`
  and `I₃` are observables of that datum.

What must be corrected is only the wording of
`sm-lagrangian-selection-rules.md`: `Q` and `I₃` are constant on **horizontal**
gauge orbits at the tower's lowest level, not on the full Markov orbit.

The Markov *trace* is consistent in a way the bare writhe is not: `tr_M` is
invariant under **both** moves (`markov-trace-ambient-s3.md`), which is why it
descends to links unaided.  The writhe does not, so anything built from it is an
observable only after the destabilisation to the bottom of the tower.

## The writhe's vertical component

The writhe is not a link observable, and the precise reason is that it *mixes
with the tower level*.  Markov II acts on the pair `(w, n)` as
`(w ± 1, n + 1)`, so from `(w, n)` one reaches exactly
`(w + a − b, n + a + b)` for `a, b ≥ 0`.  Machine-checked over random move
sequences: `w`, `w − n` and `w + n` are all **non**-invariant, while
`(w − n) mod 2` **is** — and it is the only invariant of the pair.

So `w` carries a genuine vertical component: on links it is defined only modulo
the tower direction, and only its parity relative to `n` survives.  Picking the
lowest level is what turns it back into a number.

## Honest scope

**Scope-(a)** — an inconsistency between two published claims, with the
invariant cited (writhe additivity under stabilisation).  It does **not** show
`Q = w/2` is wrong; it shows the *level* at which it is defined is not the one
`sm-lagrangian-selection-rules.md` asserts.  Nothing numerical changes.

Integer arithmetic, generic; no `Real`, no division except the displayed `Q`
(§7c).
-/

import Mathlib.Data.Int.Basic
import Mathlib.Data.List.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace QOU.StandardModel.MarkovInvariance

/-- A braid word: entry `±i` denotes `σᵢ^{±1}`.  Same convention as
`ChiralFermionBraidWords.lean`; restated here so this file stands alone. -/
abbrev BraidWord := List ℤ

/-- The writhe: the sum of the crossing signs. -/
def writhe (β : BraidWord) : ℤ := (β.map Int.sign).sum

/-- The inverse braid word: reverse the letters and invert each generator. -/
def inv (a : BraidWord) : BraidWord := (a.reverse).map (fun g => -g)

/-- Sum is additive over concatenation (proved inline; the Mathlib name is not
in the restored cache). -/
private theorem sum_append_int (a b : List ℤ) : (a ++ b).sum = a.sum + b.sum := by
  induction a with
  | nil => simp
  | cons x xs ih => rw [List.cons_append, List.sum_cons, List.sum_cons, ih]; ring

/-- Sum is reverse-invariant. -/
private theorem sum_reverse_int (a : List ℤ) : a.reverse.sum = a.sum := by
  induction a with
  | nil => rfl
  | cons x xs ih =>
      rw [List.reverse_cons, sum_append_int, ih, List.sum_cons, List.sum_cons]
      simp
      ring

/-- The writhe is additive under concatenation. -/
theorem writhe_append (a b : BraidWord) :
    writhe (a ++ b) = writhe a + writhe b := by
  unfold writhe
  rw [List.map_append, sum_append_int]

/-- Negating every letter negates the writhe. -/
theorem writhe_neg_map (a : BraidWord) :
    writhe (a.map (fun g => -g)) = - writhe a := by
  unfold writhe
  rw [List.map_map]
  induction a with
  | nil => rfl
  | cons x xs ih =>
      rw [List.map_cons, List.map_cons, List.sum_cons, List.sum_cons, ih]
      simp [Function.comp, Int.sign_neg]
      ring

/-- The writhe of the inverse word is the negation. -/
theorem writhe_inv (a : BraidWord) : writhe (inv a) = - writhe a := by
  unfold inv
  rw [writhe_neg_map]
  unfold writhe
  rw [List.map_reverse, sum_reverse_int]

/-! ### Markov I (conjugation) is safe -/

/-- **Conjugation preserves the writhe.**

The horizontal / fixed-`n` direction of the gauge groupoid leaves the writhe
alone, so `Q = w/2` and `I₃` *are* invariant under it. -/
theorem writhe_conj (γ β : BraidWord) :
    writhe (γ ++ β ++ inv γ) = writhe β := by
  rw [writhe_append, writhe_append, writhe_inv]
  ring

/-! ### Markov II (stabilisation) is not -/

/-- **Stabilisation shifts the writhe by `+1`.**

`β ↦ βσ_n` presents the *same link* but adds one positive crossing. -/
theorem writhe_stabilize (β : BraidWord) (n : ℤ) (hn : 0 < n) :
    writhe (β ++ [n]) = writhe β + 1 := by
  rw [writhe_append]
  congr 1
  unfold writhe
  simp [Int.sign_eq_one_iff_pos.mpr hn]

/-- Negative stabilisation shifts it by `-1`. -/
theorem writhe_stabilize_neg (β : BraidWord) (n : ℤ) (hn : n < 0) :
    writhe (β ++ [n]) = writhe β - 1 := by
  rw [writhe_append]
  have : writhe [n] = -1 := by
    unfold writhe
    simp [Int.sign_eq_neg_one_iff_neg.mpr hn]
  rw [this]; ring

/-- **The Coulomb charge is not stabilisation-invariant.**

`Q = w/2` shifts by `1/2` under a move that does not change the link.  So `Q`
is a function of the braid word (or of a canonical normal form), not of the
link — contrary to `sm-lagrangian-selection-rules.md`'s claim that it is
constant on gauge orbits, given that the same corpus says vertical moves are
part of the gauge freedom. -/
theorem coulombCharge_not_stabilization_invariant
    (β : BraidWord) (n : ℤ) (hn : 0 < n) :
    ((writhe (β ++ [n]) : ℚ) / 2) = ((writhe β : ℚ) / 2) + 1 / 2 := by
  rw [writhe_stabilize β n hn]
  push_cast
  ring

end QOU.StandardModel.MarkovInvariance
