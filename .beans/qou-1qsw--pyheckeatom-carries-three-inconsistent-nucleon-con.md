---
# qou-1qsw
title: pyhecke.atom carries THREE inconsistent nucleon constructions (nets differ by 24%) and different consumers read different ones
status: todo
type: task
priority: normal
created_at: 2026-08-29T16:24:57Z
updated_at: 2026-08-29T16:25:40Z
---

Surfaced by the `qou-cds1` takeover work (`74a52d3486`), which recorded it as
**"New, and it is a defect in the tree, not in this bean: ... Not filed as its
own bean yet."** Filing it so it stops living inside another bean's history.

## The defect

`pyhecke.atom` carries three mutually inconsistent nucleon constructions, and
their Markov-trace nets disagree by up to ~24 %:

| constructor | crossings | net |
|---|---|---|
| `build_nucleon_nf` | 9 | `-0.1883216147` |
| `build_atom_nf_exact` | 11, interleaved | `-0.2272041420` |
| `nucleon_gen_chains` | 11, gen-grouped | `-0.2332458961` |

The two 11-crossing models carry the **same multiset of typed crossings** and
differ only in ORDER — `build_atom_nf_exact` interleaves gen-0/gen-1,
`nucleon_gen_chains` emits all gen-0 then all gen-1. `H_3(q)` is not commutative
across generators, so these are genuinely different elements; their nets differ
by 2.6 %.

## Why it bites — the consumers are split

Different call sites read different constructions, so "the nucleon" is not one
object in this codebase:

- the exact atom/mass path uses `build_atom_nf_exact`
- the module constants `PROTON_NF` / `NEUTRON_NF` are `build_nucleon_nf`
- the fork-pricing probe reads `_PROTON_G0` / `_G1`

A result quoted from one path is not comparable with a result quoted from
another, and nothing in the tree marks which is which.

## Prior art the fix must respect

`build_nucleon_nf` omits the 2-`sigma_0` gluon dressing **deliberately** — its
own docstring says *"No separate gluon dressing — B_3 IS the gluon structure"*.
So this is not simply "one is missing crossings"; the 9-crossing model is a
different physical convention, not a truncation bug. Any consolidation has to
decide which convention is canonical rather than assume the longest wins.

`qou-bg3w`'s `Delta_L` (`-0.233198`) is the **gen-grouped** one, which the first
version of the cds1 exclusion probe never touched — an example of the confusion
this causes reaching a real analysis.

## What is needed

1. Determine which construction is canonical (owner call if the gluon-dressing
   convention is genuinely open).
2. Make the non-canonical ones either aliases, or explicitly-named variants that
   a reader cannot pick up by accident.
3. Re-point the split consumers; check whether any committed witness carries a
   value from a now-non-canonical constructor.

Not started. Filed from the cds1 takeover record, not re-measured here — the
numbers above are quoted from that probe's output, and step 1 should re-verify
them before acting.
