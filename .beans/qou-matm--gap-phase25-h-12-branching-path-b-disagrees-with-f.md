---
# qou-matm
title: 'GAP: phase25 H_12 branching Path B disagrees with F1 at O(1) on every dim>1 irrep'
status: todo
type: task
created_at: 2026-08-26T16:03:20Z
updated_at: 2026-08-26T16:03:20Z
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
