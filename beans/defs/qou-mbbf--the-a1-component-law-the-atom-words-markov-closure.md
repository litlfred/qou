---
# qou-mbbf
title: 'The A+1 component law: the atom word''s Markov closure misses every census carrier, and 7db032fb48 did NOT invalidate that'
status: in-progress
pr: 8260
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T15:47:03Z
updated_at: 2026-10-04T15:14:08Z
parent: qou-v2om
---

## What was asked, and what I nearly got wrong

The question was "where is the EM-linking arc (`qou-o6ml`)". That arc closed its
route (2) on a refutation recorded in `he4-link-volume-braid-closure.witness.json`:
the Markov closure of the canonical atomic braid word gives **4** components at
A = 3, where the census-assigned binding carriers have **1** (`8_11`, for 3H) and
**3** (`L6a4` = Borromean, for 3He). The bean states it as *"refuted at the two
isotopes where the answer is checkable"*.

**That witness is dated 2026-07-04, and its import cone changed after it.** The
chain is `he4_link_volume_braid_closure` -> `canonical_braid_crossings.atom_canonical_crossings`
-> `mass_at_3A_proper.atom_braid_word_3A`, and commit `7db032fb48` (2026-09-05)
changed that word's default `intra_order` to `"borromean"`, so each nucleon's
confinement core became the alternating `(s0 s1^-1)^3`. The same change moved
`tr_M(p)` by 45 % and `tr_M(n)` by 52 % and left >= 8 committed witnesses carrying
the retired values (bean `qou-sikd`).

So the natural conclusion -- and the one I was writing -- is that the arc's closing
measurement is stale, which would reopen route (2).

## MEASURED, AND THE CONCLUSION IS THE OPPOSITE

`computations/probes/atom_closure_component_count_probe.py`, 5/5:

```
isotope   A intra_order  letters strands comps
2H        2 borromean         23       6     3
2H        2 grouped           23       6     3
3H        3 borromean         35       9     4
3H        3 grouped           35       9     4
3He       3 borromean         35       9     4
3He       3 grouped           35       9     4
4He       4 borromean         47      12     5
4He       4 grouped           47      12     5
6Li       6 borromean         71      18     7
6Li       6 grouped           71      18     7
```

The two words **are** genuinely different (asserted, so the invariance below is
not vacuous -- the `: True := trivial` shape that produced four vacuous
declarations in `QOU.MobiusEnergy`). The component count is **identical** under
both. So the refutation's load-bearing half is **NOT stale**, and re-running it
would have changed nothing.

**Why it cannot be stale**, which is the reusable half: the closure's component
count is the orbit count of the permutation the braid induces on its strands, and
**crossing sign does not enter it**. The two intra-orderings differ in sign pattern
and letter order within each nucleon's core, not in which transpositions occur. So
no re-ordering of this kind can move the count. That is a structural reason, not
an empirical coincidence over four isotopes.

## AND IT IS STRONGER THAN THE ARC BEAN STATES

Not two isotopes -- **every** A tested: the closure has exactly `A + 1` components
on `3A` strands, at A = 2, 3, 4, 6, under both orderings. A 4-component closure is
not a 1-component knot (`8_11`) and not a 3-component link (`L6a4`), and no re-run
at any word ordering makes it one. The census carriers are 1 and 3 components; the
closure is `A + 1`; the two families agree at **no** A (`A + 1 = 3` needs A = 2,
where the assigned carrier is the Hopf link and Owner Ruling A says the deuteron
binding is not a volume term anyway).

## SCOPE -- read this before citing it

**Scope (b) on the component count**, invariant cited: the orbit count of the
induced permutation is a topological invariant of the closure and is insensitive
to crossing sign. This is a structural exclusion of *this* identification, not of
knot energy, not of route (2)'s machinery, and not of the census assignment's own
correctness (`qou-5vhf` handles that separately, and independently finds it an
admitted AME-driven fit).

**NOT re-measured**: the witness's `geometric: no` and `Vol: 0` rows. `snappy` and
`spherogram` are absent in this container, so those are neither confirmed nor
denied here. The component count alone is decisive for the identification question,
which is why this probe does not need them.

**NOT claimed**: that `A + 1` is the *wrong* answer. It is wrong for the census
carriers. Whether a nucleus should close to a `A + 1`-component link at all is the
open question -- and it is the more interesting reading of this result, since the
census assignment is itself an admitted fit that the owner ruled out on 2026-09-08
(`qou-ales`). Two objects disagree and only one of them was ever derived.

## Cross-links

- `qou-o6ml` -- the arc; its route (2) closure rests on this measurement. It has
  **zero** mention of `qou-ales` or the 2026-09-08 gamma-gamma ruling, so it is
  blind to its own successor.
- `qou-sikd` -- the same `7db032fb48` change, on the trace side, where it *did*
  invalidate the recorded numbers. Same commit, opposite verdict: worth holding
  both, because "the element changed" is not by itself an answer about any
  particular quantity.
- `qou-5vhf` -- carriers are an admitted AME-driven census search.
- `qou-ales` -- the owner's replacement selection route (gamma-gamma + confinement
  SDP), now at step 10.

## 2026-09-13 (later) — THE CARRIER QUESTION IS ANSWERED BY MEASUREMENT, not left to the owner

The entry above closed with *"whether a nucleus should close to an `A + 1`-component
link at all is the open question"* and named one missing input: **is the closure
hyperbolic?** I could not get it — `snappy`/`spherogram` were absent. They
`pip install` cleanly (`snappy 3.3.2`, `spherogram 2.4.1`); the assumption that
they were unavailable was never tested.

`computations/probes/atom_closure_geometry_probe.py`, 5/5, calibrated against
`Vol(4_1) = 2.0298832128` before trusting any of its output:

**Every ATOM is non-geometric with volume exactly 0, in all SIX settings** — both
intra-orderings crossed with all three averaging modes (`averaged -> +sigma`,
`-> -sigma`, `-> drop`). 3H, 3He and 4He all return `contains degenerate
tetrahedra` on 12/12 randomised attempts.

So the 2026-07-04 witness's atom rows **reproduce exactly under the live word**,
and the option of promoting the `A + 1` closure to a binding carrier is not an
owner judgement call — it is **closed by measurement**. The closure has no
hyperbolic volume, so it cannot feed the volume-based binding route at all.
Retiring the census assignment in its favour would not re-base the binding
numbers; it would delete their input.

**What that leaves for `qou-o6ml`.** The census carrier survives as the framework's
binding input by default — but it survives as an object the owner ruled out as a
SELECTION mechanism (2026-09-08) with no derived replacement available from this
direction. That is a sharper statement of the arc's blocker than "which of two
objects is the target": there is only one candidate, and it is the fitted one.
The `A + 1` closure is not a rival; it is not a carrier at all.

## By-product: two rows of the producer's own baked table are stale

The NUCLEON rows flipped. Under the live `"borromean"` word the proton and
neutron closures are **hyperbolic in all three modes**, where the baked
`CLOSURE` dict records `geometric: False, vol 0.0` — and the producer's comment
*"Every mode gives the same non-geometric outcome"* is now false for them. It
holds under `"grouped"`, which reproduces the baked table exactly, all five rows.

🛑 The volume is **mode-dependent** (proton 9.966512 / 11.942872 / 10.215606 —
a 2x spread), so it is NOT a derived nucleon volume and must not be quoted as
one. Only the qualitative flip is mode-independent. Filed as `qou-v5sr`, not
fixed — it is a producer-output change gated by the ask-first rule, and it is
the same commit and the same open question as `qou-sikd`.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
