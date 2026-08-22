---
# qou-9ttb
title: 'PROVE(lean): the two Morton-Franks-Williams inequalities — currently hypotheses on MFWWitness'
status: todo
type: task
priority: normal
created_at: 2026-08-22T02:02:43Z
updated_at: 2026-08-22T02:03:17Z
---

## What is open

`QOU.Knot.MortonFranksWilliams` (PR #5380, bean `qou-dr8m`) carries the two
MFW degree bounds as **hypotheses** on the `MFWWitness` structure:

    mfw_lower : dmin >= e - n + 1
    mfw_upper : dmax <= e + n - 1

Everything downstream of them is derived and sorry-free — `braid_bound`,
`spread_le_two_mul_sub_two`, `selfLinking_le`, `no_representative_of_spread_gt`,
and the two measured instances (`sixOne`, `torusFourFive`). What is NOT proved
is the pair itself.

This is §3b-cond used honestly: the class carries the *inputs* and the theorems
*derive* the conclusions. It is deliberately not a class carrying
`braid index >= ...` as a field. But the inequalities remain assumed.

## Why it is research-scale

Morton's proof needs two ingredients:

1. **Markov invariance of the Ocneanu trace** — that the trace is unchanged by
   stabilization, so the HOMFLY of a closure is a link invariant rather than a
   braid-word invariant.
2. **A degree argument** on the Hecke-algebra representation bounding the
   `v`-degree window by the writhe and strand count.

## Dependency — do NOT duplicate

Ingredient 1 overlaps bean `qou-bhrx` (**in-progress**, F4-opt1: abstract
Ocneanu cyclic-trace lemma on MarkovStabilization). That bean already delivered
`QOU.Machinery.BilinearTraceCyclicity` (sorry-free, all-n) reducing cyclicity to
Gram symmetry, and names the remaining open keystone as the Ocneanu word-length
induction OR the Wedderburn decomposition `tr_M = sum_lambda w_lambda chi_lambda`.

Whoever picks this up should build ON qou-bhrx rather than re-deriving the trace
machinery. Ingredient 2 (the degree argument) appears to be genuinely
independent of it and is the part with no in-corpus precedent I could find.

## Corpus-grep done (2026-08-22)

- `.beans/` for morton / franks / ocneanu / markov-invariance -> **5 files
  matched**, assessed as follows (corrected 2026-08-22; an earlier version of
  this bean said "only qou-bhrx and qou-dr8m", which overstated what had
  actually been checked):
  - `qou-bhrx` — **relevant**, ingredient 1, in-progress. See above.
  - `qou-dr8m` — mine, completed; the *derivation* consuming these as
    hypotheses, not a proof of them.
  - `qou-qb8e`, `46ke`, `qou-b3nk` — matched on the string **"Ocneanu" only**,
    not on Morton / Franks / Markov-invariance. They concern other uses of the
    trace (hh1 carrier magnitude; canonical-watcher CODATA literals; the
    qbeta trace-convention registry). Not MFW; no overlap.
- No `PROVE` bean for the inequalities themselves existed.
- `grep -rli "morton-franks\|morton_franks" content/ computations/ docs/` -> only
  files this PR adds or edits. In particular `computations/homflypt_engine.py`
  matches **only** on a comment added by this PR; `origin/main`'s copy has zero
  mentions of Morton / Franks / braid index. So there was no pre-existing MFW
  machinery in the corpus, which is what #5380's "neither existing source can
  supply a v-degree" rests on.

## Possibly-related downstream consumers

Two open beans want braid-index data and may be served by the producer
`computations/homfly_braid_index_mfw.py` that #5380 adds — worth checking
before either is worked, though neither is blocked on *proving* MFW:

- "production hygiene: add the m <= p (braid index) guard to
  rosso_jones_three_strand_delta_q and alpha_k_per_force_assembly"
- "compute: name the braid index in the isotope writhe comparisons"

Note `computations/knot_braid_database.py` carries 3-strand knots only, which is
why `6_1` had no in-repo braid index before #5380.

## Scope note

Nothing is blocked on this. The braid indices derived in #5380 are correct as
computed facts; MFW is a cited theorem there, exactly as a textbook result would
be. This bean exists so the assumption is visible and attributable rather than
silently inherited.
