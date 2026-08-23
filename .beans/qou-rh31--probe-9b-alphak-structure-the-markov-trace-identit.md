---
# qou-rh31
title: 'probe_9b_alphak_structure: the Markov trace identity is broken at BOTH pins — stale witness, import-cone drift'
status: todo
type: task
priority: normal
created_at: 2026-08-23T08:05:32Z
updated_at: 2026-08-23T08:06:07Z
---

Exposed 2026-08-23 while re-running the `load_q_50dps` callers (PR #5494,
bean `qou-dkm2`). **NOT caused by the pin change** — measured, see below.

## The three failing assertions

    numeric_z_series_depth_le2               2.04e-71  ->  0.1260658347330721
    numeric_tr_T121_closed_form              5.43e-71  ->  0.1397230640399885
    alpha3_value_not_derived_near_match_10pc 0.104388  ->  0.128089  (exp 0.104, tol 0.01)

The first is `tr_M(T_w) = z^{ℓ(w)}` for depth ≤ 2 — a Markov trace identity
that should hold exactly.

## It is NOT the pin — measured at both

    muon    q=1.10997859555733472  max|tr_M - z^l| = 0.126066
    proton  q=1.10997858275138081  max|tr_M - z^l| = 0.126066

**Identical.** So the identity is broken at the muon pin too, i.e. it was
already broken before the re-pin. The committed witness recorded `2.04e-71`
at the muon pin; today's code gives `0.126066` at that same pin, so the code
changed under the witness.

## Import-cone drift, dated

    witness computedAt          2026-07-02
    y_lambda_wenzl_bridge.py    changed 2026-08-11 (c3a7e16856)

Textbook instance of the class AGENTS.md §idle-backlog describes: the
producer's own source can be byte-stable while a module it CALLS changes.
A file-local `git diff` cannot see it.

## What is open

Whether the identity SHOULD hold under the current `y_lambda_wenzl_bridge` /
`chi_lambda_mpmath`, or whether the 2026-08-11 change was correct and the
identity's statement needs revising (the convention C -> D ruling is the
obvious suspect: `load_q_50dps` returns `z = 1/(√q+1/√q)` = **z_C**, while
the canonical convention is D). **Not diagnosed here** — this bean records
the measurement and the dating, not a verdict.

The regenerated witness is committed with `allPassed: false`: that is the
honest record. The failure was there before; it was invisible because nothing
had re-run the producer since July.
