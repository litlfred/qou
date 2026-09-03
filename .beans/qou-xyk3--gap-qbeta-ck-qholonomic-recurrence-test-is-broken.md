---
# qou-xyk3
title: 'GAP: qbeta_ck_qholonomic_recurrence_test is BROKEN on main — TypeError: cannot create mpf from None at :359'
status: todo
type: task
priority: normal
created_at: 2026-08-29T21:29:14Z
updated_at: 2026-08-29T21:29:43Z
---

Parent: qou-x5mi. Found while trying to declare `q0Anchor: comparison` on it.
Independent of the environment hazard that bean records — this one fails in ANY
environment and is a defect on main.

## The failure

    python3 computations/probes/qbeta_ck_qholonomic_recurrence_test.py
    -> TypeError: cannot create mpf from None

    File ".../qbeta_ck_qholonomic_recurrence_test.py", line 358, in main
        worst_ext = max(
    File "...", line 359, in <genexpr>
        abs(anchors["muon"]["c_emp"][k] - mp.mpf(ext[f"c_{k}"]))

`ext[f"c_{k}"]` is `None` for at least one k.

## It is NOT my change

Verified by stashing my patch and running main's version verbatim: identical
traceback, identical exit 1. My edit was in the witness-write block at ~:580,
which the traceback never reaches.

## Consequences

* the producer CANNOT be re-run, so its witness cannot be refreshed by anyone;
* the q0Anchor declaration it needs (`comparison` — it reads both pins
  deliberately, `extract_empirical_ladder(Q0_MUON)` at :328 alongside the
  proton leg) cannot be landed, because a producer-side declaration only
  reaches the witness through a re-run;
* whatever is currently in
  `computations/probes/qbeta-ck-qholonomic-recurrence-test.witness.json` is the
  last output of a version that ran, and nothing on main reproduces it.

## Not diagnosed

I did not chase WHY `ext["c_k"]` is None — whether an upstream extraction
returns None for a rung that is genuinely unavailable (in which case the
consumer needs a guard) or whether something that used to populate it has
changed. That is the first question for whoever picks this up. Note the
c_k ladder is convention-C-frame and cds1-gated (AGENTS.md), so "just make it
not-None" may be the wrong fix; the honest answer might be that the rung has no
value under the current state and the producer should say so.
