---
# qou-e6db
title: Formalize HOMFLY + braid closure in Lean — the sole residue of MFW (split from qou-9ttb)
status: in-progress
type: task
priority: normal
created_at: 2026-08-22T19:25:24Z
updated_at: 2026-08-22T20:42:06Z
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


## Step 1 landed (2026-08-22) — closure permutation + component count

**The gap was real and specific.** `MFWSkeinInduction` states the window in terms
of `n`, `e`, `c`. `n` and `e` existed (`BraidKnot.BraidWord.writhe`); **`c` did
not exist anywhere in the Lean tree**, so no braid word could be connected to the
window it is supposed to satisfy. Now supplied in
`QOU/Knot/BraidClosure.lean` — sorry-free, zero linter warnings, all six results
axiom-clean (`propext` / `Classical.choice` / `Quot.sound`; `writhe_append` needs
only `propext`).

- `crossingSwap` — the transposition a crossing induces. **The sign is
  irrelevant**, which is the structural reason `c` is invariant under crossing
  changes while `e` moves; that is exactly what the skein induction needs.
- `closurePerm`, `closurePerm_nil/cons/append`
- `writhe_append` — additivity over concatenation
- `components` — orbits of `closurePerm` (nontrivial cycles + fixed points)
- `components_nil = n` — the identity braid closes to the n-component unlink

**Non-vacuity checked, not assumed.** A definition that type-checks can still
compute the wrong number, so `components` is pinned to known answers:
`components_two_one_crossing = 1` (one crossing on two strands closes to the
UNKNOT, not two circles — the smallest case where an off-by-one would hide) and
`components_two_two_crossings = 2`.

## FINDING — `BraidWord` is defined NINE times; this blocks the bean

Before adding anything I grepped, and the tree already defines `BraidWord` in
nine places across six namespaces: `PhotonThreading` (structure), four separate
`StandardModel` files (`WritheLevelParity`, `QuarkBraidChargeObstruction`,
`WritheMarkovInvariance`, `ChiralFermionBraidWords` — each `abbrev List ℤ`),
`Archimedean/NuclearGroebnerReduction` (`List ℕ`), `Archimedean/HeckeRep`
(`List (Fin (n-1) × Bool)`), `BraidKnot/BraidGroupNStrand`
(`List (BraidCrossing n)`), `BraidKnot/BraidWordBasisGram` (`List ℕ`), and
`KnotTheory` (structure). **`writhe` is defined at least five times, four of them
character-identical** (`(β.map Int.sign).sum`).

I built on `BraidKnot.BraidGroupNStrand.BraidWord` rather than adding a tenth: it
is the only one indexed by strand count AND carrying the crossing sign, which is
what MFW needs.

**This is a genuine obstacle to the bean, not a tidiness complaint.** HOMFLY must
be defined on ONE braid-word type or it cannot be connected to the MFW window,
the Markov trace (`MathlibExt/MarkovTrace` uses yet another), or the Hecke
representation. Consolidation should be scoped before step 3.

## Also checked, so it is not re-checked

`Knot/HomflySkeinReference.lean` exists but is **only the 2-strand skein value**
settling a mirror-convention dispute (bean `qou-7ue5`) — a numeric recursion
`skein : ℕ → R`, not a general HOMFLY. It does not advance steps 2-4.

## Next

Step 2 (the descending predicate + reduction to a descending word by crossing
changes, with a well-founded order). `computations/homfly_skein_braid.py`
(`first_bad` / `traverse`) already descends that order in executable form.
