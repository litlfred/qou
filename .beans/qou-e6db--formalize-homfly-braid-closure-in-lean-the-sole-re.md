---
# qou-e6db
title: Formalize HOMFLY + braid closure in Lean — the sole residue of MFW (split from qou-9ttb)
status: in-progress
type: task
priority: normal
created_at: 2026-08-22T19:25:24Z
updated_at: 2026-08-22T21:26:29Z
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


## Step 2 (partial) — the skein moves, proved on actual braid words

`MFWSkeinInduction.mfw_step` takes the window shifts as *arithmetic hypotheses*:
switching moves `e ↦ e-2`, smoothing `e ↦ e-1`, both keeping `n`. Nothing proved
a braid word actually **realises** those shifts. Now proved, sorry-free, zero
warnings, axiom-clean (`writhe_smooth` needs only `propext`):

- `crossingSwap_flipSign` / `closurePerm_switch` / `components_switch` —
  **switching a crossing does not move the permutation, hence not `c`.** This is
  the structural reason the induction works: `e` slides while `c` and `n` stay
  fixed, so the window translates without changing width.
- `writhe_switch` — switching moves the writhe by exactly `2`, signed by the
  crossing's original sign.
- `closurePerm_smooth` — smoothing removes exactly that transposition from the
  permutation, which is where `c` moves.
- `writhe_smooth` — smoothing moves the writhe by exactly `1`.

**What is still missing for step 2**: that multiplying by a transposition
changes the orbit count by exactly `±1` (so smoothing moves `c` by one), plus
the descending predicate itself and the well-founded reduction. The `±1` fact is
the next concrete target and is a standard permutation-combinatorics lemma —
check Mathlib for it before proving it by hand (`#check` against the oleans; the
cache carries no `.lean` source and the LSP is down, so name-grep does not work
in this container).


## Parity layer proved (2026-08-22)

The base-case measurement behind `MFWSkeinInduction` found `|e|` and `n - c`
always sharing a parity, with the bound tight whenever they agree. That is now
**proved**, not observed, and it is the structure that makes `|e| <= n - c` a
*same-parity, smaller-magnitude* statement rather than a bare inequality:

- `sign_closurePerm` — the closure permutation's sign is `(-1)^(crossing count)`.
  Each crossing is one transposition **whatever its sign**, the same
  sign-blindness that makes `c` invariant under switching.
- `length_parity_cycleType` — read through `Equiv.Perm.sign_of_cycleType`.
- `writhe_sub_length_even` — the writhe has the parity of the crossing count.
- `writhe_parity_cycleType` — the writhe's parity is fixed by the closure
  permutation's cycle data.

All sorry-free, zero warnings, axiom-clean. 23 results in the file now.

**Deliberate weakening, stated so it is not mistaken for the full result.** The
last theorem is phrased against `cycleType.sum + cycleType.card` rather than
`n - c`. Getting to the `n - c` form needs two pieces of `ℕ`-subtraction
bookkeeping I did not do: `support.card ≤ n` (easy — `Finset.card_le_univ` plus
`Fintype.card_fin`) and `cycleType.card ≤ support.card` (each cycle has length
≥ 2 and they are disjoint; **`Equiv.Perm.card_cycleType_le_card_support` does
NOT exist in Mathlib** — checked by `#check` — so it needs proving by hand).
Without the second, `components ≤ n` is not available and `(n : ℤ) - components`
cannot be formed cleanly. That is the next concrete target.

**Still missing for step 2 overall**: that a transposition changes the orbit
count by exactly `±1` (the magnitude half — this parity work is only the parity
half), the descending predicate, and the well-founded reduction.
