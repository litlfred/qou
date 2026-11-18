---
# qou-wc8f
title: 'GAP: topic2 mirror-pair Phi_8 multiplicities do not reproduce on main, and the fresh values violate the documented scaling law'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T14:21:18Z
updated_at: 2026-10-04T15:20:29Z
parent: qou-trd0
---

Found while draining `qou-srvu` slice C. Not drained — deliberately LEFT, and
the witness reverted to its `main` state, because refreshing it would land
numbers that contradict a documented, corpus-recorded regularity.

## The measurement

Re-running `computations/topic2_mirror_pair_phi8_boundary_scan.py` on current
`main` (`bce13f8046`), with **zero source changes**, does not reproduce its own
committed witness. Isolated deliberately: I first ran it with an added
assertion, saw the drift, then reverted the producer to `main` and re-ran — the
drift is identical, so it is not my edit.

| mirror pair | A | `mult(Φ_8)` committed | fresh re-run | law `A−1` odd / `A−2` even |
|---|---|---|---|---|
| ³He − ³H  | 3  | 2  | 4  | 2  |
| ⁵Li − ⁵He | 5  | 4  | 8  | 4  |
| ⁶He − ⁶Be | 6  | 4  | 9  | 4  |
| ⁷Be − ⁷Li | 7  | 6  | 12 | 6  |
| ⁸B − ⁸Li  | 8  | 6  | 13 | 6  |
| ⁹B − ⁹Be  | 9  | 8  | 16 | 8  |
| ¹⁰C − ¹⁰Be| 10 | 8  | 17 | 8  |
| ¹²N − ¹²B | 12 | 10 | 21 | 10 |
| ¹⁴O − ¹⁴C | 14 | 12 | 25 | 12 |

`M_max_used` also moves on three rows: ³He−³H 15→16, ⁵Li−⁵He 19→20,
⁹B−⁹Be 27→26, ¹²N−¹²B 31→30.

## Why the committed values are the ones to keep

**The committed column matches the documented scaling law on all 9 rows; the
fresh column matches it on 0.** The law is
`docs/audits/2026-06-01-qbeta-habiro-phi8-mirror-multiplicity-scaling.md`:
`mult(Φ_8) = A − 1` for odd A, `2⌊(A−1)/2⌋ = A − 2` for even A.

Sharper: the law forces an **even** multiplicity for even A, and four of the
fresh values are **odd** (9, 13, 17, 21, 25). Those cannot be `2⌊(A−1)/2⌋` for
any A. This is not a small numerical shift, it is a parity violation of the
stated form.

The committed witness is also already POST-correction. The ⁶He−⁶Be row reads 2
in the table of `docs/audits/2026-06-01-mirror-pair-phi8-universal-boundaries.md`
and 4 in the committed witness, which is exactly what that doc's own banner
says to expect: *"Only the `mult(Φ_8)` column below is superseded"* after the
2026-08-18 a_m-differencing normalisation fix
(`2026-08-18-mirror-pair-a-m-differencing-normalisation-defect.md`). So the
committed witness reflects the corrected differencing, and re-running today
breaks it again.

## What survives, and it matters

`M_first_Φ_8 = 7` on **every** row, unchanged, in both the committed witness and
the fresh re-run. So the probe's headline claim — the PR #1625 Wenzl-annihilator
universal boundary, extended from atomic-step pairs to mirror pairs — is NOT
affected, and neither is `M_first_Φ_8² = 15`. Only the multiplicity column moved.
Both audit docs' surviving claims stand.

## Where to look

`M_max_used = min(max(ax), max(ay))` is the Habiro depth available in the
upstream `habiro-coefficients-<slug>.witness.json` files, and it changed. That
is direct evidence the **upstream data** moved, not the scan. The cone is
`habiro_coefficients_atomic.load_a_m` / `mirror_trace_diff_numerator` over the
`_habiro_coefficient_extract.py` witness family.

Note the scan's own source comment on that exact site:

> *"under convention C they agree at q=1 on every canonical pair … while under D
> they differ by a factor of 4 and every multiplicity collapses to 0."*

A factor-of-2 move in the multiplicity, in a file whose own comment says a
convention change moves the same object by a factor of 4, wants a
convention-aware reader before anything is refreshed. `qou-cds1` is the
convention-D re-derivation tranche.

## Why this is not being fixed here

Three reasons, in order of weight:

1. **The refreshed numbers are probably wrong**, per the parity argument above.
   Landing them would put law-violating multiplicities into a witness cited by
   two audit docs.
2. **The upstream is a multi-slice producer.** `_habiro_coefficient_extract.py`
   writes 26 witnesses spread across all five `qou-srvu` agents' slices, so
   whoever adjudicates this owns the whole family, not 6 of it.
3. It is a data-correctness question, not a witness-hygiene one. The drain task
   is the wrong vehicle.

## The drain that is ready when this is settled

The scan has a real falsifiable claim and currently asserts nothing
(`allPassed: true` over an empty assertion list — that is why I was here). The
assertion, written and verified to pass, is:

    universal_M_first_Phi_8_eq_7_holds_for_every_mirror_pair
      computed = n_phi8_pairs - universal_match = 0
      expected = 0
      guarded on n_phi8_pairs > 0, so it cannot itself be vacuous

Patch kept at `/tmp/srvu-c-topic2-patched.py` for the session; trivial to
rewrite. The entry stays in `computations/audits/vacuous-green-baseline.json`
until then.
