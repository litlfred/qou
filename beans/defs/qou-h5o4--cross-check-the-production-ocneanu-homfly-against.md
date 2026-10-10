---
# qou-h5o4
title: Cross-check the production Ocneanu HOMFLY against the exact two-variable skein engine
status: completed
type: task
priority: normal
created_at: 2026-08-28T15:50:41Z
updated_at: 2026-08-28T18:10:44Z
---

## Done

`computations/test_homfly_skein_vs_ocneanu_su2.py`. The production engine
`homfly_ocneanu_trace.homfly_signed_su2` was validated only against the
2-strand torus family plus the figure-eight (its own `_spanning_set` /
`_holdout_set`). The exact two-variable engine `homfly_skein_braid.homfly` is
defined on arbitrary words. Nothing compared them -- the same omission that
produced `qou-7ue5`.

**Specialisation**: `s = sqrt(q0)`, `v = a = s^2`, `z = s - 1/s`.
`P(v,z)` at that point == `homfly_signed_su2(..., framed=False)`.

**Result: 17 words agree, worst |delta| = 5.554e-40** at 70 dps working
precision (mpmath end to end, so that tracks the arithmetic, not a float64
floor). Coverage now includes 3-, 4- and 5-strand mixed-sign words and the
`6_1` word from `qou-dr8m` -- the region the engine is used in and its own
validation never reached.

Parts: A specialisation agreement; B the engine's own framing relation
`unframed = a^w * framed` (exact, 0.0 -- pins the writhe convention that
`framed=True` production ships); C1 the Lean-proved mirror `(v,z) -> (v^-1,
-z)` on braid words, with the naive `v -> v^-1` shown to fail on 4 of them;
C2 chirality survives the specialisation (13 chiral separate by >= 0.0138,
4 amphichiral agree exactly).

**Teeth verified**: Part A fails on 14/17 words under `framed=True`.

## One thing surfaced, and it is a sharpening not a discovery

The proton word `(s1 s2^-1)^3` and neutron word `(s1^-1 s2)^3` are mirrors,
and their closure (Borromean rings) is amphichiral, so their two-variable
HOMFLY are **the same polynomial** -- not merely equal at the SU(2) point.

The corpus already knows the coarse version:
`computations/_deprecated/schur_weyl_q_hecke.py` was deprecated with the note
that it works from cycle type and "cannot distinguish proton from neutron",
and the answer is the colour weighting (`bring_color_weighted`, canonical per
the 2026-08-15 ruling R3). What is sharpened is the *level*: not an artifact
of a coarse invariant, and not the specialisation losing information.

Scope-(a): HOMFLY alone does not separate these two closures. NOT a claim
that no braid-level invariant can -- the writhe does in general, and the
colour weighting is exactly a structure HOMFLY cannot see.

## Two duds caught by screening rather than assumed

- My first 5-strand word `[1,2,-3,4,1,-2,3,-4]` is **the unknot** (P = 1). A
  word that looks complicated is not necessarily a test. Replaced with
  `[1,1,2,3,3,4,-2,4]` (14 terms, v-spread 8, chiral).
- C1's naive-inversion guard bit on only 1 of 14 words, because knots have
  only even z-degrees; odd ones need multi-component links (parity c-1).
  Added Hopf+/Hopf-/(2,4) torus link, and the assertion now demands >= 3.



## Merged

PR #5898, rebase-merged to main 2026-08-28 as 115e860ea. Three commits land
as a linear sequence per AGENTS.md rule 8.

Re-verified on the post-rebase head (68936891c) before merging — the earlier
run predated a 12-commit rebase onto main, so the checklist would otherwise
have described a different tree than the one merged. All three green on the
actual merge head: cross-check PASS (17 words, worst 5.554e-40), y_lambda
gate PASS with identical numbers, import-time-dps ratchet 0 findings.
