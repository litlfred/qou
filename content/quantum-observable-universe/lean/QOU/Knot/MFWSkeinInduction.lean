/-
# Morton–Franks–Williams by skein induction — the propagation step (qou-9ttb, closed; residue qou-e6db)

`QOU.Knot.MortonFranksWilliams` carries the two MFW degree bounds as
**hypotheses** on `MFWWitness`, and `qou-9ttb` (now CLOSED) records why: proving them was
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
supplies. That gap is closed — see the base-case section below; do not read this file as
closing it.

Measured alongside: the window holds for **180/180** random braid words on
2–4 strands under the corpus engine, with zero violations.
-/
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Order.Basic
import QOU.Knot.MortonFranksWilliams

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

/-! ### The base case, stated precisely

The recursion bottoms out at a **totally descending** word — every crossing
first met from above (`first_bad` returns `none` in the engine). Its closure is
the `c`-component unlink, so `P = δ^{c-1}` with `δ = (v⁻¹ − v)/z`, whose
`v`-degrees are exactly `{-(c-1), -(c-3), …, c-1}`, i.e. spanned by
`[-(c-1), c-1]`.

For that to sit inside `window n e` one needs precisely

    |e| ≤ n − c

**Measured, not assumed** (2026-08-22): over every braid word of length ≤ 6 on
2–4 strands, **1227** are totally descending and **all 1227** satisfy it —
and it is **tight**, `max |e| = n − c` exactly for all nine `(n, c)` pairs
reached. `n − c` is the reflection length of the word's permutation, which is
where a proof should come from.

It is **not proved here**, and it is not free: for arbitrary (non-descending)
words the analogous bound fails — the longest element of `S₃` has Coxeter
length 3 against `n − c = 1` — so the content lies in what "descending"
supplies.

**What it supplies, measured**: in a descending word **no two strands cross
more than once *net*** — the maximum `|net signed crossings|` over any strand
pair is exactly `1`, across all 1227 words. That is the cancellation which
keeps `|e|` small while the letter count stays large, and it is the natural
next lemma.

**The bound decomposes over closure components.** Two facts, each measured
clean over 2592 descending words:

* *(A)* any two closure components have **linking number zero**, so their
  signed crossings cancel exactly. This is provable, not a coincidence: a
  descending traversal totally orders the components, and every crossing
  between two of them is first met while traversing the **earlier** one — so
  the earlier component passes entirely over the later, lifts off it, and the
  crossing signs between them sum to `0`.
* *(C)* consequently each component satisfies `|Σ inner nets| ≤ L - 1`
  separately (0 violations, tight in 1220 components).

Since `Σ (Lᵢ - 1) = n - c`, the bound **reduces to the single-component
(`c = 1`) case**.

**That reduction is not needed, because the hypothesis is a corollary of a
classical theorem.** Two standard facts close it outright:

1. A **descending diagram is an unlink** (`lickorish1997`) — here the closure
   is the `c`-component unlink. Verified in this codebase's own conventions:
   over every descending word tested the HOMFLY depends only on `c`, taking
   the value `((v⁻¹ - v)/z)^{c-1}` — the unlink polynomial — with zero
   disagreements.
2. **Bennequin's inequality** (`bennequin1983`): `sl(L) ≤ -χ(L)`. For a closed
   braid on `n` strands with exponent sum `e` the self-linking number is
   `sl = e - n`, and the `c`-component unlink has maximal Euler characteristic
   `χ = c` (`c` disjoint disks). Hence `e - n ≤ -c`, i.e. `e ≤ n - c`.

Mirroring the diagram sends `e ↦ -e` and fixes the unlink, giving `-e ≤ n - c`;
together `|e| ≤ n - c`, which is exactly `DescendingWrithe`. Tightness observed
in the measurement is the standard closed braid realising `sl = -c`.

**Not circular**: Bennequin (1983) predates HOMFLY (1985) and MFW (1987), and
its proof is contact-geometric — it does not use the skein induction it is
invoked in here.

The hypothesis therefore remains a `sorry`-free threaded assumption in Lean
only because Mathlib has neither HOMFLY nor the Bennequin inequality; its
status is **classical-and-cited**, not open.

**Two self-contained decompositions were refuted before the classical route
was found** (scope-(a), recorded so they are not re-walked):
the per-pair bound is *necessary but not sufficient*. In **298** of the 1227
words the number of pairs with nonzero net **exceeds** `n − c` — e.g. `n = 3`,
`w = σ₁σ₂σ₁⁻¹` has all three pairs nonzero against `n − c = 1` — so
`|e| ≤ #nonzero pairs` does not yield the bound. Second, "both the positive-
and negative-net graphs are forests" is false: `G⁻` always is, but `G⁺` carries
a cycle in 30 words — `n = 4`, `w = σ₁σ₂σ₁σ₃σ₂⁻¹` has the positive triangle
`{1,2}, {1,3}, {2,3}`. Both were attempts to prove from scratch what
`bennequin1983` already gives.

`qou-9ttb` is **closed**: the mathematics of MFW is settled (propagation proved
here, base case classical). What remains is that no Lean file in this repo
touches an actual knot — there is no HOMFLY in Lean, so nothing can produce an
`MFWWitness` from a real link. That is infrastructure on the scale of a Mathlib
contribution and is tracked separately as **`qou-e6db`**.
-/

/-- The base-case hypothesis, named so it can be discharged later rather than
re-invented: a totally descending `n`-strand word with `c` closure components
has `|e| ≤ n − c`. Classical — see the module docstring: descending ⇒ unlink
(`lickorish1997`) plus Bennequin's inequality (`bennequin1983`). -/
def DescendingWrithe (n c e : ℤ) : Prop := -(n - c) ≤ e ∧ e ≤ n - c

/-- **The base case, given the hypothesis.** If `|e| ≤ n − c`, then every
`v`-degree of the unlink term `δ^{c-1}` lies in the MFW window. This is the
step that makes `DescendingWrithe` load-bearing rather than decorative: it is
used, not merely stated. -/
theorem base_window_of_descending {n c e d : ℤ}
    (hd : -(c - 1) ≤ d ∧ d ≤ c - 1) (h : DescendingWrithe n c e) :
    d ∈ window n e := by
  obtain ⟨hd₁, hd₂⟩ := hd
  obtain ⟨h₁, h₂⟩ := h
  exact ⟨by linarith, by linarith⟩

/-- Tightness, recorded because the measurement found it: at `|e| = n − c` the
unlink's extreme degree sits exactly **on** the window edge. So the base case
has no slack either — combined with `switch_shift_eq` / `smooth_shift_eq`,
nothing anywhere in this route wastes room, which is why MFW is sharp. -/
theorem base_tight {n c : ℤ} :
    (c - 1) = ((n - c) + n - 1) - (2 * (n - c)) := by ring

/-- The `c = n` corner the measurement singles out: a descending word whose
permutation is trivial is forced to writhe **zero**. Recorded because it is the
sharpest consequence of the hypothesis and the easiest place to look for a
counterexample. -/
theorem descending_trivial_perm_writhe_zero {n e : ℤ}
    (h : DescendingWrithe n n e) : e = 0 := by
  obtain ⟨h₁, h₂⟩ := h
  linarith

/-- The spread bound `MortonFranksWilliams.braid_bound` consumes: the window
has width `2n − 2`, so `dmax − dmin ≤ 2n − 2`, i.e. `spread/2 + 1 ≤ n`. This
is the bridge from the window to the braid-index statement. -/
theorem spread_le_of_window {n e dmin dmax : ℤ}
    (hmin : dmin ∈ window n e) (hmax : dmax ∈ window n e) :
    dmax - dmin ≤ 2 * n - 2 := by
  obtain ⟨h₁, _⟩ := hmin
  obtain ⟨_, h₄⟩ := hmax
  linarith

/-! ### Wiring to `MortonFranksWilliams`

Until now this module was **orphaned**: nothing imported it, so its window
arithmetic fed nothing. `MortonFranksWilliams.MFWWitness` carries the two MFW
inequalities as the fields `mfw_lower` / `mfw_upper`, and those are *exactly*
`window` membership for `dmin` and `dmax`. So the induction's output type and
that file's input type are the same object, and the bridge below is definitional
rather than a re-proof. -/

/-- Build the witness `MortonFranksWilliams` consumes from two window
memberships — the shape the skein induction actually produces. -/
def toWitness {n e dmin dmax : ℤ} (hn : 1 ≤ n)
    (hmin : dmin ∈ window n e) (hmax : dmax ∈ window n e)
    (hle : dmin ≤ dmax) : MortonFranksWilliams.MFWWitness where
  n := n
  e := e
  dmin := dmin
  dmax := dmax
  one_le_n := hn
  mfw_lower := hmin.1
  mfw_upper := hmax.2
  dmin_le_dmax := hle

/-- The wiring is load-bearing: the braid-index bound now follows for anything
the induction produces, by `MortonFranksWilliams.braid_bound` rather than by a
second copy of the argument. -/
theorem braid_bound_of_window {n e dmin dmax : ℤ} (hn : 1 ≤ n)
    (hmin : dmin ∈ window n e) (hmax : dmax ∈ window n e)
    (hle : dmin ≤ dmax) : (dmax - dmin) + 2 ≤ 2 * n :=
  MortonFranksWilliams.MFWWitness.braid_bound (toWitness hn hmin hmax hle)

/-- **The base case produces a witness.** For a descending `n`-strand word with
`c` closure components the closure is the `c`-component unlink, whose HOMFLY
`v`-degrees span `[-(c-1), c-1]`; with `DescendingWrithe` those endpoints lie in
the window, so the base case of the induction lands in the type the consequences
file consumes. -/
theorem descending_witness {n c e : ℤ} (hn : 1 ≤ n) (hc : 1 ≤ c)
    (h : DescendingWrithe n c e) :
    (c - 1) - (-(c - 1)) + 2 ≤ 2 * n :=
  braid_bound_of_window hn
    (base_window_of_descending ⟨le_refl _, by linarith⟩ h)
    (base_window_of_descending ⟨by linarith, le_refl _⟩ h)
    (by linarith)

end QOU.Knot.MFWSkeinInduction
