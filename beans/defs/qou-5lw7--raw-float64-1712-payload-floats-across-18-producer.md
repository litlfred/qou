---
# qou-5lw7
title: 'raw-float64: 1712 payload floats across 18 producers — scope, classification, and why it is not a serialization sweep'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T20:23:58Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
---


Investigated while running `/prepare-merge` on branch `claude/hecke-open-beans-x64l`
(PR #4879). That branch touches **zero** files under `computations/` — verified
with `git diff --name-only origin/main...HEAD` — so all of this is inherited.
Recorded here rather than fixed in that PR, with the scoping done so the owning
arc does not have to redo it.

## What the ratchet reports

`scripts/precision-gates.sh` → `raw-float64 ratchet` is the only real blocking
red (the other four reds in that run were `mpmath` being absent from the
sandbox — see the preflight added in the same PR):

    witnesses carrying raw float64 : 1600
    total raw float64 fields       : 541,950
    NEW dirty witnesses            : 20
    REGRESSED (count increased)    : 2
    drained since baseline         : 6 file(s), -1,616 field(s)

So the corpus is being drained — six files went to zero or lower — while 22 new
ones arrived. This is a queue, not a wall.

## The 22, classified by how their numbers are produced

| fields | producer kind | files |
|---|---|---|
| ~1150 | `mpmath` already, serialized with `float(...)` | 13 |
| ~350 | `numpy` + `mpmath` mixed | 4 |
| ~90 | `numpy` only, or plain float | 4 |
| 59 | already imports `fmt`, partial adoption | 2 |

The first group is the tractable one and it is a **real** fix: e.g.
`deltalambda/threerow_qcross_trend_probe.py` computes at 50 dps in `mp.mpf`
throughout and then writes `"S_at_lo": float(f(Q_LO))`, discarding 35 digits on
the way into JSON. Its own `add_parameter` calls already do the right thing
(`mp.nstr(Q0, 30)`), so the file disagrees with itself.

The last two groups are **not** serialization defects. Those producers compute in
float64 by construction — `np.linalg.norm`, `np.eye`, `np.trace` — so "fix at the
producer" there means re-deriving the numerics in mpmath, which is a change to
what the probe computes, not to how it is written down. That is a decision for
whoever owns those probes.

## The target form, confirmed against an already-drained witness

`computations/inverse-markov-qvalues.witness.json` (38 → 0) writes numeric
**strings**: `"Q_exp": "0.782333409310022"`. So the mechanical fix is
`float(x)` → `fmt(x)` at the point of emission, keeping the arithmetic in mpmath
up to that point.

## Framework fields are NOT the bulk — measured, because the small files mislead

The four smallest offenders are entirely framework-emitted and suggest a single
central fix in `WitnessBuilder`:

* `ground-state-ordering-argmin-sweep` — one float, `wall_seconds = 130.5`
* `volume-binding-four-point`, `markov-z-fibre-rank-bar-covariance` — every float
  is in an `assertions[].computed / expected / tolerance` triple

That generalisation is **wrong at scale**. Counting `wall_seconds`, `durationMs`
and the assertion triples across all 22: **36 framework fields, 1712 scientific
payload**. Changing `WitnessBuilder` would move 36 of 1748 while reshaping every
witness in the corpus — high blast radius, negligible yield. Do the producers.

## Why this is not a one-pass sweep

Each file needs: the emission points changed without changing any intermediate
arithmetic; the producer **re-run**; and the resulting witness reviewed, because
the committed values gain ~35 significant digits — a substantive change to
recorded results, not a reformat. Several producers are long-running probes
(`threerow-qcross-trend` prints per-leg wall times in the hundreds of seconds;
`GRID_4HE` runs 30 iterations per crossing). Budget per producer, not per corpus.

## Also seen in the same run

* **REGRESSED**: `chi-helium-4-h12-at-q0-50dps` 1 → 78 and
  `probes/keystone-colored-sigma235-wrt` 36 → 52. A file named `…-50dps` writing
  78 raw float64 fields is worth looking at first — that is a precision claim in
  the filename contradicted by the payload.
* Two committed audit witnesses were stale on real counts and were regenerated
  in PR #4879: `q0-value-drift-audit` (proton-pin 688 → 690, canonical 609 → 612)
  and `witness-raw-float64-audit` (dirty 1598 → 1600, new_not_baselined 18 → 20).
  Both moved from upstream content, not from that branch.

---

## 2026-08-09 (later) — two corrections, one of which changes the whole shape

### 1. It is NOT a serialization sweep. The flagship case cannot be re-run at all.

`deltalambda/threerow_qcross_trend_probe.py` — the file cited above as the clean
mechanical example — was run end to end. After **586 seconds** it died:

    TypeError: atom_braid_word_3A: q is an mpf holding only float64 information
    (the `mpf(str(q_parameter.Q))` idiom) — ~17 real digits in a 50-dps path.
    Pass q_parameter.Q_50_DIGIT_STR. allow_float64=True to declare a
    deliberately f64 sweep.

`pyhecke.atom.reject_float64_q` refuses it. So the 126 raw float64 fields in that
witness are not a formatting mistake at the output — **the input `q` was
float64-degraded and the entire computation ran at ~17 real digits inside a
50-dps path.** The committed witness predates the guard.

This inverts the earlier plan. Rewriting `float(x)` → `fmt(x)` there would emit
50-digit strings carrying 17 digits of information — strictly worse than today,
because the result would *look* precise and would pass the ratchet. The ratchet
would go green on a witness that got less trustworthy.

**The guard is the producer-side fix, already in the tree, already working.**

### 2. The 13/4/4 classification was measured the wrong way

It came from grepping top-level `import numpy` / `import mpmath`. That is not the
same question as where the emitted numbers come from, and it is demonstrably
unreliable: `threerow_qcross_trend_probe.py` contains no `import numpy` yet fails
without numpy, because the dependency arrives transitively through
`threerow_chi_sparse`. Treat the split as indicative. The threerow finding itself
stands only because its emission sites were read directly.

### The right first step, which is cheap

Do **not** start editing. Run all 22 producers and collect the failures —
`reject_float64_q` performs the classification for you, for free:

* **fails the guard** → the q-anchor is degraded. Fixing it changes computed
  results, needs the owning arc, and is not estimable from outside.
* **runs clean** → serialization is genuinely the only problem, and it is cheap.

Measured runtimes so far: `volume_binding_four_point` 0.9 s,
`markov_z_fibre_rank_bar_covariance_probe` 1.8 s, `c3_w2_c1_pole_divisor` 6.5 s,
`threerow_qcross_trend_probe` 586 s to reach its failure. So the audit is maybe an
hour of wall time, mostly waiting on the two or three big probes.

### Retracted estimate

"30–60 min per mechanical file, 2–3 focused days" was based on the assumption
that these are output-formatting defects. At least one is not, and the guard
exists precisely because that class of defect is known here. No total can be
given until the anchor audit above is run.

### Environment note, and it is not incidental

This sandbox had **no scientific Python stack at all** — `mpmath`, `sympy`,
`numpy` and `scipy` were all absent. Nothing under `computations/` could run.
That is the same failure the precision-gates preflight now catches for the gate
scripts (four of five reds were phantom), one layer deeper: the gates could not
evaluate, and the producers could not execute. Provision the stack before
concluding anything about this queue.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8282, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
