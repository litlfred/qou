---
# qou-lr57
title: block_swap_binding's June value is explained — and June's y_lambda table violated the two-row cap by 7%
status: in-progress
pr: 8260
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-27T06:21:30Z
updated_at: 2026-10-04T15:16:43Z
parent: qou-v2om
---

## Answered: the 3.3x is the y_lambda table, and June's table VIOLATED the two-row cap

PR #5867 refreshed `block-swap-binding.witness.json` and said plainly that
the 3.3x-17x move was **unexplained** — not the pin, not the y_lambda
table choice (18 ppb), not the engine swap (1e-50), not the prune (exact
0.0). It is now explained, and reproduced.

## Reproduction

The committed 2026-06-22 value is recovered to **7 significant figures**
by using June's y_lambda table with June's code path:

    committed 2026-06-22            0.885616920128525
    June y_lambda + GP, all 77      0.885616401506468    ratio 0.99999941
    June y_lambda + GP, 7 two-row   0.823184070441132    ratio 0.92950355
    TODAY (D table, 7 two-row)      2.899590021358060    ratio 3.2740

The June table is the pre-`acfc4fb2b8` version;
`acfc4fb2b8` (2026-06-30, "regenerate y-lambda-mpfr-witness at muon q0")
landed **eight days after** the witness was computed.

## The finding that matters more than the provenance

**Under June's weights the two-row cap did not hold.**

    June-15   >2-row max|y| = 1.98e-4    two-row min|y| = 8.77e-5   ratio 2.26
    today     >2-row max|y| = 1.03e-73   two-row min|y| = 2.29e-4   ratio 4.5e-70

In June the shapes with `ell(lambda) > 2` were the SAME ORDER as the
two-row ones — larger than the smallest surviving weight — and they
carried **7.05 % of tr_M** (0.8856 vs 0.8232). Today they are ~1e-73 and
the restriction is exact to 0.0.

Convention D (Wenzl level r = 2) proves those weights are exactly zero:
`QOU.MassTheory.TwoRowCapDerived.massWeight_eq_zero_of_three_rows_of_wenzl`,
sorry-free. So June's table was **not** convention-D compliant, and any
June-era result that summed it is a pre-migration object.

## What this means for the two numbers

Neither value is "wrong" in its own frame:

  * `-0.3579` (June) is correct for the pre-migration weight family.
  * `-0.4306` (today) is correct under convention D, which the
    2026-08-15 owner ruling makes canonical.

So the refresh in #5867 was right, and for a better reason than the one
given there — not merely "the code is correct today" but "the June value
belongs to a weight family the corpus has since replaced, and which
provably violates a cap now proved in Lean".

## The cheap check nobody had

A y_lambda table can be tested against the cap in one line, without any
producer, any word, or any anchor:

    max(|y| for ell(lambda) > 2)  vs  min(|y| for ell(lambda) <= 2)

Convention D forces that ratio to ~1e-70. June's table gave **2.26**.
A table whose >2-row weights are the same order as its two-row weights is
not a D-frame table, whatever it is labelled. Worth wiring as a gate —
it is O(number of partitions) and needs nothing but the table.

## Method note

The history was only reachable with `git log --full-history`. Plain
`git log -- <path>` reported **4 commits, oldest a merge dated
2026-08-25** — merge simplification following one parent — which reads
exactly like a shallow-clone boundary and would have ended the
investigation with "the history isn't in this clone". It is (25538
commits back to 2026-03-12); the default just does not show it.
