---
# qou-rh31
title: 'probe_9b_alphak_structure: the Markov trace identity is broken at BOTH pins — stale witness, import-cone drift'
status: todo
type: task
priority: normal
created_at: 2026-08-23T08:05:32Z
updated_at: 2026-08-23T08:12:38Z
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


## DIAGNOSED (2026-08-23) — it is convention C vs D, measured decisively

Compared `tr_M(T_w)` against both conventions at the proton pin:

    max|tr_M - z_D^l| = 2.5391265e-50    <- zero to the arithmetic floor
    max|tr_M - z_C^l| = 0.12606583       <- the observed break

Per word:

    T1   l=1   tr_M = 0.61268803714647   z_D = 0.61268803714647   z_C = 0.49932033418369
    T12  l=2   tr_M = 0.37538663086239   z_D^2 = 0.37538663086239  z_C^2 = 0.24932079612932

So the Hecke machinery (`y_lambda_wenzl_bridge` + `chi_lambda_mpmath`)
computes in **convention D** — consistent with the owner's 2026-08-15 ruling —
while `_li_2_q_util.load_q_50dps` returns
`z = 1/(√q + 1/√q) = √q/(q+1)` = **z_C**.

The probe compares a D-computed trace against a C-supplied z. That is the whole
break. The 2026-08-11 change to `y_lambda_wenzl_bridge.py` was almost certainly
the D migration, which is why the July witness predates it.

**The identity is NOT broken.** It holds exactly, in D. What is broken is the
z the probe compares it against.

## This also answers qou-324i, which I had left open

I recorded there that I would **not** claim `load_q_50dps`'s z is *the* Markov
parameter, because a brane-tower pair weight sharing a formula with it is a
glyph-collision hazard. That question is now answered by measurement: the
identity `tr_M(T_w) = z^{ℓ(w)}` **is** the defining Markov property, and it
holds with z_D. Two callers also name it outright —
`pentagon_reduction_li2q.py` binds it as `z_markov`, `e0_lambda_composite.py`
as `ZMARK`.

So: **`load_q_50dps` is a live convention-C site under the canonical-D regime,
with 24 consumers binding its z.** The convention-C detector does not see it
because it is a tuple-element return — the blindness recorded in qou-324i.

## Not fixed here

Switching the returned z to z_D moves 24 producers' numbers. That belongs with
the convention-D tranche (`qou-cds1` / `qou-cds2`), not with a q₀-pin PR, and
some consumers may use the returned z in a **pair-weight** role
(`compute_t2_t3_from_vols` uses `T3 = z²·Σ_{i<j}`) rather than the Markov role —
which still needs the per-consumer read before anything is changed.
