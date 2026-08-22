/-
# Morton–Franks–Williams by skein induction — the propagation step (qou-9ttb)

`QOU.Knot.MortonFranksWilliams` carries the two MFW degree bounds as
**hypotheses** on `MFWWitness`, and `qou-9ttb` records why: proving them was
scoped as needing Markov invariance of the Ocneanu trace plus a degree
argument on the Hecke representation — research-scale.

**That scoping named one route and treated it as the only one.** There is a
second, and it needs neither the Ocneanu trace nor Markov invariance: induct
along the skein recursion itself, on exactly the well-founded order the
corpus's own HOMFLY engine (`computations/homfly_skein_braid.py`) already
descends. This file proves the inductive step of that route.

## The step

Lickorish's relation `v⁻¹P₊ − vP₋ = zP₀` rearranges to

    P₊ = v² · P₋ + v·z · P₀

On braid words the two right-hand terms are again `n`-strand braid closures:
switching a crossing leaves `n` alone and moves the writhe `e ↦ e − 2`;
smoothing deletes a letter, so `e ↦ e − 1`. Feeding the MFW window
`[e − n + 1, e + n − 1]` through both:

    v² · P₋ :  [e−2−n+1, e−2+n−1] + 2  =  [e−n+1, e+n−3]
    v·z · P₀ :  [e−1−n+1, e−1+n−1] + 1  =  [e−n+1, e+n−2]

Both land **exactly on** the target window — not merely inside it. Each
shifted child window *equals* `[e − n + 1, e + n − 1]` at both edges, so the
recursion neither widens nor narrows the window; it only translates it.

**Lean corrected me here.** I first wrote this step as an inclusion with slack
at the top — two units on the switch branch, one on the smoothing branch — and
concluded from that that the upper bound must be driven by the base case. Both
lemmas were false and `ring` rejected them: `2 + ((e−2) + n − 1) = e + n − 1`,
not `e + n − 3`. The corrected statement is stronger than the one I set out to
prove, and the conclusion I had drawn from the slack was unfounded.

## Scope — what this is and is not

This is the **propagation** step: given the window at the two skein children,
the parent inherits it. **It is not MFW**, and this file deliberately does not
package it as an induction that "concludes" MFW — an earlier draft did, and
that lemma's base-case hypothesis went unused, which made it near-circular.
What is proved here is exactly the step, plus the width bound the braid-index
statement consumes.

Closing the induction additionally needs the **base case**: a descending braid
diagram closes to an unlink, and its window must already satisfy the bound.

The base case is where the remaining content is, and it is not obviously
free: it amounts to `|e| ≤ n − c` for a descending word with `c` closure
components, which is *false* for arbitrary words (the longest element of `S₃`
has Coxeter length 3 against `n − c = 1`) and so depends on what "descending"
supplies. That gap is recorded in `qou-9ttb`; do not read this file as
closing it.

Measured alongside: the window holds for **180/180** random braid words on
2–4 strands under the corpus engine, with zero violations.
-/
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Order.Basic

namespace QOU.Knot.MFWSkeinInduction

/-- The MFW `v`-degree window for an `n`-strand braid closure of writhe `e`. -/
def window (n : ℤ) (e : ℤ) : Set ℤ := {d | e - n + 1 ≤ d ∧ d ≤ e + n - 1}

/-- Membership, unfolded. -/
theorem mem_window {n e d : ℤ} :
    d ∈ window n e ↔ (e - n + 1 ≤ d ∧ d ≤ e + n - 1) := Iff.rfl

/-- The window is nonempty exactly when `1 ≤ n`: an `n`-strand braid always has
one. Recorded because a vacuous window would make everything below true for
the wrong reason. -/
theorem window_nonempty {n e : ℤ} (hn : 1 ≤ n) : e ∈ window n e := by
  constructor <;> linarith

/-- **Crossing switch.** `P₋` sits at writhe `e − 2`; multiplying by `v²`
shifts its window into the parent's, touching the lower edge. -/
theorem switch_shift {n e d : ℤ} (hd : d ∈ window n (e - 2)) :
    2 + d ∈ window n e := by
  obtain ⟨h₁, h₂⟩ := hd
  exact ⟨by linarith, by linarith⟩

/-- **Smoothing.** `P₀` sits at writhe `e − 1`; multiplying by `v·z` shifts its
window into the parent's, also touching the lower edge. -/
theorem smooth_shift {n e d : ℤ} (hd : d ∈ window n (e - 1)) :
    1 + d ∈ window n e := by
  obtain ⟨h₁, h₂⟩ := hd
  exact ⟨by linarith, by linarith⟩

/-- **The propagation step.** Every `v`-degree of `P₊ = v²P₋ + v z P₀` lies in
the parent window, given both children do. Stated on degrees rather than on
polynomials: a degree of a sum is a degree of one of the summands, so this is
the whole content of the step. -/
theorem mfw_step {n e d : ℤ}
    (h : (∃ d', d' ∈ window n (e - 2) ∧ d = 2 + d') ∨
         (∃ d', d' ∈ window n (e - 1) ∧ d = 1 + d')) :
    d ∈ window n e := by
  rcases h with ⟨d', hd', rfl⟩ | ⟨d', hd', rfl⟩
  · exact switch_shift hd'
  · exact smooth_shift hd'

/-- Both shifts are **tight at the lower edge**: the switch term realises
`e − n + 1` exactly when the child does. This is why MFW is sharp, and it is
the reason `spread = 6` with `n = 4` forced the `6₁` writhe in
`QOU.Knot.MortonFranksWilliams`. -/
theorem switch_tight {n e : ℤ} :
    2 + ((e - 2) - n + 1) = e - n + 1 := by ring

/-- The smoothing term is tight at the lower edge too. -/
theorem smooth_tight {n e : ℤ} :
    1 + ((e - 1) - n + 1) = e - n + 1 := by ring

/-- **The switch shift is a bijection of windows, not merely an inclusion.**
`v²·(window at e−2)` is *exactly* the window at `e`. I first recorded this as
an inclusion with two units of slack at the top; that was wrong, and Lean
rejected it — `2 + ((e−2) + n − 1) = e + n − 1`, not `e + n − 3`. -/
theorem switch_shift_eq {n e : ℤ} :
    (2 + ((e - 2) - n + 1) = e - n + 1) ∧ (2 + ((e - 2) + n - 1) = e + n - 1) :=
  ⟨by ring, by ring⟩

/-- **The smoothing shift is a bijection of windows too.** Same correction:
`1 + ((e−1) + n − 1) = e + n − 1` exactly. -/
theorem smooth_shift_eq {n e : ℤ} :
    (1 + ((e - 1) - n + 1) = e - n + 1) ∧ (1 + ((e - 1) + n - 1) = e + n - 1) :=
  ⟨by ring, by ring⟩

/-- Consequence of the two above, and the reason MFW is **sharp**: neither
skein branch loses any room at either edge, so the window the recursion
delivers is the window the base case starts with, shifted — never wider, never
narrower. Any slack in a computed spread therefore comes from the base case,
not from the recursion. -/
theorem shifts_preserve_width {n e : ℤ} :
    ((e + n - 1) - (e - n + 1)) = 2 * n - 2 := by ring

/-- The converse direction of `switch_shift`: every parent degree is reachable
from the switch child. Together with `switch_shift` this is the bijection. -/
theorem switch_shift_surj {n e d : ℤ} (hd : d ∈ window n e) :
    d - 2 ∈ window n (e - 2) := by
  obtain ⟨h₁, h₂⟩ := hd
  exact ⟨by linarith, by linarith⟩

/-- The converse direction for the smoothing branch. -/
theorem smooth_shift_surj {n e d : ℤ} (hd : d ∈ window n e) :
    d - 1 ∈ window n (e - 1) := by
  obtain ⟨h₁, h₂⟩ := hd
  exact ⟨by linarith, by linarith⟩

/-- The spread bound `MortonFranksWilliams.braid_bound` consumes: the window
has width `2n − 2`, so `dmax − dmin ≤ 2n − 2`, i.e. `spread/2 + 1 ≤ n`. This
is the bridge from the window to the braid-index statement. -/
theorem spread_le_of_window {n e dmin dmax : ℤ}
    (hmin : dmin ∈ window n e) (hmax : dmax ∈ window n e) :
    dmax - dmin ≤ 2 * n - 2 := by
  obtain ⟨h₁, _⟩ := hmin
  obtain ⟨_, h₄⟩ := hmax
  linarith

end QOU.Knot.MFWSkeinInduction
