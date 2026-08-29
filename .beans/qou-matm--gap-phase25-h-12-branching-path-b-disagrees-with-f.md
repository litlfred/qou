---
# qou-matm
title: 'GAP: phase25 H_12 branching Path B disagrees with F1 at O(1) on every dim>1 irrep'
status: completed
type: task
priority: normal
created_at: 2026-08-26T16:03:20Z
updated_at: 2026-08-26T16:41:00Z
---

`sublemma_2_1_h12_he4_phase25.py` verifies the H_12 ⁴He character two ways:
Path A = F1's cached `chi_lambda` per λ ⊢ 12; Path B = iterated Sub-lemma 2.1
branching `H_12 ↓ H_9 × H_3` with Halley-refined H_3 Wedderburn projectors
(`path_b_chi_h12` in `sublemma_2_1_h12_he4_branching.py`).

Until 3d38dab07 this comparison never ran: F1's witness was re-schema'd at
#4619 and the loader read the pre-#4619 field through a `.get(..., [])`, so it
silently got an empty Path A and asserted `0 == 0`. With the loader fixed, the
first real measurement is:

| λ                  | dim | rel residual |
|--------------------|-----|--------------|
| (12,)              | 1   | 7.15e-05     |
| (11,1)             | 11  | 1.20e+00     |
| (10,2)             | 54  | 9.48e-01     |
| (10,1,1)           | 55  | 1.75e+00     |
| (3,1^9)            | 55  | 1.20e+00     |
| (2,2,1^8)          | 54  | 9.69e-01     |
| (2,1^10)           | 11  | 1.09e+00     |
| (1^12)             | 1   | 7.15e-05     |

0 of 8, six of them O(1).

The dimension split is the whole signal: the only two that agree are the two
ONE-DIMENSIONAL representations, where the character is a product of scalars
and there is no branching decomposition to get wrong. Path B is correct exactly
where it is trivial and wrong on every λ with dim > 1.

That points at the branching reconstruction rather than at the cache. Two
things have been ruled out already:

- **Not the field rename.** `chi_lambda` (live) vs `chi_q_at_q0` (the
  `_deprecated` copy) agree on all 77 partitions to ~1e-4, which is the 8-sig-fig
  serialization of the live witness. Same quantity.
- **Not float64.** The failures are O(1). The producer's whole compute cone is
  numpy complex128 and cannot resolve below ~1e-16, but nothing at this scale is
  an arithmetic artifact.

NOT yet established, and each would change the fix:

- whether `path_b_chi_h12`'s η-restriction grouping (`syt_restriction_shape` at
  9) is selecting the right SYT classes;
- whether `_LR_TABLE_9_3` carries the right Littlewood–Richardson coefficients
  for the (η, ν, λ) triples in play;
- whether the H_3 sub-action `H3_GROUP_AT_H12` is indexed against the right
  strands (10..12) for the generator numbering `beta_full` uses;
- whether the 7.15e-5 on the 1-dim reps is itself meaningful. It is suspiciously
  close to the ~7e-5 by which F1's own value MOVED between the `_deprecated` and
  live witnesses, which would make it a Path-A staleness rather than a Path-B
  error. Not bisected.

Cheapest next step: run one dim>1 λ — (11,1) is the smallest at dim 11 — and
compare `path_b_chi_h12`'s per-(η,ν) partial sums against a direct H_12
seminormal character, to see whether the discrepancy is one bad LR coefficient
or a wholesale misgrouping.

Related but separate: draining this producer's remaining 32 raw float64 witness
fields (the per-λ character dicts) requires moving `path_b_chi_h12` off numpy
complex128, which is why its witness stays uncommitted (`qou-poi1`).


## Re-measured 2026-08-26 post-#5824 — the finding SPLITS, and survives

Main now carries #5824's p-n convention flip
(`GRAM_PN_CONVENTION -> BringColorWeighted`), which changes
`he4_braid_canonical`'s I_pn offset via `pn_interface_offset_from_h`. Re-ran
phase25 against it with no change to `path_b_chi_h12`:

| λ | dim | pre-flip | post-flip |
|---|---|---|---|
| (12,) | 1 | 7.15e-05 | **1.25e-08** |
| (11,1) | 11 | 1.20e+00 | 1.20e+00 |
| (10,2) | 54 | 9.48e-01 | 9.48e-01 |
| (10,1,1) | 55 | 1.75e+00 | 1.75e+00 |
| (3,1^9) | 55 | 1.20e+00 | 1.20e+00 |
| (2,2,1^8) | 54 | 9.69e-01 | 9.69e-01 |
| (2,1^10) | 11 | 1.09e+00 | 1.09e+00 |
| (1^12) | 1 | 7.15e-05 | **1.07e-08** |

**The 1-dim rows moved by 5700×; the six dim>1 rows did not move at all,** to
every digit displayed. So there were two independent effects and the flip
removed exactly one:

1. The 7.15e-5 on the one-dimensional irreps **was the p-n convention.** Gone.
2. The O(1) disagreement on every dim>1 irrep is **untouched by it** and is
   structural in `path_b_chi_h12`. That is this bean, and it is now cleaner —
   one confound removed, and the dimension split it rests on is sharper than
   before, not weaker.

### Two corrections, both to claims made above

- **The residual 1.2e-8 is NOT a discrepancy.** F1 stores `chi_lambda` to 8
  significant figures — `2.41983670e+00` vs `2.41983673e+00` is the whole of
  it. Those two irreps now agree to the limit of what the upstream records. The
  producer's `rel < 1e-9` pass threshold is **unmeetable against an 8-sig-fig
  cache** no matter what the mathematics does, so the two 1-dim rows will read
  ✗ forever until either the threshold or F1's serialization changes. Anyone
  reading "0/8" should read it as "0 of 8, of which 2 are a serialization
  floor and 6 are real".
- **The Path-A-staleness speculation is REFUTED.** This bean suggested the
  7.15e-5 might be Path-A staleness, on the grounds that F1's own value moved
  by ~7e-5 between its `_deprecated` and live witnesses — a coincidence of
  magnitude. It was the convention. The two ~7e-5 quantities were unrelated.
  The speculation was labelled not-bisected, which is the only reason it did
  not become a wrong finding.

### What this does to the next step

The cheapest-probe recommendation is unchanged and now better targeted: run
(11,1), dim 11, and compare `path_b_chi_h12`'s per-(η,ν) partial sums against a
direct H_12 seminormal character. Nothing about the p-n interface is in play any
more, so a discrepancy there is the η-restriction grouping, `_LR_TABLE_9_3`, or
the `H3_GROUP_AT_H12` strand indexing — the three candidates listed above, with
the fourth (Path-A staleness) now eliminated.


## RETRACTED 2026-08-26 — `path_b_chi_h12` is exact; this was two different braid words

This bean's premise was wrong, and the dimension split I built it on has a much
simpler cause. Superseded by **`qou-oppb`**.

Diagnostic:
[`computations/probes/he4_canonical_braid_word_disagreement_probe.py`](../computations/probes/he4_canonical_braid_word_disagreement_probe.py).

**1. The branching is complete.** For all 8 targets,
`dim λ == Σ_{η,ν} c^λ_{η,ν}·d_η·d_ν` exactly; every η-class size equals the sum
of its ranks; no SYT skipped. `_LR_TABLE_9_3` and `syt_restriction_shape` are
correct — two of the four candidate causes listed above, eliminated.

**2. Path B is exact.** For (11,1): the H_3 Wedderburn projectors are idempotent
to 2e-16, of exactly the expected rank, mutually orthogonal, and sum to the
identity on each η-class. Path B reproduces `tr(ρ_λ(β))` with defect **0.0** —
not small, zero. The third candidate (`H3_GROUP_AT_H12` strand indexing) is
eliminated with them.

**3. The two paths run on different words.** Path A is F1's cached value, and
F1's parameters record `atom_braid_word_3A(2, 2)`; Path B runs on
`he4_braid_canonical()`. They differ in 36 of 47 positions while carrying the
identical multiset of letters (5.0e-17 apart) and of generators.

So the dimension split is commutativity, not a defect: 1-dim characters are
products of scalars and are order-independent; dim>1 are matrix products and are
not. Every one of my four candidate causes is eliminated, including the fourth
(Path-A staleness), which the p-n flip had already refuted.

**phase25 was never measuring what it reported.** It compares the characters of
two different braid words and calls the difference a verification failure. Its
0/8 is real as an observation and meaningless as a verdict on the branching
machinery.

### Correction to the post-#5824 note above

That note said "the O(1) disagreement is an unrelated structural defect in
`path_b_chi_h12`" and called the finding "cleaner, one confound removed". The
first half is now retracted — there is no defect in `path_b_chi_h12`. The second
half stands and was in fact the useful part: removing the p-n confound is what
left a residual clean enough to chase to the actual cause.

### What remains open

Not this. `qou-oppb`: which of the two canonical-⁴He constructions is intended,
and collapsing them to one so the question cannot recur. Also `qou-b4xn`, whose
subject is `atom_braid_word_3A` and which may bear on the same choice.

Leaving this bean open would keep pointing agents at `path_b_chi_h12`, which is
correct.
