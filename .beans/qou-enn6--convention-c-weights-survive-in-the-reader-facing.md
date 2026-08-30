---
# qou-enn6
title: Convention-C weights survive in the reader-facing three-channel H_3 table (alt weight 0.02 vs 0 exactly)
status: todo
type: task
priority: normal
created_at: 2026-08-30T19:55:48Z
updated_at: 2026-08-30T20:24:23Z
---

Found 2026-08-30 draining `qou-58zw`'s tolerance-floor audit. The producer
`computations/atom_mass_full_hecke_qdeformed.py` is fixed (`f61deb33bf`); the
**content blocks are not**, and one part of the fix is not available to me.

## What is wrong

The reader-facing block
[`observations/atom-mass-full-hecke.md`](https://github.com/litlfred/qou/blob/claude/convention-c-migration-tranche-1-2026-08-30/content/quantum-observable-universe/observations/atom-mass-full-hecke.md)
states, in prose:

> At $q \approx 1.11$, $\hat y_{\mathrm{sym}} \approx 0.42$,
> $\hat y_{\mathrm{std}} \approx 0.56$, and $\hat y_{\mathrm{alt}} \approx 0.02$.

All three are **convention-C** values. Under the derived two-row cap the live
producer gives **0.5054 / 0.4946 / 0 exactly** — `y_lambda_at(3, Q)` routes to
`y_lambda_su_n(n, q, 2)`, the SU(2) specialisation, whose rank cap *is* the cap
(`FibreDimensionForcesTL.lean`, `qou-n1dj`).

Its "Key observations" §2 says the alternating block is **suppressed**. Under D
it is **absent**: identically zero, not small. That is an interpretive claim,
not just a number.

The sibling table block `atom-mass-full-hecke-table-data.md` carries the C-era
`tr_full` column **verbatim** — every entry matches the pre-fix witness exactly.
Measured shift, committed witness (C, 2026-06-22) vs the regenerated one (D):

| atom | tr_full C | tr_full D | rel |
|---|---|---|---|
| 4He | 0.516 | 0.577 | 11.7 % |
| 7Li | 0.294 | 0.397 | 35.0 % |
| 9Be | 0.343 | 0.371 | 8.0 % |
| 11B | 0.245 | 0.353 | 44.1 % |
| 12C | 0.533 | 0.615 | 15.4 % |
| 14N | 0.512 | 0.660 | 28.7 % |
| 16O | 0.677 | 0.766 | 13.1 % |
| 19F | 0.170 | 0.322 | **89.6 %** |
| 20Ne | 0.932 | 1.027 | 10.2 % |

## Why I did not update the blocks

The table's **`B/A_Skein`** and **`Δ (MeV)`** columns are derived from
`tr_full`, and I could find **no live producer** for them — every grep hit is
under `computations/_deprecated/`. So I can regenerate one of the table's three
number columns and not the other two. Updating `tr_full` alone would leave the
table internally inconsistent in a way that reads as correct, which is worse
than the present state where all three columns are consistently stale.

The prose weights and observation §2 *could* be fixed independently of that, and
are the cheaper half.

## Options

1. **Fix the prose only** (weights `0.42/0.56/0.02` → `0.5054/0.4946/0`, and §2
   "suppressed" → "absent, by the two-row cap"). Cheap, self-contained, no
   producer needed. Leaves the table stale but does not make it *more*
   inconsistent. **Recommended** — this is my judgement, not a finding.
2. **Also fix `tr_full`, and mark `B/A_Skein` / `Δ` as unrefreshed.** Honest but
   leaves a table whose columns come from two different conventions, flagged in
   prose. Cheap; risks a reader taking a row as coherent.
3. **Find or rebuild the `B/A_Skein` producer and regenerate the whole table.**
   Correct, and the only option that ends with a coherent table. Unknown cost —
   the formula's provenance is not in the live tree.
4. **Do nothing.** The default. The block keeps stating convention-C weights and
   a "suppressed" alt channel that is actually zero, in a reader-facing
   observations block. The producer is fixed either way, so the witness and the
   prose now disagree.

## Related but distinct

`qou-5ll9` hits the **same block** from the other input: `atomic-tr-m-helium4`
is 7.55 % stale pre-C→D, feeding the per-channel `|tr_M|` traces. That is the
*trace* leg; this is the *weights* leg. Both would have to land for the table to
be right, which is an argument for doing them together under option 3.


---

## RE-SCOPED 2026-08-30 — main fixed the prose half, and better than my option 1

Rebasing onto `origin/main` brought in a sibling's fix to
`observations/atom-mass-full-hecke.md`. It does more than correct the numbers:
it gives a **two-convention table** (D `0.5054 / 0.4946 / 0` beside C
`0.42 / 0.56 / 0.02`), states that the alternating weight is *exactly zero*
under the canonical convention rather than small, names a nonzero
`ŷ_alt` as **itself a convention-C signature**, and then closes the honesty
gap explicitly:

> The convention-C row is retained because the results tabulated below were
> computed in it and have not been recomputed under D. They are reported as
> measured, in the frame that produced them.

That is option 1 done better than I proposed it, plus the flag I could not
supply. **Options 1 and 2 are therefore gone**, and the priority drops from
high to normal: the block no longer *misstates* anything, it declares its own
frame.

## What is left, and it is now genuinely optional

The table's `tr_full` column is still convention C, correctly labelled as such.
**I have the D values** (regenerated in `f61deb33bf`, producer fixed and
re-run):

| atom | tr_full C (labelled) | tr_full D (measured) | rel |
|---|---|---|---|
| 4He | 0.516 | 0.577 | 11.7 % |
| 7Li | 0.294 | 0.397 | 35.0 % |
| 9Be | 0.343 | 0.371 | 8.0 % |
| 11B | 0.245 | 0.353 | 44.1 % |
| 12C | 0.533 | 0.615 | 15.4 % |
| 14N | 0.512 | 0.660 | 28.7 % |
| 16O | 0.677 | 0.766 | 13.1 % |
| 19F | 0.170 | 0.322 | **89.6 %** |
| 20Ne | 0.932 | 1.027 | 10.2 % |

Supplying them alone still leaves `B/A_Skein` and `Δ (MeV)` in C, and those
still have **no live producer** — every grep hit is under `_deprecated/`. So
the remaining choice is only between:

3. **Rebuild the `B/A_Skein` producer and regenerate the whole table.** The
   only option that ends with a coherent D table. Unknown cost; the formula's
   provenance is not in the live tree. `qou-5ll9` hits the same block from the
   trace leg (`atomic-tr-m-helium4` 7.55 % stale pre-C→D), so both would have
   to land together.
4. **Leave it.** Now the *reasonable* default rather than a silent defect: the
   block declares its frame, the D weights are on the page, and the D
   `tr_full` values are recorded here and in the regenerated witness for
   whoever does option 3.

**Recommendation (judgement, not finding): 4 for now, 3 bundled with
`qou-5ll9`** when someone takes the trace leg. Half-migrating a three-column
table is the one move worth avoiding.
