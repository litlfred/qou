---
# qou-e6db
title: Formalize HOMFLY + braid closure in Lean — the sole residue of MFW (split from qou-9ttb)
status: todo
type: task
priority: normal
created_at: 2026-08-22T19:25:24Z
updated_at: 2026-08-22T19:25:24Z
---

## Why this bean exists

Split out of `qou-9ttb` (Prove/Lean the two Morton-Franks-Williams inequalities)
when that bean's **mathematical** content was completed on 2026-08-22. Opening
this separately rather than leaving it as an open residue on a bean whose
mathematics is done — owner-authorised.

## What is already DONE (do not redo)

- **Propagation** — `QOU.Knot.MFWSkeinInduction.mfw_step` and the window
  arithmetic (`switch_shift`, `smooth_shift`, `shifts_preserve_width`, the
  surjectivity lemmas). Sorry-free. Lickorish's relation rearranges to
  `P₊ = v²·P₋ + v·z·P₀`; switching moves `e ↦ e−2`, smoothing `e ↦ e−1`, so the
  MFW window propagates by pure interval arithmetic.
- **Base case** — `DescendingWrithe` (`|e| ≤ n − c` for a totally descending
  word) is **classical, not open**: a descending diagram is an unlink
  (`lickorish1997`) and Bennequin's inequality `sl ≤ −χ` (`bennequin1983`) with
  `sl = e − n` and `χ = c` for the c-component unlink gives exactly `e ≤ n − c`;
  mirroring gives the other side. Not circular — Bennequin (1983) predates
  HOMFLY (1985) and MFW (1987) and its proof is contact-geometric. Verified
  empirically at 2592 words: 0 violations, tight, and HOMFLY depends only on `c`.
- **Wiring** — `toWitness` / `braid_bound_of_window` / `descending_witness`
  connect the induction to `QOU.Knot.MortonFranksWilliams.MFWWitness`, whose
  `mfw_lower` / `mfw_upper` fields ARE window membership. All `#print axioms`
  clean (propext / Classical.choice / Quot.sound; `toWitness` none).

## What is ACTUALLY open — and it is infrastructure, not mathematics

**Neither Lean file touches a real knot.** `MortonFranksWilliams` says so
itself: *"the file asserts nothing about any actual knot."* Both files are
arithmetic over `ℤ` with the MFW bounds carried as hypotheses/fields. Nothing
can produce an `MFWWitness` from an actual link because there is no Lean
HOMFLY.

To close MFW in Lean one needs, roughly in order:

1. **Braid words + closure.** A `BraidWord n` type (`QOU/MathlibExt/BraidGroup.lean`
   exists — check what it already gives), the closure permutation, the component
   count `c`, and the exponent sum `e`.
2. **The descending predicate** and the reduction of an arbitrary word to a
   descending one by crossing changes, with a well-founded order. The corpus's
   own engine already descends such an order —
   `computations/homfly_skein_braid.py` (`first_bad` / `traverse`) — so the
   termination argument is available in executable form to port.
3. **HOMFLY itself**, as the skein-recursive invariant, plus its
   well-definedness (the hard part: invariance under Markov moves / Reidemeister
   moves).
4. **`mindeg_v` / `maxdeg_v`** and then the induction assembling `mfw_step` +
   `descending_witness` into MFW for all words.

Step 3 is the large one and is a genuine Mathlib-gap project — Mathlib has
neither HOMFLY nor the Jones polynomial. Consider whether it belongs under the
`08a2` keystone de-abstraction epic.

## Honest scoping

This is **not** a residue that a session can drain. It is a formalization
project on the scale of a Mathlib contribution. Anyone picking it up should
size it accordingly and should NOT represent partial progress as closing MFW.
The mathematics of MFW is settled classically; what is missing is Lean
infrastructure.
