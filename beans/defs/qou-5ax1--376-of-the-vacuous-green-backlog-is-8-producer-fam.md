---
# qou-5ax1
title: 37.6% of the vacuous-green backlog is 8 producer families, not 423 problems
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T14:35:45Z
updated_at: 2026-10-04T15:16:04Z
parent: qou-5vkl
---

## Measurement

Reverse-indexed every `computations/**/*.witness.json` on its own `witness.scriptFile`
(not guessed from filenames) against the 423 live entries in
`computations/audits/vacuous-green-baseline.json`:

| producer | writes | of which vacuous-green |
|---|---:|---:|
| `canonical_isotope_witness.py` | 120 | **120** |
| `_habiro_coefficient_extract.py` | 26 | **26** |
| `chi_at_q0_via_matrix_m_mpfr.py` | 4 | 4 |
| `canonical_tr_m_via_chi_cache.py` | 2 | 2 |
| `atomic_tr_m_mpfr_50dps.py` | 2 | 2 |
| `A_operator_extract_at_level.py` | 2 | 2 |
| `markov_peel_atomic_witness.py` | 2 | 2 |
| `binding_energy_categorical_deuteron.py` | 2 | 1 |
| **total** | | **159 of 423 = 37.6 %** |

**Every family is all-or-nothing** — 120/120, 26/26, 4/4. A producer that emits a
vacuous-green witness emits vacuous-green witnesses for its whole shard set, which
is what makes the concentration actionable rather than merely notable: one fix to
`canonical_isotope_witness.py` drains **28 % of the entire backlog**.

## Why this matters for how the drain is scoped

The five-way `qou-srvu` dispatch partitioned by WITNESS, so each of the 8 families
was split across 3-5 agents. Every agent independently hit the same wall and,
correctly, refused to re-run a producer writing outside its slice — so all 159 are
untouched, and three agents each spent triage effort re-deriving the same
MULTI-SLICE list. **Partition the next tranche by PRODUCER, not by witness.**

Slices A/B/D drained 8/9/11 = 28 witnesses, all from the ~264 single-producer
remainder. Those are genuinely 1:1 and were the right thing to do first.

## Two traps recorded before anyone re-runs the isotope family

Both found by slice A reading the source, not inferred:

1. **`--z` restricts which shards are written, but `emit_index()` runs
   unconditionally** — a restricted re-run would rewrite
   `canonical-isotope-witness-index.json` with only the restricted set. A partial
   re-run of this producer is **not** automatically safe.
2. **Its own docstring calls it a "read-many, compute-little orchestrator"** with
   `rows` a 1:1 list comprehension over AME entries. So a `rows_total` assertion
   would be **pure self-comparison** — precisely the `qou-3e5m` defect this bean's
   parent exists to remove. Whatever gets asserted here has to be something the
   producer *computes*, not something it *counts*.

`atomic_tr_m_mpfr_50dps` is the dual-layer case AGENTS.md already documents
(one witness per anchor layer), and is also implicated in `qou-tfj0` — the
tr_M three-path comparison whose ⁴He row renders `0.0` because ⁴He is absent
from that producer's output entirely.

## Next honest step

Assign each of the 8 families to exactly one owner and drain by producer. The
largest two (`canonical_isotope_witness`, `_habiro_coefficient_extract` = 146 of
the 159) deserve their own tranche; the remaining six are 13 witnesses total and
can ride together.

Do **not** treat 159 as 159 units of work — it is 8, with a long tail of shards
that follow from each.


---

## 🛑 CORRECTION (same session, before anyone acts on this)

**"One fix to `canonical_isotope_witness.py` drains 28 % of the entire backlog"
is wrong, and it is the whole point of the table above.** Slice C read that
producer's source and reports it as a **LEAVE on the merits**, independent of
slice ownership — its own docstring calls it a *"read-many, compute-little
orchestrator"*, `assemble_row` copies `prediction_MeV_50dps` and AME references
out of upstream witnesses and groups by Z, so **every invariant available to it**
(`row.Z == shard Z`, `A == Z + N`, row count vs the AME filter) is true **by
construction**. Asserting any of them is a self-fulfilling assertion — the
`qou-3e5m` defect that the parent bean exists to remove.

So the corrected reading of the 159:

| family | witnesses | disposition |
|---|---:|---|
| `canonical_isotope_witness.py` | 120 | **LEAVE** — orchestrator, all invariants true by construction |
| `_habiro_coefficient_extract.py` | 26 | open; and see `qou-wc8f` below |
| the other six families | 13 | open |

**39 open, not 159.** The concentration finding survives — the backlog is 8
families rather than 159 problems, and partitioning the next tranche by PRODUCER
rather than by witness is still the right call. What does not survive is the
implied size of the prize.

**`_habiro_coefficient_extract.py` is now the largest open family, and it is
implicated in an unresolved data question.** `qou-wc8f` (slice C) found that
re-running `topic2_mirror_pair_phi8_boundary_scan` doubles `mult(Φ_8)` on 9 of 9
rows, and that `M_max_used` moved on 3 rows — `M_max_used` is the Habiro depth of
the upstream witnesses, i.e. direct evidence that **this producer's output
drifted**. The committed column satisfies the documented scaling law on 9 of 9
rows and the fresh column on 0 of 9, with five fresh values odd where the law
forces even. **Settle `qou-wc8f` before re-running this family**, or the drain
will bake in numbers that a parity argument says are wrong.

Recorded rather than edited away, because the error is the instructive part: the
table was measured correctly and the conclusion drawn from it was not. Witness
COUNT is evidence about the backlog's shape; it is not evidence that a producer
has anything falsifiable to assert. Only reading the source establishes that, and
the largest row is exactly where that shortcut costs the most.

- **Round 95 (`litlfred/qou#8426`)**: Advanced in `feat/round95-layout-lowerbound-bondrule-maxcontact-simplex-43c1` (Commit 1 `d482ea2750e00fbd6e9e74457e935101b2f8b093`, Commit 2 `8ed5dd0ff69b4804c5e40f393e7c9157a2067a42`, probe sha256 `8b786124c3dfda15d0d1672a05f3bc16f486d17a5f41250533162305ad901679`).
