---
# qou-sa14
title: 'raw-float64 backlog triaged by what draining would require: 72 pct is ordinary scalar work, not the solver wall the large entries suggest'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T13:19:30Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
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


---

## CORRECTION 2026-09-13 — I reported 29,023 dirty; it is 25,725, and I cannot reproduce 29,023

The figure in this bean's first pass was **wrong and I cannot reconstruct how I
got it.** Measured three ways today against the same tree:

| measure | fields |
|---|---:|
| baseline total | 30,985 |
| sum of BASELINE figures over entries still dirty | 25,891 |
| **sum of ON-DISK counts over entries still dirty** | **25,725** |
| what I reported | 29,023 |

29,023 matches neither, so it is not the "ranked by baseline vs ranked by disk"
slip I first assumed — that slip is worth only 166 fields. I am recording it as
unreproducible rather than explaining it, because a plausible-sounding
reconstruction I cannot check is worse than an admitted gap.

**24 baseline entries (5,094 baseline fields) are already 0 on disk.** Four of
them sit in the mid-size band I was screening, so I had been screening
already-clean targets: `binding-reeb-phase-decomposition` (296),
`channel-product-mass` (270), `delta-lambda-fr-identity-phase5c` (246),
`term7-alpha5-crystal-derivation` (210) — 1,022 fields of stale baseline.

**Rank off disk, not off the baseline.** The baseline figure is the value when
the entry was added; it does not move when the producer is drained.

## The queue, structurally

    LIVE dirty                      979 entries / 25,725 fields
      minus qou-baye orphans        -21 entries / -1,550
      = drainable                   958 entries / 24,175 fields

## A false alarm I caught before publishing it

A raw traversal with `count_raw_floats` over every `computations/**/*.witness.json`
reports **302 dirty witnesses / 116,432 fields outside the baseline** — 4.5× the
whole baselined backlog. That is **not a gap**: `count_raw_floats` is not what the
audit uses. `scan()` applies the LP-dual, ephemeral-duration, integrator and
deprecated-f64 carve-outs and skips `_deprecated/`. Run `scan()` and the answer is
**0 unbaselined dirty entries**.

Second time this session a bypassed exclusion produced a large fake number. The
rule: **measure with `scan()`, never with `count_raw_floats` over a glob.**

## And my own orphan detector was blind to 17 of 21

I wrote a clean-twin test — a baselined dirty entry whose same-stem twin is 0 —
and it found **4 orphans / 615 fields**. `qou-baye` had already measured **21 /
1,550** by the right instrument: a **source scan** for the stem in a write
context. My test only fires when the twin happens to be clean; for the other 17
the twin is dirty too, so it classified them as ordinary double-counting.

Worth naming because the failure is the one the detector-blindness taxonomy
keeps recording: **a detector that answers a proxy question and reports the
answer as if it were the real one.** "Twin is clean" is evidence about the twin;
"no producer writes this path" is the claim. Reading `qou-baye` is what caught
it, not the code.

`qou-kcii`'s 19 groups / 1,205 redundant fields reproduce exactly.

## Queue after exclusions — the top is nearly all accounted for

Ranks 1-6, 9, 10 and 14 of the on-disk top-14 are excluded (regeneration-blocked,
contended, orphan, owner-call, or mine-in-progress). The first genuinely
screenable entries are **#7 `all-nuclides-sdp-admissibility` (336)** and **#8
`deltalambda/he4-binding-k-stage2` (316)**.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8388, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
