---
# qou-sa14
title: 'raw-float64 backlog triaged by what draining would require: 72 pct is ordinary scalar work, not the solver wall the large entries suggest'
status: todo
type: task
priority: normal
created_at: 2026-09-13T13:19:30Z
updated_at: 2026-09-13T13:20:26Z
---

Measured 2026-09-13 after three consecutive drain targets (`r5-full-canonical-knot-solver`,
`binding_k_solver`, `pn-alpha-lp-dual`) all hit a solver or matrix wall rather
than a fixable cast. That was starting to read as "the backlog is mostly
undrainable". **At the population level it is not**, and the sample was biased:
those three are the LARGEST entries, and size correlates with having a solver in
the producer.

## The measurement

All 1003 baseline entries, profiled by their ON-DISK non-integral float count
(not the baseline number) and bucketed by field-path signature:

    baseline entries                1003
      already CLEAN on disk           23
      still dirty on disk            980

    baseline records            30,985 fields
    ACTUALLY DIRTY on disk      29,023 fields   (94 pct of the baseline)

| bucket | files | fields | what draining needs |
|---|---:|---:|---|
| scalar / not-obviously-solver | **827** | **20,781** | a producer edit |
| matrix | 102 | 4,237 | exact linear algebra at the block dims |
| LP-solver | 46 | 3,819 | an exact LP/SDP backend; Clarabel returns f64 |
| mixed | 5 | 186 | both |

**72 pct of the remaining fields and 84 pct of the remaining files are ordinary
producer work.** The solver/matrix walls are real but are 26 pct of the fields,
concentrated in the big entries.

## 🛑 The bucket label is weaker than it sounds — read this before using it

"scalar / not-obviously-solver" is a **keyword heuristic on field paths**
(`x_star`, `y_star`, `duality_gap`, `lp_dual`, ... for LP; `matrix`, `eig`,
`det`, `chi`, `min_eig`, `frob`, `gram`, ... for matrix). It means "the
majority of this witness's float paths do not match those keywords". It does
**not** mean verified-drainable, and two entries in that very bucket are already
known not to be:

  * `intermediate-knot-detection` (350) — bucketed scalar, and `qou-jtgk`
    establishes it needs an upstream `hecke_core` change (that module exports
    `z`, `h`, `q0` as Python floats and `G` as a float64 ndarray).
  * `hadron-knot-table` (452) — bucketed scalar, excluded on cost: AGENTS.md
    measures it at >50 min for ONE bound atom of nineteen.

Also suspicious: `all-nuclides-sdp-admissibility` shows **471 on disk against a
336 baseline** and has "sdp" in its name, yet bucketed scalar because its LP
fields were 135, just under half. Likely a mixed case the majority rule
mislabels.

So treat the table as **an upper bound on the drainable tail**, and pre-screen
each target the way this session's did.

## Known exclusions already established, so the ranking stops offering them

| entry | fields | why |
|---|---:|---|
| `r5-full-canonical-knot-solver` | 637 | blocked behind a regeneration decision (`qou-sogb`) |
| `binding-single-pipeline-comparison` | 299 | blocked behind a regeneration decision (`qou-gjkv` / `qou-5c64`) |
| `hadron-knot-table` | 452 | >50 min per bound atom |
| `intermediate-knot-detection` | 350 | needs `hecke_core` exact (`qou-jtgk`) |
| `audits/stale-probe-audit` | 349 | contended tree-measuring witness (`qou-v0t8`) |
| `pentagon-rt-torus-knot-higgs` +3 | 615 | orphans, clean twin exists (`qou-baye`) |
| `adjacent-vs-full-probe` x2 +17 | 1205 | double-counted pairs (`qou-kcii`) |

## Method note

Bucket by ON-DISK counts, never by the baseline number. Doing it the other way
put 9,955 fields in `scalar` because 15 already-drained entries still carry
their baseline figure (`k-star-search-phase5d-5` records 1647 and has 1 float on
disk). The first version of this table said exactly that and was wrong.
